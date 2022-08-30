#!/usr/bin/env python

import asyncio
import random
import websockets
print('status')
async def time(websocket, path):
    while True:
        await websocket.send('hi')
        print('xxx')
        await asyncio.sleep(random.random() * 3)

start_server = websockets.serve(time, '127.0.0.1', 12123)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()

