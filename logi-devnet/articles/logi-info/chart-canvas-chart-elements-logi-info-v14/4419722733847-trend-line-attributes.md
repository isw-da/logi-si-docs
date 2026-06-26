---
title: "Trend Line Attributes"
id: 4419722733847
section: "Chart Canvas Chart Elements - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419722733847-Trend-Line-Attributes
updated_at: 2022-07-17T02:08:50Z
---

# Trend Line Attributes

# Trend Line Attributes

The Trend Line element has the following attributes:

| Attribute | Description |
| --- | --- |
| Color | Sets the line color. Enter a color by name, decimal RGB value, or hex RGB value. Prefix hex values with the pound sign, e.g. *#112233*. New for 14.1 Or, enter the token @Gradient to use a gradient fill to represent the data. |
| ID | The unique element ID. |
| Legend Label | Specifies the text that will be shown inside the chart legend for the trend line. A value *must* be provided here for an entry to appear in the legend. |
| Line Algorithm | Specifies the regression algorithm that will be used to generate the data points plotted by the trend line. Options include *LinearRegression* (the default) and the curve-fitting *LOWESS* algorithm. |
| Line Style | Specifies the pattern of the trend line as either *Solid* (the default) or a combination of dashes and/or dots. |
| Line Thickness | Specifies the thickness of the line, in pixels. The default value is *1* pixel. |
| Transparency | Specifies the transparency of the line color. The lowest value of *0* specifies that the line is opaque, with no transparency. At the other end of the scale, *15* specifies a completely transparent line. |
