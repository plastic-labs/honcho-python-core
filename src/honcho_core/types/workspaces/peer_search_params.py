# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Required, TypedDict

__all__ = ["PeerSearchParams"]


class PeerSearchParams(TypedDict, total=False):
    workspace_id: Required[str]

    query: Required[str]
    """Search query"""

    filters: Optional[Dict[str, object]]
    """Filters to scope the search"""

    limit: int
    """Number of results to return"""
