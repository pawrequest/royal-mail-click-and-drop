from __future__ import annotations

from typing import ClassVar

from royal_mail_click_and_drop.models.deleted_order_info import DeletedOrderInfo
from royal_mail_click_and_drop.models.order_error_info import OrderErrorInfo
from royal_mail_click_and_drop.models.base import RMBaseModel


class DeleteOrdersResource(RMBaseModel):
    deleted_orders: list[DeletedOrderInfo] | None = None
    errors: list[OrderErrorInfo] | None = None

    @property
    def idents(self) -> list[int]:
        return [_.order_identifier for _ in self.deleted_orders]

    @property
    def idents_str(self) -> str:
        return ','.join(str(_) for _ in self.idents)

    __properties: ClassVar[list[str]] = ['deletedOrders', 'errors']
