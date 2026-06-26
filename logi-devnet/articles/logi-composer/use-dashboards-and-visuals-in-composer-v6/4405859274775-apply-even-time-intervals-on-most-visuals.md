---
title: "Apply Even Time Intervals on Most Visuals"
id: 4405859274775
section: "Use Dashboards and Visuals in Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405859274775-Apply-Even-Time-Intervals-on-Most-Visuals
updated_at: 2021-09-21T01:27:52Z
---

# Apply Even Time Intervals on Most Visuals

# Apply Even Time Intervals on Most Visuals

For more information about even time intervals, see [*Even Time Intervals*](https://devnet.logianalytics.com/hc/en-us/articles/4405850992919-Even-Time-Intervals).

To apply even time intervals to data on bar, box plot, donut, floating bubble, heat map, line, packed bubble, pie, scatter, tree map, and word cloud visuals:

1. [Edit](https://devnet.logianalytics.com/hc/en-us/articles/4405850982039-Edit-a-Dashboard) a dashboard with one of these visual styles that uses a data source containing date or time fields.
2. Select a time attribute for the visual Group (x-axis).
3. Select the Time Granularity box on the x-axis.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4406743865623/even-time-intervals_192x237.png)
4. Slide **Include Blanks** on to request even time intervals. By default, the ability to show all values is disabled and only attributes with a value greater than NULL are displayed.
5. Slide **Include Blanks** on to request even time intervals. By default, the ability to show all values is disabled and only attributes with a value greater than NULL are displayed.

   If this is a line chart, you can also select the **Display null as zero** checkbox to request that null values display as zeros on the chart:

   ![](https://devnet.logianalytics.com/hc/article_attachments/4406743866007/even-time-intervals-linecht_192x279.png)

The dashboard updates to include all values from the data source.
