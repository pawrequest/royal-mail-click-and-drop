from __future__ import annotations

from typing import ClassVar

from pydantic import StrictInt, Field

from royal_mail_click_and_drop.models.create_order_response import CreateOrderResponse
from royal_mail_click_and_drop.models.failed_order_response import FailedOrderResponse
from royal_mail_click_and_drop.models.base import RMBaseModel


class CreateOrdersResponse(RMBaseModel):
    success_count: StrictInt | None = None
    errors_count: StrictInt | None = None
    created_orders: list[CreateOrderResponse] = Field(default_factory=list)
    failed_orders: list[FailedOrderResponse] = Field(default_factory=list)

    @property
    def created_orders_idents(self) -> list[int]:
        return [_.order_identifier for _ in self.created_orders]

    @property
    def created_orders_idents_str(self) -> str:
        return ','.join(str(_) for _ in self.created_orders_idents)

    __properties: ClassVar[list[str]] = ['successCount', 'errorsCount', 'createdOrders', 'failedOrders']
