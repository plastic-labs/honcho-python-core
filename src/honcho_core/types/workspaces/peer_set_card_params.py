# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from ..._types import SequenceNotStr

__all__ = ["PeerSetCardParams"]


class PeerSetCardParams(TypedDict, total=False):
    workspace_id: Required[str]
    """ID of the workspace"""

    peer_card: Required[SequenceNotStr[str]]
    """The peer card content to set"""

    target: Optional[str]
    """The peer whose card to set. If not provided, sets the observer's own card"""
