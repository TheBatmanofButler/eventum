from app.models import Event
from mongoengine import connect
from jinja2 import Environment, PackageLoader
import datetime

def generate_events_email(emails_path):

	connect('eventum')

	today_weekday = datetime.date.today().weekday()

	date_start = datetime.date.today()-datetime.timedelta(today_weekday+1)
	print date_start, date_start+datetime.timedelta(7)

	events = []
	for each_event in Event.objects():
		if date_start <= each_event.start_date <= date_start+datetime.timedelta(7):
			events.append(each_event)

	env = Environment(loader=PackageLoader('app', 'templates'))
	template = env.get_template('email/weekly.html')

	print template.render(events=events) 