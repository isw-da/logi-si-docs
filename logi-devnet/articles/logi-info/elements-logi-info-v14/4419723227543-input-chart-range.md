---
title: "Input Chart.Range"
id: 4419723227543
section: "Elements - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419723227543-Input-Chart-Range
updated_at: 2022-07-17T02:23:11Z
---

# Input Chart.Range

# Input Chart.Range

*A number of Classic Charts have been deprecated; they are still
supported and will work, but their elements are no longer available in
Studio. Use Chart Canvas Charts instead for all new development.*

This element enables a **Classic Chart** to become an input control.
Once a static Line, Spline, or Scatter chart has been made the
child of this element, users can select a region in the chart by drawing a
selection box (by dragging the mouse) on it. When the page is submitted,
the maximum and minimum Label and Data values of the selected chart region
are passed to the next Report or Process task.

![](https://devnet.logianalytics.com/hc/article_attachments/7522735864855/introui_23.png)

The selected region is displayed in a distinctly different color from the
rest of the chart by default.

## Using It

The attributes of this element include:

| Attribute | Description |
| --- | --- |
| ID | (Required) A unique element ID. |
| MaxXaxisID | Specifies the name of the Request token that will provide the upper X-axis (Label) value in the next report or process. |
| MaxYaxisID | Specifies the name of the Request token that will provide the upper Y-axis (Data) value in the next report or process. |
| MinXaxisID | Specifies the name of the Request token that will provide the lower X-axis (Label) value in the next report or process. |
| MinYaxisID | Specifies the name of the Request token that will provide the lower Y-axis (Data) value in the next report or process. |
| Region Border Color | Specifies the border color of the region drawn on the chart, by name, decimal RGB value, or hex RGB value. Prefix hex values with the pound sign, like *#112233*. |
| Region Color | Specifies the color of the region drawn on the chart, by name, decimal RGB value, or hex RGB value. Prefix hex values with the pound sign, like *#112233*. |
| Region Transparency | Specifies the transparency level of the region drawn on the chart. The lowest possible value of *0* indicates that the region is opaque, with no transparency. The other end of the scale, *15*, indicates a completely transparent bar or wedge. |

This element *cannot* be used within an
**Input Grid** element.

![](https://devnet.logianalytics.com/hc/article_attachments/7522745474327/_newplus.jpg) New for 14.1 Adding **HTML Attribute Params** to your User Input elements enables you to apply your application to work with other frameworks or libraries easier. Depending on the type of HTML Attribute Params you add, there will be different parameters available to use, or you can define your own parameters. If an attribute was set in both Element and HTML Attribute Params, the one set in the HTML Attribute Params will be ignored.

## Getting Its Data

The minimum and maximum **Label** and **Data** values of the region
drawn on the chart are available in the next Report or Process task with
@Request tokens. For example, if the element's MaxXaxisID attribute is set
to *EndDate* then the token
@Request.EndDate~will equal the maximum Label value.

If no selection region is drawn and the page is submitted, then the
Request tokens will exist but they will be empty ("").

## Special Event Elements

Two special, child event elements, **Area Drawn** and
**Area Cleared**, are available for use with this element; both take
Action elements as their children.

**Area Drawn** triggers its child Action element as soon as the user
finishes drawing the area on the chart.

After an area has been drawn on the chart, if the user clicks somewhere on
the chart again, the drawn area will be removed and
**Area Cleared** will then trigger its child Action element.

## More Information

For additional information, see the Element Reference entry for
[Input Chart Range](https://clm.logianalytics.com/rdPage.aspx?rdReport=ElementRefDetail&itemID=2582&iName=InputChart.Range&iType=Element&iLabel=InputChart.Range&lnkpg=0).
