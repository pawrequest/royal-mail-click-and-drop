
from __future__ import annotations

from typing import ClassVar

from pydantic import Field
from typing import Annotated
from royal_mail_click_and_drop.models.address import AddressRequest

from royal_mail_click_and_drop.models.base import RMBaseModel


class BillingDetailsRequest(RMBaseModel):
    """
    <b>Billing</b> along with <b>billing.address</b> objects are required in specific case when 'Use shipping address for billing address' setting is set to 'false' and 'Recipient.AddressBookReference' is provided.
    """
    address: AddressRequest | None = None
    phone_number: Annotated[str, Field(strict=True, max_length=25)] | None = None
    email_address: Annotated[str, Field(strict=True, max_length=254)] | None = None
    __properties: ClassVar[list[str]] = ['address', 'phoneNumber', 'emailAddress']
