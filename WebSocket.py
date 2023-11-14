from flask import Flask, render_template, request
from flask_socketio import SocketIO, send

app = Flask(__name__)
socket_io = SocketIO(app, cors_allowed_origins='*')

@app.route('/', methods = ['GET'])
def index():
    print('---------------------')
    print(type(request.headers))
    print(request.headers)
    print()
    print(request.cookies.get('user_cookie_name'))
    print('---------------------')

    # 출력
    # ---------------------
    # <class 'werkzeug.datastructures.headers.EnvironHeaders'>
    # Host: 127.0.0.1
    # Connection: keep-alive
    # Cache-Control: max-age=0
    # Sec-Ch-Ua: "Whale";v="3", "Not-A.Brand";v="8", "Chromium";v="118"
    # Sec-Ch-Ua-Mobile: ?0
    # Sec-Ch-Ua-Platform: "Windows"
    # Upgrade-Insecure-Requests: 1
    # User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Whale/3.23.214.10 Safari/537.36
    # Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
    # Sec-Fetch-Site: none
    # Sec-Fetch-Mode: navigate
    # Sec-Fetch-User: ?1
    # Sec-Fetch-Dest: document
    # Accept-Encoding: gzip, deflate, br
    # Accept-Language: ko,en-US;q=0.9,en;q=0.8,ko-KR;q=0.7



    # None
    # ---------------------
    return "WebSocket Test"

@app.route('/chat')
def chat():
    return render_template('chat.html')

@socket_io.on('login')
def login(message_from_client):
    print('login request from "' + message_from_client +'"')

@socket_io.on('message')
def arequest(message_from_client):
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