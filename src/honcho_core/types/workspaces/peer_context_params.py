# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["PeerContextParams"]


class PeerContextParams(TypedDict, total=False):
    workspace_id: Required[str]

    include_most_frequent: bool
    """Whether to include the most frequent conclusions in the representation"""

    max_conclusions: Optional[int]
    """Maximum number of conclusions to include in the representation"""

    search_max_distance: Optional[float]
    """Only used if `search_query` is provided.

    Maximum distance for semantically relevant conclusions
    """

    search_query: Optional[str]
    """Optional query to curate the representation around semantic search results"""

    search_top_k: Optional[int]
    """Only used if `search_query` is provided.

    Number of semantic-search-retrieved conclusions to include
    """

    target: Optional[str]
    """Optional target peer to get context for, from the observer's perspective.

    If not provided, returns the observer's own context (self-observation)
    """
