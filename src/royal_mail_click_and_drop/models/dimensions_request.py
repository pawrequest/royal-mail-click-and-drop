
from __future__ import annotations

from typing import ClassVar, List

from pydantic import StrictInt

from royal_mail_click_and_drop.models.base import RMBaseModel


class DimensionsRequest(RMBaseModel):
    """
    It is not mandatory to include the dimensions field. If the dimensions field is included then the inner fields heightInMms, widthInMms and depthInMms must be specified with non-zero values.
    """ # noqa: E501
    height_in_mms: StrictInt
    width_in_mms: StrictInt
    depth_in_mms: StrictInt
    __properties: ClassVar[List[str]] = ["heightInMms", "widthInMms", "depthInMms"]
