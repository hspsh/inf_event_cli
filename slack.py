#!/usr/bin/python
# -*- coding: utf-8 -*-
from slackclient import SlackClient


def _import_api_key():
    with open('.credentials/slack_key.txt', 'r') as file:
        key = file.readline().strip()

    return key


def _import_klara_id():
    with open('.credentials/slack_klara_id.txt', 'r') as file:
        key = file.readline().strip()

    return key


def _import_wydarzenia_id():
    with open('.credentials/slack_wydarzenia_id.txt', 'r') as file:
        key = file.readline().strip()

    return key


slack_token = _import_api_key()
klara = _import_klara_id()
wydarzenia = _import_wydarzenia_id()
sc = SlackClient(slack_token)


def read_wydarzenia_channel():
    return sc.api_call(
        "channels.history",
        channel=wydarzenia,
        unreads='true',
    )

def search_for_msgs_with_new_events():
    msg_history = read_wydarzenia_channel()
    print(msg_history)
    for msg in msg_history:
        print(msg)


if __name__ == '__main__':
    search_for_msgs_with_new_events()


