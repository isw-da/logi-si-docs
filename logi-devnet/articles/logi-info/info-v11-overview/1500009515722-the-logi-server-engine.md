---
title: "The Logi Server Engine"
id: 1500009515722
section: "Info v11 Overview"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009515722-The-Logi-Server-Engine
updated_at: 2021-06-17T01:58:32Z
---

# The Logi Server Engine

# The Logi Server Engine

The **Logi Server Engine** is a file set, included with each Logi application, that extends the functionality of the web server. The files are processed at runtime and are usually cached by the web server for best performance. As web server extensions, they provide the server with the ability to interpret Logi definitions and data and generate appropriate output. The **Logi Data Engine** is the part of the Server Engine that handles data retrieval, temporary caching of that data as XML, and
manipulation of the data such as filtering and grouping. This topic discusses important aspects of the Server and Data Engines.

* About the Server Engine
* [Hybrid Caching](#Hybrid)
* [Improvements in the v10.1 Engine](#v10_1)

## About the Server Engine

The Server Engine is a collection of files that are part of every Logi application. As a result, multiple applications with different versions can co-exist on the same web server, and applications can be independently up- or down-graded to different versions. This has proven to be a worthwhile trade off for the additional disk space consumed by (possibly) redundant engine files.

The Data Engine is embedded within the Logi Server Engine and doesn't appear as a separate component during product installation. However, developers who have a good understanding of how it works may be able to take advantage of certain features in order to improve the performance of their applications.

At runtime, the Data Engine handles making a connection to data sources and retrieving the raw data. The raw data may be cached in memory or on disk depending on the *hybrid caching* scheme discussed in the next section. The cached data is then subjected to filtering, grouping, and other required manipulations before its ready to be rendered by other portions of the Server Engine.

The Debug Trace page displays distinct milestones for each phase of the data retrieval and manipulation process, and includes links that the developer can use to view the actual data in each phase. This is very useful in understanding the effects of and, given that a time scale is presented, the processing time required for, each operation.

The Server Engine includes a companion utility, **Server Manager**, which provides all the necessary application management features typically necessary on a production web server. This makes it unnecessary to license and install Logi Studio on the production server.

## Hybrid Caching

In Logi Info and Logi ETL, the Data Engine includes our "hybrid caching" feature, which provides improved management of web server resources, especially memory. *This feature is not available in Logi Report.*

When the a Logi application is responding to a request for a report, there are three distinct production phases that involve data manipulation:

1. When a datalayer *retrieves* data and *caches* it as an XML stream,
2. When that cache is *processed* using filtering, grouping, and aggregation,
3. When the HTML output (the report page) is being *generated*.

These activities typically use web server **memory** but, if the amount of data involved is very large, the potential exists to literally run out of memory. The Data Engine manages this situation as illustrated below:

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778540311/serverengine_01.png)

The hybrid caching feature *prevents* out-of-memory conditions by allowing the data streams used in these operations to be dynamically switched between the web server's **memory** and the web server's **file system**. The engine continuously monitors the amount of data it's manipulating in each production phase and, if it exceeds a specific threshold, switches caching to the file system. If the amount of data drops below the threshold during subsequent phases, caching switches back to
memory.

Logi report developers can use the default memory consumption threshold (10MB) or set **special constants** in their application to tailor the threshold as needed.

### Configure Hybrid Caching

The following constant can be added to the **Constants** element in your \_Settings definition to configure the hybrid caching of data and rendered HTML:

|  |  |
| --- | --- |
| **Name** | **Description** |
| rdMemoryStreamLimit | This value sets the threshold, in MB, for shifting from memory caching to file system caching. A value of *0* will force all data and HTML caching to the file system; a value of *2048*, the maximum, will force it to memory. The default value is *10MB*. |

In general, the default setting is good for most purposes. Changes should be considered *only* if actual problems with memory or performance are observed. Switching to 100% memory-based caching may sound appealing from a performance perspective but may not actually provide the best overall use of resources in your server.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778385687/attnicon.gif) Note that the rdDataCache and rdDownload system folders are used to store a variety of other temporary files. Changing to 100% memory-based caching of data and HTML will *not* prevent these other files from being written to these folders.

## Improvements in the v10.1 Data Engine

Beginning with v10.1.18, a new version of the Data Engine, v10.1, has been included which delivers significant performance improvements.

In earlier versions, datalayers that had a number of child data manipulation elements (sorting, calculated columns, filters, grouping, etc.) handled those data operations in a rather *sequential* way: each manipulation required a full pass through the cached data. With the v10.1 engine, those data operations are analyzed and arranged into one or more *data operations plans*, which "pipeline" or group certain types of manipulations together, reducing the number of read/write passes required.

The result is a **20% - 50%****improvement** in data processing time and it's especially noticeable when working with large datasets and those requiring many manipulations, such as OLAP data.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771650711/serverengine_02.png)

A fragment of the **Debugger Trace** page is shown above. It provides a way for you to see what the Data Engine is doing by displaying the data operation plan, operations, and resulting data.

### Configure the Data Engine

The following constant can be added to the **Constants** element in your \_Settings definition to configure the Data Engine:

| Name | Description |
| --- | --- |
| rdDataEngine | Set this constant to *Version10.0* to "downshift" the Data Engine back to version 10.0 |
