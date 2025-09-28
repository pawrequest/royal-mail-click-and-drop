
from __future__ import annotations

from typing import ClassVar, List

from royal_mail_click_and_drop.models.order_update_error import OrderUpdateError
from royal_mail_click_and_drop.models.updated_order_info import UpdatedOrderInfo
from royal_mail_click_and_drop.models.base import RMBaseModel


class UpdateOrderStatusResponse(RMBaseModel):
    updated_orders: List[UpdatedOrderInfo] | None = None
    errors: List[OrderUpdateError] | None = None
    __properties: ClassVar[List[str]] = ["updatedOrders", "errors"]
