---
title: "Styling the Axis Labels"
id: 4419715151383
section: "Chart Canvas Chart Elements - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419715151383-Styling-the-Axis-Labels
updated_at: 2022-07-17T02:25:03Z
---

# Styling the Axis Labels

# Styling the Axis Labels

The axis labels can be styled using the **Label Style** child element. For example, Label Style has a set of font-related attributes that allow you to specify font family, color, size, angle, etc.

![](https://devnet.logianalytics.com/hc/article_attachments/7522832671511/introcccharts_101.png)

In the example above, the labels have been styled to have a 45-degree font angle and a Blue font color.

![](https://devnet.logianalytics.com/hc/article_attachments/7522854689943/introcccharts_102.png)

Labels can also be arranged into multiple rows, using the element's **Stagger Labels** attribute, as shown above.
This element also has **Offset X** and **Offset Y** attributes that allow you to shift the entire set of labels in any direction and a **Format** attribute that allows you to format the label data, using standard Logi formatting options. For more information on Logi formatting, see [Format Data](https://devnet.logianalytics.com/hc/en-us/articles/4419722930327-Format-Data).

![](https://devnet.logianalytics.com/hc/article_attachments/7522848642711/introcccharts_102a.png)

If you want to "stack" the labels into two lines, as shown above, it's easy to do:

First, concatenate the text "<br>" into your label data at the point where you want to insert the line break. Here's an example SQL query:

SELECT LEFT(DATENAME(m, start\_date), 3) + '<br>' + RIGHT(DATEPART(yy, start\_date), 2) AS StartDate...

Then, set the Label Style element's **Format** attribute to *HTML*. Finally, use (for this example) *StartDate* as the series' **X-Axis Data Column**.

The Label Style element's **Maximum Label Length** attribute lets you specify the maximum number of characters that will be displayed for a label before the
text is truncated and ellipsis (...) is appended.

When used beneath a Y-Axis element, the Label Style element's **Format** attribute can include ####;(###) to display negative numbers within parentheses.

The default formatting of automatic tooltips is inherited from the **Format** attribute of the Label Style element.

## New for 14.1 Auto Rotation

Enable auto rotation to prevent overlapping labels on your horizontal axis using the Chart Canvas attribute, Auto Rotation Degrees. By default, the value for this attribute is "undefined" and labels will word-wrap, when possible. When undefined, the top and bottom axes default to a -45 degree rotation. To utilize this feature, enter a numeric value between 0-90 in the Auto Rotation Degrees attribute.

![](https://devnet.logianalytics.com/hc/article_attachments/7522879652119/image-20220118-141214_1074x325.png)

For more information about configuring your chart axes, see [Axis Element Attributes](https://devnet.logianalytics.com/hc/en-us/articles/4419722735767-Axis-Element-Attributes).
