---
title: "Basic Tab Elements"
id: 4406818033175
section: "Elements - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406818033175-Basic-Tab-Elements
updated_at: 2022-04-06T06:09:46Z
---

# Basic Tab Elements

# Basic Tab Elements

Two elements, **Tabs** and **Tab Panel**, are used to implement tabbed panels in Logi reports:

![](https://devnet.logianalytics.com/hc/article_attachments/4417583647127/tabpanels_03.png)

As shown above, the **Tabs** element is the parent of one or more **Tab Panel** child elements.

![](https://devnet.logianalytics.com/hc/article_attachments/4417583647383/tabpanels_04.png)

As mentioned earlier, Tab Panel elements can contain a wide variety of other elements, including those for tables, charts, user input, images, labels, and more. In the example above, a Chart Canvas pie chart has been placed in the first tab panel.

Notice that the example shown above uses a Division element ("divChart") in the Tab Panel, and it contains the pie chart. This is the proper way to *align* content in the panel. The division's Class attribute can be set to a style class that will, for example, center its contents, and you must also set its Output HTML Div Tag attribute to *True* to make it work*.*

You can specify an exact size for Tab Panels but, if you do not, they will automatically size themselves to their contents.
