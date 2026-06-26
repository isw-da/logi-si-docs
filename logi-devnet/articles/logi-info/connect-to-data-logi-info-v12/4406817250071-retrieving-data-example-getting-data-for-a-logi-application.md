---
title: "Retrieving Data Example: Getting Data for a Logi Application"
id: 4406817250071
section: "Connect to Data - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817250071-Retrieving-Data-Example-Getting-Data-for-a-Logi-Application
updated_at: 2022-04-06T06:04:56Z
---

# Retrieving Data Example: Getting Data for a Logi Application

# Retrieving Data Example: Getting Data for a Logi Application

Here's a very simple example of a Logi application that uses the data from the [Create a Data Definition](https://devnet.logianalytics.com/hc/en-us/articles/4406817246871-Creating-a-JSON-Data-Definition) topic. The Json Style is blank (*RowsToObjects)* in that example.

![](https://devnet.logianalytics.com/hc/article_attachments/4417575792791/usingdatadefs_07.png)

In the report definition above, Data Table and DataLayer.Json File elements have been added. The datalayer's Json File attribute has been set to:

https://localhost/v12test/rdTemplate/rdData.aspx?rdData=myDataDef

A Flattener element has been used to flatten the JSON data array into rows and columns for use in the data table and an Auto Columns element handles our columns. For more information on these elements, see [The Flattener](https://devnet.logianalytics.com/hc/en-us/articles/4406817464343-The-Flattener) and [Auto Columns](https://devnet.logianalytics.com/hc/en-us/articles/4406822055959-Auto-Columns).

![](https://devnet.logianalytics.com/hc/article_attachments/4417563413783/usingdatadefs_08.png)

And, if we preview the report definition, the resulting output is shown above.
