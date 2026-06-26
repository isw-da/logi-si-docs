---
title: "InfoGo - Selecting Data"
id: 4419707887639
section: "Use InfoGo/Discovery Module - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419707887639-InfoGo-Selecting-Data
updated_at: 2022-07-17T01:35:10Z
---

# InfoGo - Selecting Data

# InfoGo - Selecting Data

Depending on how your application has been configured, you may or may
not see this feature. Skip this topic if you do not see a "Data" tab
or button at the top of your Analysis Grid.

Click the "Data" tab or button to open its panel:

![](https://devnet.logianalytics.com/hc/article_attachments/4419699933591/usinginfogo125_10.png)

The first thing you'll need to do is select the Data Table or view
you want to work with. The data source tables and views available to you
have been determined by the application developer.

Your application may be configured for multiple data sources; if so,
it will look like the example shown above, right. If that case, you'll
need to select a data source first, then a table or view.

![](https://devnet.logianalytics.com/hc/article_attachments/4419699933847/usinginfogo125_11.png)

As soon as you select data, a Data Table will appear showing it. A set
of column selection check boxes will also appear, as shown above. You can
un-check the boxes for columns you *don't* want to include in your analysis work. If it's visible, click **Apply Column Selection** to update the table, otherwise the table may update automatically.

![](https://devnet.logianalytics.com/hc/article_attachments/4419699934103/usinginfogo125_12.png)

Your application may be configured to allow you to "join" different
Data Tables. If so, you'll see additional data selection lists, as shown
above, right.

By default, items like Orders - Customers indicate an *Inner Join*, while items like Orders![](https://devnet.logianalytics.com/hc/article_attachments/4419714617623/menuarrowrt.png)Order Details indicate a *Left Outer Join*. However, these designations can be customized by your application's developer and other Join
types may be available.

![](https://devnet.logianalytics.com/hc/article_attachments/4419706629655/noteicon.jpg)
What's a "join"? A join combines two sets of data to produce a single
dataset. Different types of joins produce different results. For example, an *Inner Join* selects all rows from both tables as long as there is a match between a column in both tables. A *Left Outer Join*selects all rows from the first table and adds
rows from the second table that match a specified column value.

![](https://devnet.logianalytics.com/hc/article_attachments/4419714922007/usinginfogo125_13.png)

When you select data that joins tables, you'll see a
color-coding scheme applied to the table that indicates where data came
from. In the example shown above, table columns with a ***blue*** border came from the original table "Orders" while columns with a ***red*** border came from the selected join.

Once you've selected data, all of the other tabs or buttons at the top of the Analysis Grid become enabled.

Click the **Data** tab or button to hide the data selection controls.
