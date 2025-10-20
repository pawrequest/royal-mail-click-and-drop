
from __future__ import annotations

from typing import ClassVar

from pydantic import Field, StrictFloat, StrictInt, StrictStr

from royal_mail_click_and_drop.models.base import RMBaseModel


class ManifestOrdersResponse(RMBaseModel):
    """
    ManifestOrdersResponse
    """
    manifest_number: StrictFloat | StrictInt = None
    document_pdf: StrictStr | None = Field(default=None, description='manifest in format base64 string')
    __properties: ClassVar[list[str]] = ['manifestNumber', 'documentPdf']
