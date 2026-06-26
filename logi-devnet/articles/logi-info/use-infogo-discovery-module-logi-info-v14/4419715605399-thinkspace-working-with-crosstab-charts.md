---
title: "Thinkspace - Working with Crosstab Charts   "
id: 4419715605399
section: "Use InfoGo/Discovery Module - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419715605399-Thinkspace-Working-with-Crosstab-Charts
updated_at: 2022-07-17T01:29:02Z
---

# Thinkspace - Working with Crosstab Charts   

# Thinkspace - Working with Crosstab Charts

Let's start by visualizing "cross-tabbed" data in a chart.

![](https://devnet.logianalytics.com/hc/article_attachments/4419707195671/dm30_workxtabs_01.png)

Our starting point will be a regular Column chart, showing *Freight* by *OrderDate*, as shown above.

![](https://devnet.logianalytics.com/hc/article_attachments/4419700007703/dm30_workxtabs_02.png)

Open the *OrderDate* pill using its gear icon, and change its Grouping to use Date Units, with # of Years = 1, as shown above. The chart will be re-drawn accordingly.

![](https://devnet.logianalytics.com/hc/article_attachments/4419707195927/dm30_workxtabs_03.png)

Drag and drop the *LastName* pill from the Data Table into the CROSSTAB drop zone, using the Blue Dot Connector, as shown above. The chart will be re-drawn accordingly.

![](https://devnet.logianalytics.com/hc/article_attachments/4419700008215/dm30_workxtabs_04.png)

The cross-tabbed data can be shown as stacked (values), stacked
(percentages), or grouped side-by-side. When the *LastName* pill was
dropped, the option for the selected chart type in the Visualization menu
acquired a "More Options" arrow icon, circled above. Click it to see the
crosstab charting options and select the **Grouped Crosstab Column** option.

![](https://devnet.logianalytics.com/hc/article_attachments/4419700008471/dm30_workxtabs_05.png)

The resulting chart will look like the example above.

![](https://devnet.logianalytics.com/hc/article_attachments/4419700008855/dm30_workxtabs_06.png)

If you'd like to view the data a little differently, for example, grouped by *LastName* instead of *OrderDate*, it's easy to do - just drag and SWAP the two column pills, as shown above.

![](https://devnet.logianalytics.com/hc/article_attachments/4419714990487/dm30_workxtabs_07.png)

And the resulting chart is shown above.
