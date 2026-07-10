#!/usr/bin/env python3
"""
Simple WebSocket client.

"""

import asyncio
import websockets


async def main():
    """
    Connect to the WebSocket server, send one message,
    receive the response, and print it.
    """
    uri = "ws://localhost:8765"

    async with websockets.connect(uri) as websocket:
        await websocket.send("Hello WebSocket")
        response = await websocket.recv()
        print(response)


if __name__ == "__main__":
    asyncio.run(main())
