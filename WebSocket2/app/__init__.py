from flask import Flask
from flask_socketio import SocketIO

socketio = SocketIO(logger=True, engineio_logger=True, cors_allowed_origins='*')


def create_app(debug=False):
    """Create an application."""
    app = Flask(__name__)
    app.debug = debug
    app.config['SECRET_KEY'] = 'hard to guess...'

    socketio.init_app(app)
    
    from app.events import ChatNamepsace
    socketio.on_namespace(ChatNamepsace('/chat'))

    from app.routes import main as main_blueprint
    app.register_blueprint(main_blueprint)

    
    return app