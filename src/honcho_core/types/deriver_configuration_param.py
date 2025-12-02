# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["DeriverConfigurationParam"]


class DeriverConfigurationParam(TypedDict, total=False):
    custom_instructions: Optional[str]
    """TODO: currently unused.

    Custom instructions to use for the deriver on this workspace/session/message.
    """

    enabled: Optional[bool]
    """Whether to enable deriver functionality."""
