import click
from utility import readYAML
from core import createEvent

@click.group()
def main():
    pass

@main.command()
@click.argument('event_file')
def add(event_file):
    eventData = readYAML(event_file)
    createEvent(eventData)

import subprocess

def _exec(command):
    subprocess.run(command, shell=True, check=True)

@main.command()
@click.argument('key')
def auth(key):
    _exec('echo "{}" > config/apikey.txt'.format(key))


if __name__ == '__main__':
    main()
