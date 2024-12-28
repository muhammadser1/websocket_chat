from fastapi import WebSocket, WebSocketDisconnect, APIRouter
from connection_manager import ConnectionManager

router = APIRouter()
manager = ConnectionManager()

@router.websocket("/ws/chat")
async def websocket_endpoint(websocket: WebSocket):
    """
    WebSocket endpoint for handling real-time chat.
    """
    client_id = await manager.connect(websocket)
    print(f"Client connected: {client_id}")
    await manager.broadcast(f"Client {client_id} joined the chat!")

    try:
        while True:
            data = await websocket.receive_text()
            print(f"Message from {client_id}: {data}")
            await manager.broadcast(f"{client_id}: {data}")
    except WebSocketDisconnect:
        manager.disconnect(client_id)
        print(f"Client disconnected: {client_id}")
        await manager.broadcast(f"Client {client_id} left the chat.")
