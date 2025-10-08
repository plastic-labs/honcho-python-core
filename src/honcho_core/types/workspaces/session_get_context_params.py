# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["SessionGetContextParams"]


class SessionGetContextParams(TypedDict, total=False):
    workspace_id: Required[str]
    """ID of the workspace"""

    last_message: Optional[str]
    """The most recent message, used to fetch semantically relevant observations"""

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

    summary: bool
    """Whether or not to include a summary _if_ one is available for the session"""

    tokens: Optional[int]
    """Number of tokens to use for the context.

    Includes summary if set to true. Includes representation and peer card if they
    are included in the response. If not provided, the context will be exhaustive
    (within 100000 tokens)
    """
