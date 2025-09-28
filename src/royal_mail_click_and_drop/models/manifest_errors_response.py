
from __future__ import annotations

from typing import ClassVar, List

from royal_mail_click_and_drop.models.manifest_errors_error_details_response import ManifestErrorsErrorDetailsResponse
from royal_mail_click_and_drop.models.base import RMBaseModel


class ManifestErrorsResponse(RMBaseModel):
    """
    ManifestErrorsResponse
    """ # noqa: E501
    errors: List[ManifestErrorsErrorDetailsResponse] | None = None
    __properties: ClassVar[List[str]] = ["errors"]
