# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .summary import Summary
from ..._models import BaseModel
from .sessions.message import Message

__all__ = ["SessionContextResponse"]


class SessionContextResponse(BaseModel):
    id: str

    messages: List[Message]

    peer_card: Optional[List[str]] = None
    """The peer card, if context is requested from a specific perspective"""

    peer_representation: Optional[str] = None
    """
    A curated subset of a peer representation, if context is requested from a
    specific perspective
    """

    summary: Optional[Summary] = None
    """The summary if available"""
