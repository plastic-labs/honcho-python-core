# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional

import httpx

from .peers import (
    PeersResource,
    AsyncPeersResource,
    PeersResourceWithRawResponse,
    AsyncPeersResourceWithRawResponse,
    PeersResourceWithStreamingResponse,
    AsyncPeersResourceWithStreamingResponse,
)
from .messages import (
    MessagesResource,
    AsyncMessagesResource,
    MessagesResourceWithRawResponse,
    AsyncMessagesResourceWithRawResponse,
    MessagesResourceWithStreamingResponse,
    AsyncMessagesResourceWithStreamingResponse,
)
from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....pagination import SyncPage, AsyncPage
from ...._base_client import AsyncPaginator, make_request_options
from ....types.workspaces import (
    session_list_params,
    session_clone_params,
    session_search_params,
    session_update_params,
    session_get_context_params,
    session_get_or_create_params,
)
from ....types.workspaces.session import Session
from ....types.workspaces.session_search_response import SessionSearchResponse
from ....types.workspaces.session_summaries_response import SessionSummariesResponse
from ....types.workspaces.session_get_context_response import SessionGetContextResponse
from ....types.workspaces.sessions.session_peer_config_param import SessionPeerConfigParam

__all__ = ["SessionsResource", "AsyncSessionsResource"]


class SessionsResource(SyncAPIResource):
    @cached_property
    def messages(self) -> MessagesResource:
        return MessagesResource(self._client)

    @cached_property
    def peers(self) -> PeersResource:
        return PeersResource(self._client)

    @cached_property
    def with_raw_response(self) -> SessionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/plastic-labs/honcho-python-core#accessing-raw-response-data-eg-headers
        """
        return SessionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SessionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/plastic-labs/honcho-python-core#with_streaming_response
        """
        return SessionsResourceWithStreamingResponse(self)

    def update(
        self,
        session_id: str,
        *,
        workspace_id: str,
        configuration: Optional[Dict[str, object]] | Omit = omit,
        metadata: Optional[Dict[str, object]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Session:
        """
        Update the metadata of a Session

        Args:
          workspace_id: ID of the workspace

          session_id: ID of the session to update

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not workspace_id:
            raise ValueError(f"Expected a non-empty value for `workspace_id` but received {workspace_id!r}")
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return self._put(
            f"/v2/workspaces/{workspace_id}/sessions/{session_id}",
            body=maybe_transform(
                {
                    "configuration": configuration,
                    "metadata": metadata,
                },
                session_update_params.SessionUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Session,
        )

    def list(
        self,
        workspace_id: str,
        *,
        page: int | Omit = omit,
        size: int | Omit = omit,
        filters: Optional[Dict[str, object]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncPage[Session]:
        """
        Get All Sessions in a Workspace

        Args:
          workspace_id: ID of the workspace

          page: Page number

          size: Page size

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not workspace_id:
            raise ValueError(f"Expected a non-empty value for `workspace_id` but received {workspace_id!r}")
        return self._get_api_list(
            f"/v2/workspaces/{workspace_id}/sessions/list",
            page=SyncPage[Session],
            body=maybe_transform({"filters": filters}, session_list_params.SessionListParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page": page,
                        "size": size,
                    },
                    session_list_params.SessionListParams,
                ),
            ),
            model=Session,
            method="post",
        )

    def delete(
        self,
        session_id: str,
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
        Delete a session by marking it as inactive

        Args:
          workspace_id: ID of the workspace

          session_id: ID of the session to delete

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not workspace_id:
            raise ValueError(f"Expected a non-empty value for `workspace_id` but received {workspace_id!r}")
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return self._delete(
            f"/v2/workspaces/{workspace_id}/sessions/{session_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def clone(
        self,
        session_id: str,
        *,
        workspace_id: str,
        message_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Session:
        """
        Clone a session, optionally up to a specific message

        Args:
          workspace_id: ID of the workspace

          session_id: ID of the session to clone

          message_id: Message ID to cut off the clone at

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not workspace_id:
            raise ValueError(f"Expected a non-empty value for `workspace_id` but received {workspace_id!r}")
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return self._get(
            f"/v2/workspaces/{workspace_id}/sessions/{session_id}/clone",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"message_id": message_id}, session_clone_params.SessionCloneParams),
            ),
            cast_to=Session,
        )

    def get_context(
        self,
        session_id: str,
        *,
        workspace_id: str,
        last_message: Optional[str] | Omit = omit,
        peer_perspective: Optional[str] | Omit = omit,
        peer_target: Optional[str] | Omit = omit,
        summary: bool | Omit = omit,
        tokens: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SessionGetContextResponse:
        """Produce a context object from the session.

        The caller provides an optional token
        limit which the entire context must fit into. If not provided, the context will
        be exhaustive (within configured max tokens). To do this, we allocate 40% of the
        token limit to the summary, and 60% to recent messages -- as many as can fit.
        Note that the summary will usually take up less space than this. If the caller
        does not want a summary, we allocate all the tokens to recent messages.

        Args:
          workspace_id: ID of the workspace

          session_id: ID of the session

          last_message: The most recent message, used to fetch semantically relevant observations

          peer_perspective: A peer to get context for. If given, response will attempt to include
              representation and card from the perspective of that peer. Must be provided with
              `peer_target`.

          peer_target: The target of the perspective. If given without `peer_perspective`, will get the
              Honcho-level representation and peer card for this peer. If given with
              `peer_perspective`, will get the representation and card for this peer _from the
              perspective of that peer_.

          summary: Whether or not to include a summary _if_ one is available for the session

          tokens: Number of tokens to use for the context. Includes summary if set to true.
              Includes representation and peer card if they are included in the response. If
              not provided, the context will be exhaustive (within 100000 tokens)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not workspace_id:
            raise ValueError(f"Expected a non-empty value for `workspace_id` but received {workspace_id!r}")
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return self._get(
            f"/v2/workspaces/{workspace_id}/sessions/{session_id}/context",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "last_message": last_message,
                        "peer_perspective": peer_perspective,
                        "peer_target": peer_target,
                        "summary": summary,
                        "tokens": tokens,
                    },
                    session_get_context_params.SessionGetContextParams,
                ),
            ),
            cast_to=SessionGetContextResponse,
        )

    def get_or_create(
        self,
        workspace_id: str,
        *,
        id: str,
        configuration: Optional[Dict[str, object]] | Omit = omit,
        metadata: Optional[Dict[str, object]] | Omit = omit,
        peers: Optional[Dict[str, SessionPeerConfigParam]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Session:
        """
        Get a specific session in a workspace.

        If session_id is provided as a query parameter, it verifies the session is in
        the workspace. Otherwise, it uses the session_id from the JWT for verification.

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
            f"/v2/workspaces/{workspace_id}/sessions",
            body=maybe_transform(
                {
                    "id": id,
                    "configuration": configuration,
                    "metadata": metadata,
                    "peers": peers,
                },
                session_get_or_create_params.SessionGetOrCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Session,
        )

    def search(
        self,
        session_id: str,
        *,
        workspace_id: str,
        query: str,
        filters: Optional[Dict[str, object]] | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SessionSearchResponse:
        """
        Search a Session

        Args:
          workspace_id: ID of the workspace

          session_id: ID of the session

          query: Search query

          filters: Filters to scope the search

          limit: Number of results to return

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not workspace_id:
            raise ValueError(f"Expected a non-empty value for `workspace_id` but received {workspace_id!r}")
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return self._post(
            f"/v2/workspaces/{workspace_id}/sessions/{session_id}/search",
            body=maybe_transform(
                {
                    "query": query,
                    "filters": filters,
                    "limit": limit,
                },
                session_search_params.SessionSearchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SessionSearchResponse,
        )

    def summaries(
        self,
        session_id: str,
        *,
        workspace_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SessionSummariesResponse:
        """
        Get available summaries for a session.

        Returns both short and long summaries if available, including metadata like the
        message ID they cover up to, creation timestamp, and token count.

        Args:
          workspace_id: ID of the workspace

          session_id: ID of the session

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not workspace_id:
            raise ValueError(f"Expected a non-empty value for `workspace_id` but received {workspace_id!r}")
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return self._get(
            f"/v2/workspaces/{workspace_id}/sessions/{session_id}/summaries",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SessionSummariesResponse,
        )


class AsyncSessionsResource(AsyncAPIResource):
    @cached_property
    def messages(self) -> AsyncMessagesResource:
        return AsyncMessagesResource(self._client)

    @cached_property
    def peers(self) -> AsyncPeersResource:
        return AsyncPeersResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncSessionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/plastic-labs/honcho-python-core#accessing-raw-response-data-eg-headers
        """
        return AsyncSessionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSessionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/plastic-labs/honcho-python-core#with_streaming_response
        """
        return AsyncSessionsResourceWithStreamingResponse(self)

    async def update(
        self,
        session_id: str,
        *,
        workspace_id: str,
        configuration: Optional[Dict[str, object]] | Omit = omit,
        metadata: Optional[Dict[str, object]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Session:
        """
        Update the metadata of a Session

        Args:
          workspace_id: ID of the workspace

          session_id: ID of the session to update

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not workspace_id:
            raise ValueError(f"Expected a non-empty value for `workspace_id` but received {workspace_id!r}")
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return await self._put(
            f"/v2/workspaces/{workspace_id}/sessions/{session_id}",
            body=await async_maybe_transform(
                {
                    "configuration": configuration,
                    "metadata": metadata,
                },
                session_update_params.SessionUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Session,
        )

    def list(
        self,
        workspace_id: str,
        *,
        page: int | Omit = omit,
        size: int | Omit = omit,
        filters: Optional[Dict[str, object]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[Session, AsyncPage[Session]]:
        """
        Get All Sessions in a Workspace

        Args:
          workspace_id: ID of the workspace

          page: Page number

          size: Page size

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not workspace_id:
            raise ValueError(f"Expected a non-empty value for `workspace_id` but received {workspace_id!r}")
        return self._get_api_list(
            f"/v2/workspaces/{workspace_id}/sessions/list",
            page=AsyncPage[Session],
            body=maybe_transform({"filters": filters}, session_list_params.SessionListParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page": page,
                        "size": size,
                    },
                    session_list_params.SessionListParams,
                ),
            ),
            model=Session,
            method="post",
        )

    async def delete(
        self,
        session_id: str,
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
        Delete a session by marking it as inactive

        Args:
          workspace_id: ID of the workspace

          session_id: ID of the session to delete

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not workspace_id:
            raise ValueError(f"Expected a non-empty value for `workspace_id` but received {workspace_id!r}")
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return await self._delete(
            f"/v2/workspaces/{workspace_id}/sessions/{session_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def clone(
        self,
        session_id: str,
        *,
        workspace_id: str,
        message_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Session:
        """
        Clone a session, optionally up to a specific message

        Args:
          workspace_id: ID of the workspace

          session_id: ID of the session to clone

          message_id: Message ID to cut off the clone at

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not workspace_id:
            raise ValueError(f"Expected a non-empty value for `workspace_id` but received {workspace_id!r}")
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return await self._get(
            f"/v2/workspaces/{workspace_id}/sessions/{session_id}/clone",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"message_id": message_id}, session_clone_params.SessionCloneParams),
            ),
            cast_to=Session,
        )

    async def get_context(
        self,
        session_id: str,
        *,
        workspace_id: str,
        last_message: Optional[str] | Omit = omit,
        peer_perspective: Optional[str] | Omit = omit,
        peer_target: Optional[str] | Omit = omit,
        summary: bool | Omit = omit,
        tokens: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SessionGetContextResponse:
        """Produce a context object from the session.

        The caller provides an optional token
        limit which the entire context must fit into. If not provided, the context will
        be exhaustive (within configured max tokens). To do this, we allocate 40% of the
        token limit to the summary, and 60% to recent messages -- as many as can fit.
        Note that the summary will usually take up less space than this. If the caller
        does not want a summary, we allocate all the tokens to recent messages.

        Args:
          workspace_id: ID of the workspace

          session_id: ID of the session

          last_message: The most recent message, used to fetch semantically relevant observations

          peer_perspective: A peer to get context for. If given, response will attempt to include
              representation and card from the perspective of that peer. Must be provided with
              `peer_target`.

          peer_target: The target of the perspective. If given without `peer_perspective`, will get the
              Honcho-level representation and peer card for this peer. If given with
              `peer_perspective`, will get the representation and card for this peer _from the
              perspective of that peer_.

          summary: Whether or not to include a summary _if_ one is available for the session

          tokens: Number of tokens to use for the context. Includes summary if set to true.
              Includes representation and peer card if they are included in the response. If
              not provided, the context will be exhaustive (within 100000 tokens)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not workspace_id:
            raise ValueError(f"Expected a non-empty value for `workspace_id` but received {workspace_id!r}")
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return await self._get(
            f"/v2/workspaces/{workspace_id}/sessions/{session_id}/context",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "last_message": last_message,
                        "peer_perspective": peer_perspective,
                        "peer_target": peer_target,
                        "summary": summary,
                        "tokens": tokens,
                    },
                    session_get_context_params.SessionGetContextParams,
                ),
            ),
            cast_to=SessionGetContextResponse,
        )

    async def get_or_create(
        self,
        workspace_id: str,
        *,
        id: str,
        configuration: Optional[Dict[str, object]] | Omit = omit,
        metadata: Optional[Dict[str, object]] | Omit = omit,
        peers: Optional[Dict[str, SessionPeerConfigParam]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Session:
        """
        Get a specific session in a workspace.

        If session_id is provided as a query parameter, it verifies the session is in
        the workspace. Otherwise, it uses the session_id from the JWT for verification.

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
            f"/v2/workspaces/{workspace_id}/sessions",
            body=await async_maybe_transform(
                {
                    "id": id,
                    "configuration": configuration,
                    "metadata": metadata,
                    "peers": peers,
                },
                session_get_or_create_params.SessionGetOrCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Session,
        )

    async def search(
        self,
        session_id: str,
        *,
        workspace_id: str,
        query: str,
        filters: Optional[Dict[str, object]] | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SessionSearchResponse:
        """
        Search a Session

        Args:
          workspace_id: ID of the workspace

          session_id: ID of the session

          query: Search query

          filters: Filters to scope the search

          limit: Number of results to return

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not workspace_id:
            raise ValueError(f"Expected a non-empty value for `workspace_id` but received {workspace_id!r}")
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return await self._post(
            f"/v2/workspaces/{workspace_id}/sessions/{session_id}/search",
            body=await async_maybe_transform(
                {
                    "query": query,
                    "filters": filters,
                    "limit": limit,
                },
                session_search_params.SessionSearchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SessionSearchResponse,
        )

    async def summaries(
        self,
        session_id: str,
        *,
        workspace_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SessionSummariesResponse:
        """
        Get available summaries for a session.

        Returns both short and long summaries if available, including metadata like the
        message ID they cover up to, creation timestamp, and token count.

        Args:
          workspace_id: ID of the workspace

          session_id: ID of the session

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not workspace_id:
            raise ValueError(f"Expected a non-empty value for `workspace_id` but received {workspace_id!r}")
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return await self._get(
            f"/v2/workspaces/{workspace_id}/sessions/{session_id}/summaries",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SessionSummariesResponse,
        )


class SessionsResourceWithRawResponse:
    def __init__(self, sessions: SessionsResource) -> None:
        self._sessions = sessions

        self.update = to_raw_response_wrapper(
            sessions.update,
        )
        self.list = to_raw_response_wrapper(
            sessions.list,
        )
        self.delete = to_raw_response_wrapper(
            sessions.delete,
        )
        self.clone = to_raw_response_wrapper(
            sessions.clone,
        )
        self.get_context = to_raw_response_wrapper(
            sessions.get_context,
        )
        self.get_or_create = to_raw_response_wrapper(
            sessions.get_or_create,
        )
        self.search = to_raw_response_wrapper(
            sessions.search,
        )
        self.summaries = to_raw_response_wrapper(
            sessions.summaries,
        )

    @cached_property
    def messages(self) -> MessagesResourceWithRawResponse:
        return MessagesResourceWithRawResponse(self._sessions.messages)

    @cached_property
    def peers(self) -> PeersResourceWithRawResponse:
        return PeersResourceWithRawResponse(self._sessions.peers)


class AsyncSessionsResourceWithRawResponse:
    def __init__(self, sessions: AsyncSessionsResource) -> None:
        self._sessions = sessions

        self.update = async_to_raw_response_wrapper(
            sessions.update,
        )
        self.list = async_to_raw_response_wrapper(
            sessions.list,
        )
        self.delete = async_to_raw_response_wrapper(
            sessions.delete,
        )
        self.clone = async_to_raw_response_wrapper(
            sessions.clone,
        )
        self.get_context = async_to_raw_response_wrapper(
            sessions.get_context,
        )
        self.get_or_create = async_to_raw_response_wrapper(
            sessions.get_or_create,
        )
        self.search = async_to_raw_response_wrapper(
            sessions.search,
        )
        self.summaries = async_to_raw_response_wrapper(
            sessions.summaries,
        )

    @cached_property
    def messages(self) -> AsyncMessagesResourceWithRawResponse:
        return AsyncMessagesResourceWithRawResponse(self._sessions.messages)

    @cached_property
    def peers(self) -> AsyncPeersResourceWithRawResponse:
        return AsyncPeersResourceWithRawResponse(self._sessions.peers)


class SessionsResourceWithStreamingResponse:
    def __init__(self, sessions: SessionsResource) -> None:
        self._sessions = sessions

        self.update = to_streamed_response_wrapper(
            sessions.update,
        )
        self.list = to_streamed_response_wrapper(
            sessions.list,
        )
        self.delete = to_streamed_response_wrapper(
            sessions.delete,
        )
        self.clone = to_streamed_response_wrapper(
            sessions.clone,
        )
        self.get_context = to_streamed_response_wrapper(
            sessions.get_context,
        )
        self.get_or_create = to_streamed_response_wrapper(
            sessions.get_or_create,
        )
        self.search = to_streamed_response_wrapper(
            sessions.search,
        )
        self.summaries = to_streamed_response_wrapper(
            sessions.summaries,
        )

    @cached_property
    def messages(self) -> MessagesResourceWithStreamingResponse:
        return MessagesResourceWithStreamingResponse(self._sessions.messages)

    @cached_property
    def peers(self) -> PeersResourceWithStreamingResponse:
        return PeersResourceWithStreamingResponse(self._sessions.peers)


class AsyncSessionsResourceWithStreamingResponse:
    def __init__(self, sessions: AsyncSessionsResource) -> None:
        self._sessions = sessions

        self.update = async_to_streamed_response_wrapper(
            sessions.update,
        )
        self.list = async_to_streamed_response_wrapper(
            sessions.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            sessions.delete,
        )
        self.clone = async_to_streamed_response_wrapper(
            sessions.clone,
        )
        self.get_context = async_to_streamed_response_wrapper(
            sessions.get_context,
        )
        self.get_or_create = async_to_streamed_response_wrapper(
            sessions.get_or_create,
        )
        self.search = async_to_streamed_response_wrapper(
            sessions.search,
        )
        self.summaries = async_to_streamed_response_wrapper(
            sessions.summaries,
        )

    @cached_property
    def messages(self) -> AsyncMessagesResourceWithStreamingResponse:
        return AsyncMessagesResourceWithStreamingResponse(self._sessions.messages)

    @cached_property
    def peers(self) -> AsyncPeersResourceWithStreamingResponse:
        return AsyncPeersResourceWithStreamingResponse(self._sessions.peers)
