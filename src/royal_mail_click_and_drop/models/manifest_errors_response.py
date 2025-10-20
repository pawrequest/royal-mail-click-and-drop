
from __future__ import annotations

from typing import ClassVar

from royal_mail_click_and_drop.models.manifest_errors_error_details_response import ManifestErrorsErrorDetailsResponse
from royal_mail_click_and_drop.models.base import RMBaseModel


class ManifestErrorsResponse(RMBaseModel):
    """
    ManifestErrorsResponse
    """
    errors: list[ManifestErrorsErrorDetailsResponse] | None = None
    __properties: ClassVar[list[str]] = ['errors']
