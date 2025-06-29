# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Required, TypedDict

__all__ = ["MessageCreateParam"]


class MessageCreateParam(TypedDict, total=False):
    content: Required[str]

    peer_id: Required[str]

    metadata: Optional[Dict[str, object]]
