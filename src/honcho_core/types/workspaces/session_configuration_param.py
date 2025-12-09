# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Optional
from typing_extensions import TypeAlias, TypedDict

from ..dream_configuration_param import DreamConfigurationParam
from ..deriver_configuration_param import DeriverConfigurationParam
from ..summary_configuration_param import SummaryConfigurationParam
from ..peer_card_configuration_param import PeerCardConfigurationParam

__all__ = ["SessionConfigurationParam"]


class SessionConfigurationParamTyped(TypedDict, total=False):
    """The set of options that can be in a session DB-level configuration dictionary.

    All fields are optional. Session-level configuration overrides workspace-level configuration, which overrides global configuration.
    """

    deriver: Optional[DeriverConfigurationParam]
    """Configuration for deriver functionality."""

    dream: Optional[DreamConfigurationParam]
    """Configuration for dream functionality.

    If deriver is disabled, dreams will also be disabled and these settings will be
    ignored.
    """

    peer_card: Optional[PeerCardConfigurationParam]
    """Configuration for peer card functionality.

    If deriver is disabled, peer cards will also be disabled and these settings will
    be ignored.
    """

    summary: Optional[SummaryConfigurationParam]
    """Configuration for summary functionality."""


SessionConfigurationParam: TypeAlias = Union[SessionConfigurationParamTyped, Dict[str, object]]
