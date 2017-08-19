import meetup.api
from datetime import datetime, timedelta
from config import target

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

# TODO not7cd: Move to utility?
# NOTE not7cd: convertTime -> datetime2milliseconds -> dt2ms, najdłuższa nazwa w mieście
def dt2ms(dt):
    """Converts datetime to milliseconds"""
    # TODO not7cd: better timezone handling?
    # account for timezone difference
    dt += timedelta(hours=6)
    ms = int(dt.timestamp() * 1000)
    return ms

def td2ms(td):
    """Converts timedelta to milliseconds"""
    ms = int(td.total_seconds() * 1000)
    return ms


def createEvent(eventData, isDev):
    apiKey = _importAPIKey()
    client = _initClient(apiKey)
    targetData = _initTargetData(client, isDev)

    eventData['time'] = dt2ms(eventData['time'])

    client.CreateEvent(** targetData, **eventData)

if __name__ == '__main__':
    test_time = datetime.now()
    print(dt2ms(test_time))
