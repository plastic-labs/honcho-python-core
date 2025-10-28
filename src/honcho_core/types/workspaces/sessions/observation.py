# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from ...._models import BaseModel

__all__ = ["Observation"]


class Observation(BaseModel):
    id: str

    content: str

    created_at: datetime

    observed_id: str
    """The peer being observed"""

    observer_id: str
    """The peer who made the observation"""

    session_id: str
