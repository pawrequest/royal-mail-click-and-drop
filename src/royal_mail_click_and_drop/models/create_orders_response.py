
from __future__ import annotations

from typing import ClassVar

from pydantic import StrictInt

from royal_mail_click_and_drop.models.create_order_response import CreateOrderResponse
from royal_mail_click_and_drop.models.failed_order_response import FailedOrderResponse
from royal_mail_click_and_drop.models.base import RMBaseModel


class CreateOrdersResponse(RMBaseModel):
    success_count: StrictInt | None = None
    errors_count: StrictInt | None = None
    created_orders: list[CreateOrderResponse] | None = None
    failed_orders: list[FailedOrderResponse] | None = None
    __properties: ClassVar[list[str]] = ['successCount', 'errorsCount', 'createdOrders', 'failedOrders']
