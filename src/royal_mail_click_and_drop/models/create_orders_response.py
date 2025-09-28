
from __future__ import annotations

from typing import ClassVar, List

from pydantic import StrictInt

from royal_mail_click_and_drop.models.create_order_response import CreateOrderResponse
from royal_mail_click_and_drop.models.failed_order_response import FailedOrderResponse
from royal_mail_click_and_drop.models.base import RMBaseModel


class CreateOrdersResponse(RMBaseModel):
    success_count: StrictInt | None = None
    errors_count: StrictInt | None = None
    created_orders: List[CreateOrderResponse] | None = None
    failed_orders: List[FailedOrderResponse] | None = None
    __properties: ClassVar[List[str]] = ["successCount", "errorsCount", "createdOrders", "failedOrders"]
