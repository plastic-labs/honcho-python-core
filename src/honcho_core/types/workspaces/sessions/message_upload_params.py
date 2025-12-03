# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from ...._types import FileTypes

__all__ = ["MessageUploadParams"]


class MessageUploadParams(TypedDict, total=False):
    workspace_id: Required[str]

    file: Required[FileTypes]

    peer_id: Required[str]

    configuration: Optional[str]

    created_at: Optional[str]

    metadata: Optional[str]
