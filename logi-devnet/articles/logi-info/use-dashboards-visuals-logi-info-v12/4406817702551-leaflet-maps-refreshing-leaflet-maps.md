---
title: "Leaflet Maps - Refreshing Leaflet Maps"
id: 4406817702551
section: "Use Dashboards & Visuals - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817702551-Leaflet-Maps-Refreshing-Leaflet-Maps
updated_at: 2022-04-06T06:07:41Z
---

# Leaflet Maps - Refreshing Leaflet Maps

# Leaflet Maps - Refreshing Leaflet Maps

You may want to refresh your map with new data, either automatically or in response to user input. To do this, you can, of course, use an **Action.Report** element to refresh the entire report page.

If you just want to refresh the *data* that drives the map markers, you can make the Leaflet Map element the direct target of an **Action.Refresh Element** or **Refresh Element Timer** element.

If you just want to refresh the *entire* map, but not the entire page, you can place your map in a separate report definition and then include it in your original report as a subreport using the **SubReport** element:

![](https://devnet.logianalytics.com/hc/article_attachments/4417583806743/introlmaps_22.png)

Make the SubReport element the target of an **Action.Refresh Element** or **Refresh Element Timer** element, as shown above. Use **Link Parameters** under the Action element to pass any necessary values to the Leaflet Map. This is the recommended method of refreshing maps in Dashboard panels.

*Special thanks to documentation contributors Michael Kujawski and Jason Scanzoni.*
