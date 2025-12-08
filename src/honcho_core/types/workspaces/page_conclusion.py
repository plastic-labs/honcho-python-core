# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .conclusion import Conclusion

__all__ = ["PageConclusion"]


class PageConclusion(BaseModel):
    items: List[Conclusion]

    page: int

    size: int

    pages: Optional[int] = None

    total: Optional[int] = None
