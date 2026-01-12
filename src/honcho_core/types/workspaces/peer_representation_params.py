# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["PeerRepresentationParams"]


class PeerRepresentationParams(TypedDict, total=False):
    workspace_id: Required[str]

    include_most_frequent: Optional[bool]
    """Only used if `search_query` is provided.

    Whether to include the most frequent conclusions in the representation
    """

    max_conclusions: Optional[int]
    """Only used if `search_query` is provided.

    Maximum number of conclusions to include in the representation
    """

    search_max_distance: Optional[float]
    """Only used if `search_query` is provided.

    Maximum distance to search for semantically relevant conclusions
    """

    search_query: Optional[str]
    """Optional input to curate the representation around semantic search results"""

    search_top_k: Optional[int]
    """Only used if `search_query` is provided.

    Number of semantic-search-retrieved conclusions to include in the representation
    """

    session_id: Optional[str]
    """Optional session ID within which to scope the representation"""

    target: Optional[str]
    """
    Optional peer ID to get the representation for, from the perspective of this
    peer
    """
