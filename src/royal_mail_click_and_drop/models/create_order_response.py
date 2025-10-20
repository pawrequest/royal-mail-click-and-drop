
from __future__ import annotations

from datetime import datetime
from typing import ClassVar

from pydantic import Field, StrictInt, StrictStr

from royal_mail_click_and_drop.models.create_order_label_error_response import CreateOrderLabelErrorResponse
from royal_mail_click_and_drop.models.base import RMBaseModel


class CreateOrderResponse(RMBaseModel):
    order_identifier: StrictInt = None
    order_reference: StrictStr | None = None
    created_on: datetime = None
    order_date: datetime | None = None
    printed_on: datetime | None = None
    manifested_on: datetime | None = None
    shipped_on: datetime | None = None
    tracking_number: StrictStr | None = None
    label: StrictStr | None = Field(default=None, description='label in format base64 string')
    label_errors: list[CreateOrderLabelErrorResponse] | None = None
    generated_documents: list[StrictStr] | None = None
    __properties: ClassVar[list[str]] = ['orderIdentifier', 'orderReference', 'createdOn', 'orderDate', 'printedOn', 'manifestedOn', 'shippedOn', 'trackingNumber', 'label', 'labelErrors', 'generatedDocuments']
