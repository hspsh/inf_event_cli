from datetime import timedelta, timezone

def meetup_time(dt):
    """Converts time to format accepted by meetup API"""
    # Account for meetup server location... WTF
    pass
def meetup_duration(arg):
    """Converts duration to format accepted by meetup API"""
    pass

def datetime2ms(dt):
    """Converts datetime to milliseconds"""
    # TODO allgreed: better timezone handling?
    # account for timezone difference
    # dt = dt.replace(tzinfo=timezone.utc).timestamp()
    # dt += timedelta(hours=4)

    ms = int(dt.timestamp() * 1000)
    return ms

def timedelta2ms(td):
    """Converts timedelta to milliseconds"""
    ms = int(td.total_seconds() * 1000)
    return ms
