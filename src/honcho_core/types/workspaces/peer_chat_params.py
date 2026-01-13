# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["PeerChatParams"]


class PeerChatParams(TypedDict, total=False):
    workspace_id: Required[str]

    query: Required[str]
    """Dialectic API Prompt"""

    reasoning_level: Literal["minimal", "low", "medium", "high", "max"]
    """Level of reasoning to apply: minimal, low, medium, high, or max"""

    session_id: Optional[str]
    """ID of the session to scope the representation to"""

    stream: bool

    target: Optional[str]
    """Optional peer to get the representation for, from the perspective of this peer"""
