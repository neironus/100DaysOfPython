import json
import socket
import threading
import re
import random
from collections import namedtuple

import config as cfg

messageTuple = namedtuple('Message', 'username text color')

s = socket.socket()
channels_dict = {}
channels_list = []


def get_random_color():
    return '#'+''.join([random.choice('ABCDEF0123456789') for _ in range(6)])


class Channel(object):

    def __init__(self, name: str):
        self.name = name
        self.messages = []
        self.users_color = {}

    def join(self) -> None:
        send_to_socket('join', self.name)

    def add_message(self, username: str, message: str) -> None:
        if username in self.users_color:
            color = self.users_color.get(username)
        else:
            color = get_random_color()
            self.users_color[username] = color

        msg = messageTuple(username, message, color)
        self.messages.append(msg)

    def get_messages(self):
        messages = self.messages
        self.messages = []

        return [message._asdict() for message in messages]


def send_to_socket(cmd: str, text: str) -> None:
    global s
    s.send(bytes(
        '{} {} \r\n'.format(cmd.upper(), text),
        'UTF-8'
    ))


def init_twitch_connexion() -> None:
    global s
    s.connect(
        (cfg.TWITCH.get('server'), cfg.TWITCH.get('port'))
    )
    send_to_socket('pass', cfg.TWITCH.get('password'))
    send_to_socket('user', cfg.TWITCH.get('nickname'))
    send_to_socket('nick', cfg.TWITCH.get('nickname'))


def join_channel(channel: str) -> None:
    if not channel.startswith('#'):
        channel = '#' + channel

    if channel in channels_list:
        return

    channel = Channel(name=channel)

    if len(channels_list) >= 5:
        c = channels_list.pop(0)
        channels_dict.pop(c)
        send_to_socket('part', c)

    channels_dict[channel.name] = channel
    channels_list.append(channel.name)

    send_to_socket('join', channel.name)


def get_messages() -> None:
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
            channel.add_message(username, message)


if __name__ == '__main__':
    init_twitch_connexion()
    join_channel('lexveldhuis')

    thread = threading.Thread(target=get_messages)
    thread.start()

