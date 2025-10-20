
from __future__ import annotations

from typing import ClassVar

from pydantic import Field
from typing import Annotated

from royal_mail_click_and_drop.models.base import RMBaseModel


class GetTagDetailsResult(RMBaseModel):
    """
    GetTagDetailsResult
    """
    key: Annotated[str, Field(strict=True, max_length=100)] | None = None
    value: Annotated[str, Field(strict=True, max_length=100)] | None = None
    __properties: ClassVar[list[str]] = ['key', 'value']
