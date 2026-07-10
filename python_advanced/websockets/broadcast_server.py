#!/usr/bin/env python3
"""
WebSocket broadcast server.

Each message received from a client is sent to every connected client.
"""

import asyncio
import websockets
from websockets.exceptions import ConnectionClosed


connected_clients = set()


async def connection_handler(websocket):
    """
    Register a client, broadcast its messages, then unregister it.
    """
    connected_clients.add(websocket)

    try:
        async for message in websocket:
            response = f"B:{message}"

            for client in connected_clients.copy():
                await client.send(response)
    except ConnectionClosed:
        pass
    finally:
        connected_clients.discard(websocket)


async def main():
    """
    Start the WebSocket broadcast server.
    """
    async with websockets.serve(
        connection_handler,
        "localhost",
        8765
    ):
        await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())
