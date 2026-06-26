---
title: "Leaflet Maps - Connecting to Map Servers"
id: 4406822442775
section: "Use Dashboards & Visuals - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406822442775-Leaflet-Maps-Connecting-to-Map-Servers
updated_at: 2022-04-06T06:07:40Z
---

# Leaflet Maps - Connecting to Map Servers

# Leaflet Maps - Connecting to Map Servers

Connections to map servers aremade in the \_Settings definition, using **Connection.Leaflet Map** elements, one for each map server:

![](https://devnet.logianalytics.com/hc/article_attachments/4417583810711/introlmaps_25.png)

Each map, or "tile",server will have its own connection configuration requirements, and some examples are provided below. Consult the map server's web site for connection details and credentials, if necessary. The Connection.Leaflet Map element's attributes are:

| Attribute | Description |
| --- | --- |
| ID | (Required) Specifies a unique element ID. |
| Tile Server | Specifies the URL of a tile server. For example: http://my.map.tile.server/{z}/{x}/{y}.png, where:  z = map zoom level x, y = map coordinates  The mapping element provides dynamic values for x, y, and z as the user interacts with the map.  There are some pre-defined values, such as "MapQuest", which point to a public MapQuest map server. A pre-defined value may be used in place of the URL value described above.  See the following section for some examples. |
| Tile Server API Key | Specifies an API key for map servers that require one, for example MapQuest and Thunderforest. |
| Tile Server Attribution | Specifies an HTML string with server attribution text, for use when the map server requires it for licensing purposes. When a map layer using this connection is displayed the attribute value is displayed in the bottom right corner of the map. |
| Tile Server Include | Specifies a URL to a JavaScript file that's required by some map servers. Multiple files may be included by delimiting each URL with the pipe "|" symbol. |
| Tile Server JavaScript | Specifies the JavaScript constructor code for creating map layers when working with certain Leaflet JavaScript plug-ins. For example, to use the official MapQuest Leaflet plug-in and retrieve their satellite map tiles, the value for this attribute should be  new MQ.satelliteLayer()   For some of the pre-defined map servers, such as MapQuest, this value is automatically provided.  Visit <http://leafletjs.com/plugins.html> to learn more about Leaflet plug-ins. |

## Attribute Configuration Examples

These are examples of the Connection.Leaflet Map element's attribute values for selected map servers. The servers pre-defined in Logi Info have the word "Easy" in their names; only the required attributes are included in the table below.   
  
![](https://devnet.logianalytics.com/hc/article_attachments/4417583587863/noteicon.png) These values may be subject to change by the map provider and are only offered here as a courtesy. If in doubt, consult the provider's website.

| Map Server | Attribute Values |
| --- | --- |
| CartoDark | Tile Server: http://a.basemaps.cartocdn.com/dark\_all/{z}/{x}/{y}.png |
| MapQuest | Tile Server Include: https://www.mapquestapi.com/sdk/leaflet/v2.2/mq-map.js?key=*<yourKey>* Tile Server Javascript: new MQ.mapLayer() |
| MapQuestEasy | Tile Server: MapQuest Tile Server API Key: *<yourKey>* |
| MapQuestSatellite | Tile Server Include: https://www.mapquestapi.com/sdk/leaflet/v2.2/mq-map.js?key=*<yourKey>* Tile Server JavaScript: new MQ.satelliteLayer() |
| MapQuestSatelliteEasy | Tile Server: MapQuest-Satellite Tile Server API Key: *<yourKey>* |
| OpenStreetMaps | Tile Server: http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png Tile Server Attribution:  Map data &copy; <a href='http://openstreetmap.org'>OpenStreetMap</a> contributors |
| StamenToner | Tile Server Include: http://maps.stamen.com/js/tile.stamen.js?v1.3.0Tile Server JavaScript: new L.StamenTileLayer('toner') |
| StamenTonerEasy | Tile Server: Stamen-Toner |
| StamenTerrain | Tile Server Include: http://maps.stamen.com/js/tile.stamen.js?v1.3.0Tile Server JavaScript: new L.StamenTileLayer('terrain') |
| StamenTerrainEasy | Tile Server: Stamen-Terrain |
| StamenWatercolor | Tile Server Include: http://maps.stamen.com/js/tile.stamen.js?v1.3.0Tile Server JavaScript: new L.StamenTileLayer('watercolor') |
| StamenWatercolorEasy | Tile Server: Stamen-Watercolor |
| ThunderforestLandscape | Tile Server:  https://{s}.tile.thunderforest.com/landscape/{z}/{x}/{y}.png?apikey=*<yourKey>* Tile Server Attribution: Maps &copy; <a href='http://www.thunderforest.com/'>Thunderforest</a>, Data &copy; <a href='http://www.openstreetmap.org/copyright'>OpenStreetMap contributors</a> |
| ThunderforestLandscapeEasy | Tile Server: Thunderforest-Landscape Tile Server API Key: *<yourKey>* |
