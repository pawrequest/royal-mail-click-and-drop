
from __future__ import annotations

from typing import ClassVar

from pydantic import ConfigDict, StrictStr

from royal_mail_click_and_drop.models.get_order_details_resource import GetOrderDetailsResource
from royal_mail_click_and_drop.models.base import RMBaseModel


class GetOrdersDetailsResponse(RMBaseModel):
    """
    GetOrdersDetailsResponse
    """
    orders: list[GetOrderDetailsResource] | None = None
    continuation_token: StrictStr | None = None
    __properties: ClassVar[list[str]] = ['orders', 'continuationToken']

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )

