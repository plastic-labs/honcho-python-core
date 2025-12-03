# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from honcho_core import Honcho, AsyncHoncho
from tests.utils import assert_matches_type
from honcho_core.pagination import SyncPage, AsyncPage
from honcho_core.types.workspaces.sessions import (
    Message,
    MessageCreateResponse,
    MessageUploadResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMessages:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Honcho) -> None:
        message = client.workspaces.sessions.messages.create(
            session_id="session_id",
            workspace_id="workspace_id",
            messages=[
                {
                    "content": "content",
                    "peer_id": "peer_id",
                }
            ],
        )
        assert_matches_type(MessageCreateResponse, message, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Honcho) -> None:
        response = client.workspaces.sessions.messages.with_raw_response.create(
            session_id="session_id",
            workspace_id="workspace_id",
            messages=[
                {
                    "content": "content",
                    "peer_id": "peer_id",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = response.parse()
        assert_matches_type(MessageCreateResponse, message, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Honcho) -> None:
        with client.workspaces.sessions.messages.with_streaming_response.create(
            session_id="session_id",
            workspace_id="workspace_id",
            messages=[
                {
                    "content": "content",
                    "peer_id": "peer_id",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = response.parse()
            assert_matches_type(MessageCreateResponse, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Honcho) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            client.workspaces.sessions.messages.with_raw_response.create(
                session_id="session_id",
                workspace_id="",
                messages=[
                    {
                        "content": "content",
                        "peer_id": "peer_id",
                    }
                ],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            client.workspaces.sessions.messages.with_raw_response.create(
                session_id="",
                workspace_id="workspace_id",
                messages=[
                    {
                        "content": "content",
                        "peer_id": "peer_id",
                    }
                ],
            )

    @parametrize
    def test_method_retrieve(self, client: Honcho) -> None:
        message = client.workspaces.sessions.messages.retrieve(
            message_id="message_id",
            workspace_id="workspace_id",
            session_id="session_id",
        )
        assert_matches_type(Message, message, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Honcho) -> None:
        response = client.workspaces.sessions.messages.with_raw_response.retrieve(
            message_id="message_id",
            workspace_id="workspace_id",
            session_id="session_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = response.parse()
        assert_matches_type(Message, message, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Honcho) -> None:
        with client.workspaces.sessions.messages.with_streaming_response.retrieve(
            message_id="message_id",
            workspace_id="workspace_id",
            session_id="session_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = response.parse()
            assert_matches_type(Message, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Honcho) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            client.workspaces.sessions.messages.with_raw_response.retrieve(
                message_id="message_id",
                workspace_id="",
                session_id="session_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            client.workspaces.sessions.messages.with_raw_response.retrieve(
                message_id="message_id",
                workspace_id="workspace_id",
                session_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `message_id` but received ''"):
            client.workspaces.sessions.messages.with_raw_response.retrieve(
                message_id="",
                workspace_id="workspace_id",
                session_id="session_id",
            )

    @parametrize
    def test_method_update(self, client: Honcho) -> None:
        message = client.workspaces.sessions.messages.update(
            message_id="message_id",
            workspace_id="workspace_id",
            session_id="session_id",
        )
        assert_matches_type(Message, message, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Honcho) -> None:
        message = client.workspaces.sessions.messages.update(
            message_id="message_id",
            workspace_id="workspace_id",
            session_id="session_id",
            metadata={"foo": "bar"},
        )
        assert_matches_type(Message, message, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Honcho) -> None:
        response = client.workspaces.sessions.messages.with_raw_response.update(
            message_id="message_id",
            workspace_id="workspace_id",
            session_id="session_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = response.parse()
        assert_matches_type(Message, message, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Honcho) -> None:
        with client.workspaces.sessions.messages.with_streaming_response.update(
            message_id="message_id",
            workspace_id="workspace_id",
            session_id="session_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = response.parse()
            assert_matches_type(Message, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Honcho) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            client.workspaces.sessions.messages.with_raw_response.update(
                message_id="message_id",
                workspace_id="",
                session_id="session_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            client.workspaces.sessions.messages.with_raw_response.update(
                message_id="message_id",
                workspace_id="workspace_id",
                session_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `message_id` but received ''"):
            client.workspaces.sessions.messages.with_raw_response.update(
                message_id="",
                workspace_id="workspace_id",
                session_id="session_id",
            )

    @parametrize
    def test_method_list(self, client: Honcho) -> None:
        message = client.workspaces.sessions.messages.list(
            session_id="session_id",
            workspace_id="workspace_id",
        )
        assert_matches_type(SyncPage[Message], message, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Honcho) -> None:
        message = client.workspaces.sessions.messages.list(
            session_id="session_id",
            workspace_id="workspace_id",
            page=1,
            reverse=True,
            size=1,
            filters={"foo": "bar"},
        )
        assert_matches_type(SyncPage[Message], message, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Honcho) -> None:
        response = client.workspaces.sessions.messages.with_raw_response.list(
            session_id="session_id",
            workspace_id="workspace_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = response.parse()
        assert_matches_type(SyncPage[Message], message, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Honcho) -> None:
        with client.workspaces.sessions.messages.with_streaming_response.list(
            session_id="session_id",
            workspace_id="workspace_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = response.parse()
            assert_matches_type(SyncPage[Message], message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Honcho) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            client.workspaces.sessions.messages.with_raw_response.list(
                session_id="session_id",
                workspace_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            client.workspaces.sessions.messages.with_raw_response.list(
                session_id="",
                workspace_id="workspace_id",
            )

    @parametrize
    def test_method_upload(self, client: Honcho) -> None:
        message = client.workspaces.sessions.messages.upload(
            session_id="session_id",
            workspace_id="workspace_id",
            file=b"raw file contents",
            peer_id="peer_id",
        )
        assert_matches_type(MessageUploadResponse, message, path=["response"])

    @parametrize
    def test_method_upload_with_all_params(self, client: Honcho) -> None:
        message = client.workspaces.sessions.messages.upload(
            session_id="session_id",
            workspace_id="workspace_id",
            file=b"raw file contents",
            peer_id="peer_id",
            configuration="configuration",
            created_at="created_at",
            metadata="metadata",
        )
        assert_matches_type(MessageUploadResponse, message, path=["response"])

    @parametrize
    def test_raw_response_upload(self, client: Honcho) -> None:
        response = client.workspaces.sessions.messages.with_raw_response.upload(
            session_id="session_id",
            workspace_id="workspace_id",
            file=b"raw file contents",
            peer_id="peer_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = response.parse()
        assert_matches_type(MessageUploadResponse, message, path=["response"])

    @parametrize
    def test_streaming_response_upload(self, client: Honcho) -> None:
        with client.workspaces.sessions.messages.with_streaming_response.upload(
            session_id="session_id",
            workspace_id="workspace_id",
            file=b"raw file contents",
            peer_id="peer_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = response.parse()
            assert_matches_type(MessageUploadResponse, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_upload(self, client: Honcho) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            client.workspaces.sessions.messages.with_raw_response.upload(
                session_id="session_id",
                workspace_id="",
                file=b"raw file contents",
                peer_id="peer_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            client.workspaces.sessions.messages.with_raw_response.upload(
                session_id="",
                workspace_id="workspace_id",
                file=b"raw file contents",
                peer_id="peer_id",
            )


class TestAsyncMessages:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncHoncho) -> None:
        message = await async_client.workspaces.sessions.messages.create(
            session_id="session_id",
            workspace_id="workspace_id",
            messages=[
                {
                    "content": "content",
                    "peer_id": "peer_id",
                }
            ],
        )
        assert_matches_type(MessageCreateResponse, message, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncHoncho) -> None:
        response = await async_client.workspaces.sessions.messages.with_raw_response.create(
            session_id="session_id",
            workspace_id="workspace_id",
            messages=[
                {
                    "content": "content",
                    "peer_id": "peer_id",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = await response.parse()
        assert_matches_type(MessageCreateResponse, message, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncHoncho) -> None:
        async with async_client.workspaces.sessions.messages.with_streaming_response.create(
            session_id="session_id",
            workspace_id="workspace_id",
            messages=[
                {
                    "content": "content",
                    "peer_id": "peer_id",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = await response.parse()
            assert_matches_type(MessageCreateResponse, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncHoncho) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            await async_client.workspaces.sessions.messages.with_raw_response.create(
                session_id="session_id",
                workspace_id="",
                messages=[
                    {
                        "content": "content",
                        "peer_id": "peer_id",
                    }
                ],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            await async_client.workspaces.sessions.messages.with_raw_response.create(
                session_id="",
                workspace_id="workspace_id",
                messages=[
                    {
                        "content": "content",
                        "peer_id": "peer_id",
                    }
                ],
            )

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncHoncho) -> None:
        message = await async_client.workspaces.sessions.messages.retrieve(
            message_id="message_id",
            workspace_id="workspace_id",
            session_id="session_id",
        )
        assert_matches_type(Message, message, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncHoncho) -> None:
        response = await async_client.workspaces.sessions.messages.with_raw_response.retrieve(
            message_id="message_id",
            workspace_id="workspace_id",
            session_id="session_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = await response.parse()
        assert_matches_type(Message, message, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncHoncho) -> None:
        async with async_client.workspaces.sessions.messages.with_streaming_response.retrieve(
            message_id="message_id",
            workspace_id="workspace_id",
            session_id="session_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = await response.parse()
            assert_matches_type(Message, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncHoncho) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            await async_client.workspaces.sessions.messages.with_raw_response.retrieve(
                message_id="message_id",
                workspace_id="",
                session_id="session_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            await async_client.workspaces.sessions.messages.with_raw_response.retrieve(
                message_id="message_id",
                workspace_id="workspace_id",
                session_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `message_id` but received ''"):
            await async_client.workspaces.sessions.messages.with_raw_response.retrieve(
                message_id="",
                workspace_id="workspace_id",
                session_id="session_id",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncHoncho) -> None:
        message = await async_client.workspaces.sessions.messages.update(
            message_id="message_id",
            workspace_id="workspace_id",
            session_id="session_id",
        )
        assert_matches_type(Message, message, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncHoncho) -> None:
        message = await async_client.workspaces.sessions.messages.update(
            message_id="message_id",
            workspace_id="workspace_id",
            session_id="session_id",
            metadata={"foo": "bar"},
        )
        assert_matches_type(Message, message, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncHoncho) -> None:
        response = await async_client.workspaces.sessions.messages.with_raw_response.update(
            message_id="message_id",
            workspace_id="workspace_id",
            session_id="session_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = await response.parse()
        assert_matches_type(Message, message, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncHoncho) -> None:
        async with async_client.workspaces.sessions.messages.with_streaming_response.update(
            message_id="message_id",
            workspace_id="workspace_id",
            session_id="session_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = await response.parse()
            assert_matches_type(Message, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncHoncho) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            await async_client.workspaces.sessions.messages.with_raw_response.update(
                message_id="message_id",
                workspace_id="",
                session_id="session_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            await async_client.workspaces.sessions.messages.with_raw_response.update(
                message_id="message_id",
                workspace_id="workspace_id",
                session_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `message_id` but received ''"):
            await async_client.workspaces.sessions.messages.with_raw_response.update(
                message_id="",
                workspace_id="workspace_id",
                session_id="session_id",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncHoncho) -> None:
        message = await async_client.workspaces.sessions.messages.list(
            session_id="session_id",
            workspace_id="workspace_id",
        )
        assert_matches_type(AsyncPage[Message], message, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncHoncho) -> None:
        message = await async_client.workspaces.sessions.messages.list(
            session_id="session_id",
            workspace_id="workspace_id",
            page=1,
            reverse=True,
            size=1,
            filters={"foo": "bar"},
        )
        assert_matches_type(AsyncPage[Message], message, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncHoncho) -> None:
        response = await async_client.workspaces.sessions.messages.with_raw_response.list(
            session_id="session_id",
            workspace_id="workspace_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = await response.parse()
        assert_matches_type(AsyncPage[Message], message, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncHoncho) -> None:
        async with async_client.workspaces.sessions.messages.with_streaming_response.list(
            session_id="session_id",
            workspace_id="workspace_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = await response.parse()
            assert_matches_type(AsyncPage[Message], message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncHoncho) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            await async_client.workspaces.sessions.messages.with_raw_response.list(
                session_id="session_id",
                workspace_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            await async_client.workspaces.sessions.messages.with_raw_response.list(
                session_id="",
                workspace_id="workspace_id",
            )

    @parametrize
    async def test_method_upload(self, async_client: AsyncHoncho) -> None:
        message = await async_client.workspaces.sessions.messages.upload(
            session_id="session_id",
            workspace_id="workspace_id",
            file=b"raw file contents",
            peer_id="peer_id",
        )
        assert_matches_type(MessageUploadResponse, message, path=["response"])

    @parametrize
    async def test_method_upload_with_all_params(self, async_client: AsyncHoncho) -> None:
        message = await async_client.workspaces.sessions.messages.upload(
            session_id="session_id",
            workspace_id="workspace_id",
            file=b"raw file contents",
            peer_id="peer_id",
            configuration="configuration",
            created_at="created_at",
            metadata="metadata",
        )
        assert_matches_type(MessageUploadResponse, message, path=["response"])

    @parametrize
    async def test_raw_response_upload(self, async_client: AsyncHoncho) -> None:
        response = await async_client.workspaces.sessions.messages.with_raw_response.upload(
            session_id="session_id",
            workspace_id="workspace_id",
            file=b"raw file contents",
            peer_id="peer_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = await response.parse()
        assert_matches_type(MessageUploadResponse, message, path=["response"])

    @parametrize
    async def test_streaming_response_upload(self, async_client: AsyncHoncho) -> None:
        async with async_client.workspaces.sessions.messages.with_streaming_response.upload(
            session_id="session_id",
            workspace_id="workspace_id",
            file=b"raw file contents",
            peer_id="peer_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = await response.parse()
            assert_matches_type(MessageUploadResponse, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_upload(self, async_client: AsyncHoncho) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            await async_client.workspaces.sessions.messages.with_raw_response.upload(
                session_id="session_id",
                workspace_id="",
                file=b"raw file contents",
                peer_id="peer_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            await async_client.workspaces.sessions.messages.with_raw_response.upload(
                session_id="",
                workspace_id="workspace_id",
                file=b"raw file contents",
                peer_id="peer_id",
            )
