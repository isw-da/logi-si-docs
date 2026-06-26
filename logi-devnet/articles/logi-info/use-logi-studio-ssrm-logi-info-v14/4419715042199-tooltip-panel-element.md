---
title: "Tooltip Panel Element "
id: 4419715042199
section: "Use Logi Studio/SSRM - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419715042199-Tooltip-Panel-Element
updated_at: 2022-07-17T02:25:29Z
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

![](https://devnet.logianalytics.com/hc/article_attachments/7522834860567/addtooltip_02.png)![](https://devnet.logianalytics.com/hc/article_attachments/7522857209879/addtooltip_02a.png)

The example above shows an **Image** element with a
**Tooltip Panel** element placed beneath it, with a child
**Label** element. The Tooltip Panel has a full set of attributes that
can be used to customize the tooltip. Let's see what it can look like:

![](https://devnet.logianalytics.com/hc/article_attachments/7522834869911/addtooltip_03.png)

In the example shown above, we see a Tooltip Panel that appears when the
mouse cursor hovers over the "help" icon. Style has been used to
color the panel background and give it a drop shadow, and the child Label
element has been set to HTML format so that the help text will be
displayed as an unordered list with bullets.
Image and Label elements now include "HTML Attribute Params", enabling you to apply your application to work with other frameworks or libraries easier. Depending on the element you add the HTML Attribute Params to, there are additional parameters for you to specify. The IMG element includes "alt", "style", and "title" parameters, while the Label element allows you to include "Id", "type", and "value". If an attribute was set in both Element and HTML attribute params, the one set in the HTML attribute params will be ignored.

![](https://devnet.logianalytics.com/hc/article_attachments/7522774430103/noteicon.jpg) The Tooltip Panel element has **Condition** and
**Security Right ID** attributes, so its appearance can be controlled
dynamically. For example, separate sets of tooltips for different users
are possible.

![](https://devnet.logianalytics.com/hc/article_attachments/7522851229719/addtooltip_04.png)

A variety of elements, including Charts, Gauges, Images, SubReports, and
others, can be included as children of the Tooltip Panel, as shown in the
example above, giving you the opportunity to make your tooltip contain
more than just text.
