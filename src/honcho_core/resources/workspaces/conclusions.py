# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable, Optional

import httpx

from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
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
from ...types.workspaces import conclusion_list_params, conclusion_query_params, conclusion_create_params
from ...types.workspaces.conclusion import Conclusion
from ...types.workspaces.conclusion_query_response import ConclusionQueryResponse
from ...types.workspaces.conclusion_create_response import ConclusionCreateResponse

__all__ = ["ConclusionsResource", "AsyncConclusionsResource"]


class ConclusionsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ConclusionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/plastic-labs/honcho-python-core#accessing-raw-response-data-eg-headers
        """
        return ConclusionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ConclusionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/plastic-labs/honcho-python-core#with_streaming_response
        """
        return ConclusionsResourceWithStreamingResponse(self)

    def create(
        self,
        workspace_id: str,
        *,
        conclusions: Iterable[conclusion_create_params.Conclusion],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConclusionCreateResponse:
        """
        Create one or more Conclusions.

        Conclusions are logical certainties derived from interactions between Peers.
        They form the basis of a Peer's Representation.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not workspace_id:
            raise ValueError(f"Expected a non-empty value for `workspace_id` but received {workspace_id!r}")
        return self._post(
            f"/v2/workspaces/{workspace_id}/conclusions",
            body=maybe_transform({"conclusions": conclusions}, conclusion_create_params.ConclusionCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConclusionCreateResponse,
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
    ) -> SyncPage[Conclusion]:
        """
        List Conclusions using optional filters, ordered by recency unless `reverse` is
        true. Results are paginated.

        Args:
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
            f"/v2/workspaces/{workspace_id}/conclusions/list",
            page=SyncPage[Conclusion],
            body=maybe_transform({"filters": filters}, conclusion_list_params.ConclusionListParams),
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
                    conclusion_list_params.ConclusionListParams,
                ),
            ),
            model=Conclusion,
            method="post",
        )

    def delete(
        self,
        conclusion_id: str,
        *,
        workspace_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete a single Conclusion by ID.

        This action cannot be undone.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not workspace_id:
            raise ValueError(f"Expected a non-empty value for `workspace_id` but received {workspace_id!r}")
        if not conclusion_id:
            raise ValueError(f"Expected a non-empty value for `conclusion_id` but received {conclusion_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/v2/workspaces/{workspace_id}/conclusions/{conclusion_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
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
    ) -> ConclusionQueryResponse:
        """Query Conclusions using semantic search.

        Use `top_k` to control the number of
        results returned.

        Args:
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
            f"/v2/workspaces/{workspace_id}/conclusions/query",
            body=maybe_transform(
                {
                    "query": query,
                    "distance": distance,
                    "filters": filters,
                    "top_k": top_k,
                },
                conclusion_query_params.ConclusionQueryParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConclusionQueryResponse,
        )


class AsyncConclusionsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncConclusionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/plastic-labs/honcho-python-core#accessing-raw-response-data-eg-headers
        """
        return AsyncConclusionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncConclusionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/plastic-labs/honcho-python-core#with_streaming_response
        """
        return AsyncConclusionsResourceWithStreamingResponse(self)

    async def create(
        self,
        workspace_id: str,
        *,
        conclusions: Iterable[conclusion_create_params.Conclusion],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConclusionCreateResponse:
        """
        Create one or more Conclusions.

        Conclusions are logical certainties derived from interactions between Peers.
        They form the basis of a Peer's Representation.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not workspace_id:
            raise ValueError(f"Expected a non-empty value for `workspace_id` but received {workspace_id!r}")
        return await self._post(
            f"/v2/workspaces/{workspace_id}/conclusions",
            body=await async_maybe_transform(
                {"conclusions": conclusions}, conclusion_create_params.ConclusionCreateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConclusionCreateResponse,
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
    ) -> AsyncPaginator[Conclusion, AsyncPage[Conclusion]]:
        """
        List Conclusions using optional filters, ordered by recency unless `reverse` is
        true. Results are paginated.

        Args:
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
            f"/v2/workspaces/{workspace_id}/conclusions/list",
            page=AsyncPage[Conclusion],
            body=maybe_transform({"filters": filters}, conclusion_list_params.ConclusionListParams),
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
                    conclusion_list_params.ConclusionListParams,
                ),
            ),
            model=Conclusion,
            method="post",
        )

    async def delete(
        self,
        conclusion_id: str,
        *,
        workspace_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete a single Conclusion by ID.

        This action cannot be undone.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not workspace_id:
            raise ValueError(f"Expected a non-empty value for `workspace_id` but received {workspace_id!r}")
        if not conclusion_id:
            raise ValueError(f"Expected a non-empty value for `conclusion_id` but received {conclusion_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/v2/workspaces/{workspace_id}/conclusions/{conclusion_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
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
    ) -> ConclusionQueryResponse:
        """Query Conclusions using semantic search.

        Use `top_k` to control the number of
        results returned.

        Args:
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
            f"/v2/workspaces/{workspace_id}/conclusions/query",
            body=await async_maybe_transform(
                {
                    "query": query,
                    "distance": distance,
                    "filters": filters,
                    "top_k": top_k,
                },
                conclusion_query_params.ConclusionQueryParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConclusionQueryResponse,
        )


class ConclusionsResourceWithRawResponse:
    def __init__(self, conclusions: ConclusionsResource) -> None:
        self._conclusions = conclusions

        self.create = to_raw_response_wrapper(
            conclusions.create,
        )
        self.list = to_raw_response_wrapper(
            conclusions.list,
        )
        self.delete = to_raw_response_wrapper(
            conclusions.delete,
        )
        self.query = to_raw_response_wrapper(
            conclusions.query,
        )


class AsyncConclusionsResourceWithRawResponse:
    def __init__(self, conclusions: AsyncConclusionsResource) -> None:
        self._conclusions = conclusions

        self.create = async_to_raw_response_wrapper(
            conclusions.create,
        )
        self.list = async_to_raw_response_wrapper(
            conclusions.list,
        )
        self.delete = async_to_raw_response_wrapper(
            conclusions.delete,
        )
        self.query = async_to_raw_response_wrapper(
            conclusions.query,
        )


class ConclusionsResourceWithStreamingResponse:
    def __init__(self, conclusions: ConclusionsResource) -> None:
        self._conclusions = conclusions

        self.create = to_streamed_response_wrapper(
            conclusions.create,
        )
        self.list = to_streamed_response_wrapper(
            conclusions.list,
        )
        self.delete = to_streamed_response_wrapper(
            conclusions.delete,
        )
        self.query = to_streamed_response_wrapper(
            conclusions.query,
        )


class AsyncConclusionsResourceWithStreamingResponse:
    def __init__(self, conclusions: AsyncConclusionsResource) -> None:
        self._conclusions = conclusions

        self.create = async_to_streamed_response_wrapper(
            conclusions.create,
        )
        self.list = async_to_streamed_response_wrapper(
            conclusions.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            conclusions.delete,
        )
        self.query = async_to_streamed_response_wrapper(
            conclusions.query,
        )
