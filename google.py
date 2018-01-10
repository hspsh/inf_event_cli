from __future__ import print_function
import httplib2
import os

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage


try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

SCOPES = 'https://www.googleapis.com/auth/calendar'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'HS Calendar'


def get_credentials():
    """Gets valid user credentials from storage.

    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.

    Returns:
        Credentials, the obtained credential.
    """
    home_dir = os.path.curdir
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,
                                   'google-calendar-hackerspace-credentials.json')

    store = Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else: # Needed only for compatibility with Python 2.6
            credentials = tools.run(flow, store)
        print('Storing credentials to ' + credential_path)
    return credentials


def add_google_calendar_event(service, summary, description, start, end, recurrence=None, location='Hackerspace Trójmiasto'):
    """
    Small function to add events using google API. For further development. Mainly recurrence param.
    :param service: Google API client
    :param summary: Event title string
    :param location: Default: 'Hackerspace Trójmiasto'
    :param description: String
    :param start: {
            'dateTime': '2018-01-28T09:00:00-07:00',
            'timeZone': 'Europe/Warsaw',
        }
    :param end: {
            'dateTime': '2018-01-28T17:00:00-07:00',
            'timeZone': 'Europe/Warsaw',
        }
    :param recurrence: For further development. Ex: recurrence = ['RRULE:FREQ=DAILY;COUNT=2']
    :return: None
    """
    event = {
        'summary': summary,
        'location': location,
        'description': description,
        'start': start,
        'end': end,
        'recurrence': recurrence,
    }

    event = service.events().insert(calendarId='8s96dmhr9qv1akadn3b2el9kk8@group.calendar.google.com', body=event).execute()
    print('Event created: %s' % (event.get('htmlLink')))


def main():
    """Shows basic usage of the Google Calendar API.

    Creates a Google Calendar API service object and outputs a list of the next
    10 events on the user's calendar.
    """
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('calendar', 'v3', http=http)

    summary = 'Google I/O 2015'
    description = 'A chance to hear more about Google\'s developer products.'
    start = {
            'dateTime': '2018-01-28T09:00:00-07:00',
            'timeZone': 'Europe/Warsaw',
        }
    end = {
            'dateTime': '2018-01-28T17:00:00-07:00',
            'timeZone': 'Europe/Warsaw',
        }

    add_google_calendar_event(service, summary, description, start, end)


if __name__ == '__main__':
    main()
