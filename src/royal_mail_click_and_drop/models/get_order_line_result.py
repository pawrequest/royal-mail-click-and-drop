
from __future__ import annotations

from typing import ClassVar

from pydantic import Field, StrictFloat, StrictInt, StrictStr

from royal_mail_click_and_drop.models.base import RMBaseModel


class GetOrderLineResult(RMBaseModel):
    """
    GetOrderLineResult
    """
    sku: StrictStr | None = None
    name: StrictStr | None = None
    quantity: StrictInt = Field(description='The number of units in a given line')
    unit_value: StrictFloat | StrictInt | None = Field(default=None, description='The price of a single unit excluding tax')
    line_total: StrictFloat | StrictInt | None = Field(default=None, description='The sum of the line items including tax')
    customs_code: StrictStr | None = None
    __properties: ClassVar[list[str]] = ['SKU', 'name', 'quantity', 'unitValue', 'lineTotal', 'customsCode']
