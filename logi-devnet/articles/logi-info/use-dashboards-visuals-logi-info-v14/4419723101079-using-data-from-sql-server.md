---
title: "Using Data from SQL Server"
id: 4419723101079
section: "Use Dashboards & Visuals - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419723101079-Using-Data-from-SQL-Server
updated_at: 2022-07-17T01:40:56Z
---

# Using Data from SQL Server

# Using Data from SQL Server

You can also set up the Map Polygons element to use DataLayer.SQL to retrieve geography data from a SQL database, for plotting geographic areas. Here, we describe examples using MS SQL Server. You may have to adjust them for your DB server, if you have things set up differently. When you use MS SQL Server Management Studio, your Geography type data is displayed as hex strings. However, if you look at the data in Logi Studio's SQL Query Builder, it appears as strings similar to:

POLYGON ((-77.15272360579938 38.899021866163743, -77.101466420629265
38.944705094496122, -77.095299197312215 38.985397708288836,
-77.169278164468949 39.026928767466487, -77.220265629834756
39.006681859583395, -77.230661807874824 38.933657409186786,
-77.15272360579938 38.899021866163743))
This format can also be displayed using a built-in SQL Server function
called STAsText(). STAsText() (and other database versions) returns the coordinates in well-known text (WKT) standard: POLYGON ((LAT LONG,[...] , LAT LONG)). As opposed to Info, which expects the coordinate values in CSV format: Long1,Lat1 Long2,Lat2 Long3,Lat3 Long4,Lat4, with one polygon per line. To use polygons in Logi maps, geographic data needs to be transformed to
include a column named *rdCoordinates*, which contains the polygon
data as a string of coordinates in a comma-delimited sequence such as: Long1,Lat1 Long2,Lat2 Long3,Lat3 Long4,Lat4
.

![](https://devnet.logianalytics.com/hc/article_attachments/4419706599575/noteicon.png) While longitude and latitude values are separated by commas, coordinate pairs are separated by spaces.

Here's an example table:

![](https://devnet.logianalytics.com/hc/article_attachments/4419699854999/gmpoly_16.png)

This data can be retrieved and plotted using DataLayer.SQL as a child of
the Map Polygons element.

## MultiPolygons

The Geography data type also supports "multipolygons", which can
be thought of as a related group of polygons.
For example, if a region represented a farm, a field in it might be
split in two by a river running through it. Each part of the field
would be a polygon, and the entire field would be a
multipolygon.
GoogleMapPolygons can now retrieve their coordinates from any DataLayer with the column rdCoordinates containing WKT formatted polygons and multipolygons. It is possible to create multiple rows of polygon data from a multipolygon
through a JOIN. Contact Logi Customer Support for the details of this
operation.
