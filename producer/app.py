from os import environ
from redis import Redis
from uuid import uuid4
from time import sleep
import random
import time

stream_key = environ.get("STREAM", "metrics")
producer = environ.get("PRODUCER", "user-admin")
MAX_MESSAGES = int(environ.get("MESSAGES", "2"))

def connect_to_redis():
    hostname = environ.get("REDIS_HOSTNAME", "localhost")
    port = environ.get("REDIS_PORT", 6379)

    r = Redis(hostname, port, retry_on_timeout=True)
    return r

def send_data(redis_connection, max_messages):
    device_id = uuid4().time
    while True:
        try:
            data = {
                "id": uuid4().hex,
                "device_id": device_id,  # Just some random data
                "metric": str(random.randint(10, 100)) + " kmg",
                "timestamp": int(time.time())
            }
            resp = redis_connection.xadd(stream_key, data)
            print(data)

        except ConnectionError as e:
            print("ERROR REDIS CONNECTION: {}".format(e))

        sleep(0.5)

if __name__ == "__main__":
    connection = connect_to_redis()
    send_data(connection, MAX_MESSAGES)