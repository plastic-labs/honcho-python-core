# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["DreamConfigurationParam"]


class DreamConfigurationParam(TypedDict, total=False):
    enabled: Optional[bool]
    """Whether to enable dream functionality.

    If deriver is disabled, dreams will also be disabled and this setting will be
    ignored.
    """
