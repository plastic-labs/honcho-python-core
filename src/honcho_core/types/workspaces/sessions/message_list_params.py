# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Required, TypedDict

__all__ = ["MessageListParams"]


class MessageListParams(TypedDict, total=False):
    workspace_id: Required[str]

    page: int
    """Page number"""

    reverse: Optional[bool]
    """Whether to reverse the order of results"""

    size: int
    """Page size"""

    filters: Optional[Dict[str, object]]
