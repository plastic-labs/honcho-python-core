# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["PeerCardConfigurationParam"]


class PeerCardConfigurationParam(TypedDict, total=False):
    create: Optional[bool]
    """Whether to generate peer card based on content."""

    use: Optional[bool]
    """Whether to use peer card related to this peer during deriver process."""
