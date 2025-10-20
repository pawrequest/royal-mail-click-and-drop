
from __future__ import annotations

from datetime import datetime
from typing import ClassVar

from pydantic import Field, StrictBool, StrictFloat, StrictInt, StrictStr
from typing import Annotated

from royal_mail_click_and_drop.models.get_order_line_result import GetOrderLineResult
from royal_mail_click_and_drop.models.get_postal_details_result import GetPostalDetailsResult
from royal_mail_click_and_drop.models.get_shipping_details_result import GetShippingDetailsResult
from royal_mail_click_and_drop.models.get_tag_details_result import GetTagDetailsResult
from royal_mail_click_and_drop.models.base import RMBaseModel


class GetOrderDetailsResource(RMBaseModel):
    """
    GetOrderDetailsResource
    """
    order_identifier: StrictInt | None = None
    order_status: StrictStr | None = None
    created_on: datetime | None = None
    printed_on: datetime | None = None
    shipped_on: datetime | None = None
    postage_applied_on: datetime | None = None
    manifested_on: datetime | None = None
    order_date: datetime | None = None
    despatched_by_other_courier_on: datetime | None = None
    trading_name: StrictStr | None = None
    channel: StrictStr | None = None
    marketplace_type_name: StrictStr | None = None
    department: StrictStr | None = None
    air_number: StrictStr | None = None
    requires_export_license: StrictBool | None = None
    commercial_invoice_number: StrictStr | None = None
    commercial_invoice_date: datetime | None = None
    order_reference: StrictStr | None = None
    channel_shipping_method: StrictStr | None = None
    special_instructions: StrictStr | None = None
    picker_special_instructions: StrictStr | None = None
    subtotal: StrictFloat | StrictInt = Field(description='The total value of all the goods in the order, excluding tax')
    shipping_cost_charged: StrictFloat | StrictInt = Field(description='The shipping costs you charged to your customer')
    order_discount: StrictFloat | StrictInt
    total: StrictFloat | StrictInt = Field(description='The sum of order subtotal, tax and retail shipping costs')
    weight_in_grams: StrictInt
    package_size: StrictStr | None = None
    account_batch_number: StrictStr | None = None
    currency_code: Annotated[str, Field(strict=True, max_length=3)] | None = None
    shipping_details: GetShippingDetailsResult
    shipping_info: GetPostalDetailsResult
    billing_info: GetPostalDetailsResult
    order_lines: list[GetOrderLineResult]
    tags: list[GetTagDetailsResult] | None = None
    __properties: ClassVar[list[str]] = ['orderIdentifier', 'orderStatus', 'createdOn', 'printedOn', 'shippedOn', 'postageAppliedOn', 'manifestedOn', 'orderDate', 'despatchedByOtherCourierOn', 'tradingName', 'channel', 'marketplaceTypeName', 'department', 'AIRNumber', 'requiresExportLicense', 'commercialInvoiceNumber', 'commercialInvoiceDate', 'orderReference', 'channelShippingMethod', 'specialInstructions', 'pickerSpecialInstructions', 'subtotal', 'shippingCostCharged', 'orderDiscount', 'total', 'weightInGrams', 'packageSize', 'accountBatchNumber', 'currencyCode', 'shippingDetails', 'shippingInfo', 'billingInfo', 'orderLines', 'tags']
