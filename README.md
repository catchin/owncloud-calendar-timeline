owncloud-simile-timeline
========================

Calendar data from owncloud is exported into an xml file which can be viewed with [Simile Timeline](http://www.simile-widgets.org/timeline/)

This project contains everything needed to display the timeline.

Prerequisites
-------------

* python3
* python3-markupsafe
* python3-postgresql

This should do it:
    apt-get install python3 python3-markupsafe python3-postgresql


How to use
----------

* Modify the sql parameters in generator.py if needed
* Generate calendar.xml file: `./generator.py`
* view timeline.html in a web browser, e.g.: `python -m http.server` and then go to http://localhost:8000/
  (see https://github.com/mrdoob/three.js/wiki/How-to-run-things-locally)


Comments / Questions
--------------------

Just contact me :)
