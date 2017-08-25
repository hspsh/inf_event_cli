import click
from utility import readYAML
from core import createEvent

@click.group()
def main():
    """Event CLI for Tricity Hackerspace

    Now go! Add some events!
    """
    pass

@main.command()
@click.argument('event_file', metavar='<file.yml>')
@click.option('--dev', is_flag=True, help="Uses Meetup Testing API group, insted of target group.")
def add(event_file, dev):
    """Publishes event on Meetup"""
    eventData = readYAML(event_file)
    createEvent(eventData, dev)

@main.command()
@click.argument('key')
def auth(key):
    """Authenticates app with Meetup API key"""
    with open('config/apikey.txt', 'w') as file:
        file.write(key)


if __name__ == '__main__':
    main()
