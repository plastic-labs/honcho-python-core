# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["PeerWorkingRepresentationParams"]


class PeerWorkingRepresentationParams(TypedDict, total=False):
    workspace_id: Required[str]
    """ID of the workspace"""

    session_id: Optional[str]
    """Get the working representation within this session"""

    target: Optional[str]
    """
    Optional peer ID to get the representation for, from the perspective of this
    peer
    """
