---
title: "DataLayer.Cached - Working with DataLayer.Cached"
id: 4406817282711
section: "Datalayers - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817282711-DataLayer-Cached-Working-with-DataLayer-Cached
updated_at: 2022-04-06T06:05:10Z
---

# DataLayer.Cached - Working with DataLayer.Cached

# DataLayer.Cached - Working with DataLayer.Cached

Reports do not always need to use the absolutely most-current data. Data generated a few hours ago, yesterday, or last month is frequently what's required. In these circumstances, there's no point in burdening datasources by requesting this kind of data from them every single time a report is run and DataLayer.Cached offers the flexibility of an alternate approach.

DataLayer.Cached modifies the normal data retrieval activities of datalayers; when it's used, data is retrieved, cached, and made available for use in Logi reports for a specific time period, after which the data is refreshed (deleted and recreated). Its primary purpose is to reduce the number of data retrieval operations, such as complex SQL queries, that need to be run against the datasource.

![](https://devnet.logianalytics.com/hc/article_attachments/4417563392151/dlcached_01.png)

In the example shown above, a **DataLayer.Cached** element has been added as a child element beneath a data table and its attributes set as shown. DataLayer.Cached requires a child datalayer element, which retrieves the data from the original datasource when necessary and can be any of the other datalayer elements available. The data lifecycle will then be as follows:

1. When the report is requested for the *first* time, the data will be retrieved by the DataLayer.SQL and cached in an XML data file in the applications' rdDataCache folder. The request will then be satisfied using this data.
2. The next time the report is requested by any user, it will be satisfied using the cached data in the XML data file; the SQL query will *not* be executed. This will remain the case for any subsequent requests until the cache expires (five hours after it was created, based on the Expiration Time Span attribute value above of *5:00*).
3. If the cache has expired, the next time the report is requested by any user, the XML data file will be deleted and the cycle will begin again with Step #1.

You can add child elements beneath DataLayer.Cached and/or its child datalayers to modify the data, including:

* **Filtering**: Sort, group, or restrict the data
* **Extending**: Add virtual columns to the datalayer that contain
  aggregated, calculated, or totaled data values
* **Securing**: Limit access to the data using Logi security
* **Linking**: Make the results reusable elsewhere in your report
  definitions

The use of many of these modifier elements is described in separate DevNet
topics.

Data retrieved into the datalayer is cached in **XML** format, in memory and/or on the web server's file system. The latter is discussed in [The Logi Server Engine](https://devnet.logianalytics.com/hc/en-us/articles/4406817743895-The-Logi-Server-Engine) and may be of interest to developers working with extremely large datasets or large numbers of concurrent users.

The data in the datalayer is available using **@Data****tokens**,
in the format @Data.*ColumnName*~. The spelling of the column name is
**case-sensitive**. The data is only available within the **scope** of the
**parent** element of the datalayer, not throughout the entire report
definition. The **DataLayer.Linked** element can be used to make the data reusable
in another datalayer outside this scope.

The [Auto Columns](https://devnet.logianalytics.com/hc/en-us/articles/4406822055959-Auto-Columns) element can be used to quickly display in your report all the data in a datalayer.

The data retrieved into the datalayer can be viewed by turning on the
**Debugging Link** in your \_settings definition (**General** element) and using
the resulting link at the bottom of your report page to view the **Debugger Trace Report** page. There will be clear indications when the cache is being built and when data from it is being used. A link on the Trace page will display the actual cached data.

![](https://devnet.logianalytics.com/hc/article_attachments/4417575776407/dlcached_02.png)

Studio includes a **wizard** that will add elements for the **columns** in the datalayer to your definition. You can select the desired columns before the operation begins. With the datalayer's parent **Data Table** or similar element selected in the Definition Editor, click the wizard link, shown above, in the Element Toolbox.
