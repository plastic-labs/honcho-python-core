# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["PeerSetConfigParams"]


class PeerSetConfigParams(TypedDict, total=False):
    workspace_id: Required[str]
    """ID of the workspace"""

    session_id: Required[str]
    """ID of the session"""

    observe_me: Optional[bool]
    """Whether honcho should form a global theory-of-mind representation of this peer"""

    observe_others: Optional[bool]
    """
    Whether this peer should form a session-level theory-of-mind representation of
    other peers in the session
    """
