# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["Representation", "Deductive", "Explicit"]


class Deductive(BaseModel):
    """Deductive observation with multiple premises and one conclusion, plus metadata."""

    conclusion: str
    """The deductive conclusion"""

    created_at: datetime

    message_ids: List[int]

    session_name: str

    premises: Optional[List[str]] = None
    """Supporting premises or evidence for this conclusion"""


class Explicit(BaseModel):
    """Explicit observation with content and metadata."""

    content: str
    """The explicit observation"""

    created_at: datetime

    message_ids: List[int]

    session_name: str


class Representation(BaseModel):
    """
    A Representation is a traversable and diffable map of observations.
    At the base, we have a list of explicit observations, derived from a peer's messages.

    From there, deductive observations can be made by establishing logical relationships between explicit observations.

    In the future, we can add more levels of reasoning on top of these.

    All of a peer's observations are stored as documents in a collection. These documents can be queried in various ways
    to produce this Representation object.

    Additionally, a "working representation" is a version of this data structure representing the most recent observations
    within a single session.

    A representation can have a maximum number of observations, which is applied individually to each level of reasoning.
    If a maximum is set, observations are added and removed in FIFO order.
    """

    deductive: Optional[List[Deductive]] = None
    """
    Conclusions that MUST be true given explicit facts and premises - strict logical
    necessities. Each deduction should have premises and a single conclusion.
    """

    explicit: Optional[List[Explicit]] = None
    """
    Facts LITERALLY stated by the user - direct quotes or clear paraphrases only, no
    interpretation or inference. Example: ['The user is 25 years old', 'The user has
    a dog']
    """
