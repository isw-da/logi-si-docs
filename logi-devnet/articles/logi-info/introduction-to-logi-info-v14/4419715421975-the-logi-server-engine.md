---
title: "The Logi Server Engine"
id: 4419715421975
section: "Introduction to Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419715421975-The-Logi-Server-Engine
updated_at: 2023-03-22T15:57:28Z
---

# The Logi Server Engine

# The Logi Server Engine

The **Logi Server Engine** is a file set, included with each Logi application, that extends the functionality of the web server. The files are processed at runtime and are usually cached by the web server for best performance. As web server extensions, they provide the server with the ability to process Logi definitions and data to generate an appropriate output. The **Logi Data Engine** is the part of the Server Engine that handles data retrieval, temporary caching of that data as XML, and
manipulation of the data such as filtering and grouping. This topic discusses important aspects of the Server and Data Engines.

The following topics discuss additional features of the Server and Data Engines:

* [Hybrid Caching](https://devnet.logianalytics.com/hc/en-us/articles/4419707752343-Hybrid-Caching#Hybrid)
* [Parallelization](https://devnet.logianalytics.com/hc/en-us/articles/4419707753367-Parallelization#Parallelization)

## About the Server Engine

The Server Engine is a collection of files that are part of every Logi application. As a result, multiple applications with different versions can co-exist on the same web server, and applications can be independently up- or down-graded to different versions. This has proven to be a worthwhile trade off for the additional disk space consumed by (possibly) redundant engine files.

The Data Engine is embedded within the Logi Server Engine and doesn't appear as a separate component during product installation. However, developers who have a good understanding of how it works may be able to take advantage of certain features in order to improve the performance of their applications.

At runtime, the Data Engine handles making a connection to data sources and retrieving the raw data. The raw data may be cached in memory or on disk depending on the *[Hybrid Caching](https://devnet.logianalytics.com/hc/en-us/articles/4419707752343-Hybrid-Caching)* scheme. The cached data is then subjected to filtering, grouping, and other required manipulations before its ready to be rendered by other portions of the Server Engine.

The Debug Trace page displays distinct milestones for each phase of the data retrieval and manipulation process, and includes links that the developer can use to view the actual data in each phase. This is very useful in understanding the effects of and, given that a time scale is presented, the processing time required for, each operation.

The Server Engine includes a companion utility, **Server Manager**, which provides all the necessary application management features typically necessary on a production web server. This makes it unnecessary to license and install Logi Studio on the production server.
