
from __future__ import annotations

from typing import ClassVar, List

from royal_mail_click_and_drop.models.update_order_status_request import UpdateOrderStatusRequest
from royal_mail_click_and_drop.models.base import RMBaseModel


class UpdateOrdersStatusRequest(RMBaseModel):
    items: List[UpdateOrderStatusRequest] | None = None
    __properties: ClassVar[List[str]] = ["items"]
