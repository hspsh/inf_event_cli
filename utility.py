import yaml
from datetime import time, timedelta
import isodate

def readYAML(filename):
    with open(filename, 'r') as stream:
        try:
            parsedData = (yaml.load(stream))
            return parsedData
        except yaml.YAMLError as exc:
            print(exc)

# NOTE: This is step backwards in converting yaml data to meetup api request
def dict2iso_interval(yaml_dt):
    """Returns one of:
    (<start>)
    (<start>, <end>)
    (<start>, <duration>)
    (<duration>, <end>) <=> (<end> - <duration>/<duration>)
    """

    try:
        _start = isodate.parse_datetime(yaml_dt['start'])
    except KeyError:
        try:
            _duration = isodate.parse_duration(yaml_dt['duration'])
            _end = isodate.parse_datetime(yaml_dt['end'])
            intervals = (_duration, _end)
            # intervals = (_end - _duration, _duration)
        except KeyError:
            raise
    else:
        if 'duration' in yaml_dt:
            _duration = isodate.parse_duration(yaml_dt['duration'])
            intervals = (_start, _duration)
        elif 'end' in yaml_dt:
            _end = isodate.parse_datetime(yaml_dt['end'])
            intervals = (_start, _end)
        else:
            intervals = (_start)

    result = intervals
    return result

def parse_iso_interval(arg):
    """Parses ISO time interval notation to dict with meetup compatible keys

    """
    pass

# TODO: change function name
def parse_datetime(raw_dt):
    """Creates dict of datetime and duration with meetup compatible keys"""
    if isinstance(raw_dt, str):
        split_dt = raw_dt.split('/')
        # print(split_dt)
        _time = split_dt[0]
        _duration = split_dt[1]

    elif isinstance(raw_dt, dict):
        # TODO: check if there is at least one point in time
        if 'start' in raw_dt and 'end' in raw_dt:
            _time = raw_dt['start']
            _duration = raw_dt['end'] - raw_dt['start']
        elif 'duration' in raw_dt:
            if 'start' in raw_dt:
                _time = raw_dt['start']
                _duration = raw_dt['duration']
            else:
                _time = raw_dt['end'] - raw_dt['duration']
                _duration = raw_dt['duration']
        else:
            try:
                _time = raw_dt['start']
            except Exception: # TODO: Exception too general
                raise

    # NOTE: This can go to separate function
    meetup_dt = {}

    meetup_dt['time'] = isodate.parse_datetime(_time)
    try:
        meetup_dt['duration'] = isodate.parse_duration(_duration)
    except KeyError:
        pass

    return meetup_dt
# tests
if __name__ == '__main__':
    short = """
---
name: "Your event name"
description: "What will happen at your event and why people should come"
time: 2017-08-20 18:00:00
datetime: 2017-08-20T18:00:00/PT3H
    """

    parsed_yaml = yaml.load(short)
    print(parsed_yaml)
    parsed_time = parse_datetime(parsed_yaml['datetime'])
    parsed_yaml.update(parsed_time)
    print(parsed_yaml)
