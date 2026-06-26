---
title: "Input Chart.List"
id: 4419715533847
section: "Elements - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419715533847-Input-Chart-List
updated_at: 2022-07-17T02:23:11Z
---

# Input Chart.List

# Input Chart.List

*A number of Classic Charts have been deprecated; they are still
supported and will work, but their elements are no longer available in
Studio. Use Chart Canvas Charts instead for all new development.*

This element enables a **Classic Chart** to become an input control.
Once a **static Bar** or **Pie** chart has been made the child of
this element, users can select one or more bars, or one or more pie
regions, by clicking on them. When the page is submitted, the Label values
of the selected chart items are passed to the next report or process.

![](https://devnet.logianalytics.com/hc/article_attachments/7522772820247/introui_22.png)

As shown above, the selected bars or wedges are displayed in a distinctly
different color from the other bars or wedges by default. If the data has
been grouped so that it's displayed as groups of several bars each, the
entire group will be selected when clicked, rather than individual bars
within the group.

## Using It

This element shares many of the standard Input element attributes and
includes these special attributes:

| Attribute | Description |
| --- | --- |
| Input Chart Value Column | Specifies the data column whose values which will be returned, such as the IDs for each selected bar in a Bar chart. The chart's Chart Label Column (aka: Label Data Column X-axis) is the default. |
| Selected Color | Specifies the selected bar or wedge's color, by name, decimal RGB value, or hex RGB value. Prefix hex values with the pound sign, such as *#112233*. |
| Selected Transparency | Specifies the transparency level of the selected bar or wedge. The lowest possible value of 0 indicates that the region is opaque, with no transparency. The other end of the scale, 15, indicates a completely transparent bar or wedge. |
| Unselected Color | Specifies the color of unselected bars or wedges, by name, decimal RGB value, or hex RGB value. Prefix hex values with the pound sign, such as *#112233*. |
| Unselected Transparency | Specifies the transparency level of the unselected bars or wedges. The lowest possible value of 0 indicates that the region is opaque, with no transparency. The other end of the scale, 15, indicates a completely transparent bar or wedge. |

This element *cannot* be used within an **Input Grid** element. A
child validation element, **Validation.Required**, is available to
ensure that a selection is made by the user, if desired.

![](https://devnet.logianalytics.com/hc/article_attachments/7522745474327/_newplus.jpg) New for 14.1 Adding **HTML Attribute Params** to your User Input elements enables you to apply your application to work with other frameworks or libraries easier. Depending on the type of HTML Attribute Params you add, there will be different parameters available to use, or you can define your own parameters. If an attribute was set in both Element and HTML Attribute Params, the one set in the HTML Attribute Params will be ignored.

## Getting Its Data

The **Label** values of the selected bars or wedges are available in
the next Report or Process task with an @Request token. For example, if
the element's **ID** is set to
*inpMyPie*
then the token
@Request.inpMyPie~will equal that value.

If no chart item is selected and the page is submitted, then this Request
token will exist but it will be empty ("").

If multiple chart items are selected, the resulting Request token will
contain a **comma-separated list** of selected values. When working use
with SQL statements, it may be desirable to surround each individual value
in the list with single quotes. This can be done using the SingleQuote
token modifier. Thus

@Request.inpCLPie~
which has a value of 1,2,3
becomes   
@SingleQuote.Request.inpCLPie~
which has a value of '1','2','3'

## More Information

For additional information, see the Element Reference entry for
[Input Chart List](https://clm.logianalytics.com/rdPage.aspx?rdReport=ElementRefDetail&itemID=2594&iName=InputChart.List&iType=Element&iLabel=InputChart.List&lnkpg=0).
