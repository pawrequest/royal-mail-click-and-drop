
from __future__ import annotations

from typing import ClassVar, List, Union

from pydantic import Field, StrictFloat, StrictInt, StrictStr

from royal_mail_click_and_drop.models.base import RMBaseModel


class ManifestOrdersResponse(RMBaseModel):
    """
    ManifestOrdersResponse
    """ # noqa: E501
    manifest_number: Union[StrictFloat, StrictInt] = None
    document_pdf: StrictStr | None = Field(default=None, description="manifest in format base64 string")
    __properties: ClassVar[List[str]] = ["manifestNumber", "documentPdf"]
