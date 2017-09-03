import logging
import meetup.api
from datetime import datetime, timedelta
from config import target
from timeutils import meetup_time, meetup_duration

logger = logging.getLogger(__name__)


def _importAPIKey():
    with open('config/apikey.txt', 'r') as file:
        key = file.readline().strip()

    return key


def _initClient(apiKey):
    return meetup.api.Client(apiKey)


def _initTargetData(client, isDev):
    """Returns dict of parameters for request target"""
    _data = {}

    _data['group_urlname'] = target.URL_NAME

    if isDev:
        _data['group_urlname'] = "Meetup-API-Testing"

    group_info = client.GetGroup(urlname=_data['group_urlname'])
    _data['group_id'] = group_info.id

    _data['venue_id'] = target.VENUE

    return _data



def update_event_data(data):
    # not7cd: is it updating?
    """Updates event data to be compatible with meetup API"""
    data.update(meetup_time(data['time']))
    if 'duration' in data:
        data.update(meetup_duration(data['duration']))
    return data


def create_event(event_data, is_dev):
    """Sends request to meetup to create event with given event_data"""

    logger.info('create meetup client')
    api_key = _importAPIKey()
    client = _initClient(api_key)

    logger.info('create request parameters')
    target_data = _initTargetData(client, is_dev)

    logger.debug(event_data)
    event_data = update_event_data(event_data)

    request_parameters = {**event_data, **target_data}
    logger.debug(request_parameters)

    logger.info('send request')
    client.create_event(**request_parameters)
