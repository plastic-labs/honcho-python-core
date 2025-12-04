# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from .observation_create_param import ObservationCreateParam

__all__ = ["ObservationCreateParams"]


class ObservationCreateParams(TypedDict, total=False):
    observations: Required[Iterable[ObservationCreateParam]]
