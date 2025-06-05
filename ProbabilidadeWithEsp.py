import asyncio
import websockets

async def handle_esp_32(websocket):
    print("Esp32 conectado com sucesso")
    try:
        async for message in websocket:
            print(f"Recebido de esp32: {message}")
            await websocket.send("mensagem recebida com sucesso")
    except websockets.ConnectionClosed:
        print("Esp32 desconectado")

async def main():
    async with websockets.serve(handle_esp_32, "192.168.0.10", 8765):
        await asyncio.Future()

asyncio.run(main())