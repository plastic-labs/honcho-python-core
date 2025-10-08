# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from honcho_core import Honcho, AsyncHoncho
from tests.utils import assert_matches_type
from honcho_core.pagination import SyncPage, AsyncPage
from honcho_core.types.workspaces import (
    Peer,
    PeerCardResponse,
    PeerChatResponse,
    PeerSearchResponse,
    PeerWorkingRepresentationResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPeers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_update(self, client: Honcho) -> None:
        peer = client.workspaces.peers.update(
            peer_id="peer_id",
            workspace_id="workspace_id",
        )
        assert_matches_type(Peer, peer, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Honcho) -> None:
        peer = client.workspaces.peers.update(
            peer_id="peer_id",
            workspace_id="workspace_id",
            configuration={"foo": "bar"},
            metadata={"foo": "bar"},
        )
        assert_matches_type(Peer, peer, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Honcho) -> None:
        response = client.workspaces.peers.with_raw_response.update(
            peer_id="peer_id",
            workspace_id="workspace_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        peer = response.parse()
        assert_matches_type(Peer, peer, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Honcho) -> None:
        with client.workspaces.peers.with_streaming_response.update(
            peer_id="peer_id",
            workspace_id="workspace_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            peer = response.parse()
            assert_matches_type(Peer, peer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Honcho) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            client.workspaces.peers.with_raw_response.update(
                peer_id="peer_id",
                workspace_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `peer_id` but received ''"):
            client.workspaces.peers.with_raw_response.update(
                peer_id="",
                workspace_id="workspace_id",
            )

    @parametrize
    def test_method_list(self, client: Honcho) -> None:
        peer = client.workspaces.peers.list(
            workspace_id="workspace_id",
        )
        assert_matches_type(SyncPage[Peer], peer, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Honcho) -> None:
        peer = client.workspaces.peers.list(
            workspace_id="workspace_id",
            page=1,
            size=1,
            filters={"foo": "bar"},
        )
        assert_matches_type(SyncPage[Peer], peer, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Honcho) -> None:
        response = client.workspaces.peers.with_raw_response.list(
            workspace_id="workspace_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        peer = response.parse()
        assert_matches_type(SyncPage[Peer], peer, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Honcho) -> None:
        with client.workspaces.peers.with_streaming_response.list(
            workspace_id="workspace_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            peer = response.parse()
            assert_matches_type(SyncPage[Peer], peer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Honcho) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            client.workspaces.peers.with_raw_response.list(
                workspace_id="",
            )

    @parametrize
    def test_method_card(self, client: Honcho) -> None:
        peer = client.workspaces.peers.card(
            peer_id="peer_id",
            workspace_id="workspace_id",
        )
        assert_matches_type(PeerCardResponse, peer, path=["response"])

    @parametrize
    def test_method_card_with_all_params(self, client: Honcho) -> None:
        peer = client.workspaces.peers.card(
            peer_id="peer_id",
            workspace_id="workspace_id",
            target="target",
        )
        assert_matches_type(PeerCardResponse, peer, path=["response"])

    @parametrize
    def test_raw_response_card(self, client: Honcho) -> None:
        response = client.workspaces.peers.with_raw_response.card(
            peer_id="peer_id",
            workspace_id="workspace_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        peer = response.parse()
        assert_matches_type(PeerCardResponse, peer, path=["response"])

    @parametrize
    def test_streaming_response_card(self, client: Honcho) -> None:
        with client.workspaces.peers.with_streaming_response.card(
            peer_id="peer_id",
            workspace_id="workspace_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            peer = response.parse()
            assert_matches_type(PeerCardResponse, peer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_card(self, client: Honcho) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            client.workspaces.peers.with_raw_response.card(
                peer_id="peer_id",
                workspace_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `peer_id` but received ''"):
            client.workspaces.peers.with_raw_response.card(
                peer_id="",
                workspace_id="workspace_id",
            )

    @parametrize
    def test_method_chat(self, client: Honcho) -> None:
        peer = client.workspaces.peers.chat(
            peer_id="peer_id",
            workspace_id="workspace_id",
            query="x",
        )
        assert_matches_type(PeerChatResponse, peer, path=["response"])

    @parametrize
    def test_method_chat_with_all_params(self, client: Honcho) -> None:
        peer = client.workspaces.peers.chat(
            peer_id="peer_id",
            workspace_id="workspace_id",
            query="x",
            session_id="session_id",
            stream=True,
            target="target",
        )
        assert_matches_type(PeerChatResponse, peer, path=["response"])

    @parametrize
    def test_raw_response_chat(self, client: Honcho) -> None:
        response = client.workspaces.peers.with_raw_response.chat(
            peer_id="peer_id",
            workspace_id="workspace_id",
            query="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        peer = response.parse()
        assert_matches_type(PeerChatResponse, peer, path=["response"])

    @parametrize
    def test_streaming_response_chat(self, client: Honcho) -> None:
        with client.workspaces.peers.with_streaming_response.chat(
            peer_id="peer_id",
            workspace_id="workspace_id",
            query="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            peer = response.parse()
            assert_matches_type(PeerChatResponse, peer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_chat(self, client: Honcho) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            client.workspaces.peers.with_raw_response.chat(
                peer_id="peer_id",
                workspace_id="",
                query="x",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `peer_id` but received ''"):
            client.workspaces.peers.with_raw_response.chat(
                peer_id="",
                workspace_id="workspace_id",
                query="x",
            )

    @parametrize
    def test_method_get_or_create(self, client: Honcho) -> None:
        peer = client.workspaces.peers.get_or_create(
            workspace_id="workspace_id",
            id="id",
        )
        assert_matches_type(Peer, peer, path=["response"])

    @parametrize
    def test_method_get_or_create_with_all_params(self, client: Honcho) -> None:
        peer = client.workspaces.peers.get_or_create(
            workspace_id="workspace_id",
            id="id",
            configuration={"foo": "bar"},
            metadata={"foo": "bar"},
        )
        assert_matches_type(Peer, peer, path=["response"])

    @parametrize
    def test_raw_response_get_or_create(self, client: Honcho) -> None:
        response = client.workspaces.peers.with_raw_response.get_or_create(
            workspace_id="workspace_id",
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        peer = response.parse()
        assert_matches_type(Peer, peer, path=["response"])

    @parametrize
    def test_streaming_response_get_or_create(self, client: Honcho) -> None:
        with client.workspaces.peers.with_streaming_response.get_or_create(
            workspace_id="workspace_id",
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            peer = response.parse()
            assert_matches_type(Peer, peer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_or_create(self, client: Honcho) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            client.workspaces.peers.with_raw_response.get_or_create(
                workspace_id="",
                id="id",
            )

    @parametrize
    def test_method_search(self, client: Honcho) -> None:
        peer = client.workspaces.peers.search(
            peer_id="peer_id",
            workspace_id="workspace_id",
            query="query",
        )
        assert_matches_type(PeerSearchResponse, peer, path=["response"])

    @parametrize
    def test_method_search_with_all_params(self, client: Honcho) -> None:
        peer = client.workspaces.peers.search(
            peer_id="peer_id",
            workspace_id="workspace_id",
            query="query",
            filters={"foo": "bar"},
            limit=1,
        )
        assert_matches_type(PeerSearchResponse, peer, path=["response"])

    @parametrize
    def test_raw_response_search(self, client: Honcho) -> None:
        response = client.workspaces.peers.with_raw_response.search(
            peer_id="peer_id",
            workspace_id="workspace_id",
            query="query",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        peer = response.parse()
        assert_matches_type(PeerSearchResponse, peer, path=["response"])

    @parametrize
    def test_streaming_response_search(self, client: Honcho) -> None:
        with client.workspaces.peers.with_streaming_response.search(
            peer_id="peer_id",
            workspace_id="workspace_id",
            query="query",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            peer = response.parse()
            assert_matches_type(PeerSearchResponse, peer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_search(self, client: Honcho) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            client.workspaces.peers.with_raw_response.search(
                peer_id="peer_id",
                workspace_id="",
                query="query",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `peer_id` but received ''"):
            client.workspaces.peers.with_raw_response.search(
                peer_id="",
                workspace_id="workspace_id",
                query="query",
            )

    @parametrize
    def test_method_working_representation(self, client: Honcho) -> None:
        peer = client.workspaces.peers.working_representation(
            peer_id="peer_id",
            workspace_id="workspace_id",
        )
        assert_matches_type(PeerWorkingRepresentationResponse, peer, path=["response"])

    @parametrize
    def test_method_working_representation_with_all_params(self, client: Honcho) -> None:
        peer = client.workspaces.peers.working_representation(
            peer_id="peer_id",
            workspace_id="workspace_id",
            session_id="session_id",
            target="target",
        )
        assert_matches_type(PeerWorkingRepresentationResponse, peer, path=["response"])

    @parametrize
    def test_raw_response_working_representation(self, client: Honcho) -> None:
        response = client.workspaces.peers.with_raw_response.working_representation(
            peer_id="peer_id",
            workspace_id="workspace_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        peer = response.parse()
        assert_matches_type(PeerWorkingRepresentationResponse, peer, path=["response"])

    @parametrize
    def test_streaming_response_working_representation(self, client: Honcho) -> None:
        with client.workspaces.peers.with_streaming_response.working_representation(
            peer_id="peer_id",
            workspace_id="workspace_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            peer = response.parse()
            assert_matches_type(PeerWorkingRepresentationResponse, peer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_working_representation(self, client: Honcho) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            client.workspaces.peers.with_raw_response.working_representation(
                peer_id="peer_id",
                workspace_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `peer_id` but received ''"):
            client.workspaces.peers.with_raw_response.working_representation(
                peer_id="",
                workspace_id="workspace_id",
            )


class TestAsyncPeers:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_update(self, async_client: AsyncHoncho) -> None:
        peer = await async_client.workspaces.peers.update(
            peer_id="peer_id",
            workspace_id="workspace_id",
        )
        assert_matches_type(Peer, peer, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncHoncho) -> None:
        peer = await async_client.workspaces.peers.update(
            peer_id="peer_id",
            workspace_id="workspace_id",
            configuration={"foo": "bar"},
            metadata={"foo": "bar"},
        )
        assert_matches_type(Peer, peer, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncHoncho) -> None:
        response = await async_client.workspaces.peers.with_raw_response.update(
            peer_id="peer_id",
            workspace_id="workspace_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        peer = await response.parse()
        assert_matches_type(Peer, peer, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncHoncho) -> None:
        async with async_client.workspaces.peers.with_streaming_response.update(
            peer_id="peer_id",
            workspace_id="workspace_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            peer = await response.parse()
            assert_matches_type(Peer, peer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncHoncho) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            await async_client.workspaces.peers.with_raw_response.update(
                peer_id="peer_id",
                workspace_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `peer_id` but received ''"):
            await async_client.workspaces.peers.with_raw_response.update(
                peer_id="",
                workspace_id="workspace_id",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncHoncho) -> None:
        peer = await async_client.workspaces.peers.list(
            workspace_id="workspace_id",
        )
        assert_matches_type(AsyncPage[Peer], peer, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncHoncho) -> None:
        peer = await async_client.workspaces.peers.list(
            workspace_id="workspace_id",
            page=1,
            size=1,
            filters={"foo": "bar"},
        )
        assert_matches_type(AsyncPage[Peer], peer, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncHoncho) -> None:
        response = await async_client.workspaces.peers.with_raw_response.list(
            workspace_id="workspace_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        peer = await response.parse()
        assert_matches_type(AsyncPage[Peer], peer, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncHoncho) -> None:
        async with async_client.workspaces.peers.with_streaming_response.list(
            workspace_id="workspace_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            peer = await response.parse()
            assert_matches_type(AsyncPage[Peer], peer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncHoncho) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            await async_client.workspaces.peers.with_raw_response.list(
                workspace_id="",
            )

    @parametrize
    async def test_method_card(self, async_client: AsyncHoncho) -> None:
        peer = await async_client.workspaces.peers.card(
            peer_id="peer_id",
            workspace_id="workspace_id",
        )
        assert_matches_type(PeerCardResponse, peer, path=["response"])

    @parametrize
    async def test_method_card_with_all_params(self, async_client: AsyncHoncho) -> None:
        peer = await async_client.workspaces.peers.card(
            peer_id="peer_id",
            workspace_id="workspace_id",
            target="target",
        )
        assert_matches_type(PeerCardResponse, peer, path=["response"])

    @parametrize
    async def test_raw_response_card(self, async_client: AsyncHoncho) -> None:
        response = await async_client.workspaces.peers.with_raw_response.card(
            peer_id="peer_id",
            workspace_id="workspace_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        peer = await response.parse()
        assert_matches_type(PeerCardResponse, peer, path=["response"])

    @parametrize
    async def test_streaming_response_card(self, async_client: AsyncHoncho) -> None:
        async with async_client.workspaces.peers.with_streaming_response.card(
            peer_id="peer_id",
            workspace_id="workspace_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            peer = await response.parse()
            assert_matches_type(PeerCardResponse, peer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_card(self, async_client: AsyncHoncho) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            await async_client.workspaces.peers.with_raw_response.card(
                peer_id="peer_id",
                workspace_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `peer_id` but received ''"):
            await async_client.workspaces.peers.with_raw_response.card(
                peer_id="",
                workspace_id="workspace_id",
            )

    @parametrize
    async def test_method_chat(self, async_client: AsyncHoncho) -> None:
        peer = await async_client.workspaces.peers.chat(
            peer_id="peer_id",
            workspace_id="workspace_id",
            query="x",
        )
        assert_matches_type(PeerChatResponse, peer, path=["response"])

    @parametrize
    async def test_method_chat_with_all_params(self, async_client: AsyncHoncho) -> None:
        peer = await async_client.workspaces.peers.chat(
            peer_id="peer_id",
            workspace_id="workspace_id",
            query="x",
            session_id="session_id",
            stream=True,
            target="target",
        )
        assert_matches_type(PeerChatResponse, peer, path=["response"])

    @parametrize
    async def test_raw_response_chat(self, async_client: AsyncHoncho) -> None:
        response = await async_client.workspaces.peers.with_raw_response.chat(
            peer_id="peer_id",
            workspace_id="workspace_id",
            query="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        peer = await response.parse()
        assert_matches_type(PeerChatResponse, peer, path=["response"])

    @parametrize
    async def test_streaming_response_chat(self, async_client: AsyncHoncho) -> None:
        async with async_client.workspaces.peers.with_streaming_response.chat(
            peer_id="peer_id",
            workspace_id="workspace_id",
            query="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            peer = await response.parse()
            assert_matches_type(PeerChatResponse, peer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_chat(self, async_client: AsyncHoncho) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            await async_client.workspaces.peers.with_raw_response.chat(
                peer_id="peer_id",
                workspace_id="",
                query="x",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `peer_id` but received ''"):
            await async_client.workspaces.peers.with_raw_response.chat(
                peer_id="",
                workspace_id="workspace_id",
                query="x",
            )

    @parametrize
    async def test_method_get_or_create(self, async_client: AsyncHoncho) -> None:
        peer = await async_client.workspaces.peers.get_or_create(
            workspace_id="workspace_id",
            id="id",
        )
        assert_matches_type(Peer, peer, path=["response"])

    @parametrize
    async def test_method_get_or_create_with_all_params(self, async_client: AsyncHoncho) -> None:
        peer = await async_client.workspaces.peers.get_or_create(
            workspace_id="workspace_id",
            id="id",
            configuration={"foo": "bar"},
            metadata={"foo": "bar"},
        )
        assert_matches_type(Peer, peer, path=["response"])

    @parametrize
    async def test_raw_response_get_or_create(self, async_client: AsyncHoncho) -> None:
        response = await async_client.workspaces.peers.with_raw_response.get_or_create(
            workspace_id="workspace_id",
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        peer = await response.parse()
        assert_matches_type(Peer, peer, path=["response"])

    @parametrize
    async def test_streaming_response_get_or_create(self, async_client: AsyncHoncho) -> None:
        async with async_client.workspaces.peers.with_streaming_response.get_or_create(
            workspace_id="workspace_id",
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            peer = await response.parse()
            assert_matches_type(Peer, peer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_or_create(self, async_client: AsyncHoncho) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            await async_client.workspaces.peers.with_raw_response.get_or_create(
                workspace_id="",
                id="id",
            )

    @parametrize
    async def test_method_search(self, async_client: AsyncHoncho) -> None:
        peer = await async_client.workspaces.peers.search(
            peer_id="peer_id",
            workspace_id="workspace_id",
            query="query",
        )
        assert_matches_type(PeerSearchResponse, peer, path=["response"])

    @parametrize
    async def test_method_search_with_all_params(self, async_client: AsyncHoncho) -> None:
        peer = await async_client.workspaces.peers.search(
            peer_id="peer_id",
            workspace_id="workspace_id",
            query="query",
            filters={"foo": "bar"},
            limit=1,
        )
        assert_matches_type(PeerSearchResponse, peer, path=["response"])

    @parametrize
    async def test_raw_response_search(self, async_client: AsyncHoncho) -> None:
        response = await async_client.workspaces.peers.with_raw_response.search(
            peer_id="peer_id",
            workspace_id="workspace_id",
            query="query",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        peer = await response.parse()
        assert_matches_type(PeerSearchResponse, peer, path=["response"])

    @parametrize
    async def test_streaming_response_search(self, async_client: AsyncHoncho) -> None:
        async with async_client.workspaces.peers.with_streaming_response.search(
            peer_id="peer_id",
            workspace_id="workspace_id",
            query="query",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            peer = await response.parse()
            assert_matches_type(PeerSearchResponse, peer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_search(self, async_client: AsyncHoncho) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            await async_client.workspaces.peers.with_raw_response.search(
                peer_id="peer_id",
                workspace_id="",
                query="query",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `peer_id` but received ''"):
            await async_client.workspaces.peers.with_raw_response.search(
                peer_id="",
                workspace_id="workspace_id",
                query="query",
            )

    @parametrize
    async def test_method_working_representation(self, async_client: AsyncHoncho) -> None:
        peer = await async_client.workspaces.peers.working_representation(
            peer_id="peer_id",
            workspace_id="workspace_id",
        )
        assert_matches_type(PeerWorkingRepresentationResponse, peer, path=["response"])

    @parametrize
    async def test_method_working_representation_with_all_params(self, async_client: AsyncHoncho) -> None:
        peer = await async_client.workspaces.peers.working_representation(
            peer_id="peer_id",
            workspace_id="workspace_id",
            session_id="session_id",
            target="target",
        )
        assert_matches_type(PeerWorkingRepresentationResponse, peer, path=["response"])

    @parametrize
    async def test_raw_response_working_representation(self, async_client: AsyncHoncho) -> None:
        response = await async_client.workspaces.peers.with_raw_response.working_representation(
            peer_id="peer_id",
            workspace_id="workspace_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        peer = await response.parse()
        assert_matches_type(PeerWorkingRepresentationResponse, peer, path=["response"])

    @parametrize
    async def test_streaming_response_working_representation(self, async_client: AsyncHoncho) -> None:
        async with async_client.workspaces.peers.with_streaming_response.working_representation(
            peer_id="peer_id",
            workspace_id="workspace_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            peer = await response.parse()
            assert_matches_type(PeerWorkingRepresentationResponse, peer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_working_representation(self, async_client: AsyncHoncho) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            await async_client.workspaces.peers.with_raw_response.working_representation(
                peer_id="peer_id",
                workspace_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `peer_id` but received ''"):
            await async_client.workspaces.peers.with_raw_response.working_representation(
                peer_id="",
                workspace_id="workspace_id",
            )
