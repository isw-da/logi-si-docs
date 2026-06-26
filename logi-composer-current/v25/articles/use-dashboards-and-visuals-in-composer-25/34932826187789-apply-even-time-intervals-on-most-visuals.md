---
title: "Apply Even Time Intervals on Most Visuals"
id: 34932826187789
section: "Use Dashboards and Visuals in Composer 25"
product: "Logi Composer v25"
url: https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932826187789-Apply-Even-Time-Intervals-on-Most-Visuals
updated_at: 2026-05-26T22:09:55Z
---

# Apply Even Time Intervals on Most Visuals

# Apply Even Time Intervals on Most Visuals

For more information about even time intervals, see [Even Time Intervals](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932833532429-Even-Time-Intervals).

**Apply even time intervals to data on bar, box plot, donut, floating bubble, heat map, line, packed bubble, pie, scatter, tree map, and word cloud visuals**

1. [Edit](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932763603597-Edit-a-Dashboard) a dashboard with one of these visual styles that uses a data source containing date or time fields.
2. Select a time attribute for the visual Group (x-axis).
3. Select the Time Granularity box on the x-axis.

   ![](https://logi-composer-v25.insightsoftware.com/hc/article_attachments/46167339915533)
4. Slide **Include Blanks** on to request even time intervals. By default, the ability to show all values is disabled and only attributes with a value greater than NULL are displayed.

   If this is a line chart, you can also select the **Display null as zero** checkbox to request that null values display as zeros on the chart:

   ![](https://logi-composer-v25.insightsoftware.com/hc/article_attachments/46167346043917)

The dashboard updates to include all values from the data source.
