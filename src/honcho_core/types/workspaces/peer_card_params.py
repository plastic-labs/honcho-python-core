# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["PeerCardParams"]


class PeerCardParams(TypedDict, total=False):
    workspace_id: Required[str]
    """ID of the workspace"""

    target: Optional[str]
    """The peer whose card to retrieve.

    If not provided, returns the observer's own card
    """
