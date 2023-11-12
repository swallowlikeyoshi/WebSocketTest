from flask import Flask
from flask_socketio import SocketIO

socket_io = SocketIO(logger = True, engineio_logger = True, cors_allowed_origins = '*')

def create_app(is_debug = False):
    app = Flask(__name__)
    app.debug = is_debug
    app.config['SECRET_KEY'] = '😍😍😍😍😍'

    socket_io.init_app(app)

    from app.events import Chat
    socket_io.on_namespace(Chat('/chat'))

    from app.routes import main
    app.register_blueprint(main)

    return app