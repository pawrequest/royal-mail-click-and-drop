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

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class Importer(BaseModel):
    """
    Importer
    """ # noqa: E501
    company_name: Optional[Annotated[str, Field(strict=True, max_length=100)]] = Field(default=None, alias="companyName")
    address_line1: Optional[Annotated[str, Field(strict=True, max_length=100)]] = Field(default=None, alias="addressLine1")
    address_line2: Optional[Annotated[str, Field(strict=True, max_length=100)]] = Field(default=None, alias="addressLine2")
    address_line3: Optional[Annotated[str, Field(strict=True, max_length=100)]] = Field(default=None, alias="addressLine3")
    city: Optional[Annotated[str, Field(strict=True, max_length=100)]] = None
    postcode: Optional[Annotated[str, Field(strict=True, max_length=20)]] = None
    country: Optional[Annotated[str, Field(strict=True, max_length=100)]] = None
    business_name: Optional[Annotated[str, Field(strict=True, max_length=100)]] = Field(default=None, alias="businessName")
    contact_name: Optional[Annotated[str, Field(strict=True, max_length=100)]] = Field(default=None, alias="contactName")
    phone_number: Optional[Annotated[str, Field(strict=True, max_length=25)]] = Field(default=None, alias="phoneNumber")
    email_address: Optional[Annotated[str, Field(strict=True, max_length=254)]] = Field(default=None, alias="emailAddress")
    vat_number: Optional[Annotated[str, Field(strict=True, max_length=15)]] = Field(default=None, alias="vatNumber")
    tax_code: Optional[Annotated[str, Field(strict=True, max_length=25)]] = Field(default=None, alias="taxCode")
    eori_number: Optional[Annotated[str, Field(strict=True, max_length=18)]] = Field(default=None, alias="eoriNumber")
    __properties: ClassVar[List[str]] = ["companyName", "addressLine1", "addressLine2", "addressLine3", "city", "postcode", "country", "businessName", "contactName", "phoneNumber", "emailAddress", "vatNumber", "taxCode", "eoriNumber"]

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
        """Create an instance of Importer from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Importer from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "companyName": obj.get("companyName"),
            "addressLine1": obj.get("addressLine1"),
            "addressLine2": obj.get("addressLine2"),
            "addressLine3": obj.get("addressLine3"),
            "city": obj.get("city"),
            "postcode": obj.get("postcode"),
            "country": obj.get("country"),
            "businessName": obj.get("businessName"),
            "contactName": obj.get("contactName"),
            "phoneNumber": obj.get("phoneNumber"),
            "emailAddress": obj.get("emailAddress"),
            "vatNumber": obj.get("vatNumber"),
            "taxCode": obj.get("taxCode"),
            "eoriNumber": obj.get("eoriNumber")
        })
        return _obj


