from datetime import timedelta, timezone

def meetup_time(dt):
    """Converts time to format accepted by meetup API"""
    # Account for meetup server location... WTF
    # TODO not7cd: better timezone handling?
    # Since we except dt to be in local tz (CEST for Gdańsk)
    # If meetup is in ETC, this should do the trick
    # TODO: Test meetup API for time
    meetup_tz = timezone(-timedelta(hours=4))
    # meetup_tz = timezone.utc
    meetup_dt = dt.replace(tzinfo=meetup_tz)

    result = datetime2ms(meetup_dt)
    return {'time': result}

def meetup_duration(td):
    """Converts duration to format accepted by meetup API"""
    result = timedelta2ms(td)
    return {'duration': result}



def datetime2ms(dt):
    """Converts datetime to milliseconds"""
    ms = int(dt.timestamp() * 1000)
    return ms

def timedelta2ms(td):
    """Converts timedelta to milliseconds"""
    ms = int(td.total_seconds() * 1000)
    return ms
