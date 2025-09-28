
from __future__ import annotations

from typing import ClassVar, List

from pydantic import StrictInt, StrictStr

from royal_mail_click_and_drop.models.base import RMBaseModel


class OrderErrorInfo(RMBaseModel):
    """
    OrderErrorInfo
    """ # noqa: E501
    order_identifier: StrictInt | None = None
    order_reference: StrictStr | None = None
    code: StrictStr | None = None
    message: StrictStr | None = None
    __properties: ClassVar[List[str]] = ["orderIdentifier", "orderReference", "code", "message"]
