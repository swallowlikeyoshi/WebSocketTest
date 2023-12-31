from flask import session, redirect, url_for, render_template, request, Blueprint
from datetime import datetime

chatting = Blueprint('chatting', __name__, url_prefix='/chat')

@chatting.route('/lobby', methods = ['GET', 'POST'])
def chatting_lobby():
    if request.method == 'POST':
        # session =  ( 'name', 'room', 'datetime', 'headers' )
        session['name'] = request.form['name']
        session['room'] = 1
        session['datetime'] = datetime.now()
        session['headers'] = str(request.headers)
        return redirect(url_for('chatting.chatting_room'))
    return render_template('chatting_lobby.html')

@chatting.route('/room')
def chatting_room():
    user_name = session.get('name', '')
    room = session.get('room', '')

    if user_name == '' or room == '':
        return redirect(url_for('.chatting_lobby'))
    
    return render_template('chatting_room.html', name = user_name, room = room)