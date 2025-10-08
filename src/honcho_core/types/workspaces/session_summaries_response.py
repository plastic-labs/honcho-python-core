# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["SessionSummariesResponse", "LongSummary", "ShortSummary"]


class LongSummary(BaseModel):
    content: str
    """The summary text"""

    created_at: str
    """The timestamp of when the summary was created (ISO format)"""

    message_id: str
    """The public ID of the message that this summary covers up to"""

    summary_type: str
    """The type of summary (short or long)"""

    token_count: int
    """The number of tokens in the summary text"""


class ShortSummary(BaseModel):
    content: str
    """The summary text"""

    created_at: str
    """The timestamp of when the summary was created (ISO format)"""

    message_id: str
    """The public ID of the message that this summary covers up to"""

    summary_type: str
    """The type of summary (short or long)"""

    token_count: int
    """The number of tokens in the summary text"""


class SessionSummariesResponse(BaseModel):
    id: str

    long_summary: Optional[LongSummary] = None
    """The long summary if available"""

    short_summary: Optional[ShortSummary] = None
    """The short summary if available"""
