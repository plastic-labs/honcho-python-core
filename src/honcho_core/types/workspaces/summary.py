# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["Summary"]


class Summary(BaseModel):
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
