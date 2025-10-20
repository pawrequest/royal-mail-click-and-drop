
from __future__ import annotations

from datetime import datetime
from typing import ClassVar

from pydantic import StrictStr

from royal_mail_click_and_drop.models.base import RMBaseModel


class GetVersionResource(RMBaseModel):
    """
    GetVersionResource
    """
    commit: StrictStr | None = None
    build: StrictStr | None = None
    release: StrictStr | None = None
    release_date: datetime | None = None
    __properties: ClassVar[list[str]] = ['commit', 'build', 'release', 'releaseDate']
