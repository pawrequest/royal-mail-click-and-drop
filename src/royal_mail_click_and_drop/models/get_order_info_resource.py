
from __future__ import annotations

from datetime import datetime
from typing import ClassVar, List

from pydantic import StrictInt, StrictStr

from royal_mail_click_and_drop.models.base import RMBaseModel


class GetOrderInfoResource(RMBaseModel):
    """
    GetOrderInfoResource
    """ # noqa: E501
    order_identifier: StrictInt
    order_reference: StrictStr | None = None
    created_on: datetime
    order_date: datetime | None = None
    printed_on: datetime | None = None
    manifested_on: datetime | None = None
    shipped_on: datetime | None = None
    tracking_number: StrictStr | None = None
    __properties: ClassVar[List[str]] = ["orderIdentifier", "orderReference", "createdOn", "orderDate", "printedOn", "manifestedOn", "shippedOn", "trackingNumber"]
