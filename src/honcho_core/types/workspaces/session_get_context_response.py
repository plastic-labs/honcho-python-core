# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .summary import Summary
from ..._models import BaseModel
from .representation import Representation
from .sessions.message import Message

__all__ = ["SessionGetContextResponse"]


class SessionGetContextResponse(BaseModel):
    id: str

    messages: List[Message]

    peer_card: Optional[List[str]] = None
    """The peer card, if context is requested from a specific perspective"""

    peer_representation: Optional[Representation] = None
    """
    A Representation is a traversable and diffable map of observations. At the base,
    we have a list of explicit observations, derived from a peer's messages.

    From there, deductive observations can be made by establishing logical
    relationships between explicit observations.

    In the future, we can add more levels of reasoning on top of these.

    All of a peer's observations are stored as documents in a collection. These
    documents can be queried in various ways to produce this Representation object.

    Additionally, a "working representation" is a version of this data structure
    representing the most recent observations within a single session.

    A representation can have a maximum number of observations, which is applied
    individually to each level of reasoning. If a maximum is set, observations are
    added and removed in FIFO order.
    """

    summary: Optional[Summary] = None
    """The summary if available"""
