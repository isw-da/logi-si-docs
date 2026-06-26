---
title: "Leaflet Maps - About Map Servers"
id: 4406817698327
section: "Use Dashboards & Visuals - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817698327-Leaflet-Maps-About-Map-Servers
updated_at: 2022-04-06T06:07:41Z
---

# Leaflet Maps - About Map Servers

# Leaflet Maps - About Map Servers

The Leaflet API is designed to work with public map servers. These provide maps as a set of "tiles" which are assembled into a map for display, allowing for dynamic scaling. Your Logi Info app connects to, and sends parameters
to, a map server and the server returns appropriate map tiles.

![](https://devnet.logianalytics.com/hc/article_attachments/4417583811735/introlmaps_07.png)

The diagram above illustrates how this fits into the Logi application architecture. Typically, the parameters that you send to the map server come from a datasource that your application queries. The results are used in the HTML pages that are output to a browser. Logi Studio elements make the process of connecting to, and communicating with, the map server *very easy*.

## Map Service Licensing

Map server providers make their services available to Internet users, sometimes charging a license fee, but more often for free while requiring attribution. You may be required to get an "API Key" from the provider web site. Providers may impose transaction limits or tiered-usage licensing.

*![](https://devnet.logianalytics.com/hc/article_attachments/4417562936855/criticalicon.png)*You, as the developer, are responsible for reviewing the current terms of use for the map server you choose to work with, and for taking whatever actions are legally necessary with regard to licensing.
