# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from honcho_core import Honcho, AsyncHoncho
from tests.utils import assert_matches_type
from honcho_core.types import (
    Workspace,
    DeriverStatus,
    WorkspaceSearchResponse,
)
from honcho_core.pagination import SyncPage, AsyncPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestWorkspaces:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_update(self, client: Honcho) -> None:
        workspace = client.workspaces.update(
            workspace_id="workspace_id",
        )
        assert_matches_type(Workspace, workspace, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Honcho) -> None:
        workspace = client.workspaces.update(
            workspace_id="workspace_id",
            configuration={
                "deriver": {
                    "custom_instructions": "custom_instructions",
                    "enabled": True,
                },
                "dream": {"enabled": True},
                "peer_card": {
                    "create": True,
                    "use": True,
                },
                "summary": {
                    "enabled": True,
                    "messages_per_long_summary": 20,
                    "messages_per_short_summary": 10,
                },
            },
            metadata={"foo": "bar"},
        )
        assert_matches_type(Workspace, workspace, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Honcho) -> None:
        response = client.workspaces.with_raw_response.update(
            workspace_id="workspace_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workspace = response.parse()
        assert_matches_type(Workspace, workspace, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Honcho) -> None:
        with client.workspaces.with_streaming_response.update(
            workspace_id="workspace_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workspace = response.parse()
            assert_matches_type(Workspace, workspace, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Honcho) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            client.workspaces.with_raw_response.update(
                workspace_id="",
            )

    @parametrize
    def test_method_list(self, client: Honcho) -> None:
        workspace = client.workspaces.list()
        assert_matches_type(SyncPage[Workspace], workspace, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Honcho) -> None:
        workspace = client.workspaces.list(
            page=1,
            size=1,
            filters={"foo": "bar"},
        )
        assert_matches_type(SyncPage[Workspace], workspace, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Honcho) -> None:
        response = client.workspaces.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workspace = response.parse()
        assert_matches_type(SyncPage[Workspace], workspace, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Honcho) -> None:
        with client.workspaces.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workspace = response.parse()
            assert_matches_type(SyncPage[Workspace], workspace, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Honcho) -> None:
        workspace = client.workspaces.delete(
            "workspace_id",
        )
        assert_matches_type(Workspace, workspace, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Honcho) -> None:
        response = client.workspaces.with_raw_response.delete(
            "workspace_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workspace = response.parse()
        assert_matches_type(Workspace, workspace, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Honcho) -> None:
        with client.workspaces.with_streaming_response.delete(
            "workspace_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workspace = response.parse()
            assert_matches_type(Workspace, workspace, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Honcho) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            client.workspaces.with_raw_response.delete(
                "",
            )

    @parametrize
    def test_method_deriver_status(self, client: Honcho) -> None:
        workspace = client.workspaces.deriver_status(
            workspace_id="workspace_id",
        )
        assert_matches_type(DeriverStatus, workspace, path=["response"])

    @parametrize
    def test_method_deriver_status_with_all_params(self, client: Honcho) -> None:
        workspace = client.workspaces.deriver_status(
            workspace_id="workspace_id",
            observer_id="observer_id",
            sender_id="sender_id",
            session_id="session_id",
        )
        assert_matches_type(DeriverStatus, workspace, path=["response"])

    @parametrize
    def test_raw_response_deriver_status(self, client: Honcho) -> None:
        response = client.workspaces.with_raw_response.deriver_status(
            workspace_id="workspace_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workspace = response.parse()
        assert_matches_type(DeriverStatus, workspace, path=["response"])

    @parametrize
    def test_streaming_response_deriver_status(self, client: Honcho) -> None:
        with client.workspaces.with_streaming_response.deriver_status(
            workspace_id="workspace_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workspace = response.parse()
            assert_matches_type(DeriverStatus, workspace, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_deriver_status(self, client: Honcho) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            client.workspaces.with_raw_response.deriver_status(
                workspace_id="",
            )

    @parametrize
    def test_method_get_or_create(self, client: Honcho) -> None:
        workspace = client.workspaces.get_or_create(
            id="id",
        )
        assert_matches_type(Workspace, workspace, path=["response"])

    @parametrize
    def test_method_get_or_create_with_all_params(self, client: Honcho) -> None:
        workspace = client.workspaces.get_or_create(
            id="id",
            configuration={
                "deriver": {
                    "custom_instructions": "custom_instructions",
                    "enabled": True,
                },
                "dream": {"enabled": True},
                "peer_card": {
                    "create": True,
                    "use": True,
                },
                "summary": {
                    "enabled": True,
                    "messages_per_long_summary": 20,
                    "messages_per_short_summary": 10,
                },
            },
            metadata={"foo": "bar"},
        )
        assert_matches_type(Workspace, workspace, path=["response"])

    @parametrize
    def test_raw_response_get_or_create(self, client: Honcho) -> None:
        response = client.workspaces.with_raw_response.get_or_create(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workspace = response.parse()
        assert_matches_type(Workspace, workspace, path=["response"])

    @parametrize
    def test_streaming_response_get_or_create(self, client: Honcho) -> None:
        with client.workspaces.with_streaming_response.get_or_create(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workspace = response.parse()
            assert_matches_type(Workspace, workspace, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_search(self, client: Honcho) -> None:
        workspace = client.workspaces.search(
            workspace_id="workspace_id",
            query="query",
        )
        assert_matches_type(WorkspaceSearchResponse, workspace, path=["response"])

    @parametrize
    def test_method_search_with_all_params(self, client: Honcho) -> None:
        workspace = client.workspaces.search(
            workspace_id="workspace_id",
            query="query",
            filters={"foo": "bar"},
            limit=1,
        )
        assert_matches_type(WorkspaceSearchResponse, workspace, path=["response"])

    @parametrize
    def test_raw_response_search(self, client: Honcho) -> None:
        response = client.workspaces.with_raw_response.search(
            workspace_id="workspace_id",
            query="query",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workspace = response.parse()
        assert_matches_type(WorkspaceSearchResponse, workspace, path=["response"])

    @parametrize
    def test_streaming_response_search(self, client: Honcho) -> None:
        with client.workspaces.with_streaming_response.search(
            workspace_id="workspace_id",
            query="query",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workspace = response.parse()
            assert_matches_type(WorkspaceSearchResponse, workspace, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_search(self, client: Honcho) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            client.workspaces.with_raw_response.search(
                workspace_id="",
                query="query",
            )

    @parametrize
    def test_method_trigger_dream(self, client: Honcho) -> None:
        workspace = client.workspaces.trigger_dream(
            workspace_id="workspace_id",
            dream_type="consolidate",
            observer="observer",
        )
        assert workspace is None

    @parametrize
    def test_method_trigger_dream_with_all_params(self, client: Honcho) -> None:
        workspace = client.workspaces.trigger_dream(
            workspace_id="workspace_id",
            dream_type="consolidate",
            observer="observer",
            observed="observed",
        )
        assert workspace is None

    @parametrize
    def test_raw_response_trigger_dream(self, client: Honcho) -> None:
        response = client.workspaces.with_raw_response.trigger_dream(
            workspace_id="workspace_id",
            dream_type="consolidate",
            observer="observer",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workspace = response.parse()
        assert workspace is None

    @parametrize
    def test_streaming_response_trigger_dream(self, client: Honcho) -> None:
        with client.workspaces.with_streaming_response.trigger_dream(
            workspace_id="workspace_id",
            dream_type="consolidate",
            observer="observer",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workspace = response.parse()
            assert workspace is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_trigger_dream(self, client: Honcho) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            client.workspaces.with_raw_response.trigger_dream(
                workspace_id="",
                dream_type="consolidate",
                observer="observer",
            )


class TestAsyncWorkspaces:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_update(self, async_client: AsyncHoncho) -> None:
        workspace = await async_client.workspaces.update(
            workspace_id="workspace_id",
        )
        assert_matches_type(Workspace, workspace, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncHoncho) -> None:
        workspace = await async_client.workspaces.update(
            workspace_id="workspace_id",
            configuration={
                "deriver": {
                    "custom_instructions": "custom_instructions",
                    "enabled": True,
                },
                "dream": {"enabled": True},
                "peer_card": {
                    "create": True,
                    "use": True,
                },
                "summary": {
                    "enabled": True,
                    "messages_per_long_summary": 20,
                    "messages_per_short_summary": 10,
                },
            },
            metadata={"foo": "bar"},
        )
        assert_matches_type(Workspace, workspace, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncHoncho) -> None:
        response = await async_client.workspaces.with_raw_response.update(
            workspace_id="workspace_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workspace = await response.parse()
        assert_matches_type(Workspace, workspace, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncHoncho) -> None:
        async with async_client.workspaces.with_streaming_response.update(
            workspace_id="workspace_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workspace = await response.parse()
            assert_matches_type(Workspace, workspace, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncHoncho) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            await async_client.workspaces.with_raw_response.update(
                workspace_id="",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncHoncho) -> None:
        workspace = await async_client.workspaces.list()
        assert_matches_type(AsyncPage[Workspace], workspace, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncHoncho) -> None:
        workspace = await async_client.workspaces.list(
            page=1,
            size=1,
            filters={"foo": "bar"},
        )
        assert_matches_type(AsyncPage[Workspace], workspace, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncHoncho) -> None:
        response = await async_client.workspaces.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workspace = await response.parse()
        assert_matches_type(AsyncPage[Workspace], workspace, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncHoncho) -> None:
        async with async_client.workspaces.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workspace = await response.parse()
            assert_matches_type(AsyncPage[Workspace], workspace, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncHoncho) -> None:
        workspace = await async_client.workspaces.delete(
            "workspace_id",
        )
        assert_matches_type(Workspace, workspace, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncHoncho) -> None:
        response = await async_client.workspaces.with_raw_response.delete(
            "workspace_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workspace = await response.parse()
        assert_matches_type(Workspace, workspace, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncHoncho) -> None:
        async with async_client.workspaces.with_streaming_response.delete(
            "workspace_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workspace = await response.parse()
            assert_matches_type(Workspace, workspace, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncHoncho) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            await async_client.workspaces.with_raw_response.delete(
                "",
            )

    @parametrize
    async def test_method_deriver_status(self, async_client: AsyncHoncho) -> None:
        workspace = await async_client.workspaces.deriver_status(
            workspace_id="workspace_id",
        )
        assert_matches_type(DeriverStatus, workspace, path=["response"])

    @parametrize
    async def test_method_deriver_status_with_all_params(self, async_client: AsyncHoncho) -> None:
        workspace = await async_client.workspaces.deriver_status(
            workspace_id="workspace_id",
            observer_id="observer_id",
            sender_id="sender_id",
            session_id="session_id",
        )
        assert_matches_type(DeriverStatus, workspace, path=["response"])

    @parametrize
    async def test_raw_response_deriver_status(self, async_client: AsyncHoncho) -> None:
        response = await async_client.workspaces.with_raw_response.deriver_status(
            workspace_id="workspace_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workspace = await response.parse()
        assert_matches_type(DeriverStatus, workspace, path=["response"])

    @parametrize
    async def test_streaming_response_deriver_status(self, async_client: AsyncHoncho) -> None:
        async with async_client.workspaces.with_streaming_response.deriver_status(
            workspace_id="workspace_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workspace = await response.parse()
            assert_matches_type(DeriverStatus, workspace, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_deriver_status(self, async_client: AsyncHoncho) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            await async_client.workspaces.with_raw_response.deriver_status(
                workspace_id="",
            )

    @parametrize
    async def test_method_get_or_create(self, async_client: AsyncHoncho) -> None:
        workspace = await async_client.workspaces.get_or_create(
            id="id",
        )
        assert_matches_type(Workspace, workspace, path=["response"])

    @parametrize
    async def test_method_get_or_create_with_all_params(self, async_client: AsyncHoncho) -> None:
        workspace = await async_client.workspaces.get_or_create(
            id="id",
            configuration={
                "deriver": {
                    "custom_instructions": "custom_instructions",
                    "enabled": True,
                },
                "dream": {"enabled": True},
                "peer_card": {
                    "create": True,
                    "use": True,
                },
                "summary": {
                    "enabled": True,
                    "messages_per_long_summary": 20,
                    "messages_per_short_summary": 10,
                },
            },
            metadata={"foo": "bar"},
        )
        assert_matches_type(Workspace, workspace, path=["response"])

    @parametrize
    async def test_raw_response_get_or_create(self, async_client: AsyncHoncho) -> None:
        response = await async_client.workspaces.with_raw_response.get_or_create(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workspace = await response.parse()
        assert_matches_type(Workspace, workspace, path=["response"])

    @parametrize
    async def test_streaming_response_get_or_create(self, async_client: AsyncHoncho) -> None:
        async with async_client.workspaces.with_streaming_response.get_or_create(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workspace = await response.parse()
            assert_matches_type(Workspace, workspace, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_search(self, async_client: AsyncHoncho) -> None:
        workspace = await async_client.workspaces.search(
            workspace_id="workspace_id",
            query="query",
        )
        assert_matches_type(WorkspaceSearchResponse, workspace, path=["response"])

    @parametrize
    async def test_method_search_with_all_params(self, async_client: AsyncHoncho) -> None:
        workspace = await async_client.workspaces.search(
            workspace_id="workspace_id",
            query="query",
            filters={"foo": "bar"},
            limit=1,
        )
        assert_matches_type(WorkspaceSearchResponse, workspace, path=["response"])

    @parametrize
    async def test_raw_response_search(self, async_client: AsyncHoncho) -> None:
        response = await async_client.workspaces.with_raw_response.search(
            workspace_id="workspace_id",
            query="query",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workspace = await response.parse()
        assert_matches_type(WorkspaceSearchResponse, workspace, path=["response"])

    @parametrize
    async def test_streaming_response_search(self, async_client: AsyncHoncho) -> None:
        async with async_client.workspaces.with_streaming_response.search(
            workspace_id="workspace_id",
            query="query",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workspace = await response.parse()
            assert_matches_type(WorkspaceSearchResponse, workspace, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_search(self, async_client: AsyncHoncho) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            await async_client.workspaces.with_raw_response.search(
                workspace_id="",
                query="query",
            )

    @parametrize
    async def test_method_trigger_dream(self, async_client: AsyncHoncho) -> None:
        workspace = await async_client.workspaces.trigger_dream(
            workspace_id="workspace_id",
            dream_type="consolidate",
            observer="observer",
        )
        assert workspace is None

    @parametrize
    async def test_method_trigger_dream_with_all_params(self, async_client: AsyncHoncho) -> None:
        workspace = await async_client.workspaces.trigger_dream(
            workspace_id="workspace_id",
            dream_type="consolidate",
            observer="observer",
            observed="observed",
        )
        assert workspace is None

    @parametrize
    async def test_raw_response_trigger_dream(self, async_client: AsyncHoncho) -> None:
        response = await async_client.workspaces.with_raw_response.trigger_dream(
            workspace_id="workspace_id",
            dream_type="consolidate",
            observer="observer",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workspace = await response.parse()
        assert workspace is None

    @parametrize
    async def test_streaming_response_trigger_dream(self, async_client: AsyncHoncho) -> None:
        async with async_client.workspaces.with_streaming_response.trigger_dream(
            workspace_id="workspace_id",
            dream_type="consolidate",
            observer="observer",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workspace = await response.parse()
            assert workspace is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_trigger_dream(self, async_client: AsyncHoncho) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            await async_client.workspaces.with_raw_response.trigger_dream(
                workspace_id="",
                dream_type="consolidate",
                observer="observer",
            )
