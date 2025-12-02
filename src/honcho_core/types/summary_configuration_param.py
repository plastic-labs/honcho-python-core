# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["SummaryConfigurationParam"]


class SummaryConfigurationParam(TypedDict, total=False):
    enabled: Optional[bool]
    """Whether to enable summary functionality."""

    messages_per_long_summary: Optional[int]
    """Number of messages per long summary.

    Must be positive, greater than or equal to 20, and greater than
    messages_per_short_summary.
    """

    messages_per_short_summary: Optional[int]
    """Number of messages per short summary.

    Must be positive, greater than or equal to 10, and less than
    messages_per_long_summary.
    """
