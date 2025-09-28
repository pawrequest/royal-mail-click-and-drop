
from __future__ import annotations

from typing import ClassVar, List

from pydantic import Field
from typing_extensions import Annotated
from royal_mail_click_and_drop.models.address import Address

from royal_mail_click_and_drop.models.base import RMBaseModel


class BillingDetailsRequest(RMBaseModel):
    """
    <b>Billing</b> along with <b>billing.address</b> objects are required in specific case when 'Use shipping address for billing address' setting is set to 'false' and 'Recipient.AddressBookReference' is provided.
    """ # noqa: E501
    address: Address | None = None
    phone_number: Annotated[str, Field(strict=True, max_length=25)] | None = None
    email_address: Annotated[str, Field(strict=True, max_length=254)] | None = None
    __properties: ClassVar[List[str]] = ["address", "phoneNumber", "emailAddress"]
