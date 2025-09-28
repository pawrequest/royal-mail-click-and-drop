
from __future__ import annotations

from datetime import datetime
from typing import ClassVar, List, Union

from pydantic import StrictBool, StrictFloat, StrictInt, StrictStr

from royal_mail_click_and_drop.models.base import RMBaseModel


class GetShippingDetailsResult(RMBaseModel):
    """
    GetShippingDetailsResult
    """ # noqa: E501
    shipping_cost: Union[StrictFloat, StrictInt]
    tracking_number: StrictStr | None = None
    shipping_tracking_status: StrictStr | None = None
    service_code: StrictStr | None = None
    shipping_service: StrictStr | None = None
    shipping_carrier: StrictStr | None = None
    receive_email_notification: StrictBool | None = None
    receive_sms_notification: StrictBool | None = None
    guaranteed_saturday_delivery: StrictBool | None = None
    request_signature_upon_delivery: StrictBool | None = None
    is_local_collect: StrictBool | None = None
    shipping_update_success_date: datetime | None = None
    __properties: ClassVar[List[str]] = ["shippingCost", "trackingNumber", "shippingTrackingStatus", "serviceCode", "shippingService", "shippingCarrier", "receiveEmailNotification", "receiveSmsNotification", "guaranteedSaturdayDelivery", "requestSignatureUponDelivery", "isLocalCollect", "shippingUpdateSuccessDate"]
