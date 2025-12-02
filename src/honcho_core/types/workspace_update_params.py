# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import TypedDict

from .workspace_configuration_param import WorkspaceConfigurationParam

__all__ = ["WorkspaceUpdateParams"]


class WorkspaceUpdateParams(TypedDict, total=False):
    configuration: Optional[WorkspaceConfigurationParam]
    """The set of options that can be in a workspace DB-level configuration dictionary.

    All fields are optional. Session-level configuration overrides workspace-level
    configuration, which overrides global configuration.
    """

    metadata: Optional[Dict[str, object]]
