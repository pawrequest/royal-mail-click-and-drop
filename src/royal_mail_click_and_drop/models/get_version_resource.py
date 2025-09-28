
from __future__ import annotations

from datetime import datetime
from typing import ClassVar, List

from pydantic import StrictStr

from royal_mail_click_and_drop.models.base import RMBaseModel


class GetVersionResource(RMBaseModel):
    """
    GetVersionResource
    """ # noqa: E501
    commit: StrictStr | None = None
    build: StrictStr | None = None
    release: StrictStr | None = None
    release_date: datetime | None = None
    __properties: ClassVar[List[str]] = ["commit", "build", "release", "releaseDate"]
