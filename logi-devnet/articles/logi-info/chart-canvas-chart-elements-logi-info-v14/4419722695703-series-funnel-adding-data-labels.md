---
title: "Series.Funnel - Adding Data Labels"
id: 4419722695703
section: "Chart Canvas Chart Elements - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419722695703-Series-Funnel-Adding-Data-Labels
updated_at: 2022-07-17T02:25:11Z
---

# Series.Funnel - Adding Data Labels

# Series.Funnel - Adding Data Labels

A "data label" is text that can be shown adjacent to each funnel segment, that shows its X-axis data value. This is controlled using the Label Location attribute.

![](https://devnet.logianalytics.com/hc/article_attachments/7522849150999/series_funnel_06.png)

As shown above, labels can be placed beside the segments, or in a legend, or not shown at all.

When the legend option is selected, "legend filtering" is active: clicking a segment's entry in the legend will toggle its appearance in the chart. For more information about legends, see [Legend](https://devnet.logianalytics.com/hc/en-us/articles/4419707322519-Legend).

![](https://devnet.logianalytics.com/hc/article_attachments/7522774430103/noteicon.jpg) When working with labels beside the funnel, you may need to adjust the Chart Canvas element's **Spacing Left** and **Spacing Right** attributes to "fit" all of the label text inside the canvas.

![](https://devnet.logianalytics.com/hc/article_attachments/7522849171095/series_funnel_07.png)

If you want to show the data *values* instead of, or with, the data *labels* near each funnel segment, as shown above, use the Series.Funnel element's **Label Location**, **Show Data Values**, and **Show Data Values Format** attributes.

The values displayed can also be styled using the **Side Label Style** element. Its attributes allow you to control the font family, color, size, and weight, the data format, background color, border color, connecting lines and more. The side labels in the image above have been styled.

The Side Label Style element's **Maximum Label Length** attribute lets you specify the maximum number of characters that will be displayed for a label before the text is truncated and ellipsis (...) is appended.
