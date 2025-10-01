# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["PeerCardResponse"]


class PeerCardResponse(BaseModel):
    peer_card: Optional[List[str]] = None
    """The peer card content, or None if not found"""
