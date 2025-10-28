# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .observation import Observation

__all__ = ["ObservationQueryResponse"]

ObservationQueryResponse: TypeAlias = List[Observation]
