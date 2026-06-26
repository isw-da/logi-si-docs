---
title: "Implementing Map Polylines"
id: 4406817487895
section: "Use Dashboards & Visuals - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817487895-Implementing-Map-Polylines
updated_at: 2022-04-06T06:06:25Z
---

# Implementing Map Polylines

# Implementing Map Polylines

The following example will demonstrate how to implement Map Polylines. The purpose of the example is to create the example we've seen in [Google Map Polylines](https://devnet.logianalytics.com/hc/en-us/articles/4406817486615-Google-Map-Polylines): routes between the Louvre Museum in Paris and several other primary tourist attractions. As is often the case, the first step is to have a look at the data.

<?xml version="1.0" encoding="UTF-8"?>  
<gpx version="1.0" xmlns="http://www.topografix.com/GPX/1/0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.topografix.com/GPX/1/0 http://www.topografix.com/GPX/1/0/gpx.xsd">  
<trk>  
<name>LouvreToCafeMetropole</name>  
<trkseg>  
 <trkpt lat="48.8610022" lon="2.3352277"></trkpt>  
<trkpt lat="48.8607410" lon="2.3350883"></trkpt>  
 <trkpt lat="48.8605857" lon="2.3356140"></trkpt>  
 <trkpt lat="48.8598023" lon="2.3351634"></trkpt>  
 <trkpt lat="48.8594352" lon="2.3366225"></trkpt>  
<trkpt lat="48.8593152" lon="2.3379850"></trkpt>  
<trkpt lat="48.8591670" lon="2.3390150"></trkpt>  
<trkpt lat="48.8589482" lon="2.3402274"></trkpt>  
<trkpt lat="48.8590470" lon="2.3402917"></trkpt>  
</trkseg>  
</trk>  
<trk>  
<name>LouvreToOrsay</name>  
<trkseg>  
<trkpt lat="48.8611857" lon="2.3351204"></trkpt>  
<trkpt lat="48.8613198" lon="2.3345196"></trkpt>  
 ...  
  
The GIS data defining the line segments for each route has been download and stored as a GPX file, and a small part of it is shown above. You can see that each route has a name and a set of latitude and longitude records, organized in a hierarchy.
The format of a KML file is somewhat different but it's still XML data and you can look at it easily enough to determine relevant field names.
