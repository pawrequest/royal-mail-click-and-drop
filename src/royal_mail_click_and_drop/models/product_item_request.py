from __future__ import annotations

from typing import ClassVar

from pydantic import Field, StrictBool, StrictStr, field_validator
from typing import Annotated

from royal_mail_click_and_drop.models.base import RMBaseModel


class ProductItemRequest(RMBaseModel):
    name: Annotated[str, Field(strict=True, max_length=800)] | None = None
    sku: Annotated[str, Field(strict=True, max_length=100)] | None = Field(
        default=None,
        description='The presence or not of field <b>SKU</b> and other fields in the request body will determine which of the following behaviours occur:- <br>1) A minimum of <b>SKU</b>, <b>unitValue</b>, <b>unitWeightInGrams</b> and <b>quantity</b> provided - In addition to the provided product fields being used for the order creation, an existing account Product with matching SKU will be overwritten with all provided product parameters. If no existing account Product with matching SKU can be found then a new product will be created with the provided SKU and product parameters.<br>2) <b>SKU</b>, <b>quantity</b> provided and <b>no other fields</b> provided - An account Product with the provided SKU will be used for the order if it exists.<br>3) <b>SKU not provided</b> and a minimum of <b>unitValue</b>, <b>unitWeightInGrams</b> and <b>quantity</b> provided - All provided product fields will be used for the order creation.<br>4) All other scenarios will result in a validation error.',
        alias='SKU',
    )
    quantity: Annotated[int, Field(le=999999, strict=True, ge=1)] = Field(
        description='The number of units in a given line'
    )
    unit_value: Annotated[float, Field(multiple_of=0.01, le=999999, strict=True, ge=0)] | Annotated[int, Field(le=999999, strict=True, ge=0)] | None = Field(
        default=None, description='The price of a single unit excluding tax'
    )
    unit_weight_in_grams: Annotated[int, Field(le=999999, strict=True, ge=0)] | None = Field(
        default=None
    )
    customs_description: Annotated[str, Field(strict=True, max_length=50)] | None = Field(
        default=None
    )
    extended_customs_description: Annotated[str, Field(strict=True, max_length=300)] | None = (
        Field(default=None)
    )
    customs_code: Annotated[str, Field(strict=True, max_length=10)] | None = Field(
        default=None
    )
    origin_country_code: Annotated[str, Field(strict=True, max_length=3)] | None = Field(
        default=None
    )
    customs_declaration_category: StrictStr | None = Field(
        default=None
    )
    requires_export_licence: StrictBool | None = Field(
        default=None
    )
    stock_location: Annotated[str, Field(strict=True, max_length=50)] | None = Field(
        default=None
    )
    use_origin_preference: StrictBool | None = None
    supplementary_units: Annotated[str, Field(strict=True, max_length=17)] | None = Field(
        default=None
    )
    license_number: Annotated[str, Field(strict=True, max_length=41)] | None = Field(
        default=None
    )
    certificate_number: Annotated[str, Field(strict=True, max_length=41)] | None = Field(
        default=None
    )
    __properties: ClassVar[list[str]] = [
        'name',
        'SKU',
        'quantity',
        'unitValue',
        'unitWeightInGrams',
        'customsDescription',
        'extendedCustomsDescription',
        'customsCode',
        'originCountryCode',
        'customsDeclarationCategory',
        'requiresExportLicence',
        'stockLocation',
        'useOriginPreference',
        'supplementaryUnits',
        'licenseNumber',
        'certificateNumber',
    ]

    @field_validator('customs_declaration_category')
    def customs_declaration_category_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in {
            'none',
            'gift',
            'commercialSample',
            'documents',
            'other',
            'returnedGoods',
            'saleOfGoods',
            'mixedContent',
        }:
            raise ValueError(
                "must be one of enum values ('none', 'gift', 'commercialSample', 'documents', 'other', 'returnedGoods', 'saleOfGoods', 'mixedContent')"
            )
        return value
