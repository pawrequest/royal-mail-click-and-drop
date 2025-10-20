
from __future__ import annotations

from typing import ClassVar

from pydantic import StrictStr

from royal_mail_click_and_drop.models.base import RMBaseModel


class ManifestErrorsErrorDetailsResponse(RMBaseModel):
    """
    ManifestErrorsErrorDetailsResponse
    """
    code: StrictStr | None = None
    description: StrictStr | None = None
    __properties: ClassVar[list[str]] = ['code', 'description']
