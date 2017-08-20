import meetup.api
from datetime import datetime
from config import target

def _importAPIKey():
    with open('config/apikey.txt', 'r') as file:
        key = file.readline()
        key = key.strip()

    return key


def _initClient(apiKey):
    return meetup.api.Client(apiKey)


def _initTargetData(client, isDev):
    _data = {}

    _data['group_urlname'] = target.URL_NAME

    if isDev:
        _data['group_urlname'] = "Meetup-API-Testing"

    group_info = client.GetGroup(urlname=_data['group_urlname'])
    _data['group_id'] = group_info.id

    _data['venue_id'] = target.VENUE

    return _data


def convertTime(time):
    timestamp = int(time.timestamp() * 1000)

    # account for timezone difference
    timestamp += 6 * 3600 * 1000

    return timestamp


def createEvent(eventData, isDev):
    apiKey = _importAPIKey()
    client = _initClient(apiKey)
    targetData = _initTargetData(client, isDev)

    eventData['time'] = convertTime(eventData['time'])

    client.CreateEvent(** targetData, **eventData)
