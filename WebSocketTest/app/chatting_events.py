from flask import session
from flask_socketio import emit, join_room, leave_room, Namespace
from datetime import datetime

class Chat(Namespace):

    def on_connect(self):
        pass

    def on_disconnect(self):
        pass

    def on_joined(self, date):
        room = session.get('room')
        join_room(room)
        emit('status', { 'sent_message': '<' + str(session.get('name')) + '> 입장'}, room = room)

    def on_text(self, data):
        room = session.get('room')
        print('<' + str(session.get('name')) + '>: ' + data['message'])
        to_client = {
            'session_name': session.get('name', ''),
            'session_room': session.get('room', ''),
            'session_token': session.get('token', ''),
            'date': str(datetime.now().date()),
            'time': str(datetime.now().time()),
            'sent_message': str(data['message'])
        }
        emit('message', to_client, room = room)

    def on_left(self, data):
        room = session.get('room')
        leave_room(room)
        emit('status', { 'sent_message': '<' + str(session.get('name')) + '> 퇴장'}, room = room)