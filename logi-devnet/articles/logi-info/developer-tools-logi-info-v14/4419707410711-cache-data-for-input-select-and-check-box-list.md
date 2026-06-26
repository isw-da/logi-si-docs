---
title: "Cache Data for Input Select and check box List"
id: 4419707410711
section: "Developer Tools - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419707410711-Cache-Data-for-Input-Select-and-check-box-List
updated_at: 2022-07-17T01:57:20Z
---

# Cache Data for Input Select and check box List

# Cache Data for Input Select and check box List

When implementing **Input Select List** and
**Input check box List** elements that will be used frequently, and
populating them with live data (rather than static options), you may want
to use **DataLayer.Cached** to retrieve the data. This will limit the
number of queries required.

If you must use a long-running SELECT DISTINCT query on a large table to
populate the list data, set up a scheduled Process Task to refresh the
cached data during off-hours.
