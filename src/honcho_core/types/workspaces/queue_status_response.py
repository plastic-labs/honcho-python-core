# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional

from ..._models import BaseModel

__all__ = ["QueueStatusResponse", "Sessions"]


class Sessions(BaseModel):
    """Status for a specific session within the processing queue."""

    completed_work_units: int
    """Completed work units"""

    in_progress_work_units: int
    """Work units currently being processed"""

    pending_work_units: int
    """Work units waiting to be processed"""

    total_work_units: int
    """Total work units"""

    session_id: Optional[str] = None
    """Session ID if filtered by session"""


class QueueStatusResponse(BaseModel):
    """Aggregated processing queue status."""

    completed_work_units: int
    """Completed work units"""

    in_progress_work_units: int
    """Work units currently being processed"""

    pending_work_units: int
    """Work units waiting to be processed"""

    total_work_units: int
    """Total work units"""

    sessions: Optional[Dict[str, Sessions]] = None
    """Per-session status when not filtered by session"""
