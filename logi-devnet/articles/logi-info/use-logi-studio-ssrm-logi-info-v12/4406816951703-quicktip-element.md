---
title: "Quicktip Element"
id: 4406816951703
section: "Use Logi Studio/SSRM - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406816951703-Quicktip-Element
updated_at: 2022-04-06T06:03:01Z
---

# Quicktip Element

# Quicktip Element

The **Quicktip** element is almost as easy to use as the Tooltip
attribute but provides a tooltip with a little different look. It can used
beneath static Chart, Gauge, Division, and Heatmap Group Column elements,
and has been included to automatically provide tooltips for the charts
found within the Analysis Chart and Analysis Grid super-elements, and in
all Chart Canvas charts.

![](https://devnet.logianalytics.com/hc/article_attachments/4417584208023/addtooltip_05.png)![](https://devnet.logianalytics.com/hc/article_attachments/4417591990423/addtooltip_05a.png)

In the example above, we see the **Quicktip** element beneath a
**Chart.XY** element, and its attributes are also shown. The resulting
tooltip that appears when the mouse *hovers* over the chart line
looks like this:

![](https://devnet.logianalytics.com/hc/article_attachments/4417591990679/addtooltip_06.png)

Visually, this is more complex than basic tooltips. The
pop-up panel has space for both a title and a description and includes a
small, angular protrusion that points to the cursor, and its color and
fonts can be controlled by assigning a theme, in this case Professional
Green, to the application.

Tokens can be used in both the **Title** and
**Description** attributes and the Quicktip element has a
**Security Right ID** attribute, so its appearance can be dynamic,
based on security roles. Because the Quicktip is displayed based on the
*onMouseOver* DHTML event, you can't put anything inside the Quicktip
itself that a user could click, such as a link.

If you're using Quicktips with a chart that includes
**Extra Grid Layers** and the primary chart datalayer is reduced to
zero rows at runtime, for example, because of filtering, then Info will not display the Quicktips, not even for the Extra Grid Layer plots.

![](https://devnet.logianalytics.com/hc/article_attachments/4417562936855/criticalicon.png) Quicktips should *not* be used inside data
tables.

![](https://devnet.logianalytics.com/hc/article_attachments/4417583587863/noteicon.png) The Quicktip is limited to text only and, as the text gets
longer, the panel will get wider and wider until, at some point, the text
will automatically wrap to another line. But you can't *force* it to
wrap and the point at which it will wrap is based on font family and size
(in the example shown above, it will wrap at 90 characters, so it can get
pretty wide before it wraps).

However, you can deliberately add additional lines by adding child
**Quicktip Row** elements beneath the Quicktip, one for each additional
line of text you want to include.

![](https://devnet.logianalytics.com/hc/article_attachments/4417575435927/notev12.7base.png)The Quicktip Row element has been made context-sensitive with the
addition of a **Condition** attribute.
