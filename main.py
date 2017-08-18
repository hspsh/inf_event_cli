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

if __name__ == '__main__':
    main()
