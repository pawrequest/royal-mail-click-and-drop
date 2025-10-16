from pydantic import ConfigDict

from royal_mail_click_and_drop import (
    Configuration,
    CreateOrdersRequest,
    CreateOrdersResponse,
    DeleteOrdersResource,
)
from royal_mail_click_and_drop.config import RoyalMailSettings
from royal_mail_click_and_drop.models.base import RMBaseModel
from royal_mail_click_and_drop.v2.actions import (
    book_shipment,
    cancel_shipment,
    do_manifest,
    fetch_orders,
    fetch_version,
    save_label,
)


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
        return book_shipment(orders, self.config)

    def cancel_shipment(self, order_ident: str | int) -> DeleteOrdersResource:
        return cancel_shipment(str(order_ident), self.config)

    def fetch_orders(self):
        return fetch_orders(self.config)

    def get_label(self, order_idents: str, outpath):
        return save_label(order_idents, outpath, self.config)

    def do_manifest(self):
        return do_manifest(self.config)

    def fetch_version(self):
        return fetch_version(self.config)

    def cancel_all_orders(self, really=False) -> DeleteOrdersResource:
        """Cancels ALL orders on the system - use with care / must pass really-True to work"""
        if not really:
            raise ValueError('Not cancelling orders, pass really=True to cancel')
        res = self.fetch_orders()
        if res.order_ident_string:
            response = self.cancel_shipment(res.order_ident_string)
            return response
        raise ValueError('No order idents in response')
