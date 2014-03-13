owncloud-calendar-timeline
========================

Calendar data from owncloud is exported into a json file. The calendar events can be viewed and filtered on a standalone webpage using [Simile Exhibit3](http://simile-widgets.org/wiki/Exhibit3) with the use of JavaScript.

Prerequisites
-------------

* python3
* python3-icalendar
* python3-postgresql

This should do it:

  `apt-get install python3 python3-icalendar python3-postgresql`


How to use
----------

* Modify the sql parameters in generator.py if needed
* Generate calendar.xml file: `./generator.py`
* view timeline.html in a web browser, e.g.: `python -m http.server` and then go to http://localhost:8000/
  (see https://github.com/mrdoob/three.js/wiki/How-to-run-things-locally)


Comments / Questions
--------------------

Just contact me :)
