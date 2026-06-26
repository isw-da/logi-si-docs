---
title: "Apply Even Time Intervals on Most Visuals"
id: 43700998633613
section: "Use Dashboards and Visuals in Composer 26"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43700998633613-Apply-Even-Time-Intervals-on-Most-Visuals
updated_at: 2026-05-29T14:11:14Z
---

# Apply Even Time Intervals on Most Visuals

# Apply Even Time Intervals on Most Visuals

For more information about even time intervals, see [Even Time Intervals](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701077393293-Even-Time-Intervals).

**Apply even time intervals to data on bar, box plot, donut, floating bubble, heat map, line, packed bubble, pie, scatter, tree map, and word cloud visuals**

1. [Edit](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701014144397-Edit-a-Dashboard) a dashboard with one of these visual styles that uses a data source containing date or time fields.
2. Select a time attribute for the visual Group (x-axis).
3. Select the Time Granularity box on the x-axis.

   ![](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46242644894349)
4. Slide **Include Blanks** on to request even time intervals. By default, the ability to show all values is disabled and only attributes with a value greater than NULL are displayed.

   If this is a line chart, you can also select the **Display null as zero** checkbox to request that null values display as zeros on the chart:

   ![](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46242629132045)

The dashboard updates to include all values from the data source.
