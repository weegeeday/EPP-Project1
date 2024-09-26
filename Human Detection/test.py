import asyncio

from websockets.asyncio.client import connect

async def hello():
    uri = "ws://localhost:8765"
    async with connect(uri) as websocket:

        greeting = await websocket.recv()
        print(greeting)

if __name__ == "__main__":
    asyncio.run(hello())