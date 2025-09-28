from pydantic import ConfigDict, Field

from royal_mail_click_and_drop import (
    Configuration,
    CreateOrdersRequest,
    CreateOrdersResponse,
    DeleteOrdersResource,
)
from royal_mail_click_and_drop.config import royal_mail_settings
from royal_mail_click_and_drop.models.base import RMBaseModel
from royal_mail_click_and_drop.v2.actions import (
    book_shipment,
    cancel_shipment,
    do_manifest,
    fetch_orders,
    fetch_version,
    get_label,
)


class RoyalMailClient(RMBaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)
    config: Configuration = Field(default_factory=lambda: royal_mail_settings().config)

    def book_shipment(self, orders: CreateOrdersRequest) -> CreateOrdersResponse:
        return book_shipment(orders, self.config)

    def cancel_shipment(self, order_ident: str) -> DeleteOrdersResource:
        return cancel_shipment(order_ident, self.config)

    def fetch_orders(self):
        return fetch_orders(self.config)

    def get_label(self, order_idents: str, outpath):
        return get_label(order_idents, outpath, self.config)

    def do_manifest(self):
        return do_manifest(self.config)

    def fetch_version(self):
        return fetch_version(self.config)

    def cancel_all_orders(self, really=False):
        res = self.fetch_orders()
        if res.order_ident_string and really:
            response = self.cancel_shipment(res.order_ident_string)
            return response
        print('Not cancelling orders, pass really=True to cancel')
        return None
