# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["SessionPeerConfigParam"]


class SessionPeerConfigParam(TypedDict, total=False):
    observe_me: Optional[bool]
    """Whether honcho should form a global theory-of-mind representation of this peer"""

    observe_others: Optional[bool]
    """
    Whether this peer should form a session-level theory-of-mind representation of
    other peers in the session
    """
