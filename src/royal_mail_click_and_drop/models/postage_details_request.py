from __future__ import annotations

from datetime import datetime
from typing import ClassVar, List

from pydantic import Field, StrictBool, StrictStr, field_validator
from typing_extensions import Annotated

from royal_mail_click_and_drop.models.base import RMBaseModel


class PostageDetailsRequest(RMBaseModel):
    """
    PostageDetailsRequest
    """ # noqa: E501
    send_notifications_to: StrictStr | None = None
    service_code: Annotated[str, Field(strict=True, max_length=10)] | None = None
    carrier_name: Annotated[str, Field(strict=True, max_length=50)] | None = None
    service_register_code: Annotated[str, Field(strict=True, max_length=2)] | None = None
    consequential_loss: Annotated[int, Field(le=10000, strict=True, ge=0)] | None = None
    receive_email_notification: StrictBool | None = None
    receive_sms_notification: StrictBool | None = None
    guaranteed_saturday_delivery: StrictBool | None = Field(default=None, description="This field has been deprecated")
    request_signature_upon_delivery: StrictBool | None = None
    is_local_collect: StrictBool | None = None
    safe_place: Annotated[str, Field(strict=True, max_length=90)] | None = None
    department: Annotated[str, Field(strict=True, max_length=150)] | None = None
    air_number: Annotated[str, Field(strict=True, max_length=50)] | None = Field(default=None, description="For B2B orders shipping from Great Britain to Northern Ireland, this field can be used to provide the Recipient UKIMs number.")
    ioss_number: Annotated[str, Field(strict=True, max_length=50)] | None = None
    requires_export_license: StrictBool | None = None
    commercial_invoice_number: Annotated[str, Field(strict=True, max_length=35)] | None = None
    commercial_invoice_date: datetime | None = None
    recipient_eori_number: StrictStr | None = None
    __properties: ClassVar[List[str]] = ["sendNotificationsTo", "serviceCode", "carrierName", "serviceRegisterCode", "consequentialLoss", "receiveEmailNotification", "receiveSmsNotification", "guaranteedSaturdayDelivery", "requestSignatureUponDelivery", "isLocalCollect", "safePlace", "department", "AIRNumber", "IOSSNumber", "requiresExportLicense", "commercialInvoiceNumber", "commercialInvoiceDate", "recipientEoriNumber"]

    @field_validator('send_notifications_to')
    def send_notifications_to_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in {'sender', 'recipient', 'billing'}:
            raise ValueError("must be one of enum values ('sender', 'recipient', 'billing')")
        return value
