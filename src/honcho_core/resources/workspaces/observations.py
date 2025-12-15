# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable, Optional

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...pagination import SyncPage, AsyncPage
from ..._base_client import AsyncPaginator, make_request_options
from ...types.workspaces import observation_list_params, observation_query_params, observation_create_params
from ...types.workspaces.observation import Observation
from ...types.workspaces.observation_create_param import ObservationCreateParam
from ...types.workspaces.observation_query_response import ObservationQueryResponse
from ...types.workspaces.observation_create_response import ObservationCreateResponse

__all__ = ["ObservationsResource", "AsyncObservationsResource"]


class ObservationsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ObservationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/plastic-labs/honcho-python-core#accessing-raw-response-data-eg-headers
        """
        return ObservationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ObservationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/plastic-labs/honcho-python-core#with_streaming_response
        """
        return ObservationsResourceWithStreamingResponse(self)

    def create(
        self,
        workspace_id: str,
        *,
        observations: Iterable[ObservationCreateParam],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ObservationCreateResponse:
        """
        Create one or more observations.

        Creates observations (theory-of-mind facts) for the specified observer/observed
        peer pairs. Each observation must reference existing peers and a session within
        the workspace. Embeddings are automatically generated for semantic search.

        Maximum of 100 observations per request.

        Args:
          workspace_id: ID of the workspace

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not workspace_id:
            raise ValueError(f"Expected a non-empty value for `workspace_id` but received {workspace_id!r}")
        return self._post(
            f"/v2/workspaces/{workspace_id}/observations",
            body=maybe_transform({"observations": observations}, observation_create_params.ObservationCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ObservationCreateResponse,
        )

    def list(
        self,
        workspace_id: str,
        *,
        page: int | Omit = omit,
        reverse: Optional[bool] | Omit = omit,
        size: int | Omit = omit,
        filters: Optional[Dict[str, object]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncPage[Observation]:
        """List all observations using custom filters.

        Observations are listed by recency
        unless `reverse` is set to `true`.

        Observations can be filtered by session_id, observer_id and observed_id using
        the filters parameter.

        Args:
          workspace_id: ID of the workspace

          page: Page number

          reverse: Whether to reverse the order of results

          size: Page size

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not workspace_id:
            raise ValueError(f"Expected a non-empty value for `workspace_id` but received {workspace_id!r}")
        return self._get_api_list(
            f"/v2/workspaces/{workspace_id}/observations/list",
            page=SyncPage[Observation],
            body=maybe_transform({"filters": filters}, observation_list_params.ObservationListParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page": page,
                        "reverse": reverse,
                        "size": size,
                    },
                    observation_list_params.ObservationListParams,
                ),
            ),
            model=Observation,
            method="post",
        )

    def delete(
        self,
        observation_id: str,
        *,
        workspace_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Delete a specific observation.

        This permanently deletes the observation (document) from the theory-of-mind
        system. This action cannot be undone.

        Args:
          workspace_id: ID of the workspace

          observation_id: ID of the observation to delete

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not workspace_id:
            raise ValueError(f"Expected a non-empty value for `workspace_id` but received {workspace_id!r}")
        if not observation_id:
            raise ValueError(f"Expected a non-empty value for `observation_id` but received {observation_id!r}")
        return self._delete(
            f"/v2/workspaces/{workspace_id}/observations/{observation_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def query(
        self,
        workspace_id: str,
        *,
        query: str,
        distance: Optional[float] | Omit = omit,
        filters: Optional[Dict[str, object]] | Omit = omit,
        top_k: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ObservationQueryResponse:
        """
        Query observations using semantic search.

        Performs vector similarity search on observations to find semantically relevant
        results. Observer and observed are required for semantic search and must be
        provided in filters.

        Args:
          workspace_id: ID of the workspace

          query: Semantic search query

          distance: Maximum cosine distance threshold for results

          filters: Additional filters to apply

          top_k: Number of results to return

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not workspace_id:
            raise ValueError(f"Expected a non-empty value for `workspace_id` but received {workspace_id!r}")
        return self._post(
            f"/v2/workspaces/{workspace_id}/observations/query",
            body=maybe_transform(
                {
                    "query": query,
                    "distance": distance,
                    "filters": filters,
                    "top_k": top_k,
                },
                observation_query_params.ObservationQueryParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ObservationQueryResponse,
        )


class AsyncObservationsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncObservationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/plastic-labs/honcho-python-core#accessing-raw-response-data-eg-headers
        """
        return AsyncObservationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncObservationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/plastic-labs/honcho-python-core#with_streaming_response
        """
        return AsyncObservationsResourceWithStreamingResponse(self)

    async def create(
        self,
        workspace_id: str,
        *,
        observations: Iterable[ObservationCreateParam],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ObservationCreateResponse:
        """
        Create one or more observations.

        Creates observations (theory-of-mind facts) for the specified observer/observed
        peer pairs. Each observation must reference existing peers and a session within
        the workspace. Embeddings are automatically generated for semantic search.

        Maximum of 100 observations per request.

        Args:
          workspace_id: ID of the workspace

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not workspace_id:
            raise ValueError(f"Expected a non-empty value for `workspace_id` but received {workspace_id!r}")
        return await self._post(
            f"/v2/workspaces/{workspace_id}/observations",
            body=await async_maybe_transform(
                {"observations": observations}, observation_create_params.ObservationCreateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ObservationCreateResponse,
        )

    def list(
        self,
        workspace_id: str,
        *,
        page: int | Omit = omit,
        reverse: Optional[bool] | Omit = omit,
        size: int | Omit = omit,
        filters: Optional[Dict[str, object]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[Observation, AsyncPage[Observation]]:
        """List all observations using custom filters.

        Observations are listed by recency
        unless `reverse` is set to `true`.

        Observations can be filtered by session_id, observer_id and observed_id using
        the filters parameter.

        Args:
          workspace_id: ID of the workspace

          page: Page number

          reverse: Whether to reverse the order of results

          size: Page size

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not workspace_id:
            raise ValueError(f"Expected a non-empty value for `workspace_id` but received {workspace_id!r}")
        return self._get_api_list(
            f"/v2/workspaces/{workspace_id}/observations/list",
            page=AsyncPage[Observation],
            body=maybe_transform({"filters": filters}, observation_list_params.ObservationListParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page": page,
                        "reverse": reverse,
                        "size": size,
                    },
                    observation_list_params.ObservationListParams,
                ),
            ),
            model=Observation,
            method="post",
        )

    async def delete(
        self,
        observation_id: str,
        *,
        workspace_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Delete a specific observation.

        This permanently deletes the observation (document) from the theory-of-mind
        system. This action cannot be undone.

        Args:
          workspace_id: ID of the workspace

          observation_id: ID of the observation to delete

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not workspace_id:
            raise ValueError(f"Expected a non-empty value for `workspace_id` but received {workspace_id!r}")
        if not observation_id:
            raise ValueError(f"Expected a non-empty value for `observation_id` but received {observation_id!r}")
        return await self._delete(
            f"/v2/workspaces/{workspace_id}/observations/{observation_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def query(
        self,
        workspace_id: str,
        *,
        query: str,
        distance: Optional[float] | Omit = omit,
        filters: Optional[Dict[str, object]] | Omit = omit,
        top_k: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ObservationQueryResponse:
        """
        Query observations using semantic search.

        Performs vector similarity search on observations to find semantically relevant
        results. Observer and observed are required for semantic search and must be
        provided in filters.

        Args:
          workspace_id: ID of the workspace

          query: Semantic search query

          distance: Maximum cosine distance threshold for results

          filters: Additional filters to apply

          top_k: Number of results to return

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not workspace_id:
            raise ValueError(f"Expected a non-empty value for `workspace_id` but received {workspace_id!r}")
        return await self._post(
            f"/v2/workspaces/{workspace_id}/observations/query",
            body=await async_maybe_transform(
                {
                    "query": query,
                    "distance": distance,
                    "filters": filters,
                    "top_k": top_k,
                },
                observation_query_params.ObservationQueryParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ObservationQueryResponse,
        )


class ObservationsResourceWithRawResponse:
    def __init__(self, observations: ObservationsResource) -> None:
        self._observations = observations

        self.create = to_raw_response_wrapper(
            observations.create,
        )
        self.list = to_raw_response_wrapper(
            observations.list,
        )
        self.delete = to_raw_response_wrapper(
            observations.delete,
        )
        self.query = to_raw_response_wrapper(
            observations.query,
        )


class AsyncObservationsResourceWithRawResponse:
    def __init__(self, observations: AsyncObservationsResource) -> None:
        self._observations = observations

        self.create = async_to_raw_response_wrapper(
            observations.create,
        )
        self.list = async_to_raw_response_wrapper(
            observations.list,
        )
        self.delete = async_to_raw_response_wrapper(
            observations.delete,
        )
        self.query = async_to_raw_response_wrapper(
            observations.query,
        )


class ObservationsResourceWithStreamingResponse:
    def __init__(self, observations: ObservationsResource) -> None:
        self._observations = observations

        self.create = to_streamed_response_wrapper(
            observations.create,
        )
        self.list = to_streamed_response_wrapper(
            observations.list,
        )
        self.delete = to_streamed_response_wrapper(
            observations.delete,
        )
        self.query = to_streamed_response_wrapper(
            observations.query,
        )


class AsyncObservationsResourceWithStreamingResponse:
    def __init__(self, observations: AsyncObservationsResource) -> None:
        self._observations = observations

        self.create = async_to_streamed_response_wrapper(
            observations.create,
        )
        self.list = async_to_streamed_response_wrapper(
            observations.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            observations.delete,
        )
        self.query = async_to_streamed_response_wrapper(
            observations.query,
        )
