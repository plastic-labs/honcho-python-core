# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Optional
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo
from ...deriver_configuration_param import DeriverConfigurationParam
from ...peer_card_configuration_param import PeerCardConfigurationParam

__all__ = ["MessageCreateParam", "Configuration"]


class Configuration(TypedDict, total=False):
    """The set of options that can be in a message DB-level configuration dictionary.

    All fields are optional. Message-level configuration overrides all other configurations.
    """

    deriver: Optional[DeriverConfigurationParam]
    """Configuration for deriver functionality."""

    peer_card: Optional[PeerCardConfigurationParam]
    """Configuration for peer card functionality.

    If deriver is disabled, peer cards will also be disabled and these settings will
    be ignored.
    """


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
