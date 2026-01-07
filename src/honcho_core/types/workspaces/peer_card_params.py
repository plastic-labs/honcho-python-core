# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["PeerCardParams"]


class PeerCardParams(TypedDict, total=False):
    workspace_id: Required[str]

    target: Optional[str]
    """Optional target peer to retrieve a card for, from the observer's perspective.

    If not provided, returns the observer's own card
    """
