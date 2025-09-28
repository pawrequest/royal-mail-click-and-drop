from __future__ import annotations

from typing import ClassVar, List

from pydantic import Field, StrictInt, StrictStr

from royal_mail_click_and_drop.models.base import RMBaseModel


class UpdatedOrderInfo(RMBaseModel):
    order_identifier: StrictInt | None = None
    order_reference: StrictStr | None = None
    status: StrictStr | None = Field(default=None, description='Current status of the order')
    __properties: ClassVar[List[str]] = ['orderIdentifier', 'orderReference', 'status']
