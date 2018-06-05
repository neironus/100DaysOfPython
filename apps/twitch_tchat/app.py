import threading
import time
import requests
from flask import Flask, render_template
import t

app = Flask(__name__)
app.config.from_object('config')


@app.before_first_request
def run_twitch():
    t.init_twitch_connexion()
    thread = threading.Thread(target=t.get_messages)

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


@app.route('/', methods=['GET'])
def index():
    return 'Hello world'


@app.route('/<string:username>', methods=['GET'])
def view(username):
    t.join_channel('#'+username)
    return username


@app.route('/msg/<string:username>', methods=['GET'])
def lol(username):
    username = '#'+username
    if username in t.channels_dict:
        channel = t.channels_dict.get(username)
        return render_template('messages.html', messages=channel.messages)
    else:
        return 'Not found'


def main():
    start_runner()
    app.run()


if __name__ == '__main__':
    main()
