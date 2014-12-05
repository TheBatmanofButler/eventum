import argparse
from oauth2client import tools
from oauth2client.client import flow_from_clientsecrets
from config import flask_config

parser = argparse.ArgumentParser(parents=[tools.argparser])
FLAGS = parser.parse_args()

def authorize_google_calendar():
    FLOW = flow_from_clientsecrets(flask_config.INSTALLED_APP_SECRET_PATH,
                   scope='https://www.googleapis.com/auth/calendar')

    # Save the credentials file here for use by the app
    storage = Storage(flask_config.INSTALLED_APP_CREDENTIALS_PATH)
    run_flow(FLOW, storage, FLAGS)

def print_usage():
    print "Usage:"
    print "%s --authorize (-a)     Authorize the Google Calendar API Client" % argv[0]

if __name__ == '__main__':
    authorize_google_calendar()
