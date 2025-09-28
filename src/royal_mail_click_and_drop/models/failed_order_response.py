
from __future__ import annotations

from typing import ClassVar, List

from royal_mail_click_and_drop.models.create_orders_request import CreateOrderRequest

from royal_mail_click_and_drop.models.create_order_error_response import CreateOrderErrorResponse
from royal_mail_click_and_drop.models.base import RMBaseModel


class FailedOrderResponse(RMBaseModel):
    order: CreateOrderRequest | None = None
    errors: List[CreateOrderErrorResponse] | None = None
    __properties: ClassVar[List[str]] = ["order", "errors"]
