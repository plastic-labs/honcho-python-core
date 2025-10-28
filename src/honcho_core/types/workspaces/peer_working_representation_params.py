# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["PeerWorkingRepresentationParams"]


class PeerWorkingRepresentationParams(TypedDict, total=False):
    workspace_id: Required[str]
    """ID of the workspace"""

    include_most_derived: Optional[bool]
    """Only used if `search_query` is provided.

    Whether to include the most derived observations in the representation
    """

    max_observations: Optional[int]
    """Only used if `search_query` is provided.

    Maximum number of observations to include in the representation
    """

    search_max_distance: Optional[float]
    """Only used if `search_query` is provided.

    Maximum distance to search for semantically relevant observations
    """

    search_query: Optional[str]
    """Optional input to curate the representation around semantic search results"""

    search_top_k: Optional[int]
    """Only used if `search_query` is provided.

    Number of semantic-search-retrieved observations to include in the
    representation
    """

    session_id: Optional[str]
    """Get the working representation within this session"""

    target: Optional[str]
    """
    Optional peer ID to get the representation for, from the perspective of this
    peer
    """
