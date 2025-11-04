from enum import StrEnum
from typing import Annotated

from pydantic import StringConstraints


def str_length_const(length: int):
    return Annotated[
        str,
        StringConstraints(strip_whitespace=True, max_length=length),
    ]


class SendNotifcationsTo(StrEnum):
    SENDER = 'sender'
    RECIPIENT = 'recipient'
    BILLING = 'billing'


class RoyalMailPackageFormat(StrEnum):
    PARCEL = 'parcel'
