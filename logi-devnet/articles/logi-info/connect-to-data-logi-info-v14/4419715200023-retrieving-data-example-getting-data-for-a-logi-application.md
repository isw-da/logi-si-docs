---
title: "Retrieving Data Example: Getting Data for a Logi Application"
id: 4419715200023
section: "Connect to Data - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419715200023-Retrieving-Data-Example-Getting-Data-for-a-Logi-Application
updated_at: 2022-07-17T01:54:56Z
---

# Retrieving Data Example: Getting Data for a Logi Application

# Retrieving Data Example: Getting Data for a Logi Application

Here's a very simple example of a Logi application that uses the data from the [Create a Data Definition](https://devnet.logianalytics.com/hc/en-us/articles/4419707453591-Creating-a-JSON-Data-Definition) topic. The Json Style is blank (*RowsToObjects)* in that example.

![](https://devnet.logianalytics.com/hc/article_attachments/4419706725143/usingdatadefs_07.png)

In the report definition above, Data Table and DataLayer.Json File elements have been added. The datalayer's Json File attribute has been set to:

https://localhost/v12test/rdTemplate/rdData.aspx?rdData=myDataDef

A Flattener element has been used to flatten the JSON data array into rows and columns for use in the Data Table and an Auto Columns element handles our columns. For more information on these elements, see [The Flattener](https://devnet.logianalytics.com/hc/en-us/articles/4419722921623-The-Flattener) and [Auto Columns](https://devnet.logianalytics.com/hc/en-us/articles/4419700048023-Auto-Columns).

![](https://devnet.logianalytics.com/hc/article_attachments/4419714703127/usingdatadefs_08.png)

And, if we preview the report definition, the resulting output is shown above.
