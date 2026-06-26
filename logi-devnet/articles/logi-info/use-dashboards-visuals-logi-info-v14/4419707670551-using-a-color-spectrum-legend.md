---
title: "Using a Color Spectrum Legend"
id: 4419707670551
section: "Use Dashboards & Visuals - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419707670551-Using-a-Color-Spectrum-Legend
updated_at: 2023-07-03T15:32:26Z
---

# Using a Color Spectrum Legend

# Using a Color Spectrum Legend

Instead of using Map Color Range elements, you can add a "color spectrum" legend to your animated map; this legend uses colors to illustrate the distribution of the data values used to generate the map and assigns those colors to the appropriate map regions.

![](https://devnet.logianalytics.com/hc/article_attachments/4419706906007/introanimap_13.png)

The first step, as shown above, is to add a **Color Spectrum Column** element beneath the datalayer. Configure its attributes to identify the data column used as the Animated Map element's Region Value Column, and the desired colors for the low, medium, and high values.

![](https://devnet.logianalytics.com/hc/article_attachments/4419699789335/introanimap_14.png)  

The next step is to add an **Animated Map Color Spectrum Legend** element, as shown above, beneath the Animated Map and to set its caption. The legend appears by default below the map, but its **Location** attribute can be set to make it appear to the right of the map.

![](https://devnet.logianalytics.com/hc/article_attachments/4419714821015/introanimap_15.png)

And the resulting map and legend are shown above.
