#!/usr/bin/python3
import postgresql
import json
import sys
import datetime
from icalendar import Event

class Generator:
	def __init__(self):
		#dbString = "pq://username:password@localhost/postgres"
		sqlLocator = "pq://owncloud:owncloud@localhost/owncloud"
		self._openSql(sqlLocator)

	def read(self):
		ps = self.db.prepare("""select o.startdate, o.enddate, summary, calendardata 
				from oc_clndr_objects o 
				join oc_clndr_calendars c on o.calendarid=c.id 
				where userid='fabi' and objecttype='VEVENT'
				order by startdate asc""")

		self.data = []
		for startdate, enddate, summary, data in ps():
			if startdate != None and enddate != None and len(summary) > 0:
				summary = self.myescape(summary)
				item = {
					'type': 'Event',
					'label': summary, 
					'start': str(startdate),
					'end': str(enddate)
				}
				if enddate - startdate > datetime.timedelta(hours=24):
					item['isDuration'] = True
				# parse ical event
				icalCalendar = Event.from_ical(data)
				for comp in icalCalendar.subcomponents:
					if comp.name == 'VEVENT':
						item['description'] = comp.get('description')
						item['location'] = comp.get('location')
						item['categories'] = comp.get('categories')
						item['id'] = comp.get('uid')
				self.data.append(item)
		return self.data

	def myescape(self, text):
		return text.replace('\\','')

	def write(self, outfile):
		with open(outfile, "w") as f:
			f.write(json.dumps({'items': self.data}, indent=2))

	def _openSql(self, sqlLocator):
		self.db = postgresql.open(sqlLocator)

if __name__ == "__main__":
	outfile = "calendar.js"
	g = Generator()
	g.read()
	g.write(outfile)
	print("Calendar data written to %s" % outfile)
	

