import socket
from flask import Flask

app = Flask(__name__)
hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)

@app.route('/')
def hello_world():  # put application's code here
    return "Hello from " + local_ip


if __name__ == '__main__':
    app.run()
