---
title: "Adding Tooltips"
id: 7522904459543
section: "Use Logi Studio/SSRM - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/7522904459543-Adding-Tooltips
updated_at: 2022-07-17T02:25:42Z
---

# Adding Tooltips

# Adding Tooltips

"Tooltips," those little balloons that can pop-up when you hover
your mouse over an image, link, button, and other elements, provide a fast
and easy method of providing additional explanation. They're generally a
kind of on-the-spot "mini online help," though they can be much
more. This topic describes adding tooltips to your Logi application, and provides links to tooltip elements.

The following topics discuss the multiple ways in which you can add
tooltips to your Logi applications:

* [Tooltip Attribute](https://devnet.logianalytics.com/hc/en-us/articles/4419700086807-Tooltip-Attribute#TTAttribute)
* [Quicktip Element](https://devnet.logianalytics.com/hc/en-us/articles/4419700085911-Quicktip-Element#Quicktip)
* [Tooltip Panel Element](https://devnet.logianalytics.com/hc/en-us/articles/4419715042199-Tooltip-Panel-Element-#TTPanel)

## About Your Tooltip Options

Logi Info offers several methods for adding tooltips to your Logi
application and each is discussed in one of the topics mentioned above, which
are presented in order of increasing complexity and functionality. Adding
tooltips is an excellent idea in situations where a little more
explanation would be useful (but it's not worth going to another web
page), or there's underlying data that would clutter up a report if all of
it was shown at once.

Some Logi
super-elements, such as the Analysis Chart and Analysis Grid, automatically incorporate tooltips into their charts, so that the
underlying data value is displayed when the mouse is hovered over
different points on the charts.

![](https://devnet.logianalytics.com/hc/article_attachments/7522745474327/_newplus.jpg) New for 14.2 Charts with multiple series or aggregations are encouraged to use the ChartCanvas element's attribute, Tooltip Split. This attribute allows you to split a chart's tooltip into one label per series, rather than per segment. The default value for this attribute is False. Once enabled, when hovering over a data point, it displays all the values for the series:

![](https://devnet.logianalytics.com/hc/article_attachments/7522836176407/image-20220627-141347_1508x427.png)

This method is recommended over shared tooltips for charts with multiple line series, and as such, takes precedence over tooltip.shared.

Given how easy it is to add tooltips, you may not want to consider your
application really *finished* until you do.
