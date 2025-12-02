# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel

__all__ = ["SessionPeerConfig"]


class SessionPeerConfig(BaseModel):
    observe_me: Optional[bool] = None
    """Whether honcho should form a global theory-of-mind representation of this peer"""

    observe_others: Optional[bool] = None
    """
    Whether this peer should form a session-level theory-of-mind representation of
    other peers in the session
    """
