import socket
import threading

import config as cfg
import re

s = socket.socket()
channels_dict = {}
channels_list = []


class Channel(object):

    def __init__(self, name):
        self.name = name
        self.messages = []

    def join(self):
        send_to_socket('join', self.name)

    def add_message(self, message):
        print('> message added')
        self.messages.append(message)


def send_to_socket(cmd, text):
    global s
    s.send(bytes(
        '{} {} \r\n'.format(cmd.upper(), text),
        'UTF-8'
    ))


def init_twitch_connexion():
    global s
    s.connect(
        (cfg.TWITCH.get('server'), cfg.TWITCH.get('port'))
    )
    send_to_socket('pass', cfg.TWITCH.get('password'))
    send_to_socket('user', cfg.TWITCH.get('nickname'))
    send_to_socket('nick', cfg.TWITCH.get('nickname'))
    # send_to_socket(s, 'join', '#soexit')


def join_channel(channel):
    if not channel.startswith('#'):
        channel = '#' + channel

    channel = Channel(name=channel)

    if len(channels_list) >= 5:
        c = channels_list.pop(0)
        channels_dict.pop(c.name)
        send_to_socket('part', c.name)

    channels_dict[channel.name] = channel
    channels_list.append(channel.name)

    send_to_socket('join', channel.name)


def get_messages():
    while True:
        line = str(s.recv(1024))
        parts = line.split(':')
        if len(parts) < 3:
            continue

        # for keyword in ignore_keyword:
        #     if keyword in parts[1]:
        #         continue
        # print(parts)
        username = parts[1].split("!")[0]
        message = parts[2]
        message = message[:len(message) - 5]
        channel_name = None
        re_channel = re.match(r'.* PRIVMSG (.+)', parts[1])
        if re_channel:
            channel_name = re_channel.group(1).strip()

        if channel_name:
            channel = channels_dict.get(channel_name)
            channel.add_message('{}> {}'.format(username, message))


if __name__ == '__main__':
    init_twitch_connexion()
    join_channel('lexveldhuis')

    thread = threading.Thread(target=get_messages)
    thread.start()

