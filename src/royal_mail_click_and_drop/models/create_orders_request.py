from __future__ import annotations

from datetime import datetime
# from datetime import datetime
from typing import ClassVar, List, Optional, Union

from pydantic import Field, StrictBool, StrictFloat, StrictInt
from typing_extensions import Annotated

from royal_mail_click_and_drop.models.address import Contact
from royal_mail_click_and_drop.models.base import RMBaseModel
from royal_mail_click_and_drop.models.billing_details_request import BillingDetailsRequest
from royal_mail_click_and_drop.models.importer import Importer
from royal_mail_click_and_drop.models.label_generation_request import LabelGenerationRequest
from royal_mail_click_and_drop.models.postage_details_request import PostageDetailsRequest
from royal_mail_click_and_drop.models.sender_details_request import SenderDetailsRequest
from royal_mail_click_and_drop.models.shipment_package_request import ShipmentPackageRequest
from royal_mail_click_and_drop.models.tag_request import TagRequest


class CreateOrderRequest(RMBaseModel):
    order_reference: Optional[Annotated[str, Field(strict=True, max_length=40)]] = None
    is_recipient_a_business: Optional[StrictBool] = Field(default=None, description="Indicates if the recipient is a business or not. Mandatory for Business senders on orders shipping from Great Britain to Northern Ireland, which require additional information for B2B shipments. (Business senders are OBA accounts and OLP accounts declaring themselves as a Business sender).")
    recipient: Contact
    sender: Optional[SenderDetailsRequest] = None
    billing: Optional[BillingDetailsRequest] = None
    packages: Optional[List[ShipmentPackageRequest]] = None
    order_date: datetime
    planned_despatch_date: Optional[datetime] = None
    special_instructions: Optional[Annotated[str, Field(strict=True, max_length=500)]] = None
    subtotal: Union[Annotated[float, Field(multiple_of=0.01, le=999999, strict=True, ge=0)], Annotated[int, Field(le=999999, strict=True, ge=0)]] | None = Field(default = None, description="The total value of all the goods in the order, excluding tax. This should not include retail shipping costs") # todo is this optional?
    shipping_cost_charged: Union[Annotated[float, Field(multiple_of=0.01, le=999999, strict=True, ge=0)], Annotated[int, Field(le=999999, strict=True, ge=0)]] | None = Field(default = None, description="The shipping costs you charged to your customer") # todo is this optional?
    other_costs: Optional[Union[Annotated[float, Field(multiple_of=0.01, le=999999, strict=True, ge=0)], Annotated[int, Field(le=999999, strict=True, ge=0)]]] = None
    customs_duty_costs: Optional[Union[Annotated[float, Field(multiple_of=0.01, le=99999.99, strict=True, ge=0)], Annotated[int, Field(le=99999, strict=True, ge=0)]]] = Field(default=None, description="Customs Duty Costs is only supported in DDP (Delivery Duty Paid) services")
    total: Union[Annotated[float, Field(multiple_of=0.01, le=999999, strict=True, ge=0)], Annotated[int, Field(le=999999, strict=True, ge=0)]] | None= Field(default=None, description="The sum of order subtotal, tax and retail shipping costs") # todo is this optional?
    currency_code: Optional[Annotated[str, Field(strict=True, max_length=3)]] = None
    postage_details: Optional[PostageDetailsRequest] = None
    tags: Optional[List[TagRequest]] = None
    label: Optional[LabelGenerationRequest] = None
    order_tax: Optional[Union[Annotated[float, Field(multiple_of=0.01, le=999999, strict=True, ge=0)], Annotated[int, Field(le=999999, strict=True, ge=0)]]] = Field(default=None, description="The total tax charged for the order")
    contains_dangerous_goods: Optional[StrictBool] = Field(default=None, description="Indicates that the package contents contain a dangerous goods item")
    dangerous_goods_un_code: Optional[Annotated[str, Field(strict=True, max_length=4)]] = Field(default=None, description="UN Code of the dangerous goods")
    dangerous_goods_description: Optional[Union[Annotated[float, Field(strict=True)], Annotated[int, Field(strict=True)]]] = Field(default=None, description="Description of the dangerous goods")
    dangerous_goods_quantity: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Quantity or volume of the dangerous goods")
    importer: Optional[Importer] = None
    __properties: ClassVar[List[str]] = ["orderReference", "isRecipientABusiness", "recipient", "sender", "billing", "packages", "orderDate", "plannedDespatchDate", "specialInstructions", "subtotal", "shippingCostCharged", "otherCosts", "customsDutyCosts", "total", "currencyCode", "postageDetails", "tags", "label", "orderTax", "containsDangerousGoods", "dangerousGoodsUnCode", "dangerousGoodsDescription", "dangerousGoodsQuantity", "importer"]



class CreateOrdersRequest(RMBaseModel):
    items: List[CreateOrderRequest]
    __properties: ClassVar[List[str]] = ["items"]
