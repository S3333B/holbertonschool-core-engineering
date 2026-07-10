#!/usr/bin/env python3
"""
WebSocket validation server.

The server validates incoming messages and responds with:
- ERR:EMPTY for empty messages
- OK:{message} for valid messages
"""

import asyncio
import websockets
from websockets.exceptions import ConnectionClosed


async def connection_handler(websocket):
    """
    Handle a WebSocket connection and validate incoming messages.
    """
    try:
        async for message in websocket:
            if message.strip() == "":
                await websocket.send("ERR:EMPTY")
            else:
                await websocket.send(f"OK:{message}")
    except ConnectionClosed:
        pass


async def main():
    """
    Start the WebSocket validation server.
    """
    async with websockets.serve(connection_handler, "localhost", 8765):
        await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())
