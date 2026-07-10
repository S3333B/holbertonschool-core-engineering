#!/usr/bin/env python3
"""
WebSocket client.

Connects to a WebSocket server, sends one message,
receives one response, and returns it.
"""

import asyncio
import os
import websockets


async def connect_and_send(uri, message):
    """
    Connect to a WebSocket server, send a message,
    receive the response, and return it.
    """
    async with websockets.connect(uri) as websocket:
        await websocket.send(message)
        response = await websocket.recv()
        return response


async def main():
    """
    Run the client using WS_URI when available.
    """
    uri = os.getenv("WS_URI", "ws://localhost:8765")
    response = await connect_and_send(uri, "demo")
    print(response, end="")


if __name__ == "__main__":
    asyncio.run(main())
