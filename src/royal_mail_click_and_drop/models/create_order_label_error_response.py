
from __future__ import annotations

from typing import ClassVar

from pydantic import StrictStr

from royal_mail_click_and_drop.models.base import RMBaseModel


class CreateOrderLabelErrorResponse(RMBaseModel):
    message: StrictStr | None = None
    __properties: ClassVar[list[str]] = ['message']
