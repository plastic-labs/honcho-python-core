# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
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
from ....types.workspaces.peer import Peer
from ....types.workspaces.session import Session
from ....types.workspaces.sessions import (
    peer_add_params,
    peer_set_params,
    peer_list_params,
    peer_set_config_params,
)
from ....types.workspaces.sessions.session_peer_config import SessionPeerConfig
from ....types.workspaces.sessions.session_peer_config_param import SessionPeerConfigParam

__all__ = ["PeersResource", "AsyncPeersResource"]


class PeersResource(SyncAPIResource):
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

    def list(
        self,
        session_id: str,
        *,
        workspace_id: str,
        page: int | Omit = omit,
        size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncPage[Peer]:
        """
        Get peers from a session

        Args:
          workspace_id: ID of the workspace

          session_id: ID of the session

          page: Page number

          size: Page size

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not workspace_id:
            raise ValueError(f"Expected a non-empty value for `workspace_id` but received {workspace_id!r}")
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return self._get_api_list(
            f"/v2/workspaces/{workspace_id}/sessions/{session_id}/peers",
            page=SyncPage[Peer],
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
        )

    def add(
        self,
        session_id: str,
        *,
        workspace_id: str,
        body: Dict[str, SessionPeerConfigParam],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Session:
        """
        Add peers to a session

        Args:
          workspace_id: ID of the workspace

          session_id: ID of the session

          body: List of peer IDs to add to the session

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
            f"/v2/workspaces/{workspace_id}/sessions/{session_id}/peers",
            body=maybe_transform(body, peer_add_params.PeerAddParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Session,
        )

    def get_config(
        self,
        peer_id: str,
        *,
        workspace_id: str,
        session_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SessionPeerConfig:
        """
        Get the configuration for a peer in a session

        Args:
          workspace_id: ID of the workspace

          session_id: ID of the session

          peer_id: ID of the peer

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not workspace_id:
            raise ValueError(f"Expected a non-empty value for `workspace_id` but received {workspace_id!r}")
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        if not peer_id:
            raise ValueError(f"Expected a non-empty value for `peer_id` but received {peer_id!r}")
        return self._get(
            f"/v2/workspaces/{workspace_id}/sessions/{session_id}/peers/{peer_id}/config",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SessionPeerConfig,
        )

    def remove(
        self,
        session_id: str,
        *,
        workspace_id: str,
        body: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Session:
        """
        Remove peers from a session

        Args:
          workspace_id: ID of the workspace

          session_id: ID of the session

          body: List of peer IDs to remove from the session

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
            f"/v2/workspaces/{workspace_id}/sessions/{session_id}/peers",
            body=maybe_transform(body, SequenceNotStr[str]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Session,
        )

    def set(
        self,
        session_id: str,
        *,
        workspace_id: str,
        body: Dict[str, SessionPeerConfigParam],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Session:
        """
        Set the peers in a session

        Args:
          workspace_id: ID of the workspace

          session_id: ID of the session

          body: List of peer IDs to set for the session

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
            f"/v2/workspaces/{workspace_id}/sessions/{session_id}/peers",
            body=maybe_transform(body, peer_set_params.PeerSetParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Session,
        )

    def set_config(
        self,
        peer_id: str,
        *,
        workspace_id: str,
        session_id: str,
        observe_me: Optional[bool] | Omit = omit,
        observe_others: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Set the configuration for a peer in a session

        Args:
          workspace_id: ID of the workspace

          session_id: ID of the session

          peer_id: ID of the peer

          observe_me: Whether other peers in this session should try to form a session-level
              theory-of-mind representation of this peer

          observe_others: Whether this peer should form a session-level theory-of-mind representation of
              other peers in the session

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not workspace_id:
            raise ValueError(f"Expected a non-empty value for `workspace_id` but received {workspace_id!r}")
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        if not peer_id:
            raise ValueError(f"Expected a non-empty value for `peer_id` but received {peer_id!r}")
        return self._post(
            f"/v2/workspaces/{workspace_id}/sessions/{session_id}/peers/{peer_id}/config",
            body=maybe_transform(
                {
                    "observe_me": observe_me,
                    "observe_others": observe_others,
                },
                peer_set_config_params.PeerSetConfigParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncPeersResource(AsyncAPIResource):
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

    def list(
        self,
        session_id: str,
        *,
        workspace_id: str,
        page: int | Omit = omit,
        size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[Peer, AsyncPage[Peer]]:
        """
        Get peers from a session

        Args:
          workspace_id: ID of the workspace

          session_id: ID of the session

          page: Page number

          size: Page size

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not workspace_id:
            raise ValueError(f"Expected a non-empty value for `workspace_id` but received {workspace_id!r}")
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return self._get_api_list(
            f"/v2/workspaces/{workspace_id}/sessions/{session_id}/peers",
            page=AsyncPage[Peer],
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
        )

    async def add(
        self,
        session_id: str,
        *,
        workspace_id: str,
        body: Dict[str, SessionPeerConfigParam],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Session:
        """
        Add peers to a session

        Args:
          workspace_id: ID of the workspace

          session_id: ID of the session

          body: List of peer IDs to add to the session

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
            f"/v2/workspaces/{workspace_id}/sessions/{session_id}/peers",
            body=await async_maybe_transform(body, peer_add_params.PeerAddParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Session,
        )

    async def get_config(
        self,
        peer_id: str,
        *,
        workspace_id: str,
        session_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SessionPeerConfig:
        """
        Get the configuration for a peer in a session

        Args:
          workspace_id: ID of the workspace

          session_id: ID of the session

          peer_id: ID of the peer

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not workspace_id:
            raise ValueError(f"Expected a non-empty value for `workspace_id` but received {workspace_id!r}")
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        if not peer_id:
            raise ValueError(f"Expected a non-empty value for `peer_id` but received {peer_id!r}")
        return await self._get(
            f"/v2/workspaces/{workspace_id}/sessions/{session_id}/peers/{peer_id}/config",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SessionPeerConfig,
        )

    async def remove(
        self,
        session_id: str,
        *,
        workspace_id: str,
        body: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Session:
        """
        Remove peers from a session

        Args:
          workspace_id: ID of the workspace

          session_id: ID of the session

          body: List of peer IDs to remove from the session

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
            f"/v2/workspaces/{workspace_id}/sessions/{session_id}/peers",
            body=await async_maybe_transform(body, SequenceNotStr[str]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Session,
        )

    async def set(
        self,
        session_id: str,
        *,
        workspace_id: str,
        body: Dict[str, SessionPeerConfigParam],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Session:
        """
        Set the peers in a session

        Args:
          workspace_id: ID of the workspace

          session_id: ID of the session

          body: List of peer IDs to set for the session

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
            f"/v2/workspaces/{workspace_id}/sessions/{session_id}/peers",
            body=await async_maybe_transform(body, peer_set_params.PeerSetParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Session,
        )

    async def set_config(
        self,
        peer_id: str,
        *,
        workspace_id: str,
        session_id: str,
        observe_me: Optional[bool] | Omit = omit,
        observe_others: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Set the configuration for a peer in a session

        Args:
          workspace_id: ID of the workspace

          session_id: ID of the session

          peer_id: ID of the peer

          observe_me: Whether other peers in this session should try to form a session-level
              theory-of-mind representation of this peer

          observe_others: Whether this peer should form a session-level theory-of-mind representation of
              other peers in the session

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not workspace_id:
            raise ValueError(f"Expected a non-empty value for `workspace_id` but received {workspace_id!r}")
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        if not peer_id:
            raise ValueError(f"Expected a non-empty value for `peer_id` but received {peer_id!r}")
        return await self._post(
            f"/v2/workspaces/{workspace_id}/sessions/{session_id}/peers/{peer_id}/config",
            body=await async_maybe_transform(
                {
                    "observe_me": observe_me,
                    "observe_others": observe_others,
                },
                peer_set_config_params.PeerSetConfigParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class PeersResourceWithRawResponse:
    def __init__(self, peers: PeersResource) -> None:
        self._peers = peers

        self.list = to_raw_response_wrapper(
            peers.list,
        )
        self.add = to_raw_response_wrapper(
            peers.add,
        )
        self.get_config = to_raw_response_wrapper(
            peers.get_config,
        )
        self.remove = to_raw_response_wrapper(
            peers.remove,
        )
        self.set = to_raw_response_wrapper(
            peers.set,
        )
        self.set_config = to_raw_response_wrapper(
            peers.set_config,
        )


class AsyncPeersResourceWithRawResponse:
    def __init__(self, peers: AsyncPeersResource) -> None:
        self._peers = peers

        self.list = async_to_raw_response_wrapper(
            peers.list,
        )
        self.add = async_to_raw_response_wrapper(
            peers.add,
        )
        self.get_config = async_to_raw_response_wrapper(
            peers.get_config,
        )
        self.remove = async_to_raw_response_wrapper(
            peers.remove,
        )
        self.set = async_to_raw_response_wrapper(
            peers.set,
        )
        self.set_config = async_to_raw_response_wrapper(
            peers.set_config,
        )


class PeersResourceWithStreamingResponse:
    def __init__(self, peers: PeersResource) -> None:
        self._peers = peers

        self.list = to_streamed_response_wrapper(
            peers.list,
        )
        self.add = to_streamed_response_wrapper(
            peers.add,
        )
        self.get_config = to_streamed_response_wrapper(
            peers.get_config,
        )
        self.remove = to_streamed_response_wrapper(
            peers.remove,
        )
        self.set = to_streamed_response_wrapper(
            peers.set,
        )
        self.set_config = to_streamed_response_wrapper(
            peers.set_config,
        )


class AsyncPeersResourceWithStreamingResponse:
    def __init__(self, peers: AsyncPeersResource) -> None:
        self._peers = peers

        self.list = async_to_streamed_response_wrapper(
            peers.list,
        )
        self.add = async_to_streamed_response_wrapper(
            peers.add,
        )
        self.get_config = async_to_streamed_response_wrapper(
            peers.get_config,
        )
        self.remove = async_to_streamed_response_wrapper(
            peers.remove,
        )
        self.set = async_to_streamed_response_wrapper(
            peers.set,
        )
        self.set_config = async_to_streamed_response_wrapper(
            peers.set_config,
        )
