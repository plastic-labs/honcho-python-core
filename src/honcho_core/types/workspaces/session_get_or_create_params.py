# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Required, TypedDict

from .session_configuration_param import SessionConfigurationParam
from .sessions.session_peer_config_param import SessionPeerConfigParam

__all__ = ["SessionGetOrCreateParams"]


class SessionGetOrCreateParams(TypedDict, total=False):
    id: Required[str]

    configuration: Optional[SessionConfigurationParam]
    """The set of options that can be in a session DB-level configuration dictionary.

    All fields are optional. Session-level configuration overrides workspace-level
    configuration, which overrides global configuration.
    """

    metadata: Optional[Dict[str, object]]

    peers: Optional[Dict[str, SessionPeerConfigParam]]
