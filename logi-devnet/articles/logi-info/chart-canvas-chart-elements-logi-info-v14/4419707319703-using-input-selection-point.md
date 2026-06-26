---
title: "Using Input Selection Point"
id: 4419707319703
section: "Chart Canvas Chart Elements - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419707319703-Using-Input-Selection-Point
updated_at: 2022-07-17T02:01:15Z
---

# Using Input Selection Point

# Using Input Selection Point

The **Input Selection Point** element enables the selection, at runtime, of one or more chart data points. This element is available for use with:

* Series.Area
* Series.Area Spline
* Series.Bar
* Series.Bar Range
* Series.Bubble
* Series.Funnel
* Series.Line
* Series.Pie
* Series.Pyramid
* Series.Scatter
* Series.Spline
* Series.Waterfall

Selection can occur by clicking individual data points or by "drawing" a selection rectangle around them.

![](https://devnet.logianalytics.com/hc/article_attachments/4419714647703/introcccharts_127.png)

Input Selection Point works with two other elements, **Input Selection Style** and **Input Selection Point Event**, along with Action and Target elements, to produce the desired effect, as shown in the typical element arrangement above.

You can link Input Select Point to User Input elements (**Input Text** and **Input Hidden**) in the same report definition and the values selected in the chart will automatically be reflected in the input elements. Selecting multiple points in the chart will create a comma-separated list of values in the User Input elements.

The following additional User Input elements now work automatically with Input Select Point: **Input check box List**, **Input Radio Buttons**, and **Input Select List**.

## Attributes

Input Selection Point attributes:

| Attribute | Description |
| --- | --- |
| ID | (Required) This is the unique element ID and is also the name of the Request variable passed when the page input selection action occurs. If this ID matches the ID of one of the User Input elements mentioned in the previous section, that element will be automatically updated with the value(s) selected in the chart. |
| Change Flag Element ID | Specifies the ID of an element to be set to indicate than an input value has been changed by the user. This is often an Input Hidden element. |
| Excluded Point Values | Specifies a comma-separated list of one or more values that cannot be selected. The values correspond to those from the element's Point Value Column attribute. For example, a bar chart with a Relevance Filter may include a bar indicating "Other", which should not be selectable. When a chart's datalayer has a Relevance Filter child element, the area represented by the filter's Irrelevance Label (the "Other" area) will automatically bethe default for the Excluded Point Values attribute. |
| Point Value Column | When a point is clicked, the default value returned is that of the Series' X-axis Data Column. This attribute specifies the name of an alternate data column to be used. |
| Selection Type | Specifies how users interact with the chart. Options include: *ClickSinglePoint* (the default) lets users click on individual data points, bars or pie wedges. A previously selected point becomes deselected. Re-clicking the point deselects it. *ClickMultiplePoints* lets users click on any number of points, bars or pie wedges. Re-clicking a point deselects it.  *ClickRangePoints* (for Bar, Area, Area Spline, Line, and Spline series only) lets the user select a range of values by clicking the range's starting and ending points. *Area* lets the user select points by drawing a rectangular region within X- and Y-axis charts. The chart example at the top of the page uses this selection type. This and the following "area" types are *not* supported for Funnel, Pyramid, and Pie series. *AreaXAxis* is the same as *Area*, except the Y-axis region fills the chart. Only the X-axis is selected by the user. *AreaYAxis* is the same as *Area*, except the X-axis region fills the chart. Only the Y-axis is selected by the user. |

In the target report or process task, all of the selected values can be referenced using the token @Request.XX~, where "XX" is the Input Selection Point element ID. The token for the example shown above would be @Request.inpSelPoint~.

If multiple selections are made, the @Request token will contain a comma-separated list of selected values. For use with SQL statements, it may be desirable to surround each individual value in the list with single quotes. This can be done using the SingleQuote token modifier. Thus
@Request.inpSelPoint~ which has a value of 1,2,3 becomes   
@SingleQuote.Request.inpSelPoint~ which has a value of '1','2','3'

In SQL query "IN" clauses, this is used as "...WHERE LastName IN ('@SingleQuote.Request.inpSelPoint~')...

The **Validation.Required** element is also available as a child element so a warning message can be displayed if the page is submitted without data points being selected.

![](https://devnet.logianalytics.com/hc/article_attachments/4419706629655/noteicon.jpg) The Validation element's *Class* attribute will not be applied.

## Input Selection Point Event

This element specifies, through its child elements, the action to be taken when point selection is completed.

| Attribute | Description |
| --- | --- |
| ID | The unique element ID. |
| Selection Event | Specifies the type of event that will trigger the action. Options include: *Change* (the default) triggers the action when the selected status of any data point changes. *PointsSelected* triggers the action only when points are selected. *PointsCleared* triggers the action when points are deselected. |

## Input Selection Style

This element allows you to style the selection point or area.

| Attribute | Description |
| --- | --- |
| Border Color | Specifies the color of the border line displayed around selected points. Enter a color by name, decimal RGB value, or hex RGB value. Prefix hex values with the pound sign, e.g. *#112233*. |
| Border Color Transparency | Specifies the transparency of the selected point border line color. The lowest value of *0* specifies that the line is opaque, with no transparency. At the other end of the scale, *15* specifies a completely transparent line. Use medium-level transparency to allow different chart layers to show through each other. |
| Border Thickness | Sets the thickness of the selected point border line, in pixels. The default value is *1* pixel. |
| Color | Specifies the color of selected points. Enter a color by name, decimal RGB value, or hex RGB value. Prefix hex values with the pound sign, e.g. *#112233*. |
| Selection Area Color | When using an "Area" Selection Type, specifies the color of the selection rectangle background. Enter a color by name, decimal RGB value, or hex RGB value. Prefix hex values with the pound sign, e.g. *#112233*. |
| Selection Area Color Transparency | When using an "Area" Selection Type, specifies the transparency of the selection rectangle. The lowest value of *0* specifies that the line is opaque, with no transparency. At the other end of the scale, *15* specifies a completely transparent line. Use medium-level transparency to allow different chart layers to show through each other. |
| Transparency | Specifies the transparency of selected points. The lowest value of *0* specifies that the line is opaque, with no transparency. At the other end of the scale, *15* specifies a completely transparent line. Use medium-level transparency to allow different chart layers to show through each other. |

When using Input Selection Point, you may want to turn off the automatic Quicktips generated by the chart. This is done by setting the Chart Canvas element's **Auto Quicktip** attribute to *False*.
