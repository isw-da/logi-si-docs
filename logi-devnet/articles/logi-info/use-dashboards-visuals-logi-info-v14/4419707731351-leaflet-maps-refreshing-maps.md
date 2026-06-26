---
title: "Leaflet Maps - Refreshing Maps"
id: 4419707731351
section: "Use Dashboards & Visuals - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419707731351-Leaflet-Maps-Refreshing-Maps
updated_at: 2022-07-17T01:42:24Z
---

# Leaflet Maps - Refreshing Maps

# Leaflet Maps - Refreshing Maps

You may want to refresh your map with new data, either automatically or in response to user input. To do this, you can, of course, use an **Action.Report** element to refresh the entire report page.

If you just want to refresh the *data* that drives the map markers, you can make the Leaflet Map element the direct target of an **Action.Refresh Element** or **Refresh Element Timer** element.

If you just want to refresh the *entire* map, but not the entire page, you can place your map in a separate report definition and then include it in your original report as a subreport using the **SubReport** element:

![](https://devnet.logianalytics.com/hc/article_attachments/4419714857751/introlmaps_22.png)

Make the SubReport element the target of an **Action.Refresh Element** or **Refresh Element Timer** element, as shown above. Use **Link Parameters** under the Action element to pass any necessary values to the Leaflet Map. This is the recommended method of refreshing maps in Dashboard panels.

*Special thanks to documentation contributors Michael Kujawski and Jason Scanzoni.*
