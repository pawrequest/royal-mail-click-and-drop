
from __future__ import annotations

from typing import ClassVar

from pydantic import Field, StrictStr
from typing import Annotated

from royal_mail_click_and_drop.models.base import RMBaseModel


class GetPostalDetailsResult(RMBaseModel):
    """
    GetPostalDetailsResult
    """
    title: StrictStr | None = None
    first_name: StrictStr | None = None
    last_name: StrictStr | None = None
    company_name: StrictStr | None = None
    address_line1: StrictStr | None = None
    address_line2: StrictStr | None = None
    address_line3: StrictStr | None = None
    city: StrictStr | None = None
    county: StrictStr | None = None
    postcode: StrictStr | None = None
    country_code: Annotated[str, Field(strict=True, max_length=3)] | None = None
    phone_number: StrictStr | None = None
    email_address: StrictStr | None = None
    __properties: ClassVar[list[str]] = ['title', 'firstName', 'lastName', 'companyName', 'addressLine1', 'addressLine2', 'addressLine3', 'city', 'county', 'postcode', 'countryCode', 'phoneNumber', 'emailAddress']
