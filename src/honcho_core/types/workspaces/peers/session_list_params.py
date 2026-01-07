# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Required, TypedDict

__all__ = ["SessionListParams"]


class SessionListParams(TypedDict, total=False):
    workspace_id: Required[str]

    page: int
    """Page number"""

    size: int
    """Page size"""

    filters: Optional[Dict[str, object]]
