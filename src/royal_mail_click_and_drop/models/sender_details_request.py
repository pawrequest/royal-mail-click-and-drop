
from __future__ import annotations

from typing import ClassVar

from pydantic import Field
from typing import Annotated

from royal_mail_click_and_drop.models.base import RMBaseModel


class SenderDetailsRequest(RMBaseModel):
    trading_name: Annotated[str, Field(strict=True, max_length=250)] | None = None
    phone_number: Annotated[str, Field(strict=True, max_length=25)] | None = None
    email_address: Annotated[str, Field(strict=True, max_length=254)] | None = None
    __properties: ClassVar[list[str]] = ['tradingName', 'phoneNumber', 'emailAddress']
