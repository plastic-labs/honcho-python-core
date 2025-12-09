# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ConclusionCreateParam"]


class ConclusionCreateParam(TypedDict, total=False):
    """Schema for creating a single conclusion."""

    content: Required[str]

    observed_id: Required[str]
    """The peer the conclusion is about"""

    observer_id: Required[str]
    """The peer making the conclusion"""

    session_id: Required[str]
    """The session this conclusion relates to"""
