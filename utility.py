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

# TODO: change function name
def parse_datetime(dt):
    """Creates dict of datetime and duration with meetup compatible keys"""
    if isinstance(dt, str):
        split_dt = dt.split('/')
        print(split_dt)
        meetup_dt = {}
        meetup_dt['time'] = isodate.parse_datetime(split_dt[0])
        # TODO: try...except duration doesn't exist
        meetup_dt['duration'] = isodate.parse_duration(split_dt[1])
        print(meetup_dt)
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
