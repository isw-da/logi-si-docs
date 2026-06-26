---
title: "Tooltip Panel Element"
id: 4406816954007
section: "Use Logi Studio/SSRM - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406816954007-Tooltip-Panel-Element
updated_at: 2022-04-06T06:03:04Z
---

# Tooltip Panel Element

# Tooltip Panel Element

The **Tooltip Panel** element is a flexible option for including more
complex tooltips. This topic describes how to add a panel element.

You can add the Tooltip Panel element as a child beneath these elements:

* Button
* Column Cell
* Data Table Column
* Division
* Image
* Label

As an element, the Tooltip Panel can have a variety of child
elements, allowing you to get more creative with what you include in the
tooltip.

![](https://devnet.logianalytics.com/hc/article_attachments/4417584207767/addtooltip_02.png)![](https://devnet.logianalytics.com/hc/article_attachments/4417591989527/addtooltip_02a.png)

The example above shows an **Image** element with a
**Tooltip Panel** element placed beneath it, with a child
**Label** element. The Tooltip Panel has a full set of attributes that
can be used to customize the tooltip. Let's see what it can look like:

![](https://devnet.logianalytics.com/hc/article_attachments/4417591989783/addtooltip_03.png)

In the example shown above, we see a Tooltip Panel that appears when the
mouse cursor hovers over the "help" icon. Style has been used to
color the panel background and give it a drop shadow, and the child Label
element has been set to HTML format so that the help text will be
displayed as an unordered list with bullets.

![](https://devnet.logianalytics.com/hc/article_attachments/4417583587863/noteicon.png) The Tooltip Panel element has **Condition** and
**Security Right ID** attributes, so its appearance can be controlled
dynamically. For example, separate sets of tooltips for different users
are possible.

![](https://devnet.logianalytics.com/hc/article_attachments/4417591990039/addtooltip_04.png)

A variety of elements, including Charts, Gauges, Images, SubReports, and
others, can be included as children of the Tooltip Panel, as shown in the
example above, giving you the opportunity to make your tooltip contain
more than just text.
