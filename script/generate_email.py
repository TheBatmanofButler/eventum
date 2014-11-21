from app.models import Event
from mongoengine import connect
from jinja2 import Environment, PackageLoader
import datetime

def generate_events_email(emails_path):

	connect('eventum')

	events = Event.objects()
	# .filter(start_date=[datetime.date.today(), datetime.date.today() + datetime.timedelta(days=7)])

	env = Environment(loader=PackageLoader('app', 'templates'))
	template = env.get_template('email/weekly.html')

	print template.render(events=events)