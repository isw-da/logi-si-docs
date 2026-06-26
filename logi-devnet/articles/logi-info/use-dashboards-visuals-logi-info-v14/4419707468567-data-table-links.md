---
title: "Data Table Links"
id: 4419707468567
section: "Use Dashboards & Visuals - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419707468567-Data-Table-Links
updated_at: 2022-07-17T01:54:14Z
---

# Data Table Links

# Data Table Links

A common requirement is to be able to click the actual data in a Data Table cell and do something with the clicked value.

![](https://devnet.logianalytics.com/hc/article_attachments/4419706742551/createtable_05.png)

The image above shows an example of this, and here are the elements needed to make that work:

![](https://devnet.logianalytics.com/hc/article_attachments/4419714714775/createtable_06.png)

As shown above, an **Action** element is placed beneath the Label element used to display the data in each column. An appropriate **Target** element is also included.

![](https://devnet.logianalytics.com/hc/article_attachments/4419706743063/createtable_07.png)

Finally, a **Link Parameters** element is added, as shown above, to pass a data value to the target.
