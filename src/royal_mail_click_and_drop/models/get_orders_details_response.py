
from __future__ import annotations

from typing import ClassVar, List

from pydantic import ConfigDict, StrictStr

from royal_mail_click_and_drop.models.get_order_details_resource import GetOrderDetailsResource
from royal_mail_click_and_drop.models.base import RMBaseModel


class GetOrdersDetailsResponse(RMBaseModel):
    """
    GetOrdersDetailsResponse
    """ # noqa: E501
    orders: List[GetOrderDetailsResource] | None = None
    continuation_token: StrictStr | None = None
    __properties: ClassVar[List[str]] = ["orders", "continuationToken"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )

