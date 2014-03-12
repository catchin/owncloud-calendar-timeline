#!/usr/bin/python3
import postgresql
import markup
from markupsafe import escape
import sys
import datetime

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

		self.xml = markup.page(mode='xml')
		self.xml.data.open()
		for startdate, enddate, summary, data in ps():
			if startdate != None and len(summary) > 0:
				if enddate - startdate <= datetime.timedelta(hours=24):
					self.xml.event(escape(summary), start=str(startdate), end=str(enddate), title=escape(summary))
				else:
					self.xml.event(escape(summary), start=str(startdate), end=str(enddate), isDuration="true", title=escape(summary))
		self.xml.data.close()
		return self.xml

	def write(self, outfile):
		with open(outfile, "w") as f:
			f.write(str(self.xml))

	def _openSql(self, sqlLocator):
		self.db = postgresql.open(sqlLocator)

if __name__ == "__main__":
	outfile = sys.argv[1]
	g = Generator()
	g.read()
	g.write(outfile)
	print("Written to %s." % outfile)
	

