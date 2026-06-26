---
title: "Tools for GIS Data Conversion"
id: 4419707761175
section: "Use Dashboards & Visuals - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419707761175-Tools-for-GIS-Data-Conversion
updated_at: 2023-11-08T16:34:13Z
---

# Tools for GIS Data Conversion

# Tools for GIS Data Conversion

Data describing
geographic region boundaries is used in Logi Info as either a
**GPX** or **KML** file. In addition, data is also widely available
in shapefiles (SHP). Note that these files need to use the standard
Mercator projection, based on the WGS 1984 Ellipsoid projection, that
Google Maps requires; "conic" projections, for example, will not
work.
A search of the Internet will yield many hits for software tools, free and
paid, that can convert GIS data into these formats. Logi Analytics does
not specifically endorse or recommend any particular tool but we have
experimented with the following.

![](https://devnet.logianalytics.com/hc/article_attachments/4419706599319/criticalicon.png) The following resources are provided to you as a courtesy. They're
external resources not associated with Logi Analytics and we cannot
guarantee that the links provided will remain viable. Developers are
encouraged to search the Internet for their own resources.

## SHP2KML 2.0

The SHP2KML program (freeware) available at
<http://www.zonums.com/shp2kml.html>
will convert a SHP file into a Google KML file.

## GPSBabel

The GPSBabel program (licensed under GNU - but should be fine for just
about every use except re-distribution) is available at
<http://www.gpsbabel.org/>
and will convert KML to GPX format.

## GPS Visualizer

<http://www.gpsvisualizer.com/convert_input?convert_output=gpx>  
 This is a free online conversion tool which is probably good for small
files but not larger ones.

## ExpertGPS

ExpertGPS makes it very easy to convert SHP files into GPX or KML formats
and is available at
<http://www.expertgps.com/>
The program isn't free, but it's relatively low cost ($74.95 for personal
use) and is available in a 30-day trial version. The program makes it very
easy to convert between SHP and other file formats.
When you download a .zip file containing SHP files, it will contain three
files. You'll need to unzip all three files to a folder and then use the
"Import" function of the ExpertGPS program to generate the GPX
file (you'll only select the .shp file for import but the process reads
from the other two files to get the appropriate labels and other
metadata). To create the appropriate GPX file for Logi Info to work you
need to make sure that you're populating the "Description" field
with the boundary name from the SHP file (e.g. zip code, county, etc);
it's suggested that you leave all the other fields empty to create the
smallest possible GPX file.
