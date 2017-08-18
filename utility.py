import yaml

def readYAML(filename):
    with open(filename, 'r') as stream:
        try:
            parsedData = (yaml.load(stream))
            return parsedData
        except yaml.YAMLError as exc:
            print(exc)
