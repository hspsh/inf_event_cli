import logging
from datetime import datetime
import click
from utility import readYAML
from core import create_event

@click.group()
def main():
    logging.basicConfig(filename='inf_event_cli.log', level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    logging.info('start')

@main.command()
@click.argument('event_file', metavar='<file.yml>')
@click.option('--dev', is_flag=True, help="Uses Meetup Testing API group, insted of target group.")
def add(event_file, dev):
    """Publishes event on Meetup"""
    event_data = readYAML(event_file)
    create_event(event_data, dev)

@main.command()
@click.argument('key')
def auth(key):
    """Authenticates app with Meetup API key"""
    with open('config/apikey.txt', 'w') as file:
        file.write(key)


if __name__ == '__main__':
    main()
