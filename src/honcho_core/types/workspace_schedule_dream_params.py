# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["WorkspaceScheduleDreamParams"]


class WorkspaceScheduleDreamParams(TypedDict, total=False):
    dream_type: Required[Literal["omni"]]
    """Type of dream to schedule"""

    observer: Required[str]
    """Observer peer name"""

    session_id: Required[str]
    """Session ID to scope the dream to"""

    observed: Optional[str]
    """Observed peer name (defaults to observer if not specified)"""
