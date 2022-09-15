import asyncio
from os import environ

from fastapi import FastAPI
from fastapi import Request
from fastapi import WebSocket
from fastapi.responses import HTMLResponse
from redis import Redis
import websocket
import _thread
import time
import rel

app = FastAPI()

stream_key = environ.get("STREAM", "metrics")
hostname = environ.get("REDIS_HOSTNAME", "localhost")
port = environ.get("REDIS_PORT", 6379)
redis_cli = Redis(hostname, port, retry_on_timeout=True)

html = """
<!DOCTYPE html>
<html>
    <head>
        <title>Listen data</title>
    </head>
    <body>
        <h1>WebSocket</h1>
        <ul id='messages'>
        </ul>
        <script>
            var ws = new WebSocket("ws://localhost:8000/ws");
            ws.onmessage = function(event) {
                var messages = document.getElementById('messages')
                var message = document.createElement('li')
                var content = document.createTextNode(event.data)
                message.appendChild(content)
                messages.appendChild(message)
            };
            function sendMessage(event) {
                var input = document.getElementById("messageText")
                ws.send(input.value)
                input.value = ''
                event.preventDefault()
            }
        </script>
    </body>
</html>
"""

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    """
    TODO:
    - Understand deeply the redis-py.xread method:
      - why we need to send a list of stream? I didn't want get the first [0] element
      - why it returns bytes, Is the .decode a good way?
      - is there a better way to convert it to python dict?
      - what is the a good number for the sleep/block?
    """
    last_id = 0
    sleep_ms = 5000

    await websocket.accept()
    while True:
        #await asyncio.sleep(0.3)
        resp = redis_cli.xread({stream_key: last_id}, count=1, block=sleep_ms)
        print("Waitting...")
        if resp:
            key, messages = resp[0]
            last_id, data = messages[0]

            data_dict = {k.decode("utf-8"): data[k].decode("utf-8") for k in data}
            data_dict["id"] = last_id.decode("utf-8")
            data_dict["key"] = key.decode("utf-8")
            print(data_dict)
            await websocket.send_json(data_dict)

@app.get('/metrics')
async def metrics():
    return HTMLResponse(html)
    