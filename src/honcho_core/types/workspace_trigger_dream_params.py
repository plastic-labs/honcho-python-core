# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["WorkspaceTriggerDreamParams"]


class WorkspaceTriggerDreamParams(TypedDict, total=False):
    dream_type: Required[Literal["consolidate", "agent"]]
    """Type of dream to trigger"""

    observer: Required[str]
    """Observer peer name"""

    observed: Optional[str]
    """Observed peer name (defaults to observer if not specified)"""
