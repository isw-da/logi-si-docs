---
title: "Retrieving Data"
id: 4419707619223
section: "Connect to Data - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419707619223-Retrieving-Data
updated_at: 2022-07-17T02:24:17Z
---

# Retrieving Data

# Retrieving Data

You can use **DataLayer.SQL** to retrieve data from Hadoop, and the
Studio's SQL Query Builder tool can help you formulate a query. It can be
invoked from the datalayer's **Source** attribute.

![](https://devnet.logianalytics.com/hc/article_attachments/7522725232151/criticalicon.png)

* Hadoop drivers were deprecated from Info Java.
* DataLayer.Active SQL is not currently available for use with this
  datasource.

![](https://devnet.logianalytics.com/hc/article_attachments/7522824157719/workhadoop_07_518x491.png)

As mentioned earlier, Hadoop uses **HiveQL** which is based on standard
SQL syntax but has a number of very important differences that you should
be aware of as you create your queries. Please refer to the
[*Hive Language Manual*](https://cwiki.apache.org/confluence/display/Hive/LanguageManual)
for more information. After the data is retrieved, you may condition,
filter, and shape it just as you would any other datalayer data.

![](https://devnet.logianalytics.com/hc/article_attachments/7522725232151/criticalicon.png) Another Studio tool, the **Database Browser**, is *not* compatible
with HiveQL.

Once data has been retrieved into the datalayer, it can be manipulated
using any of the elements typically used to filter, aggregate, and
condition data.
For more information on how to manipulate data, see [Manipulating the Data](https://devnet.logianalytics.com/hc/en-us/articles/4419723035799-Manipulating-the-Data).
