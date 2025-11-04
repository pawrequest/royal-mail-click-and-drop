from pprint import pprint

from pydantic import ConfigDict

from royal_mail_click_and_drop import (
    ApiClient,
    ApiException,
    Configuration,
    CreateOrdersRequest,
    CreateOrdersResponse,
    DeleteOrdersResource,
    GetOrdersResponse,
    LabelsApi,
    ManifestOrdersResponse,
    ManifestsApi,
    OrdersApi,
    VersionApi,
)
from royal_mail_click_and_drop.config import RoyalMailSettings
from royal_mail_click_and_drop.models.base import RMBaseModel


class RoyalMailClient(RMBaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)
    settings: RoyalMailSettings
    _config: Configuration | None = None

    @property
    def config(self):
        if self._config is None:
            self._config = self.settings.config
        return self._config

    def book_shipment(self, orders: CreateOrdersRequest) -> CreateOrdersResponse:
        with ApiClient(self.config) as client:
            api = OrdersApi(client)
            response = api.create_orders_async(create_orders_request=orders)
            errors = [
                f'Error in {error.fields}: {error.error_code} - {error.error_message}'
                for fail in response.failed_orders
                for error in fail.errors
            ]
            if errors:
                pprint(errors, indent=4, width=120)
                raise ApiException('\n'.join(errors))
            return response

    def cancel_shipment(self, order_ident: str | int) -> DeleteOrdersResource:
        ident = str(order_ident)
        with ApiClient(self.config) as client:
            api = OrdersApi(client)
            try:
                response = api.delete_orders_async(order_identifiers=ident)
            except ApiException as e:
                print(f'Exception when calling OrdersApi->delete_orders_async: {e}\n')
                raise
        return response

    def fetch_orders(self):
        with ApiClient(self.config) as client:
            api = OrdersApi(client)
            try:
                response: GetOrdersResponse = api.get_orders_async()
                pprint(response.model_dump(), indent=4, width=120)
            except ApiException as e:
                print(f'Exception when calling OrdersApi->delete_orders_async: {e}\n')
                raise
        return response

    def get_label_content(self, order_idents: str):
        with ApiClient(self.config) as client:
            api = LabelsApi(client)
            try:
                response: bytearray = api.get_orders_label_async(
                    order_identifiers=order_idents,
                    document_type='postageLabel',
                    include_returns_label=False,
                    include_cn=False,
                )
            except ApiException as e:
                print(f'Exception when calling LabelsApi->get_orders_label_async: {e}\n')
                raise
        return response

    def get_save_label(self, order_idents: str, outpath) -> bytearray:
        response = self.get_label_content(order_idents)
        with open(outpath, 'wb') as f:
            f.write(response)
        return response

    def do_manifest(self) -> ManifestOrdersResponse:
        with ApiClient(self.config) as client:
            api = ManifestsApi(client)
            resp: ManifestOrdersResponse = api.manifest_eligible_async()
            mainfest_num = resp.manifest_number
            print(f'Manifested Orders, fetched Manifest Number: {mainfest_num}')
            return resp

    def fetch_version(self):
        with ApiClient(self.config) as client:
            api = VersionApi(client)
            try:
                response = api.get_version_async_with_http_info()
                pprint(response.model_dump(), indent=4)
            except ApiException:
                print('ERROR')
        return response

    def cancel_all_orders(self, really=False) -> DeleteOrdersResource:
        """Cancels ALL orders on the system - use with care / must pass really-True to work"""
        if not really:
            raise ValueError('Not cancelling orders, pass really=True to cancel')
        res = self.fetch_orders()
        if res.order_ident_string:
            response = self.cancel_shipment(res.order_ident_string)
            return response
        raise ValueError('No order idents in response')
