from flask import session, redirect, url_for, render_template, request, Blueprint

chatting = Blueprint('chatting', __name__, url_prefix='/chat')

@chatting.route('/lobby', methods = ['GET', 'POST'])
def chatting_lobby():
    if request.method == 'POST':
        session['name'] = request.form['name']
        session['room'] = 1
        # session['user_ip'] = request.remote_addr
        # print('-----------------------------------') # 유사시 사용 가능할 듯
        # print(request.form['name'])
        # print(request.headers.get('User-Agent'))
        # print(request.cookies.get('user_cookie_name'))
        # print(request.url)
        # print(request.method)
        # print(request.remote_addr)
        # print('-----------------------------------')
        return redirect(url_for('chatting.chatting_room'))
    return render_template('chatting_lobby.html')

@chatting.route('/room')
def chatting_room():
    user_name = session.get('name', '')
    room = session.get('room', '')

    if user_name == '' or room == '':
        return redirect(url_for('.chatting_lobby'))
    
    return render_template('chatting_room.html', name = user_name, room = room)