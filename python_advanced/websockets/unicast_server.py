#!/usr/bin/env python3
"""
WebSocket unicast server.

The server keeps track of connected clients and sends each response
only to the client that sent the message.
"""

import asyncio
import websockets
from websockets.exceptions import ConnectionClosed


connected_clients = set()


async def connection_handler(websocket):
    """
    Handle a WebSocket connection.

    Add the client on connection, process incoming messages,
    send responses only to the sender, and remove the client
    on disconnection.
    """
    connected_clients.add(websocket)

    try:
        async for message in websocket:
            await websocket.send(f"U:{message}")
    except ConnectionClosed:
        pass
    finally:
        connected_clients.remove(websocket)


async def main():
    """
    Start the WebSocket unicast server.
    """
    async with websockets.serve(connection_handler, "localhost", 8765):
        await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())
