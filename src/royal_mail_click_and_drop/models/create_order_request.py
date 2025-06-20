# coding: utf-8

"""
    ChannelShipper & Royal Mail Public API

    Import your orders, retrieve your orders and generate labels.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictFloat, StrictInt
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing_extensions import Annotated
from royal_mail_click_and_drop.models.billing_details_request import BillingDetailsRequest
from royal_mail_click_and_drop.models.importer import Importer
from royal_mail_click_and_drop.models.label_generation_request import LabelGenerationRequest
from royal_mail_click_and_drop.models.postage_details_request import PostageDetailsRequest
from royal_mail_click_and_drop.models.recipient_details_request import RecipientDetailsRequest
from royal_mail_click_and_drop.models.sender_details_request import SenderDetailsRequest
from royal_mail_click_and_drop.models.shipment_package_request import ShipmentPackageRequest
from royal_mail_click_and_drop.models.tag_request import TagRequest
from typing import Optional, Set
from typing_extensions import Self

class CreateOrderRequest(BaseModel):
    """
    CreateOrderRequest
    """ # noqa: E501
    order_reference: Optional[Annotated[str, Field(strict=True, max_length=40)]] = Field(default=None, alias="orderReference")
    is_recipient_a_business: Optional[StrictBool] = Field(default=None, description="Indicates if the recipient is a business or not. Mandatory for Business senders on orders shipping from Great Britain to Northern Ireland, which require additional information for B2B shipments. (Business senders are OBA accounts and OLP accounts declaring themselves as a Business sender).", alias="isRecipientABusiness")
    recipient: RecipientDetailsRequest
    sender: Optional[SenderDetailsRequest] = None
    billing: Optional[BillingDetailsRequest] = None
    packages: Optional[List[ShipmentPackageRequest]] = None
    order_date: datetime = Field(alias="orderDate")
    planned_despatch_date: Optional[datetime] = Field(default=None, alias="plannedDespatchDate")
    special_instructions: Optional[Annotated[str, Field(strict=True, max_length=500)]] = Field(default=None, alias="specialInstructions")
    subtotal: Union[Annotated[float, Field(multiple_of=0.01, le=999999, strict=True, ge=0)], Annotated[int, Field(le=999999, strict=True, ge=0)]] = Field(description="The total value of all the goods in the order, excluding tax. This should not include retail shipping costs")
    shipping_cost_charged: Union[Annotated[float, Field(multiple_of=0.01, le=999999, strict=True, ge=0)], Annotated[int, Field(le=999999, strict=True, ge=0)]] = Field(description="The shipping costs you charged to your customer", alias="shippingCostCharged")
    other_costs: Optional[Union[Annotated[float, Field(multiple_of=0.01, le=999999, strict=True, ge=0)], Annotated[int, Field(le=999999, strict=True, ge=0)]]] = Field(default=None, alias="otherCosts")
    customs_duty_costs: Optional[Union[Annotated[float, Field(multiple_of=0.01, le=99999.99, strict=True, ge=0)], Annotated[int, Field(le=99999, strict=True, ge=0)]]] = Field(default=None, description="Customs Duty Costs is only supported in DDP (Delivery Duty Paid) services", alias="customsDutyCosts")
    total: Union[Annotated[float, Field(multiple_of=0.01, le=999999, strict=True, ge=0)], Annotated[int, Field(le=999999, strict=True, ge=0)]] = Field(description="The sum of order subtotal, tax and retail shipping costs")
    currency_code: Optional[Annotated[str, Field(strict=True, max_length=3)]] = Field(default=None, alias="currencyCode")
    postage_details: Optional[PostageDetailsRequest] = Field(default=None, alias="postageDetails")
    tags: Optional[List[TagRequest]] = None
    label: Optional[LabelGenerationRequest] = None
    order_tax: Optional[Union[Annotated[float, Field(multiple_of=0.01, le=999999, strict=True, ge=0)], Annotated[int, Field(le=999999, strict=True, ge=0)]]] = Field(default=None, description="The total tax charged for the order", alias="orderTax")
    contains_dangerous_goods: Optional[StrictBool] = Field(default=None, description="Indicates that the package contents contain a dangerous goods item", alias="containsDangerousGoods")
    dangerous_goods_un_code: Optional[Annotated[str, Field(strict=True, max_length=4)]] = Field(default=None, description="UN Code of the dangerous goods", alias="dangerousGoodsUnCode")
    dangerous_goods_description: Optional[Union[Annotated[float, Field(strict=True)], Annotated[int, Field(strict=True)]]] = Field(default=None, description="Description of the dangerous goods", alias="dangerousGoodsDescription")
    dangerous_goods_quantity: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Quantity or volume of the dangerous goods", alias="dangerousGoodsQuantity")
    importer: Optional[Importer] = None
    __properties: ClassVar[List[str]] = ["orderReference", "isRecipientABusiness", "recipient", "sender", "billing", "packages", "orderDate", "plannedDespatchDate", "specialInstructions", "subtotal", "shippingCostCharged", "otherCosts", "customsDutyCosts", "total", "currencyCode", "postageDetails", "tags", "label", "orderTax", "containsDangerousGoods", "dangerousGoodsUnCode", "dangerousGoodsDescription", "dangerousGoodsQuantity", "importer"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of CreateOrderRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of recipient
        if self.recipient:
            _dict['recipient'] = self.recipient.to_dict()
        # override the default output from pydantic by calling `to_dict()` of sender
        if self.sender:
            _dict['sender'] = self.sender.to_dict()
        # override the default output from pydantic by calling `to_dict()` of billing
        if self.billing:
            _dict['billing'] = self.billing.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in packages (list)
        _items = []
        if self.packages:
            for _item_packages in self.packages:
                if _item_packages:
                    _items.append(_item_packages.to_dict())
            _dict['packages'] = _items
        # override the default output from pydantic by calling `to_dict()` of postage_details
        if self.postage_details:
            _dict['postageDetails'] = self.postage_details.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in tags (list)
        _items = []
        if self.tags:
            for _item_tags in self.tags:
                if _item_tags:
                    _items.append(_item_tags.to_dict())
            _dict['tags'] = _items
        # override the default output from pydantic by calling `to_dict()` of label
        if self.label:
            _dict['label'] = self.label.to_dict()
        # override the default output from pydantic by calling `to_dict()` of importer
        if self.importer:
            _dict['importer'] = self.importer.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CreateOrderRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "orderReference": obj.get("orderReference"),
            "isRecipientABusiness": obj.get("isRecipientABusiness"),
            "recipient": RecipientDetailsRequest.from_dict(obj["recipient"]) if obj.get("recipient") is not None else None,
            "sender": SenderDetailsRequest.from_dict(obj["sender"]) if obj.get("sender") is not None else None,
            "billing": BillingDetailsRequest.from_dict(obj["billing"]) if obj.get("billing") is not None else None,
            "packages": [ShipmentPackageRequest.from_dict(_item) for _item in obj["packages"]] if obj.get("packages") is not None else None,
            "orderDate": obj.get("orderDate"),
            "plannedDespatchDate": obj.get("plannedDespatchDate"),
            "specialInstructions": obj.get("specialInstructions"),
            "subtotal": obj.get("subtotal"),
            "shippingCostCharged": obj.get("shippingCostCharged"),
            "otherCosts": obj.get("otherCosts"),
            "customsDutyCosts": obj.get("customsDutyCosts"),
            "total": obj.get("total"),
            "currencyCode": obj.get("currencyCode"),
            "postageDetails": PostageDetailsRequest.from_dict(obj["postageDetails"]) if obj.get("postageDetails") is not None else None,
            "tags": [TagRequest.from_dict(_item) for _item in obj["tags"]] if obj.get("tags") is not None else None,
            "label": LabelGenerationRequest.from_dict(obj["label"]) if obj.get("label") is not None else None,
            "orderTax": obj.get("orderTax"),
            "containsDangerousGoods": obj.get("containsDangerousGoods"),
            "dangerousGoodsUnCode": obj.get("dangerousGoodsUnCode"),
            "dangerousGoodsDescription": obj.get("dangerousGoodsDescription"),
            "dangerousGoodsQuantity": obj.get("dangerousGoodsQuantity"),
            "importer": Importer.from_dict(obj["importer"]) if obj.get("importer") is not None else None
        })
        return _obj


