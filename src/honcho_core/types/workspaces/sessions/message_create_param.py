# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Optional
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo
from ...reasoning_configuration_param import ReasoningConfigurationParam

__all__ = ["MessageCreateParam", "Configuration"]


class Configuration(TypedDict, total=False):
    """The set of options that can be in a message DB-level configuration dictionary.

    All fields are optional. Message-level configuration overrides all other configurations.
    """

    reasoning: Optional[ReasoningConfigurationParam]
    """Configuration for reasoning functionality."""


class MessageCreateParam(TypedDict, total=False):
    content: Required[str]

    peer_id: Required[str]

    configuration: Optional[Configuration]
    """The set of options that can be in a message DB-level configuration dictionary.

    All fields are optional. Message-level configuration overrides all other
    configurations.
    """

    created_at: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]

    metadata: Optional[Dict[str, object]]
