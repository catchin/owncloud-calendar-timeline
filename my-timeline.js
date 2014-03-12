var tl;
function onLoad() {
  var eventSource = new Timeline.DefaultEventSource();
  var bandInfos = [
    Timeline.createBandInfo({
      eventSource:    eventSource,
      width:          "70%", 
      date:           "Jun 28 2006 00:00:00 GMT",
      intervalUnit:   Timeline.DateTime.MONTH, 
      intervalPixels: 100
    }),
    Timeline.createBandInfo({
      overview:       true,
      eventSource:    eventSource,
      width:          "30%", 
      date:           "Jun 28 2006 00:00:00 GMT",
      intervalUnit:   Timeline.DateTime.YEAR, 
      intervalPixels: 200
    })
  ];
  bandInfos[1].syncWith = 0;
  bandInfos[1].highlight = true;
  tl = Timeline.create(document.getElementById("my-timeline"), bandInfos);

  Timeline.loadXML("example1.xml", function(xml, url) { eventSource.loadXML(xml, url); });
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
// vim:tabstop=2 expandtab
