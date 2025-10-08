# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .summary import Summary
from ..._models import BaseModel

__all__ = ["SessionSummariesResponse"]


class SessionSummariesResponse(BaseModel):
    id: str

    long_summary: Optional[Summary] = None
    """The long summary if available"""

    short_summary: Optional[Summary] = None
    """The short summary if available"""
