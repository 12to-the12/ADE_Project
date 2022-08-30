#!/usr/bin/env python

import asyncio
import websockets
print('status')
async def send_message(websocket, path):
    while True:
        await websocket.send('surfstation')
        print('running')
        await asyncio.sleep(1)

start_server = websockets.serve(send_message, '192.168.0.226', 12123)
print('status')
asyncio.get_event_loop().run_until_complete(start_server)
print('status')
asyncio.get_event_loop().run_forever()

