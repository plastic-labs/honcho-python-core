# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["PeerContextResponse"]


class PeerContextResponse(BaseModel):
    """Context for a peer, including representation and peer card."""

    peer_id: str
    """The ID of the peer"""

    target_id: str
    """The ID of the target peer being observed"""

    peer_card: Optional[List[str]] = None
    """The peer card for the target peer from the observer's perspective"""

    representation: Optional[str] = None
    """
    A curated subset of the representation of the target peer from the observer's
    perspective
    """
