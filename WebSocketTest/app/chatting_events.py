from flask import session
from flask_socketio import emit, join_room, leave_room, Namespace
from datetime import datetime
from app import chatting_DB

class Chat(Namespace):

    def _make_session_info_dict():
        session_info = dict()
        data_set = { 'name', 'room', 'ip', 'User-Agent', 'cookie' }
        for name in data_set:
            session_info[name] = session.get(name, '')
        return session_info

    def on_connect(self):
        session_info = Chat._make_session_info_dict()
        chatting_DB.users(session_info, isOnline = True)
        pass

    def on_disconnect(self):
        session_info = Chat._make_session_info_dict()
        chatting_DB.users(session_info, isOnline = False)
        pass

    def on_joined(self, date):
        room = session.get('room')
        join_room(room)
        emit('status', { 'sent_message': '<' + str(session.get('name')) + '>: 입장'}, room = room)

    def on_text(self, data):
        room = session.get('room')
        print('<' + str(session.get('name')) + '>: ' + data['message'])
        session_info = Chat._make_session_info_dict()
        to_client = {
            'session_name': session_info['name'],
            'session_room': session_info['room'],
            'date': str(datetime.now().date()),
            'time': str(datetime.now().time()),
            'sent_message': str(data['message'])
        }
        emit('message', to_client, room = room)
        chatting_DB.texts(session_info, data['message'])

    def on_left(self, data):
        room = session.get('room')
        leave_room(room)
        emit('status', { 'sent_message': '<' + str(session.get('name')) + '> 퇴장'}, room = room)