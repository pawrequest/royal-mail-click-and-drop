
from __future__ import annotations

from typing import ClassVar

from pydantic import StrictInt, StrictStr

from royal_mail_click_and_drop.models.base import RMBaseModel


class OrderErrorResponse(RMBaseModel):
    """
    OrderErrorResponse
    """
    account_order_number: StrictInt | None = None
    channel_order_reference: StrictStr | None = None
    code: StrictStr | None = None
    message: StrictStr | None = None
    __properties: ClassVar[list[str]] = ['accountOrderNumber', 'channelOrderReference', 'code', 'message']
