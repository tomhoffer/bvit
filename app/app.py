import socket

from flask import Flask, Response

app = Flask(__name__)
hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)


@app.route('/')
def hello_world():
    resp = Response("Hello from " + local_ip)
    resp.headers['Cache-Control'] = 'max-age=604800'
    return resp


if __name__ == '__main__':
    app.run()
