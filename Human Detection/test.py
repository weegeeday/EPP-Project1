import asyncio
import websockets

async def read_websocket(uri):
    async with websockets.connect(uri) as websocket:
        while True:
            message = await websocket.recv()
            print(f"Received message: {message}")

if __name__ == "__main__":
    uri = "ws://localhost:8765"  # Replace with your WebSocket server URI
    asyncio.get_event_loop().run_until_complete(read_websocket(uri))