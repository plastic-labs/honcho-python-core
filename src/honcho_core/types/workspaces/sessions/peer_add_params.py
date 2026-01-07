# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, TypedDict

from .session_peer_config_param import SessionPeerConfigParam

__all__ = ["PeerAddParams"]


class PeerAddParams(TypedDict, total=False):
    workspace_id: Required[str]

    body: Required[Dict[str, SessionPeerConfigParam]]
    """List of peer IDs (with session-level configuration) to add to the session"""
