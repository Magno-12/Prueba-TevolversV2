from os import environ
from redis import Redis
import json
from win10toast import ToastNotifier

stream_key = environ.get("STREAM", "metrics")

def connect_to_redis():
    hostname = environ.get("REDIS_HOSTNAME", "localhost")
    port = environ.get("REDIS_PORT", 6379)

    r = Redis(hostname, port, retry_on_timeout=True)
    return r

def get_data(redis_connection):
    last_id = 0
    sleep_ms = 5000
    toaster = ToastNotifier()
    while True:
        try:
            resp = redis_connection.xread(
                {stream_key: last_id}, count=1, block=sleep_ms
            )
            if resp:
                key, messages = resp[0]
                last_id, data = messages[0]
                result = {k.decode("utf-8"): data[k].decode("utf-8") for k in data}
                metricComplete = result['metric']
                metricValue = int(metricComplete.split(" ")[0])
                if metricValue > 95:
                    toaster.show_toast(
                            "Alarma",
                            "Cuidado, recibimos una metrica de "+metricComplete,
                            duration=0.5
                        )

                print("REDIS ID: ", last_id)
                print("      --> ", data)


        except ConnectionError as e:
            print("ERROR REDIS CONNECTION: {}".format(e))


if __name__ == "__main__":
    connection = connect_to_redis()
    get_data(connection)