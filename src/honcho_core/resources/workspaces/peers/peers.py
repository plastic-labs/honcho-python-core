# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional

import httpx

from .sessions import (
    SessionsResource,
    AsyncSessionsResource,
    SessionsResourceWithRawResponse,
    AsyncSessionsResourceWithRawResponse,
    SessionsResourceWithStreamingResponse,
    AsyncSessionsResourceWithStreamingResponse,
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
    peer_card_params,
    peer_chat_params,
    peer_list_params,
    peer_search_params,
    peer_update_params,
    peer_get_or_create_params,
    peer_working_representation_params,
)
from ....types.workspaces.peer import Peer
from ....types.workspaces.peer_card_response import PeerCardResponse
from ....types.workspaces.peer_chat_response import PeerChatResponse
from ....types.workspaces.peer_search_response import PeerSearchResponse
from ....types.workspaces.peer_working_representation_response import PeerWorkingRepresentationResponse

__all__ = ["PeersResource", "AsyncPeersResource"]


class PeersResource(SyncAPIResource):
    @cached_property
    def sessions(self) -> SessionsResource:
        return SessionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> PeersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/plastic-labs/honcho-python-core#accessing-raw-response-data-eg-headers
        """
        return PeersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PeersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/plastic-labs/honcho-python-core#with_streaming_response
        """
        return PeersResourceWithStreamingResponse(self)

    def update(
        self,
        peer_id: str,
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
    ) -> Peer:
        """
        Update a Peer's name and/or metadata

        Args:
          workspace_id: ID of the workspace

          peer_id: ID of the peer to update

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not workspace_id:
            raise ValueError(f"Expected a non-empty value for `workspace_id` but received {workspace_id!r}")
        if not peer_id:
            raise ValueError(f"Expected a non-empty value for `peer_id` but received {peer_id!r}")
        return self._put(
            f"/v2/workspaces/{workspace_id}/peers/{peer_id}",
            body=maybe_transform(
                {
                    "configuration": configuration,
                    "metadata": metadata,
                },
                peer_update_params.PeerUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Peer,
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
    ) -> SyncPage[Peer]:
        """
        Get All Peers for a Workspace

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
            f"/v2/workspaces/{workspace_id}/peers/list",
            page=SyncPage[Peer],
            body=maybe_transform({"filters": filters}, peer_list_params.PeerListParams),
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
                    peer_list_params.PeerListParams,
                ),
            ),
            model=Peer,
            method="post",
        )

    def card(
        self,
        peer_id: str,
        *,
        workspace_id: str,
        target: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PeerCardResponse:
        """
        Get a peer card for a specific peer relationship.

        Returns the peer card that the observer peer has for the target peer if it
        exists. If no target is specified, returns the observer's own peer card.

        Args:
          workspace_id: ID of the workspace

          peer_id: ID of the observer peer

          target: The peer whose card to retrieve. If not provided, returns the observer's own
              card

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not workspace_id:
            raise ValueError(f"Expected a non-empty value for `workspace_id` but received {workspace_id!r}")
        if not peer_id:
            raise ValueError(f"Expected a non-empty value for `peer_id` but received {peer_id!r}")
        return self._get(
            f"/v2/workspaces/{workspace_id}/peers/{peer_id}/card",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"target": target}, peer_card_params.PeerCardParams),
            ),
            cast_to=PeerCardResponse,
        )

    def chat(
        self,
        peer_id: str,
        *,
        workspace_id: str,
        query: str,
        session_id: Optional[str] | Omit = omit,
        stream: bool | Omit = omit,
        target: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PeerChatResponse:
        """
        Chat

        Args:
          workspace_id: ID of the workspace

          peer_id: ID of the peer

          query: Dialectic API Prompt

          session_id: ID of the session to scope the representation to

          target: Optional peer to get the representation for, from the perspective of this peer

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not workspace_id:
            raise ValueError(f"Expected a non-empty value for `workspace_id` but received {workspace_id!r}")
        if not peer_id:
            raise ValueError(f"Expected a non-empty value for `peer_id` but received {peer_id!r}")
        return self._post(
            f"/v2/workspaces/{workspace_id}/peers/{peer_id}/chat",
            body=maybe_transform(
                {
                    "query": query,
                    "session_id": session_id,
                    "stream": stream,
                    "target": target,
                },
                peer_chat_params.PeerChatParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PeerChatResponse,
        )

    def get_or_create(
        self,
        workspace_id: str,
        *,
        id: str,
        configuration: Optional[Dict[str, object]] | Omit = omit,
        metadata: Optional[Dict[str, object]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Peer:
        """
        Get a Peer by ID

        If peer_id is provided as a query parameter, it uses that (must match JWT
        workspace_id). Otherwise, it uses the peer_id from the JWT.

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
            f"/v2/workspaces/{workspace_id}/peers",
            body=maybe_transform(
                {
                    "id": id,
                    "configuration": configuration,
                    "metadata": metadata,
                },
                peer_get_or_create_params.PeerGetOrCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Peer,
        )

    def search(
        self,
        peer_id: str,
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
    ) -> PeerSearchResponse:
        """
        Search a Peer

        Args:
          workspace_id: ID of the workspace

          peer_id: ID of the peer

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
        if not peer_id:
            raise ValueError(f"Expected a non-empty value for `peer_id` but received {peer_id!r}")
        return self._post(
            f"/v2/workspaces/{workspace_id}/peers/{peer_id}/search",
            body=maybe_transform(
                {
                    "query": query,
                    "filters": filters,
                    "limit": limit,
                },
                peer_search_params.PeerSearchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PeerSearchResponse,
        )

    def working_representation(
        self,
        peer_id: str,
        *,
        workspace_id: str,
        session_id: Optional[str] | Omit = omit,
        target: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PeerWorkingRepresentationResponse:
        """
        Get a peer's working representation for a session.

        If a session_id is provided in the body, we get the working representation of
        the peer in that session. If a target is provided, we get the representation of
        the target from the perspective of the peer. If no target is provided, we get
        the omniscient Honcho representation of the peer.

        Args:
          workspace_id: ID of the workspace

          peer_id: ID of the peer

          session_id: Get the working representation within this session

          target: Optional peer ID to get the representation for, from the perspective of this
              peer

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not workspace_id:
            raise ValueError(f"Expected a non-empty value for `workspace_id` but received {workspace_id!r}")
        if not peer_id:
            raise ValueError(f"Expected a non-empty value for `peer_id` but received {peer_id!r}")
        return self._post(
            f"/v2/workspaces/{workspace_id}/peers/{peer_id}/representation",
            body=maybe_transform(
                {
                    "session_id": session_id,
                    "target": target,
                },
                peer_working_representation_params.PeerWorkingRepresentationParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PeerWorkingRepresentationResponse,
        )


class AsyncPeersResource(AsyncAPIResource):
    @cached_property
    def sessions(self) -> AsyncSessionsResource:
        return AsyncSessionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncPeersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/plastic-labs/honcho-python-core#accessing-raw-response-data-eg-headers
        """
        return AsyncPeersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPeersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/plastic-labs/honcho-python-core#with_streaming_response
        """
        return AsyncPeersResourceWithStreamingResponse(self)

    async def update(
        self,
        peer_id: str,
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
    ) -> Peer:
        """
        Update a Peer's name and/or metadata

        Args:
          workspace_id: ID of the workspace

          peer_id: ID of the peer to update

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not workspace_id:
            raise ValueError(f"Expected a non-empty value for `workspace_id` but received {workspace_id!r}")
        if not peer_id:
            raise ValueError(f"Expected a non-empty value for `peer_id` but received {peer_id!r}")
        return await self._put(
            f"/v2/workspaces/{workspace_id}/peers/{peer_id}",
            body=await async_maybe_transform(
                {
                    "configuration": configuration,
                    "metadata": metadata,
                },
                peer_update_params.PeerUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Peer,
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
    ) -> AsyncPaginator[Peer, AsyncPage[Peer]]:
        """
        Get All Peers for a Workspace

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
            f"/v2/workspaces/{workspace_id}/peers/list",
            page=AsyncPage[Peer],
            body=maybe_transform({"filters": filters}, peer_list_params.PeerListParams),
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
                    peer_list_params.PeerListParams,
                ),
            ),
            model=Peer,
            method="post",
        )

    async def card(
        self,
        peer_id: str,
        *,
        workspace_id: str,
        target: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PeerCardResponse:
        """
        Get a peer card for a specific peer relationship.

        Returns the peer card that the observer peer has for the target peer if it
        exists. If no target is specified, returns the observer's own peer card.

        Args:
          workspace_id: ID of the workspace

          peer_id: ID of the observer peer

          target: The peer whose card to retrieve. If not provided, returns the observer's own
              card

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not workspace_id:
            raise ValueError(f"Expected a non-empty value for `workspace_id` but received {workspace_id!r}")
        if not peer_id:
            raise ValueError(f"Expected a non-empty value for `peer_id` but received {peer_id!r}")
        return await self._get(
            f"/v2/workspaces/{workspace_id}/peers/{peer_id}/card",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"target": target}, peer_card_params.PeerCardParams),
            ),
            cast_to=PeerCardResponse,
        )

    async def chat(
        self,
        peer_id: str,
        *,
        workspace_id: str,
        query: str,
        session_id: Optional[str] | Omit = omit,
        stream: bool | Omit = omit,
        target: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PeerChatResponse:
        """
        Chat

        Args:
          workspace_id: ID of the workspace

          peer_id: ID of the peer

          query: Dialectic API Prompt

          session_id: ID of the session to scope the representation to

          target: Optional peer to get the representation for, from the perspective of this peer

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not workspace_id:
            raise ValueError(f"Expected a non-empty value for `workspace_id` but received {workspace_id!r}")
        if not peer_id:
            raise ValueError(f"Expected a non-empty value for `peer_id` but received {peer_id!r}")
        return await self._post(
            f"/v2/workspaces/{workspace_id}/peers/{peer_id}/chat",
            body=await async_maybe_transform(
                {
                    "query": query,
                    "session_id": session_id,
                    "stream": stream,
                    "target": target,
                },
                peer_chat_params.PeerChatParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PeerChatResponse,
        )

    async def get_or_create(
        self,
        workspace_id: str,
        *,
        id: str,
        configuration: Optional[Dict[str, object]] | Omit = omit,
        metadata: Optional[Dict[str, object]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Peer:
        """
        Get a Peer by ID

        If peer_id is provided as a query parameter, it uses that (must match JWT
        workspace_id). Otherwise, it uses the peer_id from the JWT.

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
            f"/v2/workspaces/{workspace_id}/peers",
            body=await async_maybe_transform(
                {
                    "id": id,
                    "configuration": configuration,
                    "metadata": metadata,
                },
                peer_get_or_create_params.PeerGetOrCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Peer,
        )

    async def search(
        self,
        peer_id: str,
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
    ) -> PeerSearchResponse:
        """
        Search a Peer

        Args:
          workspace_id: ID of the workspace

          peer_id: ID of the peer

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
        if not peer_id:
            raise ValueError(f"Expected a non-empty value for `peer_id` but received {peer_id!r}")
        return await self._post(
            f"/v2/workspaces/{workspace_id}/peers/{peer_id}/search",
            body=await async_maybe_transform(
                {
                    "query": query,
                    "filters": filters,
                    "limit": limit,
                },
                peer_search_params.PeerSearchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PeerSearchResponse,
        )

    async def working_representation(
        self,
        peer_id: str,
        *,
        workspace_id: str,
        session_id: Optional[str] | Omit = omit,
        target: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PeerWorkingRepresentationResponse:
        """
        Get a peer's working representation for a session.

        If a session_id is provided in the body, we get the working representation of
        the peer in that session. If a target is provided, we get the representation of
        the target from the perspective of the peer. If no target is provided, we get
        the omniscient Honcho representation of the peer.

        Args:
          workspace_id: ID of the workspace

          peer_id: ID of the peer

          session_id: Get the working representation within this session

          target: Optional peer ID to get the representation for, from the perspective of this
              peer

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not workspace_id:
            raise ValueError(f"Expected a non-empty value for `workspace_id` but received {workspace_id!r}")
        if not peer_id:
            raise ValueError(f"Expected a non-empty value for `peer_id` but received {peer_id!r}")
        return await self._post(
            f"/v2/workspaces/{workspace_id}/peers/{peer_id}/representation",
            body=await async_maybe_transform(
                {
                    "session_id": session_id,
                    "target": target,
                },
                peer_working_representation_params.PeerWorkingRepresentationParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PeerWorkingRepresentationResponse,
        )


class PeersResourceWithRawResponse:
    def __init__(self, peers: PeersResource) -> None:
        self._peers = peers

        self.update = to_raw_response_wrapper(
            peers.update,
        )
        self.list = to_raw_response_wrapper(
            peers.list,
        )
        self.card = to_raw_response_wrapper(
            peers.card,
        )
        self.chat = to_raw_response_wrapper(
            peers.chat,
        )
        self.get_or_create = to_raw_response_wrapper(
            peers.get_or_create,
        )
        self.search = to_raw_response_wrapper(
            peers.search,
        )
        self.working_representation = to_raw_response_wrapper(
            peers.working_representation,
        )

    @cached_property
    def sessions(self) -> SessionsResourceWithRawResponse:
        return SessionsResourceWithRawResponse(self._peers.sessions)


class AsyncPeersResourceWithRawResponse:
    def __init__(self, peers: AsyncPeersResource) -> None:
        self._peers = peers

        self.update = async_to_raw_response_wrapper(
            peers.update,
        )
        self.list = async_to_raw_response_wrapper(
            peers.list,
        )
        self.card = async_to_raw_response_wrapper(
            peers.card,
        )
        self.chat = async_to_raw_response_wrapper(
            peers.chat,
        )
        self.get_or_create = async_to_raw_response_wrapper(
            peers.get_or_create,
        )
        self.search = async_to_raw_response_wrapper(
            peers.search,
        )
        self.working_representation = async_to_raw_response_wrapper(
            peers.working_representation,
        )

    @cached_property
    def sessions(self) -> AsyncSessionsResourceWithRawResponse:
        return AsyncSessionsResourceWithRawResponse(self._peers.sessions)


class PeersResourceWithStreamingResponse:
    def __init__(self, peers: PeersResource) -> None:
        self._peers = peers

        self.update = to_streamed_response_wrapper(
            peers.update,
        )
        self.list = to_streamed_response_wrapper(
            peers.list,
        )
        self.card = to_streamed_response_wrapper(
            peers.card,
        )
        self.chat = to_streamed_response_wrapper(
            peers.chat,
        )
        self.get_or_create = to_streamed_response_wrapper(
            peers.get_or_create,
        )
        self.search = to_streamed_response_wrapper(
            peers.search,
        )
        self.working_representation = to_streamed_response_wrapper(
            peers.working_representation,
        )

    @cached_property
    def sessions(self) -> SessionsResourceWithStreamingResponse:
        return SessionsResourceWithStreamingResponse(self._peers.sessions)


class AsyncPeersResourceWithStreamingResponse:
    def __init__(self, peers: AsyncPeersResource) -> None:
        self._peers = peers

        self.update = async_to_streamed_response_wrapper(
            peers.update,
        )
        self.list = async_to_streamed_response_wrapper(
            peers.list,
        )
        self.card = async_to_streamed_response_wrapper(
            peers.card,
        )
        self.chat = async_to_streamed_response_wrapper(
            peers.chat,
        )
        self.get_or_create = async_to_streamed_response_wrapper(
            peers.get_or_create,
        )
        self.search = async_to_streamed_response_wrapper(
            peers.search,
        )
        self.working_representation = async_to_streamed_response_wrapper(
            peers.working_representation,
        )

    @cached_property
    def sessions(self) -> AsyncSessionsResourceWithStreamingResponse:
        return AsyncSessionsResourceWithStreamingResponse(self._peers.sessions)
