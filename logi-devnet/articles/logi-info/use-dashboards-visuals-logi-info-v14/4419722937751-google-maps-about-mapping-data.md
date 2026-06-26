---
title: "Google Maps - About Mapping Data"
id: 4419722937751
section: "Use Dashboards & Visuals - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419722937751-Google-Maps-About-Mapping-Data
updated_at: 2022-07-17T01:48:00Z
---

# Google Maps - About Mapping Data

# Google Maps - About Mapping Data

Data used for Google Maps typically contains, at the least, address information. When this information is sent to the web service, the map generated will be scaled to fit the data into the dimensions you set for the map (in the Google Map element).

![](https://devnet.logianalytics.com/hc/article_attachments/4419706854423/introgmaps_15.png)![](https://devnet.logianalytics.com/hc/article_attachments/4419706854679/introgmaps_15a.png)

For example, if your data only includes state/province information for a single state, the map generated will be scaled to show as much of the state as necessary to include all of the map markers (above, left). This could be the result, for example, of a SQL query statement that includes a WHERE State = 'MT' clause.

However, if your data includes street address, city, and state/province information, the map generated will be scaled as a street-level map (above, right). This could be the result, for example, of a SQL query statement that includes a WHERE City = 'New York' clause.

![](https://devnet.logianalytics.com/hc/article_attachments/4419699744407/introgmaps_17.png)

As shown above, one of the benefits of the interactive nature of these maps is that you can display additional information when the map marker is clicked. So, your data might include business intelligence data in addition to the address information.

For example, revenue figures or employee counts. This data can be displayed, as in the example, in the Info Window that pops up when a marker is clicked. The Info Window can also contain images, charts, gauges, sub-reports, and links, all driven
by data.

![](https://devnet.logianalytics.com/hc/article_attachments/4419706599319/criticalicon.png) If your data already includes latitude and longitude positioning data, so much the better. The use of Geocode Column elements to provide that data involves making additional network "trips" to the web service and that could mean additional transaction fees. Google imposes geocoding limits based on your license type; enterprise users may have other contractual
limits. See this [Google
Maps Geocoding Usage Billing](https://developers.google.com/maps/documentation/geocoding/usage-and-billing) page for more information about prices and limits.

Logi Info now includes the **Connection.Nominatim** element, for connections to a free, public, OpenStreetMap (OSM) [Nominatim](https://wiki.openstreetmap.org/wiki/Nominatim) server for geographic data. For more information, see [Datasource Connections](https://devnet.logianalytics.com/hc/en-us/articles/4419707715735-Datasource-Connections).

Support for data that includes "MultiGeometry" tags is included.

This concludes this introduction to Google Maps. For additional information, see [Google Map Tutorial](https://devnet.logianalytics.com/hc/en-us/articles/4419707611927-Google-Map-Tutorial).

*With special thanks to contributing writer Michael Kujawski.*
