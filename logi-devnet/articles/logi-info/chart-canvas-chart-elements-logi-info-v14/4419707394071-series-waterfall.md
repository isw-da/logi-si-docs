---
title: "Series.Waterfall"
id: 4419707394071
section: "Chart Canvas Chart Elements - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419707394071-Series-Waterfall
updated_at: 2022-07-17T01:58:17Z
---

# Series.Waterfall

# Series.Waterfall

The Chart Canvas element's Series child elements cause a data visualization (the chart) to be rendered in the canvas.

The following topics discuss the Series.Waterfall child element:

* [Using Multiple Series](https://devnet.logianalytics.com/hc/en-us/articles/4419707397783-Series-Waterfall-Using-Multiple-Series#Multiple)
* [Series.Waterfall Attributes](https://devnet.logianalytics.com/hc/en-us/articles/4419707394967-Series-Waterfall-Attributes#Attributes)
* [Using the Data Labels Element](https://devnet.logianalytics.com/hc/en-us/articles/4419715144599-Series-Waterfall-Using-the-Data-Labels-Element#Labels)
* [Using the Quicktips Element](https://devnet.logianalytics.com/hc/en-us/articles/4419722728727-Series-Waterfall-Using-the-Quicktips-Element#Quicktips)
* [Using Action Elements](https://devnet.logianalytics.com/hc/en-us/articles/4419707395863-Series-Waterfall-Using-Action-Elements#Action)
* [Using Input Selection](https://devnet.logianalytics.com/hc/en-us/articles/4419707396887-Series-Waterfall-Using-Input-Selection#Selection)
* [Using the Refresh Series Timer](https://devnet.logianalytics.com/hc/en-us/articles/4419722729623-Series-Waterfall-Using-the-Refresh-Series-Timer#Timer)

## About Series.Waterfall

The **Series.Waterfall** element generates a Waterfall chart, which helps in understanding the cumulative effect of sequentially introduced positive or negative values.

![](https://devnet.logianalytics.com/hc/article_attachments/4419699584663/series_waterfall_01.png)

The example above shows a Waterfall chart, with negative values shown in red. A special "total bar", labeled *Profit* above, is automatically generated from the sum of all other values. It appears as the last bar on the right or, at the top, if the axes are swapped. Its generation can be controlled in the Series attributes.

![](https://devnet.logianalytics.com/hc/article_attachments/4419714672791/series_waterfall_02.png)

As shown above, the chart is created by adding Series.Waterfall to the canvas, along with a datalayer. Very few attributes need to be set for the Series element in order to produce a basic chart.

![](https://devnet.logianalytics.com/hc/article_attachments/4419706629655/noteicon.jpg) A datalayer element can be used either beneath Series.Waterfall, as shown above, or beneath Chart Canvas. If used as a child of Chart Canvas, its data is available to *all* child Series elements. This can improve performance if you have several series, all using the *same* data, beneath the same Chart Canvas element.
