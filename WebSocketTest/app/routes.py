from flask import session, redirect, url_for, render_template, request, Blueprint

main = Blueprint('main', __name__)

@main.route('/', methods = ['GET', 'POST'])
def index():
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
        return redirect(url_for('main.chat'))
    return render_template('index.html')

@main.route('/chat')
def chat():
    user_name = session.get('name', '')
    room = session.get('room', '')

    if user_name == '' or room == '':
        return redirect(url_for('.index'))
    
    return render_template('chat.html', name = user_name, room = room)