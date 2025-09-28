
from __future__ import annotations

from typing import ClassVar, List

from pydantic import StrictStr

from royal_mail_click_and_drop.models.base import RMBaseModel


class ErrorResponse(RMBaseModel):
    """
    ErrorResponse
    """ # noqa: E501
    code: StrictStr | None = None
    message: StrictStr
    details: StrictStr | None = None
    __properties: ClassVar[List[str]] = ["code", "message", "details"]
