import meetup.api
from datetime import datetime, timedelta
from config import target
from timeutils import meetup_time, meetup_duration

def _importAPIKey():
    with open('config/apikey.txt', 'r') as file:
        key = file.readline()
        # trimms newline character
        key = key[:-1]

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

# not7cd: is it updating?
def update_event_data(data):
    """Updates event data to be compatible with meetup API"""
    data.update(meetup_time(data['time']))
    if 'duration' in data:
        data.update(meetup_duration(data['duration']))
    return data

def createEvent(eventData, isDev):
    apiKey = _importAPIKey()
    client = _initClient(apiKey)
    targetData = _initTargetData(client, isDev)

    eventData = update_event_data(eventData)

    client.CreateEvent(** targetData, **eventData)

if __name__ == '__main__':
    test_time = datetime.now()
    print(meetup_time(test_time))
