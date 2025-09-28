
from __future__ import annotations

from typing import ClassVar, List

from pydantic import StrictInt, StrictStr

from royal_mail_click_and_drop.models.base import RMBaseModel


class OrderErrorResponse(RMBaseModel):
    """
    OrderErrorResponse
    """ # noqa: E501
    account_order_number: StrictInt | None = None
    channel_order_reference: StrictStr | None = None
    code: StrictStr | None = None
    message: StrictStr | None = None
    __properties: ClassVar[List[str]] = ["accountOrderNumber", "channelOrderReference", "code", "message"]
