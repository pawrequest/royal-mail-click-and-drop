
from __future__ import annotations

from typing import ClassVar, List

from pydantic import StrictStr

from royal_mail_click_and_drop.models.base import RMBaseModel


class ManifestErrorsErrorDetailsResponse(RMBaseModel):
    """
    ManifestErrorsErrorDetailsResponse
    """ # noqa: E501
    code: StrictStr | None = None
    description: StrictStr | None = None
    __properties: ClassVar[List[str]] = ["code", "description"]
