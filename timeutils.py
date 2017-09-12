import logging
from datetime import timedelta, timezone, datetime
logger = logging.getLogger(__name__)

MEETUP_TZ = timezone(timedelta(hours=-4))
HS_TZ = timezone(timedelta(hours=2))

def meetup_time(dt):
    """Converts time to format accepted by meetup API"""
    logger.debug("%s, %s", dt, dt.timestamp())
    logger.info('change timezone')
    dt = dt.replace(tzinfo=HS_TZ)
    logger.debug("%s, %s", dt, dt.timestamp())
    result = datetime2ms(dt)
    return {'time': result}


def meetup_duration(td):
    """Converts duration to format accepted by meetup API"""
    result = timedelta2ms(td)
    return {'duration': result}


def sec2ms(sec):
    return int(sec * 1000)


def datetime2ms(dt):
    """Converts datetime to milliseconds"""
    ms = sec2ms(dt.timestamp())
    return ms


def timedelta2ms(td):
    """Converts timedelta to milliseconds"""
    ms = sec2ms(td.total_seconds())
    return ms
