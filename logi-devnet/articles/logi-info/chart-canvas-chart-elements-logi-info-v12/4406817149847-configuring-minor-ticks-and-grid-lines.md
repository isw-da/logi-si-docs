---
title: "Configuring Minor Ticks and Grid Lines"
id: 4406817149847
section: "Chart Canvas Chart Elements - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817149847-Configuring-Minor-Ticks-and-Grid-Lines
updated_at: 2022-04-06T06:04:19Z
---

# Configuring Minor Ticks and Grid Lines

# Configuring Minor Ticks and Grid Lines

"Minor" tick marks and grid lines are drawn in between major tick marks and grid lines. Adding them provides an additional visual reference without adding additional axis labels. Minor tick marks and grid lines can be configured using the **Minor Ticks and Grid** child element.

![](https://devnet.logianalytics.com/hc/article_attachments/4417563492887/introcccharts_107.png)

In the example shown above, the Minor Ticks and Grid element's **Tick Interval** attribute has been set to *1,250*. Minor grid lines can be customized in a number of ways, including color, width, and transparency. Tick marks can be customized similarly and their length, position and interval can also be set.

The Tick Interval is sensitive to the axis data type. For DateTime data, you can select standard values including *Years*, *Weeks,**Hours* and more. For Numeric data, you should enter a numeric value, such as *100* or *1000*. The default value, *Auto*, automatically calculates the Tick Interval based on the data values.

If used with a linear axis and the standard value, *Auto*, is selected, the minor
Tick Interval will be calculated as one fifth of the Major Tick Interval value.

![](https://devnet.logianalytics.com/hc/article_attachments/4417562936855/criticalicon.png) Setting the Tick Interval for numeric data to an unrealistically small value will cause an error when the chart is rendered. For example, using a value of *2* for the chart above will cause the Logi engine to time-out after attempting to render 25,000 tick marks and labels.
