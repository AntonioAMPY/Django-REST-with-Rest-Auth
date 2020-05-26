from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
socketio = SocketIO(app, cors_allowed_origins="*")

users = set()


@app.route('/')
def sessions():
    return render_template('index.html')


@socketio.on('join')
def join(data):
    print(data)
    users.add(data['data'])
    emit('join', list(users), broadcast=True)


@socketio.on('leave')
def leave(data):
    users.discard(data['data'])
    emit('leave', list(users), broadcast=True)


if __name__ == '__main__':
    socketio.run(app, debug=True)
