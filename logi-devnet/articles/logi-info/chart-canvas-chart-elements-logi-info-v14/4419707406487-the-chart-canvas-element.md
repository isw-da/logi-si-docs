---
title: "The Chart Canvas Element"
id: 4419707406487
section: "Chart Canvas Chart Elements - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419707406487-The-Chart-Canvas-Element
updated_at: 2022-07-17T02:25:01Z
---

# The Chart Canvas Element

# The Chart Canvas Element

The **Chart Canvas** element is the parent, or "container", for all of the other elements used in these charts. As such, its attributes specify the size and appearance of the overall chart, the canvas, and the plot area.

Here are its attributes:

| Attribute | Description |
| --- | --- |
| Alternate Text | Specifies text to be displayed when the browser's options are set to *not* display images. The text is also used by browsers that convert text to speech or Braille output. |
| Animation Duration | Sets the duration of chart animations, in milliseconds. To disable animation, enter a *0* value. |
| Auto Quicktip | Enables the display of Quicktips, with automatically determined information, when the mouse is hovered over data points. To create customized Quicktips, add a Quicktip element under the Series element. |
| Background Color | Sets the canvas background color. Enter a color by name, decimal RGB value, or hex RGB value. Prefix hex values with the pound sign, e.g. #112233. |
| Background Color Transparency | Specifies the transparency of the canvas background color. The lowest value of *0* specifies that the background is opaque, with no transparency. At the other end of the scale, *15* specifies a completely transparent background. Use medium-level transparency to allow different chart layers to show through each other. |
| Border Color | Sets the canvas border line color. Enter a color by name, decimal RGB value, or hex RGB value. Prefix hex values with the pound sign, e.g. #112233. |
| Border Color Transparency | Specifies the transparency of the canvas border line color. The lowest value of *0* specifies that the border line is opaque, with no transparency. At the other end of the scale, *15* specifies a completely transparent line. Use medium-level transparency to allow different chart layers to show through each other. |
| Border Radius | Sets the amount of rounding for canvas border line corners, in pixels. |
| Border Thickness | Sets the canvas border line thickness, in pixels. The default value is *0*, for no border. |
| Caption | Specifies the text for the chart main title. Line feeds may be used in this attribute. In Logi Studio, open the Attribute Zoom window for this attribute and use the Enter key while typing text to introduce line feeds where desired. The text will appear on different lines when the chart is drawn. |
| New for 14.2 Chart Description | Specifies the text for the chart's description. The default value for this attribute is *empty*. Enter a description to enable this feature. |
| Class | Specifies the Cascading Style Sheet class used by the element. When set, this class will also be used by all child elements that don't have their own class. The class should be defined in the report's style sheet file or theme. |
| Height | Specifies the height of the canvas, in pixels. If left blank, a height will be determined automatically. Must be set to a value in order to export chart to PDF. |
| MinHeight | Specifies the minimum height of the canvas. Set this value to greater than the chart's current height to enable scroll bars. |
| MinWidth | Specifies the minimum width of the canvas. Set this value to greater than the chart's current width to enable scroll bars. |
| No Data Caption | Specifies text to be shown in the plot area when no data is received in the chart's datalayers. |
| No Debugger Link | Specifies whether or not individual chart debug icons will appear when debugging is turned on. You may want to suppress them to reduce "visual clutter" and ensure a realistic layout when debugging a page. The default value is *False.* |
| Orientation | Allows swapping of the X- and Y-axes. The default value is *Vertical*, meaning data points are plotted on the Y-axis and labels are listed across the X-axis. |
| Plot Background Color | Sets the plot area background color. Enter a color by name, decimal RGB value, or hex RGB value. Prefix hex values with the pound sign, e.g. #112233. |
| Plot Background Color Transparency | Specifies the transparency of the plot background area color. The lowest value of *0* specifies that the border line is opaque, with no transparency. At the other end of the scale, *15* specifies a completely transparent line. Use medium-level transparency to allow different chart layers to show through each other. |
| Plot Background Image | Specifies the complete URL of an image to be displayed in the chart plot area (a chart "background" image). Use CSS, rather than this attribute, to specify a background image for the entire canvas. |
| Plot Border Color | Sets the plot area border line color. Enter a color by name, decimal RGB value, or hex RGB value. Prefix hex values with the pound sign, e.g. #112233. |
| Plot Border Color Transparency | Specifies the transparency of the plot area border line color. The lowest value of *0* specifies that the border line is opaque, with no transparency. At the other end of the scale, *15* specifies a completely transparent line. Use medium-level transparency to allow different chart layers to show through each other. |
| Plot Border Thickness | Sets the plot area border line thickness, in pixels. The default value is *0*, for no border. |
| Polar | Set to *True* to transform Cartesian charts (e.g. Area, Bar, Line, and Spline) into the Polar/Radial coordinate system, producing a "Polar Chart". The default value is *False*. |
| New for 14.2 Show DrillTo Breadcrumb | Specifies whether the breadcrumb trail displays when using the Drill To feature. The default value is *False*, no breadcrumb trail displays. |
| Spacing Bottom | Sets the space between the bottom edge of the chart content (including the plot area and labels) and the bottom border of the chart, in pixels. The default value is *15* pixels. |
| Spacing Left | Sets the space between the left edge of the chart content (including the plot area and labels) and the left border of the chart, in pixels. The default value is *10* pixels. |
| Spacing Right | Sets the space between the right edge of the chart content (including the plot area and any labels) and the right border of the chart, in pixels. The default value is *10* pixels. |
| Spacing Top | Sets the space between the top edge of the chart content (including the plot area and any captions) and the top border of the chart, in pixels. The default value is *10* pixels. |
| SubCaption | Specifies a subcaption for the chart, which normally appears below the chart caption. Line feeds may be used in this attribute. In Logi Studio, open the Attribute Zoom window for this attribute and use the Enter key while typing text to introduce line feeds where desired. The text will appear on different lines when the chart is drawn. |
| New for 14.2 Tooltip Split | Specifies whether the tooltip displays the value per segment, or per series. The default value is *False*. To enable this feature, set the attribute to *True*. The following charts do not possess this capability: Gauge, Pie, Funnel, Pyramid, and Heatmap. Furthermore, when the Chart Orientation attribute is set to *Swap Axes*, and the Polar attribute is set to *True*, this feature will not work.  This option takes precedence over tooltip.shared. |
| Width | Specifies the width of the canvas. By default, the unit of measure is pixels, but you may type in a value and the percent sign to indicate a percentage of its container. If left blank, a width will be determined automatically. Must be set to a value in order to export chart to PDF. |

It's recommended that you set a unique element ID for charts if there will be more than one chart in a definition.

## Getting Data

The example shown earlier used a datalayer beneath the Chart Canvas element, which makes the data retrieved available to *all* of its other child elements.

![](https://devnet.logianalytics.com/hc/article_attachments/7522817656599/introcccharts_04a.png)

However, as shown above, instead of using a common datalayer, you can use *individual* datalayers beneath the child elements, where appropriate, to give them their own data.

![](https://devnet.logianalytics.com/hc/article_attachments/7522725232151/criticalicon.png) Do not mix these two arrangements. Either use a single datalayer as a child of the Chart Canvas element OR a datalayer as a child of each Series element. *Do not* use a datalayer as a child of the Chart Canvas element AND a datalayer as a child of one or more Series elements.

![](https://devnet.logianalytics.com/hc/article_attachments/7522817678615/introcccharts_04b.png)

As shown in the example above, when using Chart Canvas charts as the child of an element that has its own datalayer, such as a DataTable or Google Map, you must use @Chart tokens, not @Data tokens,in any elements used to condition the chart's datalayer.

![](https://devnet.logianalytics.com/hc/article_attachments/7522725179159/noteicon.png) Due to order-of-operations differences, datalayers that have the [Handle Quotes Inside Tokens](https://clm.logianalytics.com/rdPage.aspx?rdReport=ElementRefDetail&itemID=999&iName=HandleQuotesInTokens&iType=Attribute&iLabel=Handle+Quotes+Inside+Tokens&lnkpg=0&dnView=G-I&dnSelect=Attribute) attribute set to *True* will not process quotes as expected when used underneath Chart
Canvas elements. In this scenario, we recommend that you use the datalayer under Local Data and link it to a datalayer for the chart.

![](https://devnet.logianalytics.com/hc/article_attachments/7522725232151/criticalicon.png) When **DataLayer.MDX** is used as a child of Chart Canvas, only *one* Series element may be used. The datalayer cannot be used as the child of a Series element.
