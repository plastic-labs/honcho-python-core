# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from honcho_core import Honcho, AsyncHoncho
from tests.utils import assert_matches_type
from honcho_core.pagination import SyncPage, AsyncPage
from honcho_core.types.workspaces import (
    Observation,
    ObservationQueryResponse,
    ObservationCreateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestObservations:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Honcho) -> None:
        observation = client.workspaces.observations.create(
            workspace_id="workspace_id",
            observations=[
                {
                    "content": "x",
                    "observed_id": "observed_id",
                    "observer_id": "observer_id",
                    "session_id": "session_id",
                }
            ],
        )
        assert_matches_type(ObservationCreateResponse, observation, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Honcho) -> None:
        response = client.workspaces.observations.with_raw_response.create(
            workspace_id="workspace_id",
            observations=[
                {
                    "content": "x",
                    "observed_id": "observed_id",
                    "observer_id": "observer_id",
                    "session_id": "session_id",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        observation = response.parse()
        assert_matches_type(ObservationCreateResponse, observation, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Honcho) -> None:
        with client.workspaces.observations.with_streaming_response.create(
            workspace_id="workspace_id",
            observations=[
                {
                    "content": "x",
                    "observed_id": "observed_id",
                    "observer_id": "observer_id",
                    "session_id": "session_id",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            observation = response.parse()
            assert_matches_type(ObservationCreateResponse, observation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Honcho) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            client.workspaces.observations.with_raw_response.create(
                workspace_id="",
                observations=[
                    {
                        "content": "x",
                        "observed_id": "observed_id",
                        "observer_id": "observer_id",
                        "session_id": "session_id",
                    }
                ],
            )

    @parametrize
    def test_method_list(self, client: Honcho) -> None:
        observation = client.workspaces.observations.list(
            workspace_id="workspace_id",
        )
        assert_matches_type(SyncPage[Observation], observation, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Honcho) -> None:
        observation = client.workspaces.observations.list(
            workspace_id="workspace_id",
            page=1,
            reverse=True,
            size=1,
            filters={"foo": "bar"},
        )
        assert_matches_type(SyncPage[Observation], observation, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Honcho) -> None:
        response = client.workspaces.observations.with_raw_response.list(
            workspace_id="workspace_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        observation = response.parse()
        assert_matches_type(SyncPage[Observation], observation, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Honcho) -> None:
        with client.workspaces.observations.with_streaming_response.list(
            workspace_id="workspace_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            observation = response.parse()
            assert_matches_type(SyncPage[Observation], observation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Honcho) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            client.workspaces.observations.with_raw_response.list(
                workspace_id="",
            )

    @parametrize
    def test_method_delete(self, client: Honcho) -> None:
        observation = client.workspaces.observations.delete(
            observation_id="observation_id",
            workspace_id="workspace_id",
        )
        assert_matches_type(object, observation, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Honcho) -> None:
        response = client.workspaces.observations.with_raw_response.delete(
            observation_id="observation_id",
            workspace_id="workspace_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        observation = response.parse()
        assert_matches_type(object, observation, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Honcho) -> None:
        with client.workspaces.observations.with_streaming_response.delete(
            observation_id="observation_id",
            workspace_id="workspace_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            observation = response.parse()
            assert_matches_type(object, observation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Honcho) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            client.workspaces.observations.with_raw_response.delete(
                observation_id="observation_id",
                workspace_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `observation_id` but received ''"):
            client.workspaces.observations.with_raw_response.delete(
                observation_id="",
                workspace_id="workspace_id",
            )

    @parametrize
    def test_method_query(self, client: Honcho) -> None:
        observation = client.workspaces.observations.query(
            workspace_id="workspace_id",
            query="query",
        )
        assert_matches_type(ObservationQueryResponse, observation, path=["response"])

    @parametrize
    def test_method_query_with_all_params(self, client: Honcho) -> None:
        observation = client.workspaces.observations.query(
            workspace_id="workspace_id",
            query="query",
            distance=0,
            filters={"foo": "bar"},
            top_k=1,
        )
        assert_matches_type(ObservationQueryResponse, observation, path=["response"])

    @parametrize
    def test_raw_response_query(self, client: Honcho) -> None:
        response = client.workspaces.observations.with_raw_response.query(
            workspace_id="workspace_id",
            query="query",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        observation = response.parse()
        assert_matches_type(ObservationQueryResponse, observation, path=["response"])

    @parametrize
    def test_streaming_response_query(self, client: Honcho) -> None:
        with client.workspaces.observations.with_streaming_response.query(
            workspace_id="workspace_id",
            query="query",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            observation = response.parse()
            assert_matches_type(ObservationQueryResponse, observation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_query(self, client: Honcho) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            client.workspaces.observations.with_raw_response.query(
                workspace_id="",
                query="query",
            )


class TestAsyncObservations:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncHoncho) -> None:
        observation = await async_client.workspaces.observations.create(
            workspace_id="workspace_id",
            observations=[
                {
                    "content": "x",
                    "observed_id": "observed_id",
                    "observer_id": "observer_id",
                    "session_id": "session_id",
                }
            ],
        )
        assert_matches_type(ObservationCreateResponse, observation, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncHoncho) -> None:
        response = await async_client.workspaces.observations.with_raw_response.create(
            workspace_id="workspace_id",
            observations=[
                {
                    "content": "x",
                    "observed_id": "observed_id",
                    "observer_id": "observer_id",
                    "session_id": "session_id",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        observation = await response.parse()
        assert_matches_type(ObservationCreateResponse, observation, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncHoncho) -> None:
        async with async_client.workspaces.observations.with_streaming_response.create(
            workspace_id="workspace_id",
            observations=[
                {
                    "content": "x",
                    "observed_id": "observed_id",
                    "observer_id": "observer_id",
                    "session_id": "session_id",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            observation = await response.parse()
            assert_matches_type(ObservationCreateResponse, observation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncHoncho) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            await async_client.workspaces.observations.with_raw_response.create(
                workspace_id="",
                observations=[
                    {
                        "content": "x",
                        "observed_id": "observed_id",
                        "observer_id": "observer_id",
                        "session_id": "session_id",
                    }
                ],
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncHoncho) -> None:
        observation = await async_client.workspaces.observations.list(
            workspace_id="workspace_id",
        )
        assert_matches_type(AsyncPage[Observation], observation, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncHoncho) -> None:
        observation = await async_client.workspaces.observations.list(
            workspace_id="workspace_id",
            page=1,
            reverse=True,
            size=1,
            filters={"foo": "bar"},
        )
        assert_matches_type(AsyncPage[Observation], observation, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncHoncho) -> None:
        response = await async_client.workspaces.observations.with_raw_response.list(
            workspace_id="workspace_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        observation = await response.parse()
        assert_matches_type(AsyncPage[Observation], observation, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncHoncho) -> None:
        async with async_client.workspaces.observations.with_streaming_response.list(
            workspace_id="workspace_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            observation = await response.parse()
            assert_matches_type(AsyncPage[Observation], observation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncHoncho) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            await async_client.workspaces.observations.with_raw_response.list(
                workspace_id="",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncHoncho) -> None:
        observation = await async_client.workspaces.observations.delete(
            observation_id="observation_id",
            workspace_id="workspace_id",
        )
        assert_matches_type(object, observation, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncHoncho) -> None:
        response = await async_client.workspaces.observations.with_raw_response.delete(
            observation_id="observation_id",
            workspace_id="workspace_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        observation = await response.parse()
        assert_matches_type(object, observation, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncHoncho) -> None:
        async with async_client.workspaces.observations.with_streaming_response.delete(
            observation_id="observation_id",
            workspace_id="workspace_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            observation = await response.parse()
            assert_matches_type(object, observation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncHoncho) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            await async_client.workspaces.observations.with_raw_response.delete(
                observation_id="observation_id",
                workspace_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `observation_id` but received ''"):
            await async_client.workspaces.observations.with_raw_response.delete(
                observation_id="",
                workspace_id="workspace_id",
            )

    @parametrize
    async def test_method_query(self, async_client: AsyncHoncho) -> None:
        observation = await async_client.workspaces.observations.query(
            workspace_id="workspace_id",
            query="query",
        )
        assert_matches_type(ObservationQueryResponse, observation, path=["response"])

    @parametrize
    async def test_method_query_with_all_params(self, async_client: AsyncHoncho) -> None:
        observation = await async_client.workspaces.observations.query(
            workspace_id="workspace_id",
            query="query",
            distance=0,
            filters={"foo": "bar"},
            top_k=1,
        )
        assert_matches_type(ObservationQueryResponse, observation, path=["response"])

    @parametrize
    async def test_raw_response_query(self, async_client: AsyncHoncho) -> None:
        response = await async_client.workspaces.observations.with_raw_response.query(
            workspace_id="workspace_id",
            query="query",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        observation = await response.parse()
        assert_matches_type(ObservationQueryResponse, observation, path=["response"])

    @parametrize
    async def test_streaming_response_query(self, async_client: AsyncHoncho) -> None:
        async with async_client.workspaces.observations.with_streaming_response.query(
            workspace_id="workspace_id",
            query="query",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            observation = await response.parse()
            assert_matches_type(ObservationQueryResponse, observation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_query(self, async_client: AsyncHoncho) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            await async_client.workspaces.observations.with_raw_response.query(
                workspace_id="",
                query="query",
            )
