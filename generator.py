#!/usr/bin/python3
import postgresql
from lxml.builder import ElementMaker

class Generator:
	def __init__(self):
		#dbString = "pq://username:password@localhost/postgres"
		sqlLocator = "pq://owncloud:owncloud@localhost/owncloud"
		self._openSql(sqlLocator)

	def read(self):
		ps = self.db.prepare("""select o.startdate, o.enddate, summary, calendardata 
				from oc_clndr_objects o 
				join oc_clndr_calendars c on o.calendarid=c.id 
				where userid='fabi' 
				order by startdate asc""")
		E = ElementMaker()
		DATA = E.data
		EVENT = E.event

		for startdate, enddate, summary, data in ps():
			if startdate != None and len(summary) > 0:
				print(startdate)

	def _openSql(self, sqlLocator):
		self.db = postgresql.open(sqlLocator)

if __name__ == "__main__":
	Generator().read()

