import asyncio
import websockets

async def echo(websocket):
	
  async for message in websocket:
        await websocket.send(message)

async def main():
    """
    Start the WebSocket server.
    """
    async with websockets.serve(echo, "localhost", 8765):
        await asyncio.Future()
        
if __name__ == "__main__":
    asyncio.run(main())
