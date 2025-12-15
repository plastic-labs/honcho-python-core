# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ObservationCreateParam"]


class ObservationCreateParam(TypedDict, total=False):
    """Schema for creating a single observation"""

    content: Required[str]

    observed_id: Required[str]
    """The peer being observed"""

    observer_id: Required[str]
    """The peer making the observation"""

    session_id: Required[str]
    """The session this observation relates to"""
