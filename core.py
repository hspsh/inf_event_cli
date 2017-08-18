import meetup.api
from datetime import datetime

apiKey = '[insert api key here]'
requiredData = {'group_urlname':'Meetup-API-Testing'}


def _initClient(apiKey):
    return meetup.api.Client(apiKey)


def convertTime(time):
    timestamp = int(time.timestamp() * 1000)

    # account for timezone difference
    timestamp += 6 * 3600 * 1000

    return timestamp


def createEvent(eventData):
    client = _initClient(apiKey)
    group_info = client.GetGroup(urlname=requiredData['group_urlname'])
    requiredData['group_id'] = group_info.id

    eventData['time'] = convertTime(eventData['time'])

    client.CreateEvent(** requiredData, **eventData, venue_id=25186630)
