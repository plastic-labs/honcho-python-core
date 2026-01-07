# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["WorkspaceScheduleDreamParams"]


class WorkspaceScheduleDreamParams(TypedDict, total=False):
    dream_type: Required[Literal["consolidate"]]
    """Type of dream to schedule"""

    observer: Required[str]
    """Observer peer name"""

    session_id: Required[str]
    """Session ID to scope the dream to"""

    observed: Optional[str]
    """Observed peer name (defaults to observer if not specified)"""

    reasoning_focus: Optional[Literal["deduction", "induction", "knowledge_update"]]
    """
    Optional focus mode to bias the dream toward specific reasoning: 'deduction'
    prioritizes logical inferences from explicit facts, 'induction' prioritizes
    pattern recognition across conclusions, 'knowledge_update' detects when facts
    have changed over time
    """
