from __future__ import annotations

from datetime import datetime
from typing import ClassVar, List

from pydantic import Field, StrictInt, StrictStr, field_validator

from royal_mail_click_and_drop.models.base import RMBaseModel


class UpdateOrderStatusRequest(RMBaseModel):
    order_identifier: StrictInt | None = None
    order_reference: StrictStr | None = None
    status: StrictStr | None = Field(
        default=None,
        description='<br/> "<i>despatchedByOtherCourier</i> ": <b>Reserved for ChannelShipper customers only - please visit <a href="https://channelshipper.com/" target="_self">ChannelShipper.com</a> for more information</b>  "<i>new</i> ": This will remove the order from its batch. Order information will not be lost during this process.  Please be aware labels generated on orders which are then set to "new" (reset) are no longer valid and must be destroyed. If the order is required to be despatched after setting to "new" status, a new label must be generated to attach to the item.  Cancelled label information is automatically shared with Royal Mail Revenue Protection, and should a cancelled label be identified on an item in the Royal Mail Network, you will be charged on your account and an additional handling fee applied. ',
    )
    tracking_number: StrictStr | None = None
    despatch_date: datetime | None = None
    shipping_carrier: StrictStr | None = None
    shipping_service: StrictStr | None = None
    __properties: ClassVar[List[str]] = [
        'orderIdentifier',
        'orderReference',
        'status',
        'trackingNumber',
        'despatchDate',
        'shippingCarrier',
        'shippingService',
    ]

    @field_validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in {'new', 'despatchedByOtherCourier', 'despatched'}:
            raise ValueError(
                "must be one of enum values ('new', 'despatchedByOtherCourier', 'despatched')"
            )
        return value
