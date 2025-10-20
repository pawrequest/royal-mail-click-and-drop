
from __future__ import annotations

from typing import ClassVar

from pydantic import Field
from typing import Annotated

from royal_mail_click_and_drop.models.base import RMBaseModel


class Importer(RMBaseModel):
    """
    Importer
    """
    company_name: Annotated[str, Field(strict=True, max_length=100)] | None = None
    address_line1: Annotated[str, Field(strict=True, max_length=100)] | None = None
    address_line2: Annotated[str, Field(strict=True, max_length=100)] | None = None
    address_line3: Annotated[str, Field(strict=True, max_length=100)] | None = None
    city: Annotated[str, Field(strict=True, max_length=100)] | None = None
    postcode: Annotated[str, Field(strict=True, max_length=20)] | None = None
    country: Annotated[str, Field(strict=True, max_length=100)] | None = None
    business_name: Annotated[str, Field(strict=True, max_length=100)] | None = None
    contact_name: Annotated[str, Field(strict=True, max_length=100)] | None = None
    phone_number: Annotated[str, Field(strict=True, max_length=25)] | None = None
    email_address: Annotated[str, Field(strict=True, max_length=254)] | None = None
    vat_number: Annotated[str, Field(strict=True, max_length=15)] | None = None
    tax_code: Annotated[str, Field(strict=True, max_length=25)] | None = None
    eori_number: Annotated[str, Field(strict=True, max_length=18)] | None = None
    __properties: ClassVar[list[str]] = ['companyName', 'addressLine1', 'addressLine2', 'addressLine3', 'city', 'postcode', 'country', 'businessName', 'contactName', 'phoneNumber', 'emailAddress', 'vatNumber', 'taxCode', 'eoriNumber']
