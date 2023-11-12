from flask import Flask, render_template
from flask_socketio import SocketIO, send

app = Flask(__name__)
socket_io = SocketIO(app, cors_allowed_origins='*')

@app.route('/')
def index():
    return "WebSocket Test"

@app.route('/chat')
def chat():
    return render_template('chat.html')

@socket_io.on('login')
def login(message_from_client):
    print('login request from "' + message_from_client +'"')

@socket_io.on('message')
def request(message_from_client):
    print(type(message_from_client))
    print('message: ' + str(message_from_client))

    message_to_client = dict()

    if message_from_client == 'freshman':
        message_to_client['message'] = '새 유저 입장'
        message_to_client['type'] = 'freshman'
    else:
        message_to_client['message'] = message_from_client
        message_to_client['type'] = 'text'

    send(message_to_client, broadcast = True)

if __name__ == '__main__':
    socket_io.run(app, debug = True, port = 80)