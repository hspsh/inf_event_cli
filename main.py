import logging

import click

from core import create_event
from utility import read_yaml


@click.group()
def main():
    """Event CLI for Tricity Hackerspace

    Now go! Add some events!
    """
    logging.basicConfig(
        filename='inf_event_cli.log',
        level=logging.DEBUG,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    logging.info('start')


@main.command()
@click.argument('event_file', metavar='<file.yml>')
@click.option(
    '--dev',
    is_flag=True,
    help="Uses Meetup Testing API group, instead of target group."
)
def add(event_file, dev):
    """Publishes event on Meetup"""
    event_data = read_yaml(event_file)
    create_event(event_data, dev)


@main.command()
@click.argument('key')
def auth(key):
    """Authenticates app with Meetup API key"""
    with open('.credentials/apikey.txt', 'w') as file:
        file.write(key)


if __name__ == '__main__':
    main()
