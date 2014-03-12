var tl;
function onLoad() {
  var eventSource = new Timeline.DefaultEventSource();
  var bandInfos = [
    Timeline.createBandInfo({
      eventSource:    eventSource,
      width:          "80%", 
      date:           "2008-06-28 00:00:00",
      intervalUnit:   Timeline.DateTime.WEEK, 
      intervalPixels: 150
    }),
    Timeline.createBandInfo({
      overview:       true,
      eventSource:    eventSource,
      width:          "13%", 
      date:           "2008-06-28 00:00:00",
      intervalUnit:   Timeline.DateTime.MONTH, 
      intervalPixels: 50
    }),
    Timeline.createBandInfo({
      overview:       true,
      eventSource:    eventSource,
      width:          "7%", 
      date:           "2008-06-28 00:00:00",
      intervalUnit:   Timeline.DateTime.YEAR, 
      intervalPixels: 150
    })
  ];
  bandInfos[1].syncWith = 0;
  bandInfos[1].highlight = true;
  bandInfos[2].syncWith = 1;
  bandInfos[2].highlight = true;
  tl = Timeline.create(document.getElementById("my-timeline"), bandInfos);

  Timeline.loadXML("calendar.xml", function(xml, url) { eventSource.loadXML(xml, url); });
}

var resizeTimerID = null;
function onResize() {
  var eventSource = new Timeline.DefaultEventSource(); 
  if (resizeTimerID == null) {
    resizeTimerID = window.setTimeout(function() {
      resizeTimerID = null;
      tl.layout();
    }, 500);
  }
}
var timerID = null;
function onFilter() {
  if (timerID != null) {
      window.clearTimeout(timerID);
  }
  timerID = window.setTimeout(performFiltering, 300);
}
function clearFilter() {
  document.getElementById('filterInput').value = '';
  onFilter();
}
function cleanString(s) {
  return s.replace(/^\s+/, '').replace(/\s+$/, '');
}
function performFiltering() {
  timerID = null;
  var text = document.getElementById("filterInput").value;
  var filterMatcher = null;
  if (text.length > 0) {
    var regex = new RegExp(text, "i");
    filterMatcher = function(evt) {
      return regex.test(evt.getText()) || regex.test(evt.getDescription());
    };
  }
  
  for (var bandIndex = 0; bandIndex < tl.getBandCount(); bandIndex++) {
    tl.getBand(bandIndex).getEventPainter().setFilterMatcher(filterMatcher);
    //tl.getBand(bandIndex).getEventPainter().setHighlightMatcher(filterMatcher);
  }
  tl.paint();
}
// vim:tabstop=2 expandtab
