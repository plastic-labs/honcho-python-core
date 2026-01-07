# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from honcho_core import Honcho, AsyncHoncho
from tests.utils import assert_matches_type
from honcho_core.pagination import SyncPage, AsyncPage
from honcho_core.types.workspaces import WebhookEndpoint

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestWebhooks:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Honcho) -> None:
        webhook = client.workspaces.webhooks.list(
            workspace_id="workspace_id",
        )
        assert_matches_type(SyncPage[WebhookEndpoint], webhook, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Honcho) -> None:
        webhook = client.workspaces.webhooks.list(
            workspace_id="workspace_id",
            page=1,
            size=1,
        )
        assert_matches_type(SyncPage[WebhookEndpoint], webhook, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Honcho) -> None:
        response = client.workspaces.webhooks.with_raw_response.list(
            workspace_id="workspace_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = response.parse()
        assert_matches_type(SyncPage[WebhookEndpoint], webhook, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Honcho) -> None:
        with client.workspaces.webhooks.with_streaming_response.list(
            workspace_id="workspace_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = response.parse()
            assert_matches_type(SyncPage[WebhookEndpoint], webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Honcho) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            client.workspaces.webhooks.with_raw_response.list(
                workspace_id="",
            )

    @parametrize
    def test_method_delete(self, client: Honcho) -> None:
        webhook = client.workspaces.webhooks.delete(
            endpoint_id="endpoint_id",
            workspace_id="workspace_id",
        )
        assert webhook is None

    @parametrize
    def test_raw_response_delete(self, client: Honcho) -> None:
        response = client.workspaces.webhooks.with_raw_response.delete(
            endpoint_id="endpoint_id",
            workspace_id="workspace_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = response.parse()
        assert webhook is None

    @parametrize
    def test_streaming_response_delete(self, client: Honcho) -> None:
        with client.workspaces.webhooks.with_streaming_response.delete(
            endpoint_id="endpoint_id",
            workspace_id="workspace_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = response.parse()
            assert webhook is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Honcho) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            client.workspaces.webhooks.with_raw_response.delete(
                endpoint_id="endpoint_id",
                workspace_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `endpoint_id` but received ''"):
            client.workspaces.webhooks.with_raw_response.delete(
                endpoint_id="",
                workspace_id="workspace_id",
            )

    @parametrize
    def test_method_get_or_create(self, client: Honcho) -> None:
        webhook = client.workspaces.webhooks.get_or_create(
            workspace_id="workspace_id",
            url="url",
        )
        assert_matches_type(WebhookEndpoint, webhook, path=["response"])

    @parametrize
    def test_raw_response_get_or_create(self, client: Honcho) -> None:
        response = client.workspaces.webhooks.with_raw_response.get_or_create(
            workspace_id="workspace_id",
            url="url",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = response.parse()
        assert_matches_type(WebhookEndpoint, webhook, path=["response"])

    @parametrize
    def test_streaming_response_get_or_create(self, client: Honcho) -> None:
        with client.workspaces.webhooks.with_streaming_response.get_or_create(
            workspace_id="workspace_id",
            url="url",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = response.parse()
            assert_matches_type(WebhookEndpoint, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_or_create(self, client: Honcho) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            client.workspaces.webhooks.with_raw_response.get_or_create(
                workspace_id="",
                url="url",
            )

    @parametrize
    def test_method_test_emit(self, client: Honcho) -> None:
        webhook = client.workspaces.webhooks.test_emit(
            "workspace_id",
        )
        assert_matches_type(object, webhook, path=["response"])

    @parametrize
    def test_raw_response_test_emit(self, client: Honcho) -> None:
        response = client.workspaces.webhooks.with_raw_response.test_emit(
            "workspace_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = response.parse()
        assert_matches_type(object, webhook, path=["response"])

    @parametrize
    def test_streaming_response_test_emit(self, client: Honcho) -> None:
        with client.workspaces.webhooks.with_streaming_response.test_emit(
            "workspace_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = response.parse()
            assert_matches_type(object, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_test_emit(self, client: Honcho) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            client.workspaces.webhooks.with_raw_response.test_emit(
                "",
            )


class TestAsyncWebhooks:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_list(self, async_client: AsyncHoncho) -> None:
        webhook = await async_client.workspaces.webhooks.list(
            workspace_id="workspace_id",
        )
        assert_matches_type(AsyncPage[WebhookEndpoint], webhook, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncHoncho) -> None:
        webhook = await async_client.workspaces.webhooks.list(
            workspace_id="workspace_id",
            page=1,
            size=1,
        )
        assert_matches_type(AsyncPage[WebhookEndpoint], webhook, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncHoncho) -> None:
        response = await async_client.workspaces.webhooks.with_raw_response.list(
            workspace_id="workspace_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = await response.parse()
        assert_matches_type(AsyncPage[WebhookEndpoint], webhook, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncHoncho) -> None:
        async with async_client.workspaces.webhooks.with_streaming_response.list(
            workspace_id="workspace_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = await response.parse()
            assert_matches_type(AsyncPage[WebhookEndpoint], webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncHoncho) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            await async_client.workspaces.webhooks.with_raw_response.list(
                workspace_id="",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncHoncho) -> None:
        webhook = await async_client.workspaces.webhooks.delete(
            endpoint_id="endpoint_id",
            workspace_id="workspace_id",
        )
        assert webhook is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncHoncho) -> None:
        response = await async_client.workspaces.webhooks.with_raw_response.delete(
            endpoint_id="endpoint_id",
            workspace_id="workspace_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = await response.parse()
        assert webhook is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncHoncho) -> None:
        async with async_client.workspaces.webhooks.with_streaming_response.delete(
            endpoint_id="endpoint_id",
            workspace_id="workspace_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = await response.parse()
            assert webhook is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncHoncho) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            await async_client.workspaces.webhooks.with_raw_response.delete(
                endpoint_id="endpoint_id",
                workspace_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `endpoint_id` but received ''"):
            await async_client.workspaces.webhooks.with_raw_response.delete(
                endpoint_id="",
                workspace_id="workspace_id",
            )

    @parametrize
    async def test_method_get_or_create(self, async_client: AsyncHoncho) -> None:
        webhook = await async_client.workspaces.webhooks.get_or_create(
            workspace_id="workspace_id",
            url="url",
        )
        assert_matches_type(WebhookEndpoint, webhook, path=["response"])

    @parametrize
    async def test_raw_response_get_or_create(self, async_client: AsyncHoncho) -> None:
        response = await async_client.workspaces.webhooks.with_raw_response.get_or_create(
            workspace_id="workspace_id",
            url="url",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = await response.parse()
        assert_matches_type(WebhookEndpoint, webhook, path=["response"])

    @parametrize
    async def test_streaming_response_get_or_create(self, async_client: AsyncHoncho) -> None:
        async with async_client.workspaces.webhooks.with_streaming_response.get_or_create(
            workspace_id="workspace_id",
            url="url",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = await response.parse()
            assert_matches_type(WebhookEndpoint, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_or_create(self, async_client: AsyncHoncho) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            await async_client.workspaces.webhooks.with_raw_response.get_or_create(
                workspace_id="",
                url="url",
            )

    @parametrize
    async def test_method_test_emit(self, async_client: AsyncHoncho) -> None:
        webhook = await async_client.workspaces.webhooks.test_emit(
            "workspace_id",
        )
        assert_matches_type(object, webhook, path=["response"])

    @parametrize
    async def test_raw_response_test_emit(self, async_client: AsyncHoncho) -> None:
        response = await async_client.workspaces.webhooks.with_raw_response.test_emit(
            "workspace_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = await response.parse()
        assert_matches_type(object, webhook, path=["response"])

    @parametrize
    async def test_streaming_response_test_emit(self, async_client: AsyncHoncho) -> None:
        async with async_client.workspaces.webhooks.with_streaming_response.test_emit(
            "workspace_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = await response.parse()
            assert_matches_type(object, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_test_emit(self, async_client: AsyncHoncho) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            await async_client.workspaces.webhooks.with_raw_response.test_emit(
                "",
            )
