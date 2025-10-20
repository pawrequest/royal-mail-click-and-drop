from __future__ import annotations

from datetime import datetime
from typing import ClassVar

from pydantic import Field, StrictBool, StrictFloat, StrictInt
from typing import Annotated

from royal_mail_click_and_drop.models.address import RecipientDetailsRequest
from royal_mail_click_and_drop.models.base import RMBaseModel
from royal_mail_click_and_drop.models.billing_details_request import BillingDetailsRequest
from royal_mail_click_and_drop.models.importer import Importer
from royal_mail_click_and_drop.models.label_generation_request import LabelGenerationRequest
from royal_mail_click_and_drop.models.postage_details_request import PostageDetailsRequest
from royal_mail_click_and_drop.models.sender_details_request import SenderDetailsRequest
from royal_mail_click_and_drop.models.shipment_package_request import ShipmentPackageRequest
from royal_mail_click_and_drop.models.tag_request import TagRequest


class CreateOrderRequest(RMBaseModel):
    recipient: RecipientDetailsRequest
    order_date: datetime
    subtotal: (
        Annotated[float, Field(multiple_of=0.01, le=999999, strict=True, ge=0)] | Annotated[int, Field(le=999999, strict=True, ge=0)]
        | None
    ) = Field(
        default=None,
        description='The total value of all the goods in the order, excluding tax. This should not include retail shipping costs',
    )  # todo is this optional?
    total: (
        Annotated[float, Field(multiple_of=0.01, le=999999, strict=True, ge=0)] | Annotated[int, Field(le=999999, strict=True, ge=0)]
        | None
    ) = Field(
        default=None, description='The sum of order subtotal, tax and retail shipping costs'
    )  # todo is this optional?
    packages: list[ShipmentPackageRequest] | None = None
    billing: BillingDetailsRequest | None = None

    order_reference: Annotated[str, Field(strict=True, max_length=40)] | None = None
    planned_despatch_date: datetime | None = None
    sender: SenderDetailsRequest | None = None
    postage_details: PostageDetailsRequest | None = None

    is_recipient_a_business: StrictBool | None = Field(
        default=None,
        description='Indicates if the recipient is a business or not. Mandatory for Business senders on orders shipping from Great Britain to Northern Ireland, which require additional information for B2B shipments. (Business senders are OBA accounts and OLP accounts declaring themselves as a Business sender).',
    )
    special_instructions: Annotated[str, Field(strict=True, max_length=500)] | None = None
    shipping_cost_charged: (
        Annotated[float, Field(multiple_of=0.01, le=999999, strict=True, ge=0)] | Annotated[int, Field(le=999999, strict=True, ge=0)]
        | None
    ) = Field(default=None, description='The shipping costs you charged to your customer')  # todo is this optional?
    other_costs: Annotated[float, Field(multiple_of=0.01, le=999999, strict=True, ge=0)] | Annotated[int, Field(le=999999, strict=True, ge=0)] | None = None
    customs_duty_costs: Annotated[float, Field(multiple_of=0.01, le=99999.99, strict=True, ge=0)] | Annotated[int, Field(le=99999, strict=True, ge=0)] | None = Field(default=None, description='Customs Duty Costs is only supported in DDP (Delivery Duty Paid) services')
    currency_code: Annotated[str, Field(strict=True, max_length=3)] | None = None
    tags: list[TagRequest] | None = None
    label: LabelGenerationRequest | None = None
    order_tax: Annotated[float, Field(multiple_of=0.01, le=999999, strict=True, ge=0)] | Annotated[int, Field(le=999999, strict=True, ge=0)] | None = Field(default=None, description='The total tax charged for the order')
    contains_dangerous_goods: StrictBool | None = Field(
        default=None, description='Indicates that the package contents contain a dangerous goods item'
    )
    dangerous_goods_un_code: Annotated[str, Field(strict=True, max_length=4)] | None = Field(
        default=None, description='UN Code of the dangerous goods'
    )
    dangerous_goods_description: Annotated[float, Field(strict=True)] | Annotated[int, Field(strict=True)] | None = Field(default=None, description='Description of the dangerous goods')
    dangerous_goods_quantity: StrictFloat | StrictInt | None = Field(
        default=None, description='Quantity or volume of the dangerous goods'
    )
    importer: Importer | None = None
    __properties: ClassVar[list[str]] = [
        'orderReference',
        'isRecipientABusiness',
        'recipient',
        'sender',
        'billing',
        'packages',
        'orderDate',
        'plannedDespatchDate',
        'specialInstructions',
        'subtotal',
        'shippingCostCharged',
        'otherCosts',
        'customsDutyCosts',
        'total',
        'currencyCode',
        'postageDetails',
        'tags',
        'label',
        'orderTax',
        'containsDangerousGoods',
        'dangerousGoodsUnCode',
        'dangerousGoodsDescription',
        'dangerousGoodsQuantity',
        'importer',
    ]


class CreateOrdersRequest(RMBaseModel):
    items: list[CreateOrderRequest]
    __properties: ClassVar[list[str]] = ['items']
