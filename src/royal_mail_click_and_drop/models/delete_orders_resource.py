from __future__ import annotations

from typing import ClassVar

from royal_mail_click_and_drop.models.deleted_order_info import DeletedOrderInfo
from royal_mail_click_and_drop.models.order_error_info import OrderErrorInfo
from royal_mail_click_and_drop.models.base import RMBaseModel


class DeleteOrdersResource(RMBaseModel):
    deleted_orders: list[DeletedOrderInfo] | None = None
    errors: list[OrderErrorInfo] | None = None

    @property
    def deleted_order_idents(self):
        return ','.join(str(_.order_identifier) for _ in self.deleted_orders)

    __properties: ClassVar[list[str]] = ['deletedOrders', 'errors']
