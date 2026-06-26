---
title: "Data Table Links"
id: 4406817273751
section: "Use Dashboards & Visuals - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817273751-Data-Table-Links
updated_at: 2022-04-06T06:05:04Z
---

# Data Table Links

# Data Table Links

A common requirement is to be able to click the actual data in a data table cell and do something with the clicked value.

![](https://devnet.logianalytics.com/hc/article_attachments/4417563393687/createtable_05.png)

The image above shows an example of this, and here are the elements needed to make that work:

![](https://devnet.logianalytics.com/hc/article_attachments/4417563394071/createtable_06.png)

As shown above, an **Action** element is placed beneath the Label element used to display the data in each column. An appropriate **Target** element is also included.

![](https://devnet.logianalytics.com/hc/article_attachments/4417584033815/createtable_07.png)

Finally, a **Link Parameters** element is added, as shown above, to pass a data value to the target.
