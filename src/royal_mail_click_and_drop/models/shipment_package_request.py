
from __future__ import annotations

from typing import ClassVar, List

from pydantic import Field, StrictStr
from typing_extensions import Annotated

from royal_mail_click_and_drop.models.dimensions_request import DimensionsRequest
from royal_mail_click_and_drop.models.product_item_request import ProductItemRequest
from royal_mail_click_and_drop.models.base import RMBaseModel


class ShipmentPackageRequest(RMBaseModel):
    weight_in_grams: Annotated[int, Field(le=30000, strict=True, ge=1)]
    package_format_identifier: StrictStr = Field(description="<b>If you have a ChannelShipper account, you can also pass the name of any of your custom package formats instead of the values below.</b><br> Enum: 'undefined', 'letter', 'largeLetter', 'smallParcel', 'mediumParcel', 'parcel', 'documents'")
    custom_package_format_identifier: StrictStr | None = Field(default=None, description="This field will be deprecated in the future. Please use 'packageFormatIdentifier' for custom package formats from ChannelShipper.")
    dimensions: DimensionsRequest | None = None
    contents: List[ProductItemRequest] | None = None
    __properties: ClassVar[List[str]] = ["weightInGrams", "packageFormatIdentifier", "customPackageFormatIdentifier", "dimensions", "contents"]
