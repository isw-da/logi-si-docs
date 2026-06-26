---
title: "DataLayer.Cached"
id: 1500009530061
section: "Introduction to Datasource Connections"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009530061-DataLayer-Cached
updated_at: 2021-06-17T01:58:09Z
---

# DataLayer.Cached

# DataLayer.Cached

The **DataLayer.Cached** element retrieves data that has been cached to disk on the web server. It manages the lifetime and refresh rate of the cached data and uses other datalayers to do the data retrieval from a datasource when necessary. This allows a "snapshot" of the data to be used to generate reports, and reduces the number of retrievals that must be run against the datasource. This topic discusses this datalayer.

* Attributes
* [Work with DataLayer.Cached](#Working)
* [Special Considerations](#Considerations)

*DataLayer.Cached is not available in Logi Report.*

## Attributes

The **DataLayer.Cached** element has the following attributes:

| Attribute | Description |
| --- | --- |
| Cache Key | (Required) An arbitrary string value assigned by the developer. This is a unique identifier for the cached data, used to identify the cache when it's created and used with any subsequent requests for access to the cached data. It has application-wide scope, so the cache can be shared among all user sessions. The value can contain tokens in order to dynamically identify the cache to be used based on request variables or other values.  Caches can be made user-specific by using the token @Session.ID~ in this attribute. Developers can also identify a cache with multiple identifiers or tokens, in a comma-separated list. |
| ID | (Required through v10.1.46) The unique element name. |
| Expiration Now | If set to *True*, causes the data cache to be immediately deleted and recreated. Primarily useful for development purposes. Default value: *False* |
| Expiration Time | The **time of day** at which the data cache expires, causing it to be deleted and recreated by the next user request. Uses the 24-hour clock in the format of *hh:mm* or *h:mm*. For example: 5:00 is 5:00 a.m. and 14:24 is 2:24 p.m. Each expiration-related attribute operates independently of other expiration-related attributes. |
| Expiration Time Span | Sets the **lifetime**, in hours and minutes, of the data cache. Once this amount of time has passed since the creation of the cache, it will be deleted and recreated by the next user request. For example: a value of 1:34 represents one hour and 34 minutes, which will cause a cache created at 2:00 p.m. to expire at 3:34 p.m. Values without a colon are treated as minutes. Each expiration-related attribute operates independently of other expiration-related attributes. |

## Work with DataLayer.Cached

Reports do not always need to use the absolutely most-current data. Data generated a few hours ago, yesterday, or last month is frequently what's required. In these circumstances, there's no point in burdening datasources by requesting this kind of data from them every single time a report is run and DataLayer.Cached offers the flexibility of an alternate approach.

DataLayer.Cached modifies the normal data retrieval activities of datalayers; when it's used, data is retrieved, cached, and made available for use in Logi reports for a specific time period, after which the data is refreshed (deleted and recreated). Its primary purpose is to reduce the number of data retrieval operations, such as complex SQL queries, that need to be run against the datasource.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771870359/dlcached_01.png)

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
documents.

The usual data caching mechanism associated with datalayers, in memory and/or on the web server's file system, also applies to this datalayer. This
is discussed in [The Logi Server Engine](https://devnet.logianalytics.com/hc/en-us/articles/1500009515722-The-Logi-Server-Engine) and may be of interest to developers working with
extremely large datasets or large numbers of concurrent users.

The data in the datalayer is available using **@Data****tokens**,
in the format @Data.*ColumnName*~. The spelling of the column name is
**case-sensitive**. The data is only available within the **scope** of the
**parent** element of the datalayer, not throughout the entire report
definition. The **DataLayer.Linked** element can be used to make the data reusable
in another datalayer outside this scope.

In Logi Info, the [Auto Columns](https://devnet.logianalytics.com/hc/en-us/articles/1500009529561-Auto-Columns)
element can be used to quickly display in your report all the data in a
datalayer.

The data retrieved into the datalayer can be viewed by turning on the
**Debugging Link** in your \_settings definition (**General** element) and using
the resulting link at the bottom of your report page to view the **Debugger Trace Report** page. There will be clear indications when the cache is being built and when data from it is being used. A link on the Trace page will display the actual cached data.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771870615/dlcached_02.png)

Studio includes a **wizard** that will add elements for the **columns** in the datalayer to your definition. You can select the desired columns before the operation begins. With the datalayer's parent **Data Table** or similar element selected in the Definition Editor, click the wizard link, shown above, in the Element Toolbox.

## Special Considerations

The following should be considered when using this datalayer:

### Joins

Developers may choose to retrieve data from multiple sources and use **Join** elements to combine it. How does DataLayer.Cached work in this scenario?

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771870871/dlcached_03.png)

As shown in the example above, all of the datalayers and joins can be placed beneath one DataLayer.Cached element and the data resulting from *all* of the joins will be cached.

This is fine if the currency of all of the data sources is similar. However, what if some of the data is updated more frequently than the rest?

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771871127/dlcached_04.png)

One approach when data has mixed currency, as shown above, is to use DataLayer.Cached to cache "long-term" data that *does not* change frequently and then join that data with another datalayer that retrieves "short-term" data that *does* change frequently.

If you have a large number of joins, then this approach depends upon your ability to relate the data appropriately (no short- and long-term datalayers interleaved).

What about caching at different levels of the join? Sorry, it's not possible to use a DataLayer.Cached element beneath a Join element.

### Time to Service Requests Can Vary

Typically, systems that cache data "snapshots", such as data marts and mini data warehouses, use independent processes to monitor the cache's expiration time and refresh it. However, no such process exists for DataLayer.Cached; cache expiration is tested with every request and the cache is refreshed when expiration is detected. This may result in some requests (those that cause the cache to be refreshed) taking longer than others, as the child datalayer that actually retrieves the data
will then run.

### Scope Issues

This datalayer can be used in multiple report definitions to access the same cached data (by using the same Cache Key value). It's very important, in such circumstances, that all instances of DataLayer.Cached, and its child elements, which access the same cache be *configured**identically*. They must have the exact same attribute settings and the exact same child datalayer, otherwise the cached data will be different and/or be set to expire differently, depending on which report definition's
request causes it to be refreshed. This is a good reason to consider implementing this datalayer as a Shared Element. For more information, see [Shared Elements](https://devnet.logianalytics.com/hc/en-us/articles/1500009531821-Shared-Elements).

### Not for Use with Subdatalayers

At this time, DataLayer.Cached should *not* be used with reports that include **Subdata Layer** elements; an error will result.
