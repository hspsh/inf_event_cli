import logging
from datetime import timedelta, timezone, datetime
logger = logging.getLogger(__name__)

# Nowy York xD
MEETUP_TZ = timezone(-timedelta(hours=4))
# CEST
HS_TZ = timezone(timedelta(hours=2))

def meetup_time(dt):
    """Converts time to format accepted by meetup API"""
    # Account for meetup server location... WTF
    # TODO not7cd: better timezone handling?
    # Since we except dt to be in local tz (CEST for Gdańsk)
    # If meetup is in ETC, this should do the trick
    # TODO: Test meetup API for time
    # make original datetime
    # meetup_tz = timezone.utc
    # meetup_dt = dt.astimezone(tz=MEETUP_TZ)
    # meetup_dt = dt.replace(tzinfo=MEETUP_TZ)
    # logger.debug(meetup_dt)

    # logger.debug((meetup_dt.astimezone(tz=timezone.utc)))

    logger.debug("%s, %s" % (dt, dt.timestamp()))
    logger.info('change timezone')
    dt = dt.replace(tzinfo=HS_TZ)
    logger.debug("%s, %s" % (dt, dt.timestamp()))
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
