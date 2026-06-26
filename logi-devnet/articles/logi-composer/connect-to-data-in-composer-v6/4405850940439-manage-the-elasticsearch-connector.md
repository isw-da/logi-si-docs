---
title: "Manage the Elasticsearch Connector"
id: 4405850940439
section: "Connect to Data in Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405850940439-Manage-the-Elasticsearch-Connector
updated_at: 2021-09-21T01:27:22Z
---

# Manage the Elasticsearch Connector

# Manage the Elasticsearch Connector

The Composer Elasticsearch connector lets you access the data available in the Elasticsearch storage using the Composer client. The Composer Elasticsearch connector supports the following Elasticsearch versions.

* Elasticsearch 6.0 - 6.8
* Elasticsearch 7.0 - 7.12

![](https://devnet.logianalytics.com/hc/article_attachments/4406747382295/noteicon.jpg) You cannot import or export Elasticsearch data sources (or the visuals and dashboards that use those Elasticsearch data sources) if the version of the Elasticsearch connector in the Composer environment is different from the version used by the data sources. For example, you cannot import an Elasticsearch 6 data source you have exported if your Composer environment only has an Elasticsearch 7 connector defined. When you change connector versions in your Composer environment, we recommend that you also create new data source configurations (and associated visuals and dashboards) for the newer version.

Before you can establish a connection from Composer to Elasticsearch storage, a connector server needs to be installed and configured.
See [*Manage Connectors and Connector Servers*](https://devnet.logianalytics.com/hc/en-us/articles/4405859186199-Manage-Connectors-and-Connector-Servers) for general instructions and [*Connect to Elasticsearch*](https://devnet.logianalytics.com/hc/en-us/articles/4405850941591-Connect-to-Elasticsearch) for details specific to the Elasticsearch connector.

After the connector has been set up, you can create data source configurations that specify the necessary connection information and identify the data you want to use. See [*Manage Data Source Configurations*](https://devnet.logianalytics.com/hc/en-us/articles/4405851027479-Manage-Data-Source-Configurations) for more information. After data sources are configured, they can be used to create dashboards and visuals from your data. See [*Create Dashboards*](https://devnet.logianalytics.com/hc/en-us/articles/4405859261207-Create-Dashboards).

This section covers the following topics:

* [*Composer Feature Support*](https://devnet.logianalytics.com/hc/en-us/articles/4405850945303-Composer-Feature-Support)
* [*Connect to Elasticsearch*](https://devnet.logianalytics.com/hc/en-us/articles/4405850941591-Connect-to-Elasticsearch)
* [*Elasticsearch Data Source Configuration Notes*](https://devnet.logianalytics.com/hc/en-us/articles/4405850944279-Elasticsearch-Data-Source-Configuration-Notes)
* [*Distinct Counts and Percentiles in Elasticsearch*](https://devnet.logianalytics.com/hc/en-us/articles/4405850942487-Distinct-Counts-and-Percentiles-in-Elasticsearch)
* [*Tokenization in Elasticsearch*](https://devnet.logianalytics.com/hc/en-us/articles/4405850952855-Tokenization-in-Elasticsearch)
* [*Elasticsearch Connector IP Address Data Type Support*](https://devnet.logianalytics.com/hc/en-us/articles/4405850949911-Elasticsearch-Connector-IP-Address-Data-Type-Support)
* [*Elasticsearch Last Value Processing*](https://devnet.logianalytics.com/hc/en-us/articles/4405850951063-Elasticsearch-Last-Value-Processing)
* [*Elasticsearch 7 Composite Aggregation*](https://devnet.logianalytics.com/hc/en-us/articles/4405859223063-Elasticsearch-7-Composite-Aggregation)
* [*Elasticsearch Source Document Storage Configurations*](https://devnet.logianalytics.com/hc/en-us/articles/4405850951959-Elasticsearch-Source-Document-Storage-Configurations)
* [*Inner Hits Configuration Property*](https://devnet.logianalytics.com/hc/en-us/articles/4405850948375-Inner-Hits-Configuration-Property)
* [*Support of X-Pack for Elasticsearch*](https://devnet.logianalytics.com/hc/en-us/articles/4405850953751-Support-of-X-Pack-for-Elasticsearch)
