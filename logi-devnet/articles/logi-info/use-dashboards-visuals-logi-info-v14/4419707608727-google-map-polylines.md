---
title: "Google Map Polylines"
id: 4419707608727
section: "Use Dashboards & Visuals - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419707608727-Google-Map-Polylines
updated_at: 2022-07-17T01:48:10Z
---

# Google Map Polylines

# Google Map Polylines

If you've used Google or Leaflet maps to provide geographic mapping solutions in your Logi application, you can take advantage of another advanced feature, **Map Polylines**. In Logi Info, this allows you to overlay solid or semi-transparent, color-coded lines on a map, based on data. They're often used to depict a route from one place to another.

The following topics discuss the use of Map Polylines:

* [Implementing Google Map Polylines](https://devnet.logianalytics.com/hc/en-us/articles/4419707609623-Implementing-Google-Map-Polylines#Data)
* [Creating a Map with Polylines](https://devnet.logianalytics.com/hc/en-us/articles/4419722935447-Creating-a-Map-with-Polylines#Polylines)

If you haven't already, you should first read [Leaflet Maps](https://devnet.logianalytics.com/hc/en-us/articles/4419707730327-Leaflet-Maps) or [Google Maps](https://devnet.logianalytics.com/hc/en-us/articles/4419722939927-Google-Maps), which provide general information.

## About Map Polylines

![](https://devnet.logianalytics.com/hc/article_attachments/4419706599575/noteicon.png) Prior to v12.5, the element being discussed in this topic was called "Google Map Polylines". However, with the introduction of Leaflet maps, the "Google" part of the name was dropped. The element works in the same way for either mapping system.
Map Polylines, plotted onto the map, are overlays that are drawn, and can be color-coded, based on data
values. Here's an example:

![](https://devnet.logianalytics.com/hc/article_attachments/4419699735703/gmpolylines_01.png)

The map above uses polylines to show a route from the Orsay Museum in Paris to the Louvre Museum. Polyline color, width, and transparency level are all configurable and can be set from data values. The line above has been configured to be semi-transparent, so that geographic features can be seen through it.

![](https://devnet.logianalytics.com/hc/article_attachments/4419706848023/gmpolylines_02.png)

Polylines can be configured with Map Marker Info pop-ups and can be related to other data. In the example above, they've been configured so that when they're clicked, an information panel is displayed containing more detailed information about the immediate location.
Other use-case examples include subway maps, traffic density indicators, and pipeline route mapping, to name but a few.

### Geographic Data

Polylines are
plotted using sets of **latitude** and **longitude****points** that describe line segments. Multiple segments are used to draw a continuous line. For use with Logi elements, these typically come from
GPX or KML files, which are GIS industry-standard XML data files. Special datalayers are provided in Logi Info to read these files. Because of their public nature, this data is often freely available on the Internet.
Data is also widely available in *shapefiles*, a popular geospatial vector format for
GIS data. Software tools, discussed in [Map Polygons](https://devnet.logianalytics.com/hc/en-us/articles/4419707760151-Map-Polygons), are available for converting shapefiles into GPX or KML data files.
Geographic data can also be retrieved from SQL database tables using DataLayer.SQL; see for more information.
