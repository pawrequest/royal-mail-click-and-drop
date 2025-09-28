
from __future__ import annotations

from typing import ClassVar, List

from pydantic import Field
from typing_extensions import Annotated

from royal_mail_click_and_drop.models.address import Address
from royal_mail_click_and_drop.models.base import RMBaseModel


class RecipientDetailsRequest(RMBaseModel):
    address: Address | None = None
    phone_number: Annotated[str, Field(strict=True, max_length=25)] | None = None
    email_address: Annotated[str, Field(strict=True, max_length=254)] | None = None
    address_book_reference: Annotated[str, Field(strict=True, max_length=100)] | None = Field(default=None, description="The presence or not of <b>addressBookReference</b> and a valid <b>recipient address object</b> in the request body will determine which of the following behaviours occur:-</br></br>1) addressBookReference <b>provided</b> and a valid recipient address object <b>provided</b> - In addition to the provided recipient address fields being used for the order creation, an existing account Address Book Reference with matching addressBookReference will be overwritten with all provided recipient address fields, including phone and email. If no existing account Address Book Reference with matching addressBookReference can be found then a new one will be created with the provided addressBookReference and address fields, including phone and email.</br>2) addressBookReference <b>provided</b> and a valid recipient address object <b>not provided</b> - An account Address Book Reference with the provided addressBookReference will be used for the order if it exists.</br>3) addressBookReference <b>not provided</b> and a valid recipient address object <b>provided</b> - All provided recipient address fields, including phone and email, will be used for the order creation.</br>4) All other scenarios will result in a validation error.")
    __properties: ClassVar[List[str]] = ["address", "phoneNumber", "emailAddress", "addressBookReference"]
