# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["PeerGetContextParams"]


class PeerGetContextParams(TypedDict, total=False):
    workspace_id: Required[str]
    """ID of the workspace"""

    include_most_derived: bool
    """Whether to include the most derived observations in the representation"""

    max_observations: Optional[int]
    """Maximum number of observations to include in the representation"""

    search_max_distance: Optional[float]
    """Only used if `search_query` is provided.

    Maximum distance for semantically relevant observations
    """

    search_query: Optional[str]
    """Optional query to curate the representation around semantic search results"""

    search_top_k: Optional[int]
    """Only used if `search_query` is provided.

    Number of semantic-search-retrieved observations to include
    """

    target: Optional[str]
    """The target peer to get context for.

    If not provided, returns the peer's own context (self-observation)
    """
