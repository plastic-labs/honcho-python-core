# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from honcho_core import Honcho, AsyncHoncho
from tests.utils import assert_matches_type
from honcho_core.pagination import SyncPage, AsyncPage
from honcho_core.types.workspaces import Peer, Session
from honcho_core.types.workspaces.sessions import (
    SessionPeerConfig,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPeers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Honcho) -> None:
        peer = client.workspaces.sessions.peers.list(
            session_id="session_id",
            workspace_id="workspace_id",
        )
        assert_matches_type(SyncPage[Peer], peer, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Honcho) -> None:
        peer = client.workspaces.sessions.peers.list(
            session_id="session_id",
            workspace_id="workspace_id",
            page=1,
            size=1,
        )
        assert_matches_type(SyncPage[Peer], peer, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Honcho) -> None:
        response = client.workspaces.sessions.peers.with_raw_response.list(
            session_id="session_id",
            workspace_id="workspace_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        peer = response.parse()
        assert_matches_type(SyncPage[Peer], peer, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Honcho) -> None:
        with client.workspaces.sessions.peers.with_streaming_response.list(
            session_id="session_id",
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
            client.workspaces.sessions.peers.with_raw_response.list(
                session_id="session_id",
                workspace_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            client.workspaces.sessions.peers.with_raw_response.list(
                session_id="",
                workspace_id="workspace_id",
            )

    @parametrize
    def test_method_add(self, client: Honcho) -> None:
        peer = client.workspaces.sessions.peers.add(
            session_id="session_id",
            workspace_id="workspace_id",
            body={"foo": {}},
        )
        assert_matches_type(Session, peer, path=["response"])

    @parametrize
    def test_raw_response_add(self, client: Honcho) -> None:
        response = client.workspaces.sessions.peers.with_raw_response.add(
            session_id="session_id",
            workspace_id="workspace_id",
            body={"foo": {}},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        peer = response.parse()
        assert_matches_type(Session, peer, path=["response"])

    @parametrize
    def test_streaming_response_add(self, client: Honcho) -> None:
        with client.workspaces.sessions.peers.with_streaming_response.add(
            session_id="session_id",
            workspace_id="workspace_id",
            body={"foo": {}},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            peer = response.parse()
            assert_matches_type(Session, peer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_add(self, client: Honcho) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            client.workspaces.sessions.peers.with_raw_response.add(
                session_id="session_id",
                workspace_id="",
                body={"foo": {}},
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            client.workspaces.sessions.peers.with_raw_response.add(
                session_id="",
                workspace_id="workspace_id",
                body={"foo": {}},
            )

    @parametrize
    def test_method_config(self, client: Honcho) -> None:
        peer = client.workspaces.sessions.peers.config(
            peer_id="peer_id",
            workspace_id="workspace_id",
            session_id="session_id",
        )
        assert_matches_type(SessionPeerConfig, peer, path=["response"])

    @parametrize
    def test_raw_response_config(self, client: Honcho) -> None:
        response = client.workspaces.sessions.peers.with_raw_response.config(
            peer_id="peer_id",
            workspace_id="workspace_id",
            session_id="session_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        peer = response.parse()
        assert_matches_type(SessionPeerConfig, peer, path=["response"])

    @parametrize
    def test_streaming_response_config(self, client: Honcho) -> None:
        with client.workspaces.sessions.peers.with_streaming_response.config(
            peer_id="peer_id",
            workspace_id="workspace_id",
            session_id="session_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            peer = response.parse()
            assert_matches_type(SessionPeerConfig, peer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_config(self, client: Honcho) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            client.workspaces.sessions.peers.with_raw_response.config(
                peer_id="peer_id",
                workspace_id="",
                session_id="session_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            client.workspaces.sessions.peers.with_raw_response.config(
                peer_id="peer_id",
                workspace_id="workspace_id",
                session_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `peer_id` but received ''"):
            client.workspaces.sessions.peers.with_raw_response.config(
                peer_id="",
                workspace_id="workspace_id",
                session_id="session_id",
            )

    @parametrize
    def test_method_remove(self, client: Honcho) -> None:
        peer = client.workspaces.sessions.peers.remove(
            session_id="session_id",
            workspace_id="workspace_id",
            body=["string"],
        )
        assert_matches_type(Session, peer, path=["response"])

    @parametrize
    def test_raw_response_remove(self, client: Honcho) -> None:
        response = client.workspaces.sessions.peers.with_raw_response.remove(
            session_id="session_id",
            workspace_id="workspace_id",
            body=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        peer = response.parse()
        assert_matches_type(Session, peer, path=["response"])

    @parametrize
    def test_streaming_response_remove(self, client: Honcho) -> None:
        with client.workspaces.sessions.peers.with_streaming_response.remove(
            session_id="session_id",
            workspace_id="workspace_id",
            body=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            peer = response.parse()
            assert_matches_type(Session, peer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_remove(self, client: Honcho) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            client.workspaces.sessions.peers.with_raw_response.remove(
                session_id="session_id",
                workspace_id="",
                body=["string"],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            client.workspaces.sessions.peers.with_raw_response.remove(
                session_id="",
                workspace_id="workspace_id",
                body=["string"],
            )

    @parametrize
    def test_method_set(self, client: Honcho) -> None:
        peer = client.workspaces.sessions.peers.set(
            session_id="session_id",
            workspace_id="workspace_id",
            body={"foo": {}},
        )
        assert_matches_type(Session, peer, path=["response"])

    @parametrize
    def test_raw_response_set(self, client: Honcho) -> None:
        response = client.workspaces.sessions.peers.with_raw_response.set(
            session_id="session_id",
            workspace_id="workspace_id",
            body={"foo": {}},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        peer = response.parse()
        assert_matches_type(Session, peer, path=["response"])

    @parametrize
    def test_streaming_response_set(self, client: Honcho) -> None:
        with client.workspaces.sessions.peers.with_streaming_response.set(
            session_id="session_id",
            workspace_id="workspace_id",
            body={"foo": {}},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            peer = response.parse()
            assert_matches_type(Session, peer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_set(self, client: Honcho) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            client.workspaces.sessions.peers.with_raw_response.set(
                session_id="session_id",
                workspace_id="",
                body={"foo": {}},
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            client.workspaces.sessions.peers.with_raw_response.set(
                session_id="",
                workspace_id="workspace_id",
                body={"foo": {}},
            )

    @parametrize
    def test_method_set_config(self, client: Honcho) -> None:
        peer = client.workspaces.sessions.peers.set_config(
            peer_id="peer_id",
            workspace_id="workspace_id",
            session_id="session_id",
        )
        assert peer is None

    @parametrize
    def test_method_set_config_with_all_params(self, client: Honcho) -> None:
        peer = client.workspaces.sessions.peers.set_config(
            peer_id="peer_id",
            workspace_id="workspace_id",
            session_id="session_id",
            observe_me=True,
            observe_others=True,
        )
        assert peer is None

    @parametrize
    def test_raw_response_set_config(self, client: Honcho) -> None:
        response = client.workspaces.sessions.peers.with_raw_response.set_config(
            peer_id="peer_id",
            workspace_id="workspace_id",
            session_id="session_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        peer = response.parse()
        assert peer is None

    @parametrize
    def test_streaming_response_set_config(self, client: Honcho) -> None:
        with client.workspaces.sessions.peers.with_streaming_response.set_config(
            peer_id="peer_id",
            workspace_id="workspace_id",
            session_id="session_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            peer = response.parse()
            assert peer is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_set_config(self, client: Honcho) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            client.workspaces.sessions.peers.with_raw_response.set_config(
                peer_id="peer_id",
                workspace_id="",
                session_id="session_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            client.workspaces.sessions.peers.with_raw_response.set_config(
                peer_id="peer_id",
                workspace_id="workspace_id",
                session_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `peer_id` but received ''"):
            client.workspaces.sessions.peers.with_raw_response.set_config(
                peer_id="",
                workspace_id="workspace_id",
                session_id="session_id",
            )


class TestAsyncPeers:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_list(self, async_client: AsyncHoncho) -> None:
        peer = await async_client.workspaces.sessions.peers.list(
            session_id="session_id",
            workspace_id="workspace_id",
        )
        assert_matches_type(AsyncPage[Peer], peer, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncHoncho) -> None:
        peer = await async_client.workspaces.sessions.peers.list(
            session_id="session_id",
            workspace_id="workspace_id",
            page=1,
            size=1,
        )
        assert_matches_type(AsyncPage[Peer], peer, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncHoncho) -> None:
        response = await async_client.workspaces.sessions.peers.with_raw_response.list(
            session_id="session_id",
            workspace_id="workspace_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        peer = await response.parse()
        assert_matches_type(AsyncPage[Peer], peer, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncHoncho) -> None:
        async with async_client.workspaces.sessions.peers.with_streaming_response.list(
            session_id="session_id",
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
            await async_client.workspaces.sessions.peers.with_raw_response.list(
                session_id="session_id",
                workspace_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            await async_client.workspaces.sessions.peers.with_raw_response.list(
                session_id="",
                workspace_id="workspace_id",
            )

    @parametrize
    async def test_method_add(self, async_client: AsyncHoncho) -> None:
        peer = await async_client.workspaces.sessions.peers.add(
            session_id="session_id",
            workspace_id="workspace_id",
            body={"foo": {}},
        )
        assert_matches_type(Session, peer, path=["response"])

    @parametrize
    async def test_raw_response_add(self, async_client: AsyncHoncho) -> None:
        response = await async_client.workspaces.sessions.peers.with_raw_response.add(
            session_id="session_id",
            workspace_id="workspace_id",
            body={"foo": {}},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        peer = await response.parse()
        assert_matches_type(Session, peer, path=["response"])

    @parametrize
    async def test_streaming_response_add(self, async_client: AsyncHoncho) -> None:
        async with async_client.workspaces.sessions.peers.with_streaming_response.add(
            session_id="session_id",
            workspace_id="workspace_id",
            body={"foo": {}},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            peer = await response.parse()
            assert_matches_type(Session, peer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_add(self, async_client: AsyncHoncho) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            await async_client.workspaces.sessions.peers.with_raw_response.add(
                session_id="session_id",
                workspace_id="",
                body={"foo": {}},
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            await async_client.workspaces.sessions.peers.with_raw_response.add(
                session_id="",
                workspace_id="workspace_id",
                body={"foo": {}},
            )

    @parametrize
    async def test_method_config(self, async_client: AsyncHoncho) -> None:
        peer = await async_client.workspaces.sessions.peers.config(
            peer_id="peer_id",
            workspace_id="workspace_id",
            session_id="session_id",
        )
        assert_matches_type(SessionPeerConfig, peer, path=["response"])

    @parametrize
    async def test_raw_response_config(self, async_client: AsyncHoncho) -> None:
        response = await async_client.workspaces.sessions.peers.with_raw_response.config(
            peer_id="peer_id",
            workspace_id="workspace_id",
            session_id="session_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        peer = await response.parse()
        assert_matches_type(SessionPeerConfig, peer, path=["response"])

    @parametrize
    async def test_streaming_response_config(self, async_client: AsyncHoncho) -> None:
        async with async_client.workspaces.sessions.peers.with_streaming_response.config(
            peer_id="peer_id",
            workspace_id="workspace_id",
            session_id="session_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            peer = await response.parse()
            assert_matches_type(SessionPeerConfig, peer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_config(self, async_client: AsyncHoncho) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            await async_client.workspaces.sessions.peers.with_raw_response.config(
                peer_id="peer_id",
                workspace_id="",
                session_id="session_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            await async_client.workspaces.sessions.peers.with_raw_response.config(
                peer_id="peer_id",
                workspace_id="workspace_id",
                session_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `peer_id` but received ''"):
            await async_client.workspaces.sessions.peers.with_raw_response.config(
                peer_id="",
                workspace_id="workspace_id",
                session_id="session_id",
            )

    @parametrize
    async def test_method_remove(self, async_client: AsyncHoncho) -> None:
        peer = await async_client.workspaces.sessions.peers.remove(
            session_id="session_id",
            workspace_id="workspace_id",
            body=["string"],
        )
        assert_matches_type(Session, peer, path=["response"])

    @parametrize
    async def test_raw_response_remove(self, async_client: AsyncHoncho) -> None:
        response = await async_client.workspaces.sessions.peers.with_raw_response.remove(
            session_id="session_id",
            workspace_id="workspace_id",
            body=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        peer = await response.parse()
        assert_matches_type(Session, peer, path=["response"])

    @parametrize
    async def test_streaming_response_remove(self, async_client: AsyncHoncho) -> None:
        async with async_client.workspaces.sessions.peers.with_streaming_response.remove(
            session_id="session_id",
            workspace_id="workspace_id",
            body=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            peer = await response.parse()
            assert_matches_type(Session, peer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_remove(self, async_client: AsyncHoncho) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            await async_client.workspaces.sessions.peers.with_raw_response.remove(
                session_id="session_id",
                workspace_id="",
                body=["string"],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            await async_client.workspaces.sessions.peers.with_raw_response.remove(
                session_id="",
                workspace_id="workspace_id",
                body=["string"],
            )

    @parametrize
    async def test_method_set(self, async_client: AsyncHoncho) -> None:
        peer = await async_client.workspaces.sessions.peers.set(
            session_id="session_id",
            workspace_id="workspace_id",
            body={"foo": {}},
        )
        assert_matches_type(Session, peer, path=["response"])

    @parametrize
    async def test_raw_response_set(self, async_client: AsyncHoncho) -> None:
        response = await async_client.workspaces.sessions.peers.with_raw_response.set(
            session_id="session_id",
            workspace_id="workspace_id",
            body={"foo": {}},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        peer = await response.parse()
        assert_matches_type(Session, peer, path=["response"])

    @parametrize
    async def test_streaming_response_set(self, async_client: AsyncHoncho) -> None:
        async with async_client.workspaces.sessions.peers.with_streaming_response.set(
            session_id="session_id",
            workspace_id="workspace_id",
            body={"foo": {}},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            peer = await response.parse()
            assert_matches_type(Session, peer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_set(self, async_client: AsyncHoncho) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            await async_client.workspaces.sessions.peers.with_raw_response.set(
                session_id="session_id",
                workspace_id="",
                body={"foo": {}},
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            await async_client.workspaces.sessions.peers.with_raw_response.set(
                session_id="",
                workspace_id="workspace_id",
                body={"foo": {}},
            )

    @parametrize
    async def test_method_set_config(self, async_client: AsyncHoncho) -> None:
        peer = await async_client.workspaces.sessions.peers.set_config(
            peer_id="peer_id",
            workspace_id="workspace_id",
            session_id="session_id",
        )
        assert peer is None

    @parametrize
    async def test_method_set_config_with_all_params(self, async_client: AsyncHoncho) -> None:
        peer = await async_client.workspaces.sessions.peers.set_config(
            peer_id="peer_id",
            workspace_id="workspace_id",
            session_id="session_id",
            observe_me=True,
            observe_others=True,
        )
        assert peer is None

    @parametrize
    async def test_raw_response_set_config(self, async_client: AsyncHoncho) -> None:
        response = await async_client.workspaces.sessions.peers.with_raw_response.set_config(
            peer_id="peer_id",
            workspace_id="workspace_id",
            session_id="session_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        peer = await response.parse()
        assert peer is None

    @parametrize
    async def test_streaming_response_set_config(self, async_client: AsyncHoncho) -> None:
        async with async_client.workspaces.sessions.peers.with_streaming_response.set_config(
            peer_id="peer_id",
            workspace_id="workspace_id",
            session_id="session_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            peer = await response.parse()
            assert peer is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_set_config(self, async_client: AsyncHoncho) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            await async_client.workspaces.sessions.peers.with_raw_response.set_config(
                peer_id="peer_id",
                workspace_id="",
                session_id="session_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            await async_client.workspaces.sessions.peers.with_raw_response.set_config(
                peer_id="peer_id",
                workspace_id="workspace_id",
                session_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `peer_id` but received ''"):
            await async_client.workspaces.sessions.peers.with_raw_response.set_config(
                peer_id="",
                workspace_id="workspace_id",
                session_id="session_id",
            )
