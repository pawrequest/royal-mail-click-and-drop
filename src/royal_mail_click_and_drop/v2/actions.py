from pprint import pprint

from royal_mail_click_and_drop import (
    ApiClient,
    ApiException,
    CreateOrdersRequest,
    CreateOrdersResponse,
    DeleteOrdersResource,
    GetOrdersResponse,
    LabelsApi,
    ManifestOrdersResponse,
    ManifestsApi,
    OrdersApi,
    Configuration,
    VersionApi,
)


def failed_order_errors(response):
    errors = [
        f'Error in {error.fields}: {error.error_code} - {error.error_message}'
        for fail in response.failed_orders
        for error in fail.errors
    ]
    if errors:
        pprint(errors, indent=4, width=120)
        raise ApiException('\n'.join(errors))


def book_shipment(orders: CreateOrdersRequest, cfg: Configuration) -> CreateOrdersResponse:
    with ApiClient(cfg) as client:
        c = OrdersApi(client)
        response = c.create_orders_async(create_orders_request=orders)
        failed_order_errors(response)
        return response


def cancel_shipment(order_ident: str, config: Configuration) -> DeleteOrdersResource:
    with ApiClient(config) as rm:
        client = OrdersApi(rm)
        try:
            response = client.delete_orders_async(order_identifiers=order_ident)
            return response
        except ApiException as e:
            print(f'Exception when calling OrdersApi->delete_orders_async: {e}\n')
            raise


def fetch_orders(config: Configuration) -> GetOrdersResponse:
    with ApiClient(config) as rm:
        client = OrdersApi(rm)
        try:
            response: GetOrdersResponse = client.get_orders_async()
            pprint(response.model_dump(), indent=4, width=120)
            return response
        except ApiException as e:
            print(f'Exception when calling OrdersApi->delete_orders_async: {e}\n')
            raise


def save_label(order_idents: str, outpath, config: Configuration):
    response = get_label_data(order_idents, config)
    with open(outpath, 'wb') as f:
        f.write(response)


def get_label_data(order_idents: str, config: Configuration):
    with ApiClient(config) as rm:
        client = LabelsApi(rm)
        try:
            response: bytearray = client.get_orders_label_async(
                order_identifiers=order_idents,
                document_type='postageLabel',
                include_returns_label=False,
                include_cn=False,
            )
            return response
        except ApiException as e:
            print(f'Exception when calling LabelsApi->get_orders_label_async: {e}\n')
            raise


def do_manifest(config: Configuration):
    with ApiClient(config) as rm:
        client = ManifestsApi(rm)
        resp: ManifestOrdersResponse = client.manifest_eligible_async()
        mainfest_num = resp.manifest_number
        print(f'Manifest Number: {mainfest_num}')
        return mainfest_num


def fetch_version(config: Configuration):
    with ApiClient(config) as rm:
        client = VersionApi(rm)
        try:
            response = client.get_version_async_with_http_info()
            pprint(response.model_dump(), indent=4)
            return response
        except ApiException as e:
            print('ERROR')


