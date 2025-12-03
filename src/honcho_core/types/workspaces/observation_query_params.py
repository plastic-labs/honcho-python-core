# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Required, TypedDict

__all__ = ["ObservationQueryParams"]


class ObservationQueryParams(TypedDict, total=False):
    query: Required[str]
    """Semantic search query"""

    distance: Optional[float]
    """Maximum cosine distance threshold for results"""

    filters: Optional[Dict[str, object]]
    """Additional filters to apply"""

    top_k: int
    """Number of results to return"""
