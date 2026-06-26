---
title: "Google Maps - Refreshing Google Maps"
id: 4406817498135
section: "Use Dashboards & Visuals - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817498135-Google-Maps-Refreshing-Google-Maps
updated_at: 2022-04-06T06:06:27Z
---

# Google Maps - Refreshing Google Maps

# Google Maps - Refreshing Google Maps

Developers may want to refresh their Google Maps with new data, either automatically or in response to user input. To do this, you can, of course, use an **Action.Report** element to refresh the entire report page.

## Use a SubReport

If you just want to refresh the map, not the entire page, you can place your Google Map in a separate report definition and then include it in your original report as a subreport using the **SubReport** element:

![](https://devnet.logianalytics.com/hc/article_attachments/4417583912983/introgmaps_26.png)

Make the SubReport element the target of an **Action.Refresh Element** or **Refresh Element Timer** element, as shown above. Use **Link Parameters** under the Action element to pass any necessary values to the Google Map. This is the recommended method of updating Google Maps in Dashboard panels.

![](https://devnet.logianalytics.com/hc/article_attachments/4417562936855/criticalicon.png) A Google Map element *cannot* be the direct target of an Action.Refresh Element or Refresh Element Timer element; not even if you wrap the map in a Division. This is why using a SubReport is recommended.

A Google Map element *can* now be the direct target of an Action.Refresh Element or Refresh Element Timer element, however, this refreshes only the Map Markers and *not* the entire map.
