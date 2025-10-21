from __future__ import annotations

from typing import ClassVar

from pydantic import StrictStr

from royal_mail_click_and_drop.models.get_order_info_resource import GetOrderInfoResource
from royal_mail_click_and_drop.models.base import RMBaseModel


class GetOrdersResponse(RMBaseModel):
    """
    GetOrdersResponse
    """

    orders: list[GetOrderInfoResource] | None = None
    continuation_token: StrictStr | None = None
    __properties: ClassVar[list[str]] = ['orders', 'continuationToken']

    @property
    def order_ident_string(self):
        return ';'.join(str(_.order_identifier) for _ in self.orders)

