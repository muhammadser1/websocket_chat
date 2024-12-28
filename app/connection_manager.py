from typing import Dict
from fastapi import WebSocket
import uuid

class ConnectionManager:
    """Manages WebSocket connections and broadcasting of messages."""

    def __init__(self):
        """Initialize the connection manager with an empty list of connections."""
        self.active_connections: Dict[str, WebSocket] = {}

    async def connect(self, websocket: WebSocket) -> str:
        """
        Accept a new WebSocket connection and assign it a unique client ID.
        """
        await websocket.accept()
        client_id = str(uuid.uuid4())  # Generate a unique identifier
        self.active_connections[client_id] = websocket
        return client_id

    def disconnect(self, client_id: str):
        """Remove a disconnected client from the active connections."""
        self.active_connections.pop(client_id, None)

    async def broadcast(self, message: str):
        """Broadcast a message to all connected clients."""
        for connection in self.active_connections.values():
            await connection.send_text(message)
