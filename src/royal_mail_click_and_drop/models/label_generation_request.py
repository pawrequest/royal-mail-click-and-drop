
from __future__ import annotations

from typing import ClassVar, List

from pydantic import StrictBool

from royal_mail_click_and_drop.models.base import RMBaseModel


class LabelGenerationRequest(RMBaseModel):
    """
    <b>Reserved for OBA customers only</b>
    """ # noqa: E501
    include_label_in_response: StrictBool
    include_cn: StrictBool | None = None
    include_returns_label: StrictBool | None = None
    __properties: ClassVar[List[str]] = ["includeLabelInResponse", "includeCN", "includeReturnsLabel"]
