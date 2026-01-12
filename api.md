# Workspaces

Types:

```python
from honcho_core.types import (
    DreamConfiguration,
    MessageSearchOptions,
    PeerCardConfiguration,
    ReasoningConfiguration,
    SummaryConfiguration,
    Workspace,
    WorkspaceConfiguration,
    WorkspaceSearchResponse,
)
```

Methods:

- <code title="put /v2/workspaces/{workspace_id}">client.workspaces.<a href="./src/honcho_core/resources/workspaces/workspaces.py">update</a>(workspace_id, \*\*<a href="src/honcho_core/types/workspace_update_params.py">params</a>) -> <a href="./src/honcho_core/types/workspace.py">Workspace</a></code>
- <code title="post /v2/workspaces/list">client.workspaces.<a href="./src/honcho_core/resources/workspaces/workspaces.py">list</a>(\*\*<a href="src/honcho_core/types/workspace_list_params.py">params</a>) -> <a href="./src/honcho_core/types/workspace.py">SyncPage[Workspace]</a></code>
- <code title="delete /v2/workspaces/{workspace_id}">client.workspaces.<a href="./src/honcho_core/resources/workspaces/workspaces.py">delete</a>(workspace_id) -> None</code>
- <code title="post /v2/workspaces">client.workspaces.<a href="./src/honcho_core/resources/workspaces/workspaces.py">get_or_create</a>(\*\*<a href="src/honcho_core/types/workspace_get_or_create_params.py">params</a>) -> <a href="./src/honcho_core/types/workspace.py">Workspace</a></code>
- <code title="post /v2/workspaces/{workspace_id}/schedule_dream">client.workspaces.<a href="./src/honcho_core/resources/workspaces/workspaces.py">schedule_dream</a>(workspace_id, \*\*<a href="src/honcho_core/types/workspace_schedule_dream_params.py">params</a>) -> None</code>
- <code title="post /v2/workspaces/{workspace_id}/search">client.workspaces.<a href="./src/honcho_core/resources/workspaces/workspaces.py">search</a>(workspace_id, \*\*<a href="src/honcho_core/types/workspace_search_params.py">params</a>) -> <a href="./src/honcho_core/types/workspace_search_response.py">WorkspaceSearchResponse</a></code>

## Peers

Types:

```python
from honcho_core.types.workspaces import (
    PagePeer,
    PageSession,
    Peer,
    PeerCardResponse,
    SessionGet,
    PeerChatResponse,
    PeerContextResponse,
    PeerRepresentationResponse,
    PeerSearchResponse,
)
```

Methods:

- <code title="put /v2/workspaces/{workspace_id}/peers/{peer_id}">client.workspaces.peers.<a href="./src/honcho_core/resources/workspaces/peers/peers.py">update</a>(peer_id, \*, workspace_id, \*\*<a href="src/honcho_core/types/workspaces/peer_update_params.py">params</a>) -> <a href="./src/honcho_core/types/workspaces/peer.py">Peer</a></code>
- <code title="post /v2/workspaces/{workspace_id}/peers/list">client.workspaces.peers.<a href="./src/honcho_core/resources/workspaces/peers/peers.py">list</a>(workspace_id, \*\*<a href="src/honcho_core/types/workspaces/peer_list_params.py">params</a>) -> <a href="./src/honcho_core/types/workspaces/peer.py">SyncPage[Peer]</a></code>
- <code title="get /v2/workspaces/{workspace_id}/peers/{peer_id}/card">client.workspaces.peers.<a href="./src/honcho_core/resources/workspaces/peers/peers.py">card</a>(peer_id, \*, workspace_id, \*\*<a href="src/honcho_core/types/workspaces/peer_card_params.py">params</a>) -> <a href="./src/honcho_core/types/workspaces/peer_card_response.py">PeerCardResponse</a></code>
- <code title="post /v2/workspaces/{workspace_id}/peers/{peer_id}/chat">client.workspaces.peers.<a href="./src/honcho_core/resources/workspaces/peers/peers.py">chat</a>(peer_id, \*, workspace_id, \*\*<a href="src/honcho_core/types/workspaces/peer_chat_params.py">params</a>) -> <a href="./src/honcho_core/types/workspaces/peer_chat_response.py">PeerChatResponse</a></code>
- <code title="get /v2/workspaces/{workspace_id}/peers/{peer_id}/context">client.workspaces.peers.<a href="./src/honcho_core/resources/workspaces/peers/peers.py">context</a>(peer_id, \*, workspace_id, \*\*<a href="src/honcho_core/types/workspaces/peer_context_params.py">params</a>) -> <a href="./src/honcho_core/types/workspaces/peer_context_response.py">PeerContextResponse</a></code>
- <code title="post /v2/workspaces/{workspace_id}/peers">client.workspaces.peers.<a href="./src/honcho_core/resources/workspaces/peers/peers.py">get_or_create</a>(workspace_id, \*\*<a href="src/honcho_core/types/workspaces/peer_get_or_create_params.py">params</a>) -> <a href="./src/honcho_core/types/workspaces/peer.py">Peer</a></code>
- <code title="post /v2/workspaces/{workspace_id}/peers/{peer_id}/representation">client.workspaces.peers.<a href="./src/honcho_core/resources/workspaces/peers/peers.py">representation</a>(peer_id, \*, workspace_id, \*\*<a href="src/honcho_core/types/workspaces/peer_representation_params.py">params</a>) -> <a href="./src/honcho_core/types/workspaces/peer_representation_response.py">PeerRepresentationResponse</a></code>
- <code title="post /v2/workspaces/{workspace_id}/peers/{peer_id}/search">client.workspaces.peers.<a href="./src/honcho_core/resources/workspaces/peers/peers.py">search</a>(peer_id, \*, workspace_id, \*\*<a href="src/honcho_core/types/workspaces/peer_search_params.py">params</a>) -> <a href="./src/honcho_core/types/workspaces/peer_search_response.py">PeerSearchResponse</a></code>
- <code title="put /v2/workspaces/{workspace_id}/peers/{peer_id}/card">client.workspaces.peers.<a href="./src/honcho_core/resources/workspaces/peers/peers.py">set_card</a>(peer_id, \*, workspace_id, \*\*<a href="src/honcho_core/types/workspaces/peer_set_card_params.py">params</a>) -> <a href="./src/honcho_core/types/workspaces/peer_card_response.py">PeerCardResponse</a></code>

### Sessions

Methods:

- <code title="post /v2/workspaces/{workspace_id}/peers/{peer_id}/sessions">client.workspaces.peers.sessions.<a href="./src/honcho_core/resources/workspaces/peers/sessions.py">list</a>(peer_id, \*, workspace_id, \*\*<a href="src/honcho_core/types/workspaces/peers/session_list_params.py">params</a>) -> <a href="./src/honcho_core/types/workspaces/session.py">SyncPage[Session]</a></code>

## Sessions

Types:

```python
from honcho_core.types.workspaces import (
    Session,
    SessionConfiguration,
    Summary,
    SessionContextResponse,
    SessionSearchResponse,
    SessionSummariesResponse,
)
```

Methods:

- <code title="put /v2/workspaces/{workspace_id}/sessions/{session_id}">client.workspaces.sessions.<a href="./src/honcho_core/resources/workspaces/sessions/sessions.py">update</a>(session_id, \*, workspace_id, \*\*<a href="src/honcho_core/types/workspaces/session_update_params.py">params</a>) -> <a href="./src/honcho_core/types/workspaces/session.py">Session</a></code>
- <code title="post /v2/workspaces/{workspace_id}/sessions/list">client.workspaces.sessions.<a href="./src/honcho_core/resources/workspaces/sessions/sessions.py">list</a>(workspace_id, \*\*<a href="src/honcho_core/types/workspaces/session_list_params.py">params</a>) -> <a href="./src/honcho_core/types/workspaces/session.py">SyncPage[Session]</a></code>
- <code title="delete /v2/workspaces/{workspace_id}/sessions/{session_id}">client.workspaces.sessions.<a href="./src/honcho_core/resources/workspaces/sessions/sessions.py">delete</a>(session_id, \*, workspace_id) -> object</code>
- <code title="post /v2/workspaces/{workspace_id}/sessions/{session_id}/clone">client.workspaces.sessions.<a href="./src/honcho_core/resources/workspaces/sessions/sessions.py">clone</a>(session_id, \*, workspace_id, \*\*<a href="src/honcho_core/types/workspaces/session_clone_params.py">params</a>) -> <a href="./src/honcho_core/types/workspaces/session.py">Session</a></code>
- <code title="get /v2/workspaces/{workspace_id}/sessions/{session_id}/context">client.workspaces.sessions.<a href="./src/honcho_core/resources/workspaces/sessions/sessions.py">context</a>(session_id, \*, workspace_id, \*\*<a href="src/honcho_core/types/workspaces/session_context_params.py">params</a>) -> <a href="./src/honcho_core/types/workspaces/session_context_response.py">SessionContextResponse</a></code>
- <code title="post /v2/workspaces/{workspace_id}/sessions">client.workspaces.sessions.<a href="./src/honcho_core/resources/workspaces/sessions/sessions.py">get_or_create</a>(workspace_id, \*\*<a href="src/honcho_core/types/workspaces/session_get_or_create_params.py">params</a>) -> <a href="./src/honcho_core/types/workspaces/session.py">Session</a></code>
- <code title="post /v2/workspaces/{workspace_id}/sessions/{session_id}/search">client.workspaces.sessions.<a href="./src/honcho_core/resources/workspaces/sessions/sessions.py">search</a>(session_id, \*, workspace_id, \*\*<a href="src/honcho_core/types/workspaces/session_search_params.py">params</a>) -> <a href="./src/honcho_core/types/workspaces/session_search_response.py">SessionSearchResponse</a></code>
- <code title="get /v2/workspaces/{workspace_id}/sessions/{session_id}/summaries">client.workspaces.sessions.<a href="./src/honcho_core/resources/workspaces/sessions/sessions.py">summaries</a>(session_id, \*, workspace_id) -> <a href="./src/honcho_core/types/workspaces/session_summaries_response.py">SessionSummariesResponse</a></code>

### Messages

Types:

```python
from honcho_core.types.workspaces.sessions import (
    Message,
    MessageCreate,
    MessageCreateResponse,
    MessageUploadResponse,
)
```

Methods:

- <code title="post /v2/workspaces/{workspace_id}/sessions/{session_id}/messages">client.workspaces.sessions.messages.<a href="./src/honcho_core/resources/workspaces/sessions/messages.py">create</a>(session_id, \*, workspace_id, \*\*<a href="src/honcho_core/types/workspaces/sessions/message_create_params.py">params</a>) -> <a href="./src/honcho_core/types/workspaces/sessions/message_create_response.py">MessageCreateResponse</a></code>
- <code title="put /v2/workspaces/{workspace_id}/sessions/{session_id}/messages/{message_id}">client.workspaces.sessions.messages.<a href="./src/honcho_core/resources/workspaces/sessions/messages.py">update</a>(message_id, \*, workspace_id, session_id, \*\*<a href="src/honcho_core/types/workspaces/sessions/message_update_params.py">params</a>) -> <a href="./src/honcho_core/types/workspaces/sessions/message.py">Message</a></code>
- <code title="post /v2/workspaces/{workspace_id}/sessions/{session_id}/messages/list">client.workspaces.sessions.messages.<a href="./src/honcho_core/resources/workspaces/sessions/messages.py">list</a>(session_id, \*, workspace_id, \*\*<a href="src/honcho_core/types/workspaces/sessions/message_list_params.py">params</a>) -> <a href="./src/honcho_core/types/workspaces/sessions/message.py">SyncPage[Message]</a></code>
- <code title="get /v2/workspaces/{workspace_id}/sessions/{session_id}/messages/{message_id}">client.workspaces.sessions.messages.<a href="./src/honcho_core/resources/workspaces/sessions/messages.py">get</a>(message_id, \*, workspace_id, session_id) -> <a href="./src/honcho_core/types/workspaces/sessions/message.py">Message</a></code>
- <code title="post /v2/workspaces/{workspace_id}/sessions/{session_id}/messages/upload">client.workspaces.sessions.messages.<a href="./src/honcho_core/resources/workspaces/sessions/messages.py">upload</a>(session_id, \*, workspace_id, \*\*<a href="src/honcho_core/types/workspaces/sessions/message_upload_params.py">params</a>) -> <a href="./src/honcho_core/types/workspaces/sessions/message_upload_response.py">MessageUploadResponse</a></code>

### Peers

Types:

```python
from honcho_core.types.workspaces.sessions import SessionPeerConfig
```

Methods:

- <code title="get /v2/workspaces/{workspace_id}/sessions/{session_id}/peers">client.workspaces.sessions.peers.<a href="./src/honcho_core/resources/workspaces/sessions/peers.py">list</a>(session_id, \*, workspace_id, \*\*<a href="src/honcho_core/types/workspaces/sessions/peer_list_params.py">params</a>) -> <a href="./src/honcho_core/types/workspaces/peer.py">SyncPage[Peer]</a></code>
- <code title="post /v2/workspaces/{workspace_id}/sessions/{session_id}/peers">client.workspaces.sessions.peers.<a href="./src/honcho_core/resources/workspaces/sessions/peers.py">add</a>(session_id, \*, workspace_id, \*\*<a href="src/honcho_core/types/workspaces/sessions/peer_add_params.py">params</a>) -> <a href="./src/honcho_core/types/workspaces/session.py">Session</a></code>
- <code title="get /v2/workspaces/{workspace_id}/sessions/{session_id}/peers/{peer_id}/config">client.workspaces.sessions.peers.<a href="./src/honcho_core/resources/workspaces/sessions/peers.py">config</a>(peer_id, \*, workspace_id, session_id) -> <a href="./src/honcho_core/types/workspaces/sessions/session_peer_config.py">SessionPeerConfig</a></code>
- <code title="delete /v2/workspaces/{workspace_id}/sessions/{session_id}/peers">client.workspaces.sessions.peers.<a href="./src/honcho_core/resources/workspaces/sessions/peers.py">remove</a>(session_id, \*, workspace_id, \*\*<a href="src/honcho_core/types/workspaces/sessions/peer_remove_params.py">params</a>) -> <a href="./src/honcho_core/types/workspaces/session.py">Session</a></code>
- <code title="put /v2/workspaces/{workspace_id}/sessions/{session_id}/peers">client.workspaces.sessions.peers.<a href="./src/honcho_core/resources/workspaces/sessions/peers.py">set</a>(session_id, \*, workspace_id, \*\*<a href="src/honcho_core/types/workspaces/sessions/peer_set_params.py">params</a>) -> <a href="./src/honcho_core/types/workspaces/session.py">Session</a></code>
- <code title="put /v2/workspaces/{workspace_id}/sessions/{session_id}/peers/{peer_id}/config">client.workspaces.sessions.peers.<a href="./src/honcho_core/resources/workspaces/sessions/peers.py">set_config</a>(peer_id, \*, workspace_id, session_id, \*\*<a href="src/honcho_core/types/workspaces/sessions/peer_set_config_params.py">params</a>) -> None</code>

## Webhooks

Types:

```python
from honcho_core.types.workspaces import WebhookEndpoint
```

Methods:

- <code title="get /v2/workspaces/{workspace_id}/webhooks">client.workspaces.webhooks.<a href="./src/honcho_core/resources/workspaces/webhooks.py">list</a>(workspace_id, \*\*<a href="src/honcho_core/types/workspaces/webhook_list_params.py">params</a>) -> <a href="./src/honcho_core/types/workspaces/webhook_endpoint.py">SyncPage[WebhookEndpoint]</a></code>
- <code title="delete /v2/workspaces/{workspace_id}/webhooks/{endpoint_id}">client.workspaces.webhooks.<a href="./src/honcho_core/resources/workspaces/webhooks.py">delete</a>(endpoint_id, \*, workspace_id) -> None</code>
- <code title="post /v2/workspaces/{workspace_id}/webhooks">client.workspaces.webhooks.<a href="./src/honcho_core/resources/workspaces/webhooks.py">get_or_create</a>(workspace_id, \*\*<a href="src/honcho_core/types/workspaces/webhook_get_or_create_params.py">params</a>) -> <a href="./src/honcho_core/types/workspaces/webhook_endpoint.py">WebhookEndpoint</a></code>
- <code title="get /v2/workspaces/{workspace_id}/webhooks/test">client.workspaces.webhooks.<a href="./src/honcho_core/resources/workspaces/webhooks.py">test_emit</a>(workspace_id) -> object</code>

## Queue

Types:

```python
from honcho_core.types.workspaces import QueueStatusResponse
```

Methods:

- <code title="get /v2/workspaces/{workspace_id}/queue/status">client.workspaces.queue.<a href="./src/honcho_core/resources/workspaces/queue.py">status</a>(workspace_id, \*\*<a href="src/honcho_core/types/workspaces/queue_status_params.py">params</a>) -> <a href="./src/honcho_core/types/workspaces/queue_status_response.py">QueueStatusResponse</a></code>

## Conclusions

Types:

```python
from honcho_core.types.workspaces import (
    Conclusion,
    ConclusionCreateResponse,
    ConclusionQueryResponse,
)
```

Methods:

- <code title="post /v2/workspaces/{workspace_id}/conclusions">client.workspaces.conclusions.<a href="./src/honcho_core/resources/workspaces/conclusions.py">create</a>(workspace_id, \*\*<a href="src/honcho_core/types/workspaces/conclusion_create_params.py">params</a>) -> <a href="./src/honcho_core/types/workspaces/conclusion_create_response.py">ConclusionCreateResponse</a></code>
- <code title="post /v2/workspaces/{workspace_id}/conclusions/list">client.workspaces.conclusions.<a href="./src/honcho_core/resources/workspaces/conclusions.py">list</a>(workspace_id, \*\*<a href="src/honcho_core/types/workspaces/conclusion_list_params.py">params</a>) -> <a href="./src/honcho_core/types/workspaces/conclusion.py">SyncPage[Conclusion]</a></code>
- <code title="delete /v2/workspaces/{workspace_id}/conclusions/{conclusion_id}">client.workspaces.conclusions.<a href="./src/honcho_core/resources/workspaces/conclusions.py">delete</a>(conclusion_id, \*, workspace_id) -> None</code>
- <code title="post /v2/workspaces/{workspace_id}/conclusions/query">client.workspaces.conclusions.<a href="./src/honcho_core/resources/workspaces/conclusions.py">query</a>(workspace_id, \*\*<a href="src/honcho_core/types/workspaces/conclusion_query_params.py">params</a>) -> <a href="./src/honcho_core/types/workspaces/conclusion_query_response.py">ConclusionQueryResponse</a></code>
