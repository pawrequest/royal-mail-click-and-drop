
from __future__ import annotations

from typing import ClassVar

from pydantic import StrictInt, StrictStr

from royal_mail_click_and_drop.models.base import RMBaseModel


class DeletedOrderInfo(RMBaseModel):
    order_identifier: StrictInt | None = None
    order_reference: StrictStr | None = None
    order_info: StrictStr | None = None
    __properties: ClassVar[list[str]] = ['orderIdentifier', 'orderReference', 'orderInfo']
