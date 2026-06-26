---
title: "Series.Waterfall"
id: 4406817129495
section: "Chart Canvas Chart Elements - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817129495-Series-Waterfall
updated_at: 2022-04-06T06:04:14Z
---

# Series.Waterfall

# Series.Waterfall

The Chart Canvas element's Series child elements cause a data visualization (the chart) to be rendered in the canvas.

The following topics discuss the Series.Waterfall child element:

* [Using Multiple Series](https://devnet.logianalytics.com/hc/en-us/articles/4406817133719-Series-Waterfall-Using-Multiple-Series#Multiple)
* [Series.Waterfall Attributes](https://devnet.logianalytics.com/hc/en-us/articles/4406817130519-Series-Waterfall-Attributes#Attributes)
* [Using the Data Labels Element](https://devnet.logianalytics.com/hc/en-us/articles/4406822167319-Series-Waterfall-Using-the-Data-Labels-Element#Labels)
* [Using the Quicktips Element](https://devnet.logianalytics.com/hc/en-us/articles/4406822168343-Series-Waterfall-Using-the-Quicktips-Element#Quicktips)
* [Using Action Elements](https://devnet.logianalytics.com/hc/en-us/articles/4406817131543-Series-Waterfall-Using-Action-Elements#Action)
* [Using Input Selection](https://devnet.logianalytics.com/hc/en-us/articles/4406817132695-Series-Waterfall-Using-Input-Selection#Selection)
* [Using the Refresh Series Timer](https://devnet.logianalytics.com/hc/en-us/articles/4406817135127-Series-Waterfall-Using-the-Refresh-Series-Timer#Timer)

## About Series.Waterfall

The **Series.Waterfall** element generates a Waterfall chart, which helps in understanding the cumulative effect of sequentially introduced positive or negative values.

![](https://devnet.logianalytics.com/hc/article_attachments/4417575866391/series_waterfall_01.png)

The example above shows a Waterfall chart, with negative values shown in red. A special "total bar", labeled *Profit* above, is automatically generated from the sum of all other values. It appears as the last bar on the right or, at the top, if the axes are swapped. Its generation can be controlled in the Series attributes.

![](https://devnet.logianalytics.com/hc/article_attachments/4417563500055/series_waterfall_02.png)

As shown above, the chart is created by adding Series.Waterfall to the canvas, along with a datalayer. Very few attributes need to be set for the Series element in order to produce a basic chart.

![](https://devnet.logianalytics.com/hc/article_attachments/4417583587863/noteicon.png) A datalayer element can be used either beneath Series.Waterfall, as shown above, or beneath Chart Canvas. If used as a child of Chart Canvas, its data is available to *all* child Series elements. This can improve performance if you have several series, all using the *same* data, beneath the same Chart Canvas element.
