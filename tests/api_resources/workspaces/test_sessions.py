# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from honcho_core import Honcho, AsyncHoncho
from tests.utils import assert_matches_type
from honcho_core.pagination import SyncPage, AsyncPage
from honcho_core.types.workspaces import (
    Session,
    SessionSearchResponse,
    SessionSummariesResponse,
    SessionGetContextResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSessions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_update(self, client: Honcho) -> None:
        session = client.workspaces.sessions.update(
            session_id="session_id",
            workspace_id="workspace_id",
        )
        assert_matches_type(Session, session, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Honcho) -> None:
        session = client.workspaces.sessions.update(
            session_id="session_id",
            workspace_id="workspace_id",
            configuration={"foo": "bar"},
            metadata={"foo": "bar"},
        )
        assert_matches_type(Session, session, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Honcho) -> None:
        response = client.workspaces.sessions.with_raw_response.update(
            session_id="session_id",
            workspace_id="workspace_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert_matches_type(Session, session, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Honcho) -> None:
        with client.workspaces.sessions.with_streaming_response.update(
            session_id="session_id",
            workspace_id="workspace_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert_matches_type(Session, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Honcho) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            client.workspaces.sessions.with_raw_response.update(
                session_id="session_id",
                workspace_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            client.workspaces.sessions.with_raw_response.update(
                session_id="",
                workspace_id="workspace_id",
            )

    @parametrize
    def test_method_list(self, client: Honcho) -> None:
        session = client.workspaces.sessions.list(
            workspace_id="workspace_id",
        )
        assert_matches_type(SyncPage[Session], session, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Honcho) -> None:
        session = client.workspaces.sessions.list(
            workspace_id="workspace_id",
            page=1,
            size=1,
            filters={"foo": "bar"},
        )
        assert_matches_type(SyncPage[Session], session, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Honcho) -> None:
        response = client.workspaces.sessions.with_raw_response.list(
            workspace_id="workspace_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert_matches_type(SyncPage[Session], session, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Honcho) -> None:
        with client.workspaces.sessions.with_streaming_response.list(
            workspace_id="workspace_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert_matches_type(SyncPage[Session], session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Honcho) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            client.workspaces.sessions.with_raw_response.list(
                workspace_id="",
            )

    @parametrize
    def test_method_delete(self, client: Honcho) -> None:
        session = client.workspaces.sessions.delete(
            session_id="session_id",
            workspace_id="workspace_id",
        )
        assert_matches_type(object, session, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Honcho) -> None:
        response = client.workspaces.sessions.with_raw_response.delete(
            session_id="session_id",
            workspace_id="workspace_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert_matches_type(object, session, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Honcho) -> None:
        with client.workspaces.sessions.with_streaming_response.delete(
            session_id="session_id",
            workspace_id="workspace_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert_matches_type(object, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Honcho) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            client.workspaces.sessions.with_raw_response.delete(
                session_id="session_id",
                workspace_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            client.workspaces.sessions.with_raw_response.delete(
                session_id="",
                workspace_id="workspace_id",
            )

    @parametrize
    def test_method_clone(self, client: Honcho) -> None:
        session = client.workspaces.sessions.clone(
            session_id="session_id",
            workspace_id="workspace_id",
        )
        assert_matches_type(Session, session, path=["response"])

    @parametrize
    def test_method_clone_with_all_params(self, client: Honcho) -> None:
        session = client.workspaces.sessions.clone(
            session_id="session_id",
            workspace_id="workspace_id",
            message_id="message_id",
        )
        assert_matches_type(Session, session, path=["response"])

    @parametrize
    def test_raw_response_clone(self, client: Honcho) -> None:
        response = client.workspaces.sessions.with_raw_response.clone(
            session_id="session_id",
            workspace_id="workspace_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert_matches_type(Session, session, path=["response"])

    @parametrize
    def test_streaming_response_clone(self, client: Honcho) -> None:
        with client.workspaces.sessions.with_streaming_response.clone(
            session_id="session_id",
            workspace_id="workspace_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert_matches_type(Session, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_clone(self, client: Honcho) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            client.workspaces.sessions.with_raw_response.clone(
                session_id="session_id",
                workspace_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            client.workspaces.sessions.with_raw_response.clone(
                session_id="",
                workspace_id="workspace_id",
            )

    @parametrize
    def test_method_get_context(self, client: Honcho) -> None:
        session = client.workspaces.sessions.get_context(
            session_id="session_id",
            workspace_id="workspace_id",
        )
        assert_matches_type(SessionGetContextResponse, session, path=["response"])

    @parametrize
    def test_method_get_context_with_all_params(self, client: Honcho) -> None:
        session = client.workspaces.sessions.get_context(
            session_id="session_id",
            workspace_id="workspace_id",
            last_message="last_message",
            peer_perspective="peer_perspective",
            peer_target="peer_target",
            summary=True,
            tokens=100000,
        )
        assert_matches_type(SessionGetContextResponse, session, path=["response"])

    @parametrize
    def test_raw_response_get_context(self, client: Honcho) -> None:
        response = client.workspaces.sessions.with_raw_response.get_context(
            session_id="session_id",
            workspace_id="workspace_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert_matches_type(SessionGetContextResponse, session, path=["response"])

    @parametrize
    def test_streaming_response_get_context(self, client: Honcho) -> None:
        with client.workspaces.sessions.with_streaming_response.get_context(
            session_id="session_id",
            workspace_id="workspace_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert_matches_type(SessionGetContextResponse, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_context(self, client: Honcho) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            client.workspaces.sessions.with_raw_response.get_context(
                session_id="session_id",
                workspace_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            client.workspaces.sessions.with_raw_response.get_context(
                session_id="",
                workspace_id="workspace_id",
            )

    @parametrize
    def test_method_get_or_create(self, client: Honcho) -> None:
        session = client.workspaces.sessions.get_or_create(
            workspace_id="workspace_id",
            id="id",
        )
        assert_matches_type(Session, session, path=["response"])

    @parametrize
    def test_method_get_or_create_with_all_params(self, client: Honcho) -> None:
        session = client.workspaces.sessions.get_or_create(
            workspace_id="workspace_id",
            id="id",
            configuration={"foo": "bar"},
            metadata={"foo": "bar"},
            peers={
                "foo": {
                    "observe_me": True,
                    "observe_others": True,
                }
            },
        )
        assert_matches_type(Session, session, path=["response"])

    @parametrize
    def test_raw_response_get_or_create(self, client: Honcho) -> None:
        response = client.workspaces.sessions.with_raw_response.get_or_create(
            workspace_id="workspace_id",
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert_matches_type(Session, session, path=["response"])

    @parametrize
    def test_streaming_response_get_or_create(self, client: Honcho) -> None:
        with client.workspaces.sessions.with_streaming_response.get_or_create(
            workspace_id="workspace_id",
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert_matches_type(Session, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_or_create(self, client: Honcho) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            client.workspaces.sessions.with_raw_response.get_or_create(
                workspace_id="",
                id="id",
            )

    @parametrize
    def test_method_search(self, client: Honcho) -> None:
        session = client.workspaces.sessions.search(
            session_id="session_id",
            workspace_id="workspace_id",
            query="query",
        )
        assert_matches_type(SessionSearchResponse, session, path=["response"])

    @parametrize
    def test_method_search_with_all_params(self, client: Honcho) -> None:
        session = client.workspaces.sessions.search(
            session_id="session_id",
            workspace_id="workspace_id",
            query="query",
            filters={"foo": "bar"},
            limit=1,
        )
        assert_matches_type(SessionSearchResponse, session, path=["response"])

    @parametrize
    def test_raw_response_search(self, client: Honcho) -> None:
        response = client.workspaces.sessions.with_raw_response.search(
            session_id="session_id",
            workspace_id="workspace_id",
            query="query",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert_matches_type(SessionSearchResponse, session, path=["response"])

    @parametrize
    def test_streaming_response_search(self, client: Honcho) -> None:
        with client.workspaces.sessions.with_streaming_response.search(
            session_id="session_id",
            workspace_id="workspace_id",
            query="query",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert_matches_type(SessionSearchResponse, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_search(self, client: Honcho) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            client.workspaces.sessions.with_raw_response.search(
                session_id="session_id",
                workspace_id="",
                query="query",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            client.workspaces.sessions.with_raw_response.search(
                session_id="",
                workspace_id="workspace_id",
                query="query",
            )

    @parametrize
    def test_method_summaries(self, client: Honcho) -> None:
        session = client.workspaces.sessions.summaries(
            session_id="session_id",
            workspace_id="workspace_id",
        )
        assert_matches_type(SessionSummariesResponse, session, path=["response"])

    @parametrize
    def test_raw_response_summaries(self, client: Honcho) -> None:
        response = client.workspaces.sessions.with_raw_response.summaries(
            session_id="session_id",
            workspace_id="workspace_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert_matches_type(SessionSummariesResponse, session, path=["response"])

    @parametrize
    def test_streaming_response_summaries(self, client: Honcho) -> None:
        with client.workspaces.sessions.with_streaming_response.summaries(
            session_id="session_id",
            workspace_id="workspace_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert_matches_type(SessionSummariesResponse, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_summaries(self, client: Honcho) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            client.workspaces.sessions.with_raw_response.summaries(
                session_id="session_id",
                workspace_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            client.workspaces.sessions.with_raw_response.summaries(
                session_id="",
                workspace_id="workspace_id",
            )


class TestAsyncSessions:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_update(self, async_client: AsyncHoncho) -> None:
        session = await async_client.workspaces.sessions.update(
            session_id="session_id",
            workspace_id="workspace_id",
        )
        assert_matches_type(Session, session, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncHoncho) -> None:
        session = await async_client.workspaces.sessions.update(
            session_id="session_id",
            workspace_id="workspace_id",
            configuration={"foo": "bar"},
            metadata={"foo": "bar"},
        )
        assert_matches_type(Session, session, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncHoncho) -> None:
        response = await async_client.workspaces.sessions.with_raw_response.update(
            session_id="session_id",
            workspace_id="workspace_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert_matches_type(Session, session, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncHoncho) -> None:
        async with async_client.workspaces.sessions.with_streaming_response.update(
            session_id="session_id",
            workspace_id="workspace_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert_matches_type(Session, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncHoncho) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            await async_client.workspaces.sessions.with_raw_response.update(
                session_id="session_id",
                workspace_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            await async_client.workspaces.sessions.with_raw_response.update(
                session_id="",
                workspace_id="workspace_id",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncHoncho) -> None:
        session = await async_client.workspaces.sessions.list(
            workspace_id="workspace_id",
        )
        assert_matches_type(AsyncPage[Session], session, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncHoncho) -> None:
        session = await async_client.workspaces.sessions.list(
            workspace_id="workspace_id",
            page=1,
            size=1,
            filters={"foo": "bar"},
        )
        assert_matches_type(AsyncPage[Session], session, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncHoncho) -> None:
        response = await async_client.workspaces.sessions.with_raw_response.list(
            workspace_id="workspace_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert_matches_type(AsyncPage[Session], session, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncHoncho) -> None:
        async with async_client.workspaces.sessions.with_streaming_response.list(
            workspace_id="workspace_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert_matches_type(AsyncPage[Session], session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncHoncho) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            await async_client.workspaces.sessions.with_raw_response.list(
                workspace_id="",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncHoncho) -> None:
        session = await async_client.workspaces.sessions.delete(
            session_id="session_id",
            workspace_id="workspace_id",
        )
        assert_matches_type(object, session, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncHoncho) -> None:
        response = await async_client.workspaces.sessions.with_raw_response.delete(
            session_id="session_id",
            workspace_id="workspace_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert_matches_type(object, session, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncHoncho) -> None:
        async with async_client.workspaces.sessions.with_streaming_response.delete(
            session_id="session_id",
            workspace_id="workspace_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert_matches_type(object, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncHoncho) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            await async_client.workspaces.sessions.with_raw_response.delete(
                session_id="session_id",
                workspace_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            await async_client.workspaces.sessions.with_raw_response.delete(
                session_id="",
                workspace_id="workspace_id",
            )

    @parametrize
    async def test_method_clone(self, async_client: AsyncHoncho) -> None:
        session = await async_client.workspaces.sessions.clone(
            session_id="session_id",
            workspace_id="workspace_id",
        )
        assert_matches_type(Session, session, path=["response"])

    @parametrize
    async def test_method_clone_with_all_params(self, async_client: AsyncHoncho) -> None:
        session = await async_client.workspaces.sessions.clone(
            session_id="session_id",
            workspace_id="workspace_id",
            message_id="message_id",
        )
        assert_matches_type(Session, session, path=["response"])

    @parametrize
    async def test_raw_response_clone(self, async_client: AsyncHoncho) -> None:
        response = await async_client.workspaces.sessions.with_raw_response.clone(
            session_id="session_id",
            workspace_id="workspace_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert_matches_type(Session, session, path=["response"])

    @parametrize
    async def test_streaming_response_clone(self, async_client: AsyncHoncho) -> None:
        async with async_client.workspaces.sessions.with_streaming_response.clone(
            session_id="session_id",
            workspace_id="workspace_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert_matches_type(Session, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_clone(self, async_client: AsyncHoncho) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            await async_client.workspaces.sessions.with_raw_response.clone(
                session_id="session_id",
                workspace_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            await async_client.workspaces.sessions.with_raw_response.clone(
                session_id="",
                workspace_id="workspace_id",
            )

    @parametrize
    async def test_method_get_context(self, async_client: AsyncHoncho) -> None:
        session = await async_client.workspaces.sessions.get_context(
            session_id="session_id",
            workspace_id="workspace_id",
        )
        assert_matches_type(SessionGetContextResponse, session, path=["response"])

    @parametrize
    async def test_method_get_context_with_all_params(self, async_client: AsyncHoncho) -> None:
        session = await async_client.workspaces.sessions.get_context(
            session_id="session_id",
            workspace_id="workspace_id",
            last_message="last_message",
            peer_perspective="peer_perspective",
            peer_target="peer_target",
            summary=True,
            tokens=100000,
        )
        assert_matches_type(SessionGetContextResponse, session, path=["response"])

    @parametrize
    async def test_raw_response_get_context(self, async_client: AsyncHoncho) -> None:
        response = await async_client.workspaces.sessions.with_raw_response.get_context(
            session_id="session_id",
            workspace_id="workspace_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert_matches_type(SessionGetContextResponse, session, path=["response"])

    @parametrize
    async def test_streaming_response_get_context(self, async_client: AsyncHoncho) -> None:
        async with async_client.workspaces.sessions.with_streaming_response.get_context(
            session_id="session_id",
            workspace_id="workspace_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert_matches_type(SessionGetContextResponse, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_context(self, async_client: AsyncHoncho) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            await async_client.workspaces.sessions.with_raw_response.get_context(
                session_id="session_id",
                workspace_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            await async_client.workspaces.sessions.with_raw_response.get_context(
                session_id="",
                workspace_id="workspace_id",
            )

    @parametrize
    async def test_method_get_or_create(self, async_client: AsyncHoncho) -> None:
        session = await async_client.workspaces.sessions.get_or_create(
            workspace_id="workspace_id",
            id="id",
        )
        assert_matches_type(Session, session, path=["response"])

    @parametrize
    async def test_method_get_or_create_with_all_params(self, async_client: AsyncHoncho) -> None:
        session = await async_client.workspaces.sessions.get_or_create(
            workspace_id="workspace_id",
            id="id",
            configuration={"foo": "bar"},
            metadata={"foo": "bar"},
            peers={
                "foo": {
                    "observe_me": True,
                    "observe_others": True,
                }
            },
        )
        assert_matches_type(Session, session, path=["response"])

    @parametrize
    async def test_raw_response_get_or_create(self, async_client: AsyncHoncho) -> None:
        response = await async_client.workspaces.sessions.with_raw_response.get_or_create(
            workspace_id="workspace_id",
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert_matches_type(Session, session, path=["response"])

    @parametrize
    async def test_streaming_response_get_or_create(self, async_client: AsyncHoncho) -> None:
        async with async_client.workspaces.sessions.with_streaming_response.get_or_create(
            workspace_id="workspace_id",
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert_matches_type(Session, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_or_create(self, async_client: AsyncHoncho) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            await async_client.workspaces.sessions.with_raw_response.get_or_create(
                workspace_id="",
                id="id",
            )

    @parametrize
    async def test_method_search(self, async_client: AsyncHoncho) -> None:
        session = await async_client.workspaces.sessions.search(
            session_id="session_id",
            workspace_id="workspace_id",
            query="query",
        )
        assert_matches_type(SessionSearchResponse, session, path=["response"])

    @parametrize
    async def test_method_search_with_all_params(self, async_client: AsyncHoncho) -> None:
        session = await async_client.workspaces.sessions.search(
            session_id="session_id",
            workspace_id="workspace_id",
            query="query",
            filters={"foo": "bar"},
            limit=1,
        )
        assert_matches_type(SessionSearchResponse, session, path=["response"])

    @parametrize
    async def test_raw_response_search(self, async_client: AsyncHoncho) -> None:
        response = await async_client.workspaces.sessions.with_raw_response.search(
            session_id="session_id",
            workspace_id="workspace_id",
            query="query",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert_matches_type(SessionSearchResponse, session, path=["response"])

    @parametrize
    async def test_streaming_response_search(self, async_client: AsyncHoncho) -> None:
        async with async_client.workspaces.sessions.with_streaming_response.search(
            session_id="session_id",
            workspace_id="workspace_id",
            query="query",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert_matches_type(SessionSearchResponse, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_search(self, async_client: AsyncHoncho) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            await async_client.workspaces.sessions.with_raw_response.search(
                session_id="session_id",
                workspace_id="",
                query="query",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            await async_client.workspaces.sessions.with_raw_response.search(
                session_id="",
                workspace_id="workspace_id",
                query="query",
            )

    @parametrize
    async def test_method_summaries(self, async_client: AsyncHoncho) -> None:
        session = await async_client.workspaces.sessions.summaries(
            session_id="session_id",
            workspace_id="workspace_id",
        )
        assert_matches_type(SessionSummariesResponse, session, path=["response"])

    @parametrize
    async def test_raw_response_summaries(self, async_client: AsyncHoncho) -> None:
        response = await async_client.workspaces.sessions.with_raw_response.summaries(
            session_id="session_id",
            workspace_id="workspace_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert_matches_type(SessionSummariesResponse, session, path=["response"])

    @parametrize
    async def test_streaming_response_summaries(self, async_client: AsyncHoncho) -> None:
        async with async_client.workspaces.sessions.with_streaming_response.summaries(
            session_id="session_id",
            workspace_id="workspace_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert_matches_type(SessionSummariesResponse, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_summaries(self, async_client: AsyncHoncho) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            await async_client.workspaces.sessions.with_raw_response.summaries(
                session_id="session_id",
                workspace_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            await async_client.workspaces.sessions.with_raw_response.summaries(
                session_id="",
                workspace_id="workspace_id",
            )
