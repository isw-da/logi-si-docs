---
title: "Series.Funnel - Attributes"
id: 4419707367959
section: "Chart Canvas Chart Elements - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419707367959-Series-Funnel-Attributes
updated_at: 2022-07-17T02:09:01Z
---

# Series.Funnel - Attributes

# Series.Funnel - Attributes

The Series.Funnel element has the following attributes:

| Attribute | Description |
| --- | --- |
| Y-Axis Data Column | (Required) Specifies the name of a datalayer column whose values determine the height of each funnel segment. |
| Colors | Sets the colors of the funnel segments, which should be entered as a comma-separated list. Enter a color by name, decimal RGB value, or hex RGB value. Prefix hex values with the pound sign, e.g. #112233.  New for 14.1 Or, enter the token @Gradient to use a gradient fill to represent the data. When there are more segmentsthan colors specified, the listed colors are used again from the beginning. A default set of colors is used if this is left blank and no theme has been applied, see [Chart Canvas Charts](https://devnet.logianalytics.com/hc/en-us/articles/4419715153303-Chart-Canvas-Charts). |
| Disable Mouse Tracking | Disables mouse tracking for the series, when set to *True*. This affects tooltips and click events. For large datasets, this may improve performance. The default value is *False*. |
| Hover Brightness | Specifies the change in a funnel segment's brightness when the mouse pointer hovers over it. Values can be *0* (no change) through *15* (lighter). The default value is *2*. |
| Label Data Column X-axis | Specifies the name of a datalayer column whose values be represented by funnel segments. |
| Label Location | Specifies where funnel segment labels will appear. Options include: *SideLayout* - (the default) labels will appear to the right, with lines connecting them to segments. *Legend* - segments to be identified in a legend. The legend items can be clicked to toggle the visibility of individual segments. *NoLabels* - labels will not be shown. |
| Neck Height | Specifies the height of the "neck", or lower part, of the funnel. May be specified as a number alone, indicating pixels, or with a percentage sign, indicating a percentage of the plot area height. The default is value is *25%*. |
| Neck Width | Specifies the width of the "neck", or lower part, of the funnel. May be specified as a number alone, indicating pixels, or with a percentage sign, indicating a percentage of the plot area width. The default is value is *30%*. |
| Show Data Values | Specifies if the value of each data point should be shown on the chart. Depending on the value of the Label Location attribute, they may be shown alone or with the label values. The default value is *False*. |
| Show Data Values Format | Specifies formatting characteristics for data values. For dates, the non-specific formats, such as *General Date*, *Short Time*, etc., are converted according to the browser's international settings. For very large reports, the non-specific formats perform better. Special formats include: *<* and *>* - change strings to lower and upper case. *Expanded Spaces* - preserves space characters that would otherwise be collapsed by the web browser. *mp* - formats numbers with the "metric prefix". For example, to format 1,234,567 as "$1.23M", enter *$#.00mp*. Supported metric prefixes are from 1000^6 to 1000^-6. For more information see [this page](http://en.wikipedia.org/wiki/Metric_prefix). *qq* - returns the number of the quarter when the value being formatted represents a date. To return the year and quarter together like "2010 Q1", set the format to *yyyy Qqq*. |
| Transparency | Specifies the transparency of the funnel segments. The lowest value of *0* specifies that the background is opaque, with no transparency. At the other end of the scale, *15* specifies a completely transparent background. Use medium-level transparency to allow different seriesto show through each other. |
