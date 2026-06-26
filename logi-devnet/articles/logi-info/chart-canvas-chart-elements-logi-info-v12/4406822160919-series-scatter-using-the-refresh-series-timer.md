---
title: "Series.Scatter - Using the Refresh Series Timer"
id: 4406822160919
section: "Chart Canvas Chart Elements - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406822160919-Series-Scatter-Using-the-Refresh-Series-Timer
updated_at: 2022-04-06T06:04:10Z
---

# Series.Scatter - Using the Refresh Series Timer

# Series.Scatter - Using the Refresh Series Timer

The **Refresh Series Timer**, added as a Series child element, updates charts automatically, based on a time interval. When the interval is reached, a request is sent back to the web server for updated data. Series are updated with a smooth animation.

![](https://devnet.logianalytics.com/hc/article_attachments/4417563502487/series_scatter_13.png)

The **Refresh Interval** attribute specifies the number of seconds to wait before refreshing the series data. A value is required and must be an integer greater than 0.

## Refresh Mode

Series may be refreshed in two ways: either all of the data is refreshed with each request, or the series data automatically slides to the left one data interval per refresh. The refresh mode is selected in the Chart X Axis element's **Axis Type** attribute.
When the Axis Type is *not* set to *DateTimeLinear*, all of the data will be refreshed.

When the Axis Type value is *DateTimeLinear*, newer values are added to the right side of the chart, previous values slide left, and older values disappear as they reach the left edge of the chart. In this case, the Refresh Series Timer element's **Time Span** attribute is used to specify the age of the data included. This value must be in *hh:mm:ss* format (for example "00:02:00"
for two minutes) and must be larger than the Refresh Interval attribute value.

When a Time Span attribute is set, the series' datalayer can make use of a special timestamp token, @Chart.rdTimeSpanStart~, in a query to retrieve just the rows necessary to update the chart. On the initial request, this token returns the current time minus the Time Span value. For subsequent refreshes, when Axis Type = *DateTimeLinear* and the
X-axis will be sliding, the token returns the last time the chart was updated, so only the newest rows are retrieved. Here's an MS SQL Server query example:

SELECT \* FROM MyTable WHERE UpdateTime BETWEEN '@Chart.rdTimeSpanStart~' AND '@Function.DateTime~'  

For best performance, avoid setting a very short refresh interval if a very large number of users will be displaying the report.
