---
title: "Implementing Map Polygons"
id: 4419707759255
section: "Use Dashboards & Visuals - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419707759255-Implementing-Map-Polygons
updated_at: 2022-07-17T01:41:00Z
---

# Implementing Map Polygons

# Implementing Map Polygons

The following example will demonstrate how to implement Map Polygons. The purpose of the example is to create a map of the state of Florida, with an overlay of all its public school districts, in order to easily compare "dropout rates" - the percentage of students who have dropped out of the school system - in the 2007-2008 school year. As is often the case, the first step is to have a look at the data.
For this example, relevant annual dropout rate data from the State of Florida's Department of Education has been downloaded and stored as an XML data file.

<?xml version="1.0"encoding="utf-8"?>  
<dropOuts District="ALACHUA" Y1999="5.7" Y2000="6.3" Y2001="6.1" Y2002="5.2" Y2003="5.1" Y2004="5.1" Y2005="5" Y2006="6.1" Y2007="6.6" Y2008="3.6" />  
<dropOuts District="BAKER" Y1999="9.7" Y2000="3" Y2001="4.2" Y2002="3.5" Y2003="3.7" Y2004="4" Y2005="4.3" Y2006="3.7" Y2007="2.8" Y2008="1.8" />  
<dropOuts District="BAY" Y1999="2.5" Y2000="3.5" Y2001="1.6" Y2002="1.5" Y2003="1.1" Y2004="1.8" Y2005="1.2" Y2006="2" Y2007="2.5" Y2008="1.7" />
A small part of the XML dropout data is shown above; note that the field *District* contains the school district name values.

<?xml version="1.0" encoding="UTF-8"?>  
<gpx xmlns="http://www.topografix.com/GPX/1/1" version="1.1" creator="ExpertGPS 3.03" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.topografix.com/GPX/1/1 http://www.topografix.com/GPX/1/1/gpx.xsd http://www.topografix.com/GPX/gpx\_overlay/0/3 http://www.topografix.com/GPX/gpx\_overlay/0/3/gpx\_overlay.xsd http://www.topografix.com/GPX/gpx\_modified/0/1 http://www.topografix.com/GPX/gpx\_modified/0/1/gpx\_modified.xsd">  
<metadata>  
<bounds minlat="24.54470100" minlon="-87.63493800" maxlat="31.00088800" maxlon="-80.03136200"/>  
<extensions>  
<time xmlns="http://www.topografix.com/GPX/gpx\_modified/0/1">2009-04-20T19:40:01.535Z</time>  
</extensions>  
</metadata>  
<extensions>  
<polyline xmlns="http://www.topografix.com/GPX/gpx\_overlay/0/3">  
<desc>ALACHUA COUNTY SCHOOL DISTRICT</desc>  
<label>  
<label\_text>ALACHUA COUNTY SCHOOL DISTRICT</label\_text>  
</label>  
<extensions>  
</extensions>  
<points>  
<pt lat="30.99692800" lon="-85.49827200"/>  
<pt lat="31.00088400" lon="-85.24363200"/>  
<pt lat="31.00083500" lon="-85.15445200"/>  
<pt lat="31.00083400" lon="-85.15221800"/>  
Similarly, the GIS data defining the boundaries of the state's school districts has been download and stored as a GPX file and a small part of it is shown above.

![](https://devnet.logianalytics.com/hc/article_attachments/4419706599575/noteicon.png) The school district name is part of the data in the *desc* field. The beginning of the latitude and longitude data for the district boundaries is at the bottom of the sample.
In our Logi application, we'll relate the *school**district**names* in these two files with each other in order to make our map overlay functional.
The format of a KML file is somewhat different but it's still XML data and you can look at it easily enough to determine relevant field names.
