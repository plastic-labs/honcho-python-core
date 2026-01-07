# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["SessionCloneParams"]


class SessionCloneParams(TypedDict, total=False):
    workspace_id: Required[str]

    message_id: Optional[str]
    """Message ID to cut off the clone at"""
