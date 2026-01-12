# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Literal

import httpx

from .queue import (
    QueueResource,
    AsyncQueueResource,
    QueueResourceWithRawResponse,
    AsyncQueueResourceWithRawResponse,
    QueueResourceWithStreamingResponse,
    AsyncQueueResourceWithStreamingResponse,
)
from ...types import (
    workspace_list_params,
    workspace_search_params,
    workspace_update_params,
    workspace_get_or_create_params,
    workspace_schedule_dream_params,
)
from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from .webhooks import (
    WebhooksResource,
    AsyncWebhooksResource,
    WebhooksResourceWithRawResponse,
    AsyncWebhooksResourceWithRawResponse,
    WebhooksResourceWithStreamingResponse,
    AsyncWebhooksResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .conclusions import (
    ConclusionsResource,
    AsyncConclusionsResource,
    ConclusionsResourceWithRawResponse,
    AsyncConclusionsResourceWithRawResponse,
    ConclusionsResourceWithStreamingResponse,
    AsyncConclusionsResourceWithStreamingResponse,
)
from .peers.peers import (
    PeersResource,
    AsyncPeersResource,
    PeersResourceWithRawResponse,
    AsyncPeersResourceWithRawResponse,
    PeersResourceWithStreamingResponse,
    AsyncPeersResourceWithStreamingResponse,
)
from ...pagination import SyncPage, AsyncPage
from ..._base_client import AsyncPaginator, make_request_options
from ...types.workspace import Workspace
from .sessions.sessions import (
    SessionsResource,
    AsyncSessionsResource,
    SessionsResourceWithRawResponse,
    AsyncSessionsResourceWithRawResponse,
    SessionsResourceWithStreamingResponse,
    AsyncSessionsResourceWithStreamingResponse,
)
from ...types.workspace_search_response import WorkspaceSearchResponse
from ...types.workspace_configuration_param import WorkspaceConfigurationParam

__all__ = ["WorkspacesResource", "AsyncWorkspacesResource"]


class WorkspacesResource(SyncAPIResource):
    @cached_property
    def peers(self) -> PeersResource:
        return PeersResource(self._client)

    @cached_property
    def sessions(self) -> SessionsResource:
        return SessionsResource(self._client)

    @cached_property
    def webhooks(self) -> WebhooksResource:
        return WebhooksResource(self._client)

    @cached_property
    def queue(self) -> QueueResource:
        return QueueResource(self._client)

    @cached_property
    def conclusions(self) -> ConclusionsResource:
        return ConclusionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> WorkspacesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/plastic-labs/honcho-python-core#accessing-raw-response-data-eg-headers
        """
        return WorkspacesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> WorkspacesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/plastic-labs/honcho-python-core#with_streaming_response
        """
        return WorkspacesResourceWithStreamingResponse(self)

    def update(
        self,
        workspace_id: str,
        *,
        configuration: Optional[WorkspaceConfigurationParam] | Omit = omit,
        metadata: Optional[Dict[str, object]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Workspace:
        """
        Update Workspace metadata and/or configuration.

        Args:
          configuration: The set of options that can be in a workspace DB-level configuration dictionary.

              All fields are optional. Session-level configuration overrides workspace-level
              configuration, which overrides global configuration.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not workspace_id:
            raise ValueError(f"Expected a non-empty value for `workspace_id` but received {workspace_id!r}")
        return self._put(
            f"/v2/workspaces/{workspace_id}",
            body=maybe_transform(
                {
                    "configuration": configuration,
                    "metadata": metadata,
                },
                workspace_update_params.WorkspaceUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Workspace,
        )

    def list(
        self,
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
    ) -> SyncPage[Workspace]:
        """
        Get all Workspaces, paginated with optional filters.

        Args:
          page: Page number

          size: Page size

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v2/workspaces/list",
            page=SyncPage[Workspace],
            body=maybe_transform({"filters": filters}, workspace_list_params.WorkspaceListParams),
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
                    workspace_list_params.WorkspaceListParams,
                ),
            ),
            model=Workspace,
            method="post",
        )

    def delete(
        self,
        workspace_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Delete a Workspace.

        This will permanently delete all sessions, peers, messages,
        and conclusions associated with the workspace.

        This action cannot be undone.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not workspace_id:
            raise ValueError(f"Expected a non-empty value for `workspace_id` but received {workspace_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/v2/workspaces/{workspace_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def get_or_create(
        self,
        *,
        id: str,
        configuration: WorkspaceConfigurationParam | Omit = omit,
        metadata: Dict[str, object] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Workspace:
        """
        Get a Workspace by ID.

        If workspace_id is provided as a query parameter, it uses that (must match JWT
        workspace_id). Otherwise, it uses the workspace_id from the JWT.

        Args:
          configuration: The set of options that can be in a workspace DB-level configuration dictionary.

              All fields are optional. Session-level configuration overrides workspace-level
              configuration, which overrides global configuration.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v2/workspaces",
            body=maybe_transform(
                {
                    "id": id,
                    "configuration": configuration,
                    "metadata": metadata,
                },
                workspace_get_or_create_params.WorkspaceGetOrCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Workspace,
        )

    def schedule_dream(
        self,
        workspace_id: str,
        *,
        dream_type: Literal["omni"],
        observer: str,
        session_id: str,
        observed: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Manually schedule a dream task for a specific collection.

        This endpoint bypasses all automatic dream conditions (document threshold,
        minimum hours between dreams) and schedules the dream task for a future
        execution.

        Currently this endpoint only supports scheduling immediate dreams. In the
        future, users may pass a cron-style expression to schedule dreams at specific
        times.

        Args:
          dream_type: Type of dream to schedule

          observer: Observer peer name

          session_id: Session ID to scope the dream to

          observed: Observed peer name (defaults to observer if not specified)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not workspace_id:
            raise ValueError(f"Expected a non-empty value for `workspace_id` but received {workspace_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            f"/v2/workspaces/{workspace_id}/schedule_dream",
            body=maybe_transform(
                {
                    "dream_type": dream_type,
                    "observer": observer,
                    "session_id": session_id,
                    "observed": observed,
                },
                workspace_schedule_dream_params.WorkspaceScheduleDreamParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def search(
        self,
        workspace_id: str,
        *,
        query: str,
        filters: Optional[Dict[str, object]] | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WorkspaceSearchResponse:
        """Search messages in a Workspace using optional filters.

        Use `limit` to control
        the number of results returned.

        Args:
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
        return self._post(
            f"/v2/workspaces/{workspace_id}/search",
            body=maybe_transform(
                {
                    "query": query,
                    "filters": filters,
                    "limit": limit,
                },
                workspace_search_params.WorkspaceSearchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WorkspaceSearchResponse,
        )


class AsyncWorkspacesResource(AsyncAPIResource):
    @cached_property
    def peers(self) -> AsyncPeersResource:
        return AsyncPeersResource(self._client)

    @cached_property
    def sessions(self) -> AsyncSessionsResource:
        return AsyncSessionsResource(self._client)

    @cached_property
    def webhooks(self) -> AsyncWebhooksResource:
        return AsyncWebhooksResource(self._client)

    @cached_property
    def queue(self) -> AsyncQueueResource:
        return AsyncQueueResource(self._client)

    @cached_property
    def conclusions(self) -> AsyncConclusionsResource:
        return AsyncConclusionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncWorkspacesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/plastic-labs/honcho-python-core#accessing-raw-response-data-eg-headers
        """
        return AsyncWorkspacesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncWorkspacesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/plastic-labs/honcho-python-core#with_streaming_response
        """
        return AsyncWorkspacesResourceWithStreamingResponse(self)

    async def update(
        self,
        workspace_id: str,
        *,
        configuration: Optional[WorkspaceConfigurationParam] | Omit = omit,
        metadata: Optional[Dict[str, object]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Workspace:
        """
        Update Workspace metadata and/or configuration.

        Args:
          configuration: The set of options that can be in a workspace DB-level configuration dictionary.

              All fields are optional. Session-level configuration overrides workspace-level
              configuration, which overrides global configuration.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not workspace_id:
            raise ValueError(f"Expected a non-empty value for `workspace_id` but received {workspace_id!r}")
        return await self._put(
            f"/v2/workspaces/{workspace_id}",
            body=await async_maybe_transform(
                {
                    "configuration": configuration,
                    "metadata": metadata,
                },
                workspace_update_params.WorkspaceUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Workspace,
        )

    def list(
        self,
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
    ) -> AsyncPaginator[Workspace, AsyncPage[Workspace]]:
        """
        Get all Workspaces, paginated with optional filters.

        Args:
          page: Page number

          size: Page size

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v2/workspaces/list",
            page=AsyncPage[Workspace],
            body=maybe_transform({"filters": filters}, workspace_list_params.WorkspaceListParams),
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
                    workspace_list_params.WorkspaceListParams,
                ),
            ),
            model=Workspace,
            method="post",
        )

    async def delete(
        self,
        workspace_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Delete a Workspace.

        This will permanently delete all sessions, peers, messages,
        and conclusions associated with the workspace.

        This action cannot be undone.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not workspace_id:
            raise ValueError(f"Expected a non-empty value for `workspace_id` but received {workspace_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/v2/workspaces/{workspace_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def get_or_create(
        self,
        *,
        id: str,
        configuration: WorkspaceConfigurationParam | Omit = omit,
        metadata: Dict[str, object] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Workspace:
        """
        Get a Workspace by ID.

        If workspace_id is provided as a query parameter, it uses that (must match JWT
        workspace_id). Otherwise, it uses the workspace_id from the JWT.

        Args:
          configuration: The set of options that can be in a workspace DB-level configuration dictionary.

              All fields are optional. Session-level configuration overrides workspace-level
              configuration, which overrides global configuration.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v2/workspaces",
            body=await async_maybe_transform(
                {
                    "id": id,
                    "configuration": configuration,
                    "metadata": metadata,
                },
                workspace_get_or_create_params.WorkspaceGetOrCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Workspace,
        )

    async def schedule_dream(
        self,
        workspace_id: str,
        *,
        dream_type: Literal["omni"],
        observer: str,
        session_id: str,
        observed: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Manually schedule a dream task for a specific collection.

        This endpoint bypasses all automatic dream conditions (document threshold,
        minimum hours between dreams) and schedules the dream task for a future
        execution.

        Currently this endpoint only supports scheduling immediate dreams. In the
        future, users may pass a cron-style expression to schedule dreams at specific
        times.

        Args:
          dream_type: Type of dream to schedule

          observer: Observer peer name

          session_id: Session ID to scope the dream to

          observed: Observed peer name (defaults to observer if not specified)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not workspace_id:
            raise ValueError(f"Expected a non-empty value for `workspace_id` but received {workspace_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            f"/v2/workspaces/{workspace_id}/schedule_dream",
            body=await async_maybe_transform(
                {
                    "dream_type": dream_type,
                    "observer": observer,
                    "session_id": session_id,
                    "observed": observed,
                },
                workspace_schedule_dream_params.WorkspaceScheduleDreamParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def search(
        self,
        workspace_id: str,
        *,
        query: str,
        filters: Optional[Dict[str, object]] | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WorkspaceSearchResponse:
        """Search messages in a Workspace using optional filters.

        Use `limit` to control
        the number of results returned.

        Args:
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
        return await self._post(
            f"/v2/workspaces/{workspace_id}/search",
            body=await async_maybe_transform(
                {
                    "query": query,
                    "filters": filters,
                    "limit": limit,
                },
                workspace_search_params.WorkspaceSearchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WorkspaceSearchResponse,
        )


class WorkspacesResourceWithRawResponse:
    def __init__(self, workspaces: WorkspacesResource) -> None:
        self._workspaces = workspaces

        self.update = to_raw_response_wrapper(
            workspaces.update,
        )
        self.list = to_raw_response_wrapper(
            workspaces.list,
        )
        self.delete = to_raw_response_wrapper(
            workspaces.delete,
        )
        self.get_or_create = to_raw_response_wrapper(
            workspaces.get_or_create,
        )
        self.schedule_dream = to_raw_response_wrapper(
            workspaces.schedule_dream,
        )
        self.search = to_raw_response_wrapper(
            workspaces.search,
        )

    @cached_property
    def peers(self) -> PeersResourceWithRawResponse:
        return PeersResourceWithRawResponse(self._workspaces.peers)

    @cached_property
    def sessions(self) -> SessionsResourceWithRawResponse:
        return SessionsResourceWithRawResponse(self._workspaces.sessions)

    @cached_property
    def webhooks(self) -> WebhooksResourceWithRawResponse:
        return WebhooksResourceWithRawResponse(self._workspaces.webhooks)

    @cached_property
    def queue(self) -> QueueResourceWithRawResponse:
        return QueueResourceWithRawResponse(self._workspaces.queue)

    @cached_property
    def conclusions(self) -> ConclusionsResourceWithRawResponse:
        return ConclusionsResourceWithRawResponse(self._workspaces.conclusions)


class AsyncWorkspacesResourceWithRawResponse:
    def __init__(self, workspaces: AsyncWorkspacesResource) -> None:
        self._workspaces = workspaces

        self.update = async_to_raw_response_wrapper(
            workspaces.update,
        )
        self.list = async_to_raw_response_wrapper(
            workspaces.list,
        )
        self.delete = async_to_raw_response_wrapper(
            workspaces.delete,
        )
        self.get_or_create = async_to_raw_response_wrapper(
            workspaces.get_or_create,
        )
        self.schedule_dream = async_to_raw_response_wrapper(
            workspaces.schedule_dream,
        )
        self.search = async_to_raw_response_wrapper(
            workspaces.search,
        )

    @cached_property
    def peers(self) -> AsyncPeersResourceWithRawResponse:
        return AsyncPeersResourceWithRawResponse(self._workspaces.peers)

    @cached_property
    def sessions(self) -> AsyncSessionsResourceWithRawResponse:
        return AsyncSessionsResourceWithRawResponse(self._workspaces.sessions)

    @cached_property
    def webhooks(self) -> AsyncWebhooksResourceWithRawResponse:
        return AsyncWebhooksResourceWithRawResponse(self._workspaces.webhooks)

    @cached_property
    def queue(self) -> AsyncQueueResourceWithRawResponse:
        return AsyncQueueResourceWithRawResponse(self._workspaces.queue)

    @cached_property
    def conclusions(self) -> AsyncConclusionsResourceWithRawResponse:
        return AsyncConclusionsResourceWithRawResponse(self._workspaces.conclusions)


class WorkspacesResourceWithStreamingResponse:
    def __init__(self, workspaces: WorkspacesResource) -> None:
        self._workspaces = workspaces

        self.update = to_streamed_response_wrapper(
            workspaces.update,
        )
        self.list = to_streamed_response_wrapper(
            workspaces.list,
        )
        self.delete = to_streamed_response_wrapper(
            workspaces.delete,
        )
        self.get_or_create = to_streamed_response_wrapper(
            workspaces.get_or_create,
        )
        self.schedule_dream = to_streamed_response_wrapper(
            workspaces.schedule_dream,
        )
        self.search = to_streamed_response_wrapper(
            workspaces.search,
        )

    @cached_property
    def peers(self) -> PeersResourceWithStreamingResponse:
        return PeersResourceWithStreamingResponse(self._workspaces.peers)

    @cached_property
    def sessions(self) -> SessionsResourceWithStreamingResponse:
        return SessionsResourceWithStreamingResponse(self._workspaces.sessions)

    @cached_property
    def webhooks(self) -> WebhooksResourceWithStreamingResponse:
        return WebhooksResourceWithStreamingResponse(self._workspaces.webhooks)

    @cached_property
    def queue(self) -> QueueResourceWithStreamingResponse:
        return QueueResourceWithStreamingResponse(self._workspaces.queue)

    @cached_property
    def conclusions(self) -> ConclusionsResourceWithStreamingResponse:
        return ConclusionsResourceWithStreamingResponse(self._workspaces.conclusions)


class AsyncWorkspacesResourceWithStreamingResponse:
    def __init__(self, workspaces: AsyncWorkspacesResource) -> None:
        self._workspaces = workspaces

        self.update = async_to_streamed_response_wrapper(
            workspaces.update,
        )
        self.list = async_to_streamed_response_wrapper(
            workspaces.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            workspaces.delete,
        )
        self.get_or_create = async_to_streamed_response_wrapper(
            workspaces.get_or_create,
        )
        self.schedule_dream = async_to_streamed_response_wrapper(
            workspaces.schedule_dream,
        )
        self.search = async_to_streamed_response_wrapper(
            workspaces.search,
        )

    @cached_property
    def peers(self) -> AsyncPeersResourceWithStreamingResponse:
        return AsyncPeersResourceWithStreamingResponse(self._workspaces.peers)

    @cached_property
    def sessions(self) -> AsyncSessionsResourceWithStreamingResponse:
        return AsyncSessionsResourceWithStreamingResponse(self._workspaces.sessions)

    @cached_property
    def webhooks(self) -> AsyncWebhooksResourceWithStreamingResponse:
        return AsyncWebhooksResourceWithStreamingResponse(self._workspaces.webhooks)

    @cached_property
    def queue(self) -> AsyncQueueResourceWithStreamingResponse:
        return AsyncQueueResourceWithStreamingResponse(self._workspaces.queue)

    @cached_property
    def conclusions(self) -> AsyncConclusionsResourceWithStreamingResponse:
        return AsyncConclusionsResourceWithStreamingResponse(self._workspaces.conclusions)
