# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from honcho_core import Honcho, AsyncHoncho
from tests.utils import assert_matches_type
from honcho_core.types.workspaces import QueueStatusResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestQueue:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_status(self, client: Honcho) -> None:
        queue = client.workspaces.queue.status(
            workspace_id="workspace_id",
        )
        assert_matches_type(QueueStatusResponse, queue, path=["response"])

    @parametrize
    def test_method_status_with_all_params(self, client: Honcho) -> None:
        queue = client.workspaces.queue.status(
            workspace_id="workspace_id",
            observer_id="observer_id",
            sender_id="sender_id",
            session_id="session_id",
        )
        assert_matches_type(QueueStatusResponse, queue, path=["response"])

    @parametrize
    def test_raw_response_status(self, client: Honcho) -> None:
        response = client.workspaces.queue.with_raw_response.status(
            workspace_id="workspace_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        queue = response.parse()
        assert_matches_type(QueueStatusResponse, queue, path=["response"])

    @parametrize
    def test_streaming_response_status(self, client: Honcho) -> None:
        with client.workspaces.queue.with_streaming_response.status(
            workspace_id="workspace_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            queue = response.parse()
            assert_matches_type(QueueStatusResponse, queue, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_status(self, client: Honcho) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            client.workspaces.queue.with_raw_response.status(
                workspace_id="",
            )


class TestAsyncQueue:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_status(self, async_client: AsyncHoncho) -> None:
        queue = await async_client.workspaces.queue.status(
            workspace_id="workspace_id",
        )
        assert_matches_type(QueueStatusResponse, queue, path=["response"])

    @parametrize
    async def test_method_status_with_all_params(self, async_client: AsyncHoncho) -> None:
        queue = await async_client.workspaces.queue.status(
            workspace_id="workspace_id",
            observer_id="observer_id",
            sender_id="sender_id",
            session_id="session_id",
        )
        assert_matches_type(QueueStatusResponse, queue, path=["response"])

    @parametrize
    async def test_raw_response_status(self, async_client: AsyncHoncho) -> None:
        response = await async_client.workspaces.queue.with_raw_response.status(
            workspace_id="workspace_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        queue = await response.parse()
        assert_matches_type(QueueStatusResponse, queue, path=["response"])

    @parametrize
    async def test_streaming_response_status(self, async_client: AsyncHoncho) -> None:
        async with async_client.workspaces.queue.with_streaming_response.status(
            workspace_id="workspace_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            queue = await response.parse()
            assert_matches_type(QueueStatusResponse, queue, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_status(self, async_client: AsyncHoncho) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            await async_client.workspaces.queue.with_raw_response.status(
                workspace_id="",
            )
