# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["SessionGetContextParams"]


class SessionGetContextParams(TypedDict, total=False):
    workspace_id: Required[str]
    """ID of the workspace"""

    include_most_derived: bool
    """Only used if `last_message` is provided.

    Whether to include the most derived observations in the representation
    """

    last_message: Optional[str]
    """The most recent message, used to fetch semantically relevant observations"""

    limit_to_session: bool
    """Only used if `last_message` is provided.

    Whether to limit the representation to the session (as opposed to everything
    known about the target peer)
    """

    max_observations: Optional[int]
    """Only used if `last_message` is provided.

    The maximum number of observations to include in the representation
    """

    peer_perspective: Optional[str]
    """A peer to get context for.

    If given, response will attempt to include representation and card from the
    perspective of that peer. Must be provided with `peer_target`.
    """

    peer_target: Optional[str]
    """The target of the perspective.

    If given without `peer_perspective`, will get the Honcho-level representation
    and peer card for this peer. If given with `peer_perspective`, will get the
    representation and card for this peer _from the perspective of that peer_.
    """

    search_max_distance: Optional[float]
    """Only used if `last_message` is provided.

    The maximum distance to search for semantically relevant observations
    """

    search_top_k: Optional[int]
    """Only used if `last_message` is provided.

    The number of semantic-search-retrieved observations to include in the
    representation
    """

    summary: bool
    """Whether or not to include a summary _if_ one is available for the session"""

    tokens: Optional[int]
    """Number of tokens to use for the context.

    Includes summary if set to true. Includes representation and peer card if they
    are included in the response. If not provided, the context will be exhaustive
    (within 100000 tokens)
    """
