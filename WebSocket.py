from flask import Flask, jsonify, render_template
from subprocess import call
from flask_socketio import SocketIO, send

app = Flask(__name__)
app.secret_key = "mysecret"

socket_io = SocketIO(app, cors_allowed_origins='*')

@app.route('/')
def index():
    return "root directory"

@app.route('/chat')
def chat():
    return render_template('chat.html')

@socket_io.on('message')
def request(message):
    print(type(message))
    print("message: " + str(message))
    to_client = dict()
    if message == "new_connect":
        to_client['message'] = "새로운 유저 등장"
        to_client['type'] = 'connect'
    else:
        to_client['message'] = message
        to_client['type'] = 'normal'
    send(to_client, broadcast = True)

if __name__ == '__main__':
    socket_io.run(app, debug = True, port = 80)