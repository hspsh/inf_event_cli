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


def found_msgs_with_like_from_klara():
    msg_history = read_wydarzenia_channel()
    msg_history = msg_history['messages']
    results = []
    events_owners = []
    for row in msg_history:
        try:
            if klara in row['reactions'][0]['users']:
                if row['reactions'][0]['name'] == '+1':
                    print('founded klara')
                    results.append(row)
        except KeyError:
            pass
    return results, events_owners

# WIP, waiting for second event with Klara like to be able to do good testing.
def search_for_msgs_with_new_events():
    msgs = found_msgs_with_like_from_klara()[0]
    keywords = ['Kiedy', 'Tytuł', 'Opis']
    print(msgs)
    msgs[0]
    indx = 0
    for msg in msgs:
        print(indx, msg)
        indx += 1

if __name__ == '__main__':
    search_for_msgs_with_new_events()


