from __future__ import annotations

from typing import ClassVar, List

from pydantic import StrictStr

from royal_mail_click_and_drop.models.base import RMBaseModel


class OrderFieldResponse(RMBaseModel):
    field_name: StrictStr | None = None
    value: StrictStr | None = None
    __properties: ClassVar[List[str]] = ["fieldName", "value"]
