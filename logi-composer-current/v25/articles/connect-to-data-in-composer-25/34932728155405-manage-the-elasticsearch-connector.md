---
title: "Manage the Elasticsearch Connector"
id: 34932728155405
section: "Connect to Data in Composer 25"
product: "Logi Composer v25"
url: https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932728155405-Manage-the-Elasticsearch-Connector
updated_at: 2026-05-26T22:06:34Z
---

# Manage the Elasticsearch Connector

# Manage the Elasticsearch Connector

The Composer Elasticsearch connector lets you access the data available in the Elasticsearch storage using the Composer client. The Composer Elasticsearch connector supports the following Elasticsearch versions.

* Elasticsearch 7.0 - 7.17

  **Note:** Use the Elasticsearch 7 connector to connect to OpenSearch earlier than 2.x. To connect to OpenSearch 2.x and higher, use the [OpenSearch connector](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/37515138873485-Manage-the-OpenSearch-Connector).
* Elasticsearch 8.1 - 8.17

**Important:** 
You cannot import or export Elasticsearch data sources (or the visuals and dashboards that use those Elasticsearch data sources) if the version of the Elasticsearch connector in the Composer environment is different from the version used by the data sources. For example, you cannot import an Elasticsearch 7 data source you have exported if your Composer environment only has an Elasticsearch 8 connector defined. When you change connector versions in your Composer environment, we recommend that you also create new data source configurations (and associated visuals and dashboards) for the newer version.

Before you can establish a connection from Composer to Elasticsearch storage, a connector server needs to be installed and configured.
See [Manage Connectors and Connector Servers](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932741363981-Manage-Connectors-and-Connector-Servers) for general instructions and [Connect to Elasticsearch](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932720750221-Connect-to-Elasticsearch) for details specific to the Elasticsearch connector.

After setting up the connector, create data sources that specify the necessary connection information and identify the data you want to use. See [Manage Data Sources](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932941009037-Manage-Data-Sources) for more information. After you set up your data sources, create [dashboards](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932763355021-Create-Dashboards) and [visuals](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933273224589-Create-and-Add-Visuals-to-the-Visual-Gallery) from from the data in these data sources. See [Create Dashboards](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932763355021-Create-Dashboards).

This section covers the following topics:

* [Composer Elasticsearch Connector Feature Support](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932745724813-Composer-Elasticsearch-Connector-Feature-Support)
* [Connect to Elasticsearch](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932720750221-Connect-to-Elasticsearch)
* [Connect to Elasticsearch Using Amazon Web Services Authentication](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932728210189-Connect-to-Elasticsearch-Using-Amazon-Web-Services-Authentication)
* [Elasticsearch Data Source Configuration Notes](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932745603597-Elasticsearch-Data-Source-Configuration-Notes)
* [Distinct Counts and Percentiles in Elasticsearch](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932745506573-Distinct-Counts-and-Percentiles-in-Elasticsearch)
* [Tokenization in Elasticsearch](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932746306701-Tokenization-in-Elasticsearch)
* [Elasticsearch Connector IP Address Data Type Support](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932736668045-Elasticsearch-Connector-IP-Address-Data-Type-Support)
* [Elasticsearch Last Value Processing](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932728934925-Elasticsearch-Last-Value-Processing)
* [Elasticsearch 7 Composite Aggregation](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932696922381-Elasticsearch-7-Composite-Aggregation)
* [Elasticsearch Source Document Storage Configurations](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932736907661-Elasticsearch-Source-Document-Storage-Configurations)
* [Inner Hits Configuration Property](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932736557197-Inner-Hits-Configuration-Property)
* [Support of X-Pack for Elasticsearch](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932721564685-Support-of-X-Pack-for-Elasticsearch)
