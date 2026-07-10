#!/usr/bin/env python3
"""
ASGI application with HTTP and WebSocket routes.

The HTTP route serves a basic HTML page.
The WebSocket route echoes each received text message.
"""

from starlette.applications import Starlette
from starlette.responses import HTMLResponse
from starlette.routing import Route, WebSocketRoute
from starlette.websockets import WebSocketDisconnect


async def homepage(request):
    """
    Return the application's HTML page.
    """
    return HTMLResponse(
        """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport"
                  content="width=device-width, initial-scale=1.0">
            <title>WebSocket App</title>
        </head>
        <body>
            <h1>WebSocket App</h1>
        </body>
        </html>
        """
    )


async def websocket_endpoint(websocket):
    """
    Accept a WebSocket connection and echo text messages.
    """
    await websocket.accept()

    try:
        while True:
            message = await websocket.receive_text()
            await websocket.send_text(message)
    except WebSocketDisconnect:
        pass


app = Starlette(
    routes=[
        Route("/", homepage),
        WebSocketRoute("/ws", websocket_endpoint),
    ]
)
