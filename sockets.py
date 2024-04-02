# websocket 연결 -> ws://127.0.0.0.1:8000/ws
from fastapi import APIRouter, WebSocket
from connection import manager
from models import Message
from dependencies import get_username
from fastapi.websockets import WebSocketDisconnect

router = APIRouter()

@router.websocket('/ws/{token}')
async def websocket_endpoint(websocket: WebSocket, token: str):
    username = get_username(token)
    await manager.connect(websocket)

    try:
        while True:
            data = await websocket.receive_text()
            message = Message(username=username, text=data)
            await manager.broadcast(message.json())

    except WebSocketDisconnect:
            manager.disconnect(websocket)