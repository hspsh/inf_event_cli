import meetup.api
from datetime import datetime, timedelta
from config import target
from timeutils import datetime2ms

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




def createEvent(eventData, isDev):
    apiKey = _importAPIKey()
    client = _initClient(apiKey)
    targetData = _initTargetData(client, isDev)

    eventData['time'] = datetime2ms(eventData['time'])

    client.CreateEvent(** targetData, **eventData)

if __name__ == '__main__':
    test_time = datetime.now()
    print(datetime2ms(test_time))
