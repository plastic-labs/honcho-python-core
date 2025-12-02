# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, TypedDict

from .workspace_configuration_param import WorkspaceConfigurationParam

__all__ = ["WorkspaceGetOrCreateParams"]


class WorkspaceGetOrCreateParams(TypedDict, total=False):
    id: Required[str]

    configuration: WorkspaceConfigurationParam
    """The set of options that can be in a workspace DB-level configuration dictionary.

    All fields are optional. Session-level configuration overrides workspace-level
    configuration, which overrides global configuration.
    """

    metadata: Dict[str, object]
