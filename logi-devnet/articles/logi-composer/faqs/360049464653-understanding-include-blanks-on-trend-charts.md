---
title: "Understanding \"Include Blanks\" on Trend Charts"
id: 360049464653
section: "FAQs"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/360049464653-Understanding-Include-Blanks-on-Trend-Charts
updated_at: 2020-07-27T23:00:01Z
---

# Understanding "Include Blanks" on Trend Charts

This article applies to Composer V5.9 and Zoomdata V4.9.

### Where can I find "Include Blanks"?

The Include Blanks checkbox can be found in the "granularity level" picker on trend charts, such as:

![Screen_Shot_2020-07-15_at_3.08.42_PM.png](https://devnet.logianalytics.com/hc/article_attachments/360079682754/Screen_Shot_2020-07-15_at_3.08.42_PM.png)

### What happens if "Include Blanks" is NOT selected?

By default, "Include Blanks" is not selected when first creating a line trend chart.

In this case, only grouped-by time elements where data exists in the specified time range will return on the chart.

### What happens if "Include Blanks" IS selected?

When "Include Blanks" is selected, Composer will apply the specified time range (as configured on the time bar) and show all the data points available within the range at the intended granularity (e.g. min, hour, etc.) on the chart. Where no data point is available within the range, the chart will display a blank space or gap.

### Example

Assume that the time range is one hour and new data is being ingested every 5 minutes (which may not always contain new data values). Furthermore, granularity level of the trend chart is set at the minute level.

#### If "Include Blanks" is not selected....

Only the minutes that contain actual data for that hour will be shown on the trend chart.

#### If "Include Blanks" is selected...

Every individual minute from that hour should be shown on the chart (because granularity is set to minute level), whether they contain data or are left blank.
