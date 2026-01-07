# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from ..._models import BaseModel

__all__ = ["Conclusion"]


class Conclusion(BaseModel):
    """Conclusion response - external view of a document."""

    id: str

    content: str

    created_at: datetime

    observed_id: str
    """The peer the conclusion is about"""

    observer_id: str
    """The peer who made the conclusion"""

    session_id: str
