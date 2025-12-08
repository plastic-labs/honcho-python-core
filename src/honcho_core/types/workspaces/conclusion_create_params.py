# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from .conclusion_create_param import ConclusionCreateParam

__all__ = ["ConclusionCreateParams"]


class ConclusionCreateParams(TypedDict, total=False):
    conclusions: Required[Iterable[ConclusionCreateParam]]
