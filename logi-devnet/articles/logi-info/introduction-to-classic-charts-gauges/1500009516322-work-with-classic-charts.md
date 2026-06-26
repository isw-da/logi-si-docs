---
title: "Work with Classic Charts"
id: 1500009516322
section: "Introduction to Classic Charts & Gauges"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009516322-Work-with-Classic-Charts
updated_at: 2021-06-17T01:58:47Z
---

# Work with Classic Charts

# Work with Classic Charts

From the beginning, Logi Info and Logi Report have offered a range of **Chart** and **Gauge** visualization elements, now collectively called "classic charting elements", that developers can include in their reports and applications. This topic discusses the use of those elements and provides guidance for implementing them. Sections include:

* About Classic Charts
* [General Chart Appearance](#General)
* [Data Retrieval and Appearance](#Data)
* [Title, Labels, and Legends](#Legends)
* [Drill-Down and Drill-Through Capabilities](#DrillDown)
* [Interactive Chart Configurations](#Interactive)
* [Working with Needle Gauges](#NGauges)
* [Default Color Sets](#DefaultColorSet)
* [Chart Release Notes](#RelNotes)

## About Classic Charts

Logi charting elements provide numerous **powerful features** for creating charts and maps. The discussion below provides an overview of how to work with these elements but is not intended to be an exhaustive survey of all the elements and attributes available.

Additional documents, focused on individual chart types, are being added to the Developer Library to provide more detail. The information presented here is intended to allow developers to quickly gain an understanding of how Logi charting elements work and to rapidly create simple charts.

Note that, due to the varying nature of the elements, the attributes used in examples below are not *all* available for *all* charting elements. Attributes and child "helper" elements may be quite chart-style specific; developers need to apply common sense when implementing charts based on the examples shown here.

Developers unfamiliar with Logi classic charting elements are encouraged to read [Introduction to Classic Charts & Gauges](https://devnet.logianalytics.com/hc/en-us/articles/1500009531141-Introduction-to-Classic-Charts-Gauges) before proceeding.

In v11.2.040, we introduced a new set of charting elements collectively called "Chart Canvas" charts. This document *does not* discuss those charts. See [Chart Canvas Charts](https://devnet.logianalytics.com/hc/en-us/articles/1500009515382-Chart-Canvas-Charts) for information about these new charts.

Logi Studio includes **wizards** that can assist you in adding and configuring charts for your application.

## General Chart Appearance

When reports are generated, each charting element is **rendered** in an "image space" and the elements have attributes that allow developers to control the **size** and **color** of that space. The shape of the image space may not match the shape of the data portion of the chart.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778400535/workcharts_01.gif)![](https://logianalytics.zendesk.com/hc/article_attachments/4402771466391/workcharts_01a.gif)

For example, as shown above, even though the chart is round, the **Height**, **Width**, and **Background Color** attributes refer to its rectangular image space. The Height and Width values use **pixels** as their unit of measurement and can be set using tokens.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771466647/workcharts_01d.png)![](https://logianalytics.zendesk.com/hc/article_attachments/4402771466903/workcharts_01e.png)

As of version 9.5, *in Logi Info only*, static charts can have a new child, the **Resizer** element. This element displays resizing "handles", as shown above, so that the chart can be **dynamically resized** by the user at runtime. Resizer changes are maintained within the Session, so every return visit to the report will maintain the size changes. Maximum and minimum sizes can be specified by the developer. In versions prior to 10.0.428, the appearance of the resizing handles was slightly
different, and in v10.2.424, they were changed to remain hidden until  the mouse pointer hovers over them.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778400791/workcharts_04.gif)![](https://logianalytics.zendesk.com/hc/article_attachments/4402771467159/workcharts_04a.gif)![](https://logianalytics.zendesk.com/hc/article_attachments/4402771467415/workcharts_04b.gif)

Many elements have a **Colors** attribute to set the colors for the data portions of the chart. If this attribute is left blank, a default color set is used, or a custom color set can be entered as a **comma-separated list**, as shown above.

Color values can be a **name** (LightBlue), a **decimal RGB** value (255,255,255) or a **hex RGB** value (#112233). In Studio, click the browse button next a color attribute value to open the **Color Selector** window and visually select colors. Color names can be followed by the word "Metallic" to produce a special effect; the word "Transparent" can also be entered as a value.

As of v10.0.227, two new attributes allow colors to be set using **data**. Chart.Pie and Chart.XY now include attributes that identify a column in the datalayer as the source for color information for static pie and bar charts.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778401047/workcharts_03c.gif)![](https://logianalytics.zendesk.com/hc/article_attachments/4402778401303/workcharts_03d.gif)

In Line, Area, Bar and other charts that use a background grid of lines to help the eye follow values, as shown above, the color of the **grid lines** can be controlled. The same properties are available for the **border** around of the edge of the canvas.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771467671/workcharts_04c.gif)![](https://logianalytics.zendesk.com/hc/article_attachments/4402771467927/workcharts_04d.gif)

The data portions of **Animated Chart.XY** charts are rendered on a "canvas", which can have its own background color, as shown above, which is set using the **Canvas Background Color** attribute. A compatible color is automatically generated for alternating values.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778401559/workcharts_04e.gif)![](https://logianalytics.zendesk.com/hc/article_attachments/4402778401815/workcharts_04f.gif)

In **static Line** charts, as shown above, the attribute that controls the canvas color is the **Plot Area Background Color**. Different colors for alternating values can be shown by entering a comma-separate list of values.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771468183/workcharts_01b.jpg)![](https://logianalytics.zendesk.com/hc/article_attachments/4402778402071/workcharts_01c.gif)

In **static****Chart.XY** charts (Area, Bar, Line) individual attributes control the colors of the data, plotting area background, and borders. Version 9.2 and later includes attributes for applying color gradient effects and for rounding outer border corners.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771468439/workcharts_01f.png)![](https://logianalytics.zendesk.com/hc/article_attachments/4402771468695/workcharts_01g.png)

As of v9.5, static **Chart.Pie** includes a **Chart Texture** attribute which can be used to apply different appearances to the chart surface. 3-D depth and 3-D angle can also be configured.

In v10.1.46, the **Chart Texture** attribute was provided for the **Chart.Heatmap** element, as well.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771468951/workcharts_02.gif)![](https://logianalytics.zendesk.com/hc/article_attachments/4402778402327/workcharts_02a.gif)![](https://logianalytics.zendesk.com/hc/article_attachments/4402771469207/workcharts_02b.gif)

Many charts also have a **3-Dimensional** attribute which controls rendering in 2-D or 3-D, as shown above. The 3-D rendering process affects not only the data portions of the chart but the canvas, too. In the case of Gauge.Needle, the **Needle Gauge Enclosure** attribute can even add a very realistic-looking "glass cover" over the face of the gauge.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771469463/workcharts_03.gif)![](https://logianalytics.zendesk.com/hc/article_attachments/4402771469719/workcharts_03a.gif)![](https://logianalytics.zendesk.com/hc/article_attachments/4402771469975/workcharts_03b.gif)

As shown above, many charts also have a **Transparency** attribute, which can be useful for letting different chart layers show through each other. The lowest value for this attribute is 0 (or blank), which makes the chart opaque, and the highest is 15, which makes the chart completely transparent. Note that this *does not* affect the canvas itself.

All charts can be saved as image files by right-clicking them and selecting **Save** from the popup menu. Animated Pie charts have additional runtime features available via their popup menu, including **Rotation** and **Slicing** (clicking a slice to explode it out from the pie).

## Data Retrieval and Appearance

Data is generally introduced into charts by adding a **datalayer** as a child of the charting element. The datalayer retrieves the data to be charted and supplies it, record by record, to the chart for plotting. The datalayer can make use of **grouping**, **filtering**, and all the other modifier elements generally available to datalayers in order to shape the data it retrieves. The [Formatted Column](https://devnet.logianalytics.com/hc/en-us/articles/1500009530781-The-Formatted-Column) element can
be particularly
useful in getting data in the datalayer formatted correctly for use in charts.

**Animated Gauges** can draw their data from a child datalayer or from external data, such as Local Data, Session, and Request tokens. However, they're not designed to be used in a report page where there are multiple gauges, each with its own child datalayer. In this case, all of the gauges will draw data *only* from the *first* child datalayer. If you have a multi-gauge page such as this in mind, design your report to use Local Data to retrieve *all* of the data needed for *all*
of the gauges, then use tokens to provide the data to the gauges.

Beginning in v10.0.299, an animated "loading" image is displayed if there's a delay in retrieving data for the chart. In v10.2.314, a new attribute, **Show Wait Icon**, was added. This attribute defaults to *True*, but you can set it to *False* if you do not want the animated icon to appear.

Beginning in v10.1.18, chart processing became **multi-threaded** and **asynchronous** so, for example, charts in multiple dashboard panels could be retrieved simultaneously. On web servers with multiple cores or multiple processors, chart generation tasks will be spread across them for even better performance.

What if no data is returned to the datalayer? Instead of displaying the chart, animated charts will automatically generate a "No data to display message". As of v10.0.85, the **Zero Rows Message** element can used to display the message of your choice in similar circumstances when using static charts.

Values from the datalayer can be used to draw the **boundaries** of graphics in the chart (the height of a bar, the size of a pie slice, etc.) and to supply **text** that appears in **tooltips**, **legends**, and chart **labels**.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771470231/workcharts_05.gif)![](https://logianalytics.zendesk.com/hc/article_attachments/4402778402583/workcharts_05a.gif)

The chart element's **Data Column Y-axis** attribute value is set to the name of a column from the chart's datalayer, causing its value for each record to be charted. This adds one **data series** to the chart.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778402839/workcharts_06.gif)![](https://logianalytics.zendesk.com/hc/article_attachments/4402778403095/workcharts_06a.gif)

**Labels** along the X-axis, based on the data, are created using the chart element's **Label Column X-axis** attribute, which is set to the name of another column in the datalayer.

 ![](https://logianalytics.zendesk.com/hc/article_attachments/4402771470487/workcharts_06b.png)

Data and Label values can be formatted for presentation, using several child elements, such as **Format Data** and **Format Label**. In v10.2.424, these two elements were *deprecated* for static charts, except Chart.Pie and Chart.Polar, but in v11.0.519 Format Data was reinstated for Chart.XY. At the same time, a new **Format** attribute was added to the **Data Scale** and **Label Scale** elements, providing the same functionality, as shown above.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778403351/workcharts_07.gif)![](https://logianalytics.zendesk.com/hc/article_attachments/4402771470743/workcharts_07a.gif)

In the example above, **three** data series are shown on a line chart. The basic chart will display one data series; to add additional series, **Extra Data Column** elements are added below the chart element. Each of these elements has an attribute that's set to the name of another column in the datalayer.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771470999/workcharts_08.gif)![](https://logianalytics.zendesk.com/hc/article_attachments/4402771471255/workcharts_08a.gif)![](https://logianalytics.zendesk.com/hc/article_attachments/4402771471639/workcharts_08b.gif)

In the example above, the chart type has been changed to a **Bar Chart**. On the left, the three data series appear as **side-by-side** bars, and on the right, as **stacked** bars. This behavior is controlled by the chart's **Extra Bar Options** attribute, shown above right.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778403607/workcharts_08.png)

You can show the data values *inside* stacked bars in a Static Bar Chart by setting the chart's **Stacked Bar Labels** attribute to *Individual*, as shown above. The default option, *Aggregate*, displays a single, combined value above the top of each stack.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778403863/workcharts_07b.png)![](https://logianalytics.zendesk.com/hc/article_attachments/4402771471895/workcharts_07c.png)

Static Chart.XY charts can have two Y-axes. The **Secondary Data Axis** element controls a secondary axis, normally appearing on the *right* side of a grid. In the example shown above, this is the "Orders" axis. This other axis represents data for an Extra Grid Layer, and has its own independent scale. Child elements, including those shown above can be used to format that data and axis appearance.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771472151/workcharts_24.png)

The tick marks displayed just outside the axis borders in Static Chart.XY charts can be shown or hidden, by setting the **Tick Marks** attribute in the **Data Font** and **Label Font** elements.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778404119/workcharts_08c.gif)![](https://logianalytics.zendesk.com/hc/article_attachments/4402771472407/workcharts_08d.gif)

The style and width of the lines representing data in Line charts can be formatted using the **Line Style** and **Line Width** attributes, as shown above. Solid, and a variety of dotted and dashed, line styles are available. New attributes in v9.5.55 allow the Line Style and Line Color to be set from a data column.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771472663/workcharts_25.png)

The appearance of static line charts can also be data-driven by setting the **Line Color Data Column** and **Line Style Data Column** attributes. This allows you to have different colors for different line segments, as shown above.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778404375/workcharts_08k.gif)![](https://logianalytics.zendesk.com/hc/article_attachments/4402778404631/workcharts_08l.gif)

As of v9.5.55, in Line and Scatter charts, the data points can be emphasized with **symbols**, as shown above. The size of the symbol, in pixels, can be set and symbols choices include Circle, Cross, Diamond, Glass Sphere, Solid Sphere, Square, Triangle, X and others. In v10.0.337, the ability to enter a comma-separated list of symbols as the Symbol attribute value was added for Line and Spline-types of Chart.XY. This allows a different symbol to be used for each data series.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771472919/workcharts_08i.gif)![](https://logianalytics.zendesk.com/hc/article_attachments/4402778404887/workcharts_08j.png)

Line chart lines can be made **discontinuous** by replacing null data values with the value **1.7E+308**, producing "broken" lines.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771473175/workcharts_08e.gif)![](https://logianalytics.zendesk.com/hc/article_attachments/4402771473687/workcharts_08f.gif)

A "trend line" can be added to static reports to give a general impression of the trend of the data. The **blue trend line** in the example above was included by adding a **Trend Line** element as a child of the chart element. The calculation involved in determining the trend line angle occurs automatically; line width and color can be set through attributes.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778405143/workcharts_08m.gif)![](https://logianalytics.zendesk.com/hc/article_attachments/4402778405655/workcharts_08n.gif)

The **Lowess Curve Line** element, available with release 9.5.78, creates a
trend line (in blue, above) that fits a curve through a static Chart.XY's data
points using the Lowess Curve Fitting algorithm.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771473943/workcharts_06c.png)

Static and Animated Pie charts can be configured so that one or more of their pie wedges are displayed as "exploded", as shown above. This is done using the **Exploded Wedges Column** attribute, which specifies a datalayer column whose values determine wedge state. Non-zero values in that column will cause the wedge for the corresponding X-axis value to be exploded. Typically, the developer will add a **Calculated Column** to the datalayer, with a formula that evaluates to *1* or
*0*, and specify that column in the Exploded Wedges Column attribute.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778405911/workcharts_08g.gif)![](https://logianalytics.zendesk.com/hc/article_attachments/4402771474199/workcharts_08h.gif)

Tooltips can be also added to charts, by setting the **Tooltip Column** (animated charts) or **Tooltip** (static charts) attribute. This causes identifying data from the datalayer to be displayed as a tooltip, as shown above, when the mouse hovers over a portion of the chart. The Tooltip Column requires only the name of a column from the datalayer, while the Tooltip attribute requires the use of an @Chart token to display data. For animated charts, a **Tooltip Font** element is available for formatting
the tooltip.

Beginning in v10.1.46, certain charts can include a feature called **Quicktips**:

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771474455/workcharts_19.png)

The **Quicktip** element, shown above left, is added as a child of the chart element and provides a small, popup "balloon" at the cursor location. The Quicktip allows the balloon to have a title and one or more rows of text. Data values can be shown by configuring the Quicktip element with the @Chart token.

In summary, data is retrieved for use in a chart by a **datalayer**. Typically, a chart on its own will display one data series but, with the addition of other helper elements, it can be made to show additional data series.

### Refresh Animated Chart.XY in Realtime

In v11.1.033, the **Realtime Update** element was introduced. It transforms an **Animated Chart.XY** into a chart that updates itself periodically, by adding new data values at its right side and scrolling the X-axis horizontally.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778406167/workcharts_19a.png)

The example above shows a Line chart displaying a value as it changes, once per second. The Realtime Update element uses AJAX technology to automatically refresh its Animated Chart parent element, based on an interval set in seconds. It works by re-running just that portion of the report that retrieves the chart data and passing it back to the browser to update the chart. The data is accumulated internally and re-processed each time the chart is displayed.

If **Extra Data Column** elements are used, they're displayed as additional lines in Line charts, and as stacked values in Area and Bar charts.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771474967/workcharts_19b.png)

As shown above, the Realtime Update element is used by adding it beneath the Animated Chart.XY element. Its only attribute is the required **Refresh Interval** attribute, which is specifies, in seconds, how frequently to refresh the chart.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771462807/stopicon.gif) Note that the Realtime Update element *cannot* be used with a chart whose datalayer has a **Crosstab Filter** applied to it.

## Title, Labels, and Legends

Logi charting elements include numerous attributes and supporting elements that can be used to tailor their chart titles, labels, and legends. These help developers get the right "look" for their charts, thereby helping users understand what they're seeing.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771475479/workcharts_10.gif)![](https://logianalytics.zendesk.com/hc/article_attachments/4402771475735/workcharts_10a.gif)

Space for titles is automatically allocated for all charts. For static charts in pre-v9.5 releases, or if the developer desires to do it manually, this can be done, as shown above, using the **Top**, **Bottom**, **Left**, and **Right****Border** attributes.

These indicate, in **pixels**, the distance on each side from the chart **canvas** to the **edge** of the chart image space. The overall vertical size of the chart is therefore calculated
as the sum of the Top Border + Height + Bottom Border. The horizontal size calculation is Left Border + Width + Right
Border.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771475991/workcharts_09.gif)![](https://logianalytics.zendesk.com/hc/article_attachments/4402778406679/workcharts_09a.gif)

**Titles** for the chart, data, and labels can be set using the **Chart Title**, **Data Title** and **Label Title** attributes as shown above.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778406935/workcharts_10.png)    ![](https://logianalytics.zendesk.com/hc/article_attachments/4402778407191/workcharts_10a.png)

Static Chart titles that are longer than the width of the chart itself are automatically truncated and have an ellipsis ("...") appended to them, as shown above left. In Animated Charts, they wrap.

Static Charts can also use the **Chart Title Font** child element to set the title font, color, size, angle, and alignment.

Static Chart titles can also be rendered in **multiple colors**, as shown above right, by using CDML tags directly in the **Chart Title** attribute value to specify different
font colors, sizes, etc. Find out more about CDML in *[Advanced Chart Title Formatting](https://devnet.logianalytics.com/hc/en-us/articles/1500009513902-Format-Classic-Chart-Label)*. The example shown above was produced using this value:

<\*color=0000FF\*>Multi-Color <\*color=FFD700\*>Chart <\*color=BA55D3\*>Titles <\*color=000000\*>Available Too!  
 

All charts include a **Max Label Length** attribute, which specifies the maximum number of characters that will be displayed for a label before the text is trimmed and the remainder replaced with an ellipsis (...). This truncation is also applied to Legend labels for Chart.Pie, if a Legend is in use (it is *not* applied to legends for other types of charts).

Static XY and Pie charts include a **Label Column Data Type** attribute, which can be used to set the way in which the charting engine will interpret the data specified in the column named in Label Data Column X-axis. This can be useful, for example, when you want dates in the data to be presented as text in the chart's X-axis labels.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778407447/workcharts_11.gif)![](https://logianalytics.zendesk.com/hc/article_attachments/4402771476247/workcharts_11a.gif)

As shown above, labels can be formatted by adding a **Label Font** element, providing control over font family, size, color, angle, and decimal point appearance. *Font angle is only configurable for static charts, not for animated charts*.

A **Label Scale** element is also available for controlling the appearance, size, and frequency of **tick marks** along the scales. One of its modes is *LinearTime*, which plots points evenly end-to-end according to an x-axis value, for use with line and area charts.

Labels can also be formatted using the **CDML** formatting language mentioned earlier.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771476759/workcharts_09b.gif)![](https://logianalytics.zendesk.com/hc/article_attachments/4402778407703/workcharts_09c.gif)

In version 9.2 and later, attributes of the **static Pie** chart allow the position, shape, and shading of pie chart labels to be set.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778408087/workcharts_12.gif)![](https://logianalytics.zendesk.com/hc/article_attachments/4402778408343/workcharts_12a.gif)

**Legends** provide an explanation of some of the **visual information** in a chart, often color-related. In the example above, the legend associates products with colors. In Static Charts, two elements, **Legend** and **Legend Font**, provide control of the location, size, font, border, orientation, and background color of legends. In some Animated Charts, providing a value for their **Legend Title** attribute automatically generates the legend. The association between the colors and the
data is generated automatically.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778408599/workcharts_12.png)

When the Legend element's **Legend Filter** attribute has been set to *True*, it becomes possible to dynamically filter the data in some Static Charts, including Pie, Line, Area, Bar, and Polar charts, by clicking items in the Legend, as shown above.

## Drill-Down and Drill-Through Capabilities

Users frequently want to be able to get **detailed information** about the data shown in charts. Developers can provide this "drill-down" functionality in Logi applications by including **Action** elements in report definitions.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771477015/workcharts_13.gif)![](https://logianalytics.zendesk.com/hc/article_attachments/4402778408855/workcharts_13a.gif)

For example, adding an **Action.Report** and **Target.Report** element as children of the **Animated Chart.Pie** element will cause each wedge in a Pie chart to become a link to the target report.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778385687/attnicon.gif)  Note that, when a chart uses its own datalayer element to retrieve data, that data is accessed with an **@Chart** token, not the @Data token that's used with data tables.

Data specific to each pie wedge can be passed to the target report using **Link Parameters** and an @Chart token. The target report can then take action, such as filtering its own data, based on an @Request token representing the Link Parameter value.

### Automatic Drill-Through Report

Charts often use grouping to aggregate data for a consolidated view. There are times, however, when it's useful to be able to examine the detail data that was used to create that view. The **Group Drillthrough** element was introduced for this purpose, in Logi Info, v10.0.385. *Feature not available in Logi Report*.

Group Drillthrough works with Chart.XY, Chart.Pie, Chart.Heatmap, and Chart.Scatter.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771477271/workcharts_13b.png)![](https://logianalytics.zendesk.com/hc/article_attachments/4402771477527/workcharts_13c.png)

In the example shown above, a **Group Drillthrough** element has been added beneath a Chart.Pie element. All of the element's attributes, other than **ID**, are optional but the example shows that a custom caption and an export button selection have been entered. More information about the attributes can be found in the element's [Element
Reference page](https://devnet.logianalytics.com/rdPage.aspx?rdReport=ElementRefDetail&itemID=2471&iName=GroupDrillthrough&iType=Element&iLabel=Group+Drillthrough&lnkpg=0).

The resulting pie chart looks no different than usual, but when one of its wedges is clicked,

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771477783/workcharts_13d.png)

a detail report, like the example shown above, is automatically generated, containing all of the relevant detail data.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778385687/attnicon.gif) Note that the Group Drillthrough element is designed to work charts with datalayers that have a **Group Filter**, **Crosstab Filter**, or **Relevance Filter** child element. This has implications if you want to use Group Drillthrough and you're working with DataLayer.SQL; for example, you'll have to use a Group Filter element instead of doing the grouping in your query.

The Group Drillthrough element's attributes allow you to customize certain aspects of the detail report. You can also include **Drillthrough Column** elements beneath the Group Drillthrough element; they allow you to set the number columns that will appear in the report and to customize their appearance.

## Interactive Chart Configurations

All of the charting elements' attributes can be "tokenized"; that is, you can use **tokens** in them as values. This allows charts to be **highly-interactive** and dynamically **customizable**.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771478039/workcharts_14.gif)

For example, a report page could include an **Input Select** element that presents the user with a choice of chart types: Bar, Line, Area. When the user makes a selection, the report is refreshed and their selection is passed as a **Link Parameter.** The resulting @Request token is used in the **Animated Chart.XY** element's **Chart Type** attribute, as shown above, to dynamically set the chart type. Other examples:

* Through the use of cookies and **@Cookie** tokens, chart configurations can be "personalized" for individual users and the settings **retained** between sessions.

* Charts can be included in reports as child elements of tables and have a "data-driven" configuration, using **@Data** tokens to provide values for chart attributes.

The chart configuration **flexibility** available through the use of tokens is quite **extensive**, providing opportunities for user-customizable chart size, colors, type, content, and more.

### Hover Highlight

The **Hover Highlight** child element causes chart features, such as bars and lines, to be highlighted
when the mouse pointer is hovered over them, making it easier for users to visualize the
item under the pointer. The element is available for use with static Pie, Bar, Line, Area, and Scatter charts.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771478295/workcharts_26.png)

The element's attributes enable customization of the highlight
overlays. The **Fill Color** attribute applies to Pie and Bar charts, the **Border Color** and **Border
Width** attributes to Line, Area, and Scatter charts, and **Line Color** applies to Line and
Area charts.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778385687/attnicon.gif)  Note that attempts to use the *ThemeAlignCenter* class, or other CSS classes that use text-align, on a container such as a DIV in order to center a chart that includes Hover Highlight are likely to fail. Hover Highlight is not a simple HTML entity, like text or an image, that other content can flow around; it's wrapped in its own
DIV
and no longer behaves like block content. One possible alternate approach is to use an HTML table instead of a DIV as the container. Due to its non-standard behavior, this kind of centering *will* work with IE 9 only.

### Zoom Chart

Introduced in Logi Info v10.2.424, the **Zoom Chart** element provides users with the ability to "zoom" into a chart's data by selecting an area on the chart. The Zoom Chart is available for use with **static** Chart.XY and Chart.Scatter elements.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778409111/workcharts_20.png)

There are two configurations of the Zoom Chart. In the first, shown above left, the "selection area" appears right over the parent chart. Resizing handles allow its size to be adjusted and it can also be dragged horizontally. When the mouse button is released, the parent chart zooms in or out to include just the data within the selection area, as shown above right. Successive selections can be made on the zoomed chart. The "Show All" button returns the view to encompass all of the
original data.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771478551/workcharts_21.png)

In the second configuration of the Zoom Chart, a smaller version of the parent chart, with selection area, appears *below* the parent chart. Changes to the selection area cause the view of the data in the parent chart to change correspondingly.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771478807/workcharts_22.png)![](https://logianalytics.zendesk.com/hc/article_attachments/4402771479063/workcharts_22a.png)

As shown above, the **Zoom Chart** element is added as a child of the parent chart and its attributes allow you to customize the selection area and chart. The **Location** attribute is set to *None* to display the selection area over the parent chart; setting it to *Bottom* displays the small selection chart beneath it.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778409367/workcharts_23.png)![](https://logianalytics.zendesk.com/hc/article_attachments/4402771479319/workcharts_23a.png)

A **Label Scale** element is also *required*, as shown above, with a **Scaling Mode** set to one of the *Linear* options (based on your X-axis data type).

### InputChart.List and InputChart.Range

Two new elements were added in v11 that allow users to work with charts as *user input* elements. Users can select data values on a chart and pass them, in manner similar to other user input elements, through Request tokens to other definitions. Both **InputChart.List** and **InputChart.Range** are added as the parent element to a static chart element.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778409623/workcharts_27.png)

As shown above, **InputChart.List** works with static Bar and Pie charts. At runtime, chart bars (or wedges) can be clicked to select them. When the report page is submitted, the X-axis values are submitted to the next definition as a Request token that includes the chart ID, whose value is comma-separated list. For example:

@Request.ChartXY\_Bar~ = "Condiments,Produce,Seafood"  
 

would result from submitting the example above. The element includes attributes common to user input elements and attributes for specifying the colors of selected and unselected bars or wedges. Standard, unrelated **Action** elements (not shown) are required to submit the page.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771479575/workcharts_28.png)

As shown above, **InputChart.Range** works with static Line, Spline, and Scatter charts. At runtime, a "selection area" can be "drawn" (by dragging the mouse) onto the chart plotting area to select values. When the report page is submitted, the maximum and minimum X-axis and Y-axis values are submitted to the next definition as individual Request tokens. For example:

@Request.minX\_value~ = "2/20/2012"  
@Request.maxX\_value~ = "3/31/2012"  
@Request.minY\_value~ = "0"  
@Request.maxY\_value~ = "1200"

would result from submitting the example above. Clicking outside of the selection area will clear it. The element includes attributes for specifying the names of the request variables to be associated with the value range and the colors of the selection area. Two special child event handler elements, **Area Drawn** and **Area Cleared**, can be used to fire standard Action elements, as shown, when the selection area is drawn or cleared, refreshing or submitting the page. In addition, or instead, standard,
unrelated **Action** elements (not shown) can also be used to submit the page.

More information is available in our document [Introduction to User Input Elements](https://devnet.logianalytics.com/hc/en-us/articles/1500009515582-Introduction-to-User-Input-Elements).

## Working with Needle Gauges

Static needle gauges look like speedometers: they have a needle pointer that swings through an arc and indicates a data value on a scale. Gauge shapes include half-round, quarter-round, and rectangular.

The **Start Angle** and **Total Angle** attributes of the **Gauge.Needle** element govern the possible positions of the needle pointer. This table provides information about configuring these gauges. Attributes left blank have been removed from the images.

|  |  |
| --- | --- |
| **Gauge Shape** | **Description** |
|  | Round gauge; Start Angle value minimum = 0, Total Angle maximum = 360. |
|  | Half-round gauge; type can be:   * *HalfTop* (shown) - Start Angle value minimum = 180, Total Angle maximum = 180 * *HalfBottom* - Start Angle value minimum = 0, Total Angle maximum = 180. |
|  | Quarter-round gauge: type can be   * *QuarterTopLeft* (shown) - Start Angle value = 180, Total Angle = 90 * *QuarterTopRight* - Start Angle value = 270, Total Angle = 90 * *QuarterBottomRight* - Start Angle value = 0, Total Angle = 90 * *QuarterBottomLeft*. - Start Angle value = 90, Total Angle = 90 |
|  | Rectangular gauge; type set to *HalfTop*. |

## Default Color Sets

If you're using one of the standard Logi themes, the theme will set the default colors. These colors can be identified by looking at the theme's Template Modifier file:  <your app folder>\rdTemplate\rdTheme\<theme name>\ThemeModifier.xml

If you're *not* using a theme and do not specify a color set, the following default color set will be applied.

### Static Charts

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| |  |  |  | | --- | --- | --- | | **#** | **Hex Code** | **Color** | | 1 | FF3333 |  | | 2 | 33FF33 |  | | 3 | 6666FF |  | | 4 | FFFF00 |  | | 5 | FF66FF |  | | 6 | 99FFFF |  | | 7 | FFCC33 |  | | 8 | CCCCC |  | | |  |  |  | | --- | --- | --- | | **#** | **Hex Code** | **Color** | | 9 | CC9999 |  | | 10 | 339966 |  | | 11 | 999900 |  | | 12 | CC3300 |  | | 13 | 669999 |  | | 14 | 993333 |  | | 15 | 006600 |  | | 16 | 990099 |  | | |  |  |  | | --- | --- | --- | | **#** | **Hex Code** | **Color** | | 17 | FF9966 |  | | 18 | 99FF99 |  | | 19 | 9999FF |  | | 20 | CC6600 |  | | 21 | 33CC33 |  | | 22 | CC99FF |  | | 23 | FF6666 |  | | 24 | 99CC66 |  | | |  |  |  | | --- | --- | --- | | **#** | **Hex Code** | **Color** | | 25 | 009999 |  | | 26 | CC3333 |  | | 27 | 9933FF |  | | 28 | FF0000 |  | | 29 | 0000FF |  | | 30 | 00FF00 |  | | 31 | FFCC99 |  | | 32 | 999999 |  | |

List continues with other colors not shown here.

### Animated Charts

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| |  |  |  | | --- | --- | --- | | **#** | **Hex Code** | **Color** | | 1 | AFD8F8 |  | | 2 | F6BD0F |  | | 3 | 8BBA00 |  | | 4 | FF8E46 |  | | 5 | 008E8E |  | | 6 | D64646 |  | | 7 | 8E468E |  | | 8 | 588526 |  | | |  |  |  | | --- | --- | --- | | **#** | **Hex Code** | **Color** | | 9 | B3AA00 |  | | 10 | 008ED6 |  | | 11 | 9D080D |  | | 12 | A186BE |  | | 13 | CC6600 |  | | 14 | FDC689 |  | | 15 | ABA000 |  | | 16 | F26D7D |  | | |  |  |  | | --- | --- | --- | | **#** | **Hex Code** | **Color** | | 17 | FFF200 |  | | 18 | 0054A6 |  | | 19 | F7941C |  | | 20 | CC3300 |  | | 21 | 006600 |  | | 22 | 663300 |  | | 23 | 6DCFF6 |  | |  |  |  | |  |

Colors are repeated again after 23 colors are applied.

## Chart Release Notes

The following enhancements to chart elements have been introduced:

| Release | Enhancements |
| --- | --- |
| 11.1.033 | * Animated Chart.XY now has a new child element: **Realtime Update**. This element behaves like the Refresh Element Timer, updating the chart with realtime data at specified intervals. * Animated Chart.XY now includes Grid Line Color, Area Gradient Color, and Line Width attributes. * Animated Chart.XY and   Animated Chart.Scatter now include an Alternating Background Color attribute. which allows them to have a single background color for the   plot area of the chart. * Animated Chart.Scatter now includes an Edge Color attribute. * Animated Chart.Scatter now includes a Chart Symbol Sides attribute, which allows specification of the number of sides for the Scatter Symbol. * Animated Chart.Pie and Animated Chart.Scatter now have font formatting child elements. * Animated Chart.Pie now includes Wedge Border Color and Wedge Border Thickness attributes. * Animated Chart.Pie now includes these attributes: 3-D Angle, 3-D Effect, and 3-Dimensional. * Animated Gauges no longer have a gauge border, so they match the look of Animated Charts. * Animated Gauge.Bar now includes an optional 3-D effect. |
| 11.0.727 | * The Java-based Heatmap Applet was deprecated; use Chart.Heatmap instead. |
| 11.0.519 | * The Format Data element was reinstated for Chart.XY. |
| 11.0.416 | * Animated Charts and Gauges have been upgraded. They can now use either **HTML5** features and JavaScript *or* Flash to render animated visualizations. By default, for now, they still use Flash, but HTML5 can be used by including the constant rdAnimatedChartRenderStyle=JavaScript   in the application's \_Settings definition. * The upgraded visualizations in v11.0.416+ **look different**, in varying degrees by chart type, than the previous versions, regardless of rendering style used. * Animated Charts and Gauges are now available for use in Mobile Reporting definitions. |
| 11.0.43 | * InputChart.List and InputChart.Ranage elements added to allow interactive selection of chart values. * Dynamic filtering provided by clicking Legend items of Static Charts (Pie, Line, Bar, Area, Polar). * Multi-color Static Charts titles can be displayed using CDML tags in Chart Title attribute. * Themes now set Legend background colors. * Static pie chart label colors can now be specified when style is set to External Layout. * Display data values for each data series within stacked Static Bar Charts. * Hover Highlight child element highlights chart features when mouse pointer is over them. |
| 10.2.424 | * Added Zoom Chart feature. * Resizer handles remain hidden until the mouse pointer hovers over them. * Static Chart title alignment can now be set in Chart Title Font element. * Titles longer than the width of the chart will be truncated and have an ellipsis ("...") appended to them. * Format Data and Format Label for static charts now deprecated. Data Scale and Label Scale elements given new Format attribute. |
| 10.2.314 | * Show Wait Icon added to control whether animated "loading" image is displayed. Default: *True* |
| 10.2.224 | * Static Chart.XY charts can show or hide "tick marks" by setting the Tick Marks attribute in Data Font and Label font elements. |
| 10.1.46 | * Quicktip element made available as a child of static Bar, Line, Spline, Scatter, Gantt, Heatmap, and Pie charts. * Chart Texture attribute added to Chart.Heatmap element. |
| 10.1.18 | * Chart processing became multi-threaded and asynchronous so, for example, charts in multiple dashboard panels could be retrieved simultaneously. On web servers with multiple cores or multiple processors, chart generation tasks will be spread across them for even better performance. |
| 10.0.428 | * Chart Resizer element: resizer handles have a new look and there are now no other handle options. |
| 10.0.385 | * Group Drillthrough element introduced. (Logi Info only) |
| 10.0.366 | * Chart.Heat Map introduced. |
| 10.0.299 | * All static charts now have anti-aliasing enabled for all text, by default. * All static charts now have an animated "Loading" image displayed while waiting for data to load. * All static charts now feature rounded borders for their legend box, if any, by default. * All static charts now display the Lowess curve line, if specified, on "top" of the chart layer. * Area, Gantt and Bar charts now have the attribute "Edge Color", so users can set the layer edge color. * Pie charts now have a "Label Pointer Color" attribute. Set to "SameAsWedgeColor" to specify same color as the corresponding pie wedge. * Gantt charts now behave as other XY charts do: when a chart border color is set, the X- and Y-axis are set to that color, too. * Scatter charts now use legend icons that match the layer symbols and their sizes change when the legend font is changed. * Line and Spline charts now set legend icons to lines, instead of the standard square box. |
| 10.0.227 | * Chart colors can now be set via a datalayer column, using these new attributes: Bar Color Data Column and Pie Color Data Column. |
| 10.0.189 | * Bubble charts: new attribute Chart Symbol Size Factor can be used to change symbol by setting a value between 0 and 1. (e.g. 0.25 would mean that the largest bubble would be 25% the size of the plot area, and all other bubbles will be resized accordingly). |
| 10.0.151 | * Studio now includes a Create a Gauge wizard to assist in configuring gauges. |
| 10.0.117 | * Static Pie Charts now include the Label Column Data Type attribute. |
| 10.0.101 | * Animated Charts now allow tokens to be used for Height or Width attribute values. |
| 10.0.85 | * Animated Charts - The Relevance Filter is now available for Animated Charts. * Animated Gauges - A new Attribute, Major Tick Color, allows the Major Tick Mark's color to be configurable. * Animated Pie - A new attribute, Show Values, allows users to hide data names in the labels. * Static Chart Legend - The Legend box will not be displayed if no data rows are returned to the datalayer. * New Zero Row Message element can customize a message to be displayed when chart datalayer retrieves no data. |
| 10.0.31 | * Animated Charts - Charts can be saved as an image file by right-clicking the chart and selecting Save. * Animated Chart.XY - A new Attribute, Max Label Length, if set, will truncate the label at a specified length and append an ellipsis (...). |
| 9.5 | * Static charts have a new child element, **Resizer**, which allows runtime resizing of the chart image * Static charts now automatically set their borders, based on data size, label length, fonts, angles, 3D properties, titles, legends, etc. Developers can still set the borders manually if desired. * Static pie charts now include a **Doughnut** style, **Texture**, shadow/gradient and 3D-angle attributes. * The Max Label Length attribute truncates Label data at the specified number of characters and append an ellipsis (...). This applies to both **Chart** labels and **Legend** labels, if any. |
| 9.2 | * Pie charts have new **Label Layout**, **Label Rounded Border**, and **Label Shading** attributes. * Chart.XY charts have new **Gradient**, **Outer Border Color**, and **Outer Border Rounding** attributes. * A new child element, **Extra Needle**, is now available under the Needle Gauge, enables users to add extra needles to an existing needle gauge. * When a Secondary Data Axis is used in a Chart.XY, users can now apply the **Marks** element to these secondary data points. Marks previously corresponded to the main Y axis only. * The **Polar Chart** element is now available under the Column Cell element. |
| 9.1 | * Pie charts have "Smart Labels"; users can manually set the label's distance from the pie edge. * Pie charts now include a new **Exploded Wedges Column** attribute for identifying the wedges to explode away from the pie. The pie's animation using draws the pie in wedge rotation, however, if column names are entered in this new attribute, the drawing will occur in slicing mode. * Chart legends can be customized by place the **Legend Font** element directly as a child of the chart; there is no longer a requirement to place it under the **Legend** element. * Labels can now be customized by using the **Label Font** element, however its **Decimal Points** attribute is disabled. * Tooltips can be customized to display data from the datalayer by using a new the new **Tooltip Column** attribute; set it to a column from the datalayer. In addition, a new **Tooltip Font** element which can be used to set different Tooltip font properties. * A new attribute, **Bar Style**, for the Animated Chart.XY element when creating a 2-D Bar-type chart, allows the bars and chart to have rounded edges. * The **Line Style** attribute, when using the Animated Chart.YX element to create Line charts, now provides a DashLine option in addition to SolidLine. When using the DashLine value, the new **Line Dash Length** attribute can be used to define the gap, in pixels, between dashes. * Default gradient color effects are now available for all charts. * A new **Show Data Values** attribute for the Animated Chart.XY element allows data values to be displayed in the chart. * Charts now use **Adobe Flash 8** and **ActionScript 2**, which provides faster loading and rendering and which provides better printing support. |
