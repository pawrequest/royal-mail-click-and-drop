from __future__ import annotations

from typing import ClassVar, List

from pydantic import Field, StrictInt, StrictStr

from royal_mail_click_and_drop.models.base import RMBaseModel


class OrderUpdateError(RMBaseModel):
    order_identifier: StrictInt | None = None
    order_reference: StrictStr | None = None
    status: StrictStr | None = Field(default=None, description="Current status of the order")
    code: StrictStr | None = None
    message: StrictStr | None = None
    __properties: ClassVar[List[str]] = ["orderIdentifier", "orderReference", "status", "code", "message"]
