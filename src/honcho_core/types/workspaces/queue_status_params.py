# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["QueueStatusParams"]


class QueueStatusParams(TypedDict, total=False):
    observer_id: Optional[str]
    """Optional observer ID to filter by"""

    sender_id: Optional[str]
    """Optional sender ID to filter by"""

    session_id: Optional[str]
    """Optional session ID to filter by"""
