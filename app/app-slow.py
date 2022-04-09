import random
import socket
import time

from flask import Flask, Response

app = Flask(__name__)
hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)


@app.route('/')
def hello_world():
    resp = Response("Hello from " + local_ip)
    if bool(random.getrandbits(1)):
        time.sleep(0.5)
    return resp


if __name__ == '__main__':
    app.run()
