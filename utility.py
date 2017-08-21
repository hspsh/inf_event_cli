import yaml

def readYAML(filename):
    """Returns dict of parsed data from file"""
    with open(filename, 'r') as stream:
        try:
            parsed_data = (yaml.load(stream))
            return parsed_data
        except yaml.YAMLError as exc:
            print(exc)
