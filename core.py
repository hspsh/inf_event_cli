import meetup.api
from datetime import datetime
from config import target

def _importAPIKey():
    with open('config/apikey.txt', 'r') as file:
        key = file.readline()
        # trimms newline character
        key = key[:-1]

    return key


def _initClient(apiKey):
    return meetup.api.Client(apiKey)


def _initTargetData(client):
    _data = {}

    _data['group_urlname'] = target.URL_NAME

    group_info = client.GetGroup(urlname=_data['group_urlname'])
    _data['group_id'] = group_info.id

    _data['venue_id'] = target.VENUE

    return _data


def convertTime(time):
    timestamp = int(time.timestamp() * 1000)

    # account for timezone difference
    timestamp += 6 * 3600 * 1000

    return timestamp


def createEvent(eventData):
    apiKey = _importAPIKey()
    client = _initClient(apiKey)
    targetData = _initTargetData(client)

    eventData['time'] = convertTime(eventData['time'])

    client.CreateEvent(** targetData, **eventData)
