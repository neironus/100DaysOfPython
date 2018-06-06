import threading
import time
import requests
from flask import Flask, render_template, jsonify, request, redirect, url_for
import twitch

app = Flask(__name__)
app.config.from_object('config')


@app.before_first_request
def run_twitch():
    twitch.init_twitch_connexion()
    thread = threading.Thread(target=twitch.get_messages)

    thread.start()


# Check when server is ready then connect to irc
def start_runner():
    def start_loop():
        not_started = True
        while not_started:
            try:
                r = requests.get('http://127.0.0.1:5000')

                if r.status_code == 200:
                    not_started = False
                time.sleep(2)
            except:
                pass
    thread = threading.Thread(target=start_loop)
    thread.start()


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        username = request.form['username']
        return redirect(url_for('view', username=username))

    return render_template('index.html')


@app.route('/<string:username>', methods=['GET'])
def view(username):
    twitch.join_channel('#' + username)
    return render_template('view.html', username=username)


@app.route('/msg/<string:username>', methods=['GET'])
def msg(username):
    username = '#'+username

    if username in twitch.channels_dict:
        channel = twitch.channels_dict.get(username)
        return jsonify(channel.get_messages())
    else:
        return 'Not found'


def main():
    start_runner()
    app.run()


if __name__ == '__main__':
    main()
