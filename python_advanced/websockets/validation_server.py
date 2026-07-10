#!/usr/bin/env python3
"""
WebSocket server with basic message validation.

"""

import asyncio
import websockets


async def validate_message(websocket):
    """
    Handle a WebSocket connection and validate each received message.

    """
    async for message in websocket:
        if message.strip() == "":
            await websocket.send("ERR:EMPTY")
        else:
            await websocket.send(f"OK:{message}")


async def main():
    """
    Start the WebSocket validation server.
    
    """
    async with websockets.serve(validate_message, "localhost", 8765):
        await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())
