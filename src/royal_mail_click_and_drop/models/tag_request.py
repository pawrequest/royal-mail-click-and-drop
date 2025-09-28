
from __future__ import annotations

from typing import ClassVar, List

from pydantic import Field
from typing_extensions import Annotated

from royal_mail_click_and_drop.models.base import RMBaseModel


class TagRequest(RMBaseModel):
    key: Annotated[str, Field(strict=True, max_length=100)] | None = None
    value: Annotated[str, Field(strict=True, max_length=100)] | None = None
    __properties: ClassVar[List[str]] = ["key", "value"]
