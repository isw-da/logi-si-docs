---
title: "Manage the OpenSearch Connector"
id: 43701074183053
section: "Connect to Data in Composer 26"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701074183053-Manage-the-OpenSearch-Connector
updated_at: 2026-05-29T14:07:49Z
---

# Manage the OpenSearch Connector

# Manage the OpenSearch Connector

The Composer OpenSearch connector lets you access the data available in the OpenSearch storage using the Composer client. The Composer

OpenSearch connector supports the following OpenSearch versions.

* OpenSearch 2.x to 2.17

**Note:** To connect to OpenSearch versions earlier than 2.x, use the [Elasticsearch 7 connector](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701025911309-Manage-the-Elasticsearch-Connector). To connect to OpenSearch 2.x and higher, use the OpenSearch connector.

**Important:** 
You cannot import or export OpenSearch data sources (or the visuals and dashboards that use those OpenSearch data sources) if the version of the OpenSearch connector in the Composer environment is different from the version used by the data sources. When you change connector versions in your Composer environment, we recommend that you also create new data source configurations (and associated visuals and dashboards) for the newer version.

Before you can establish a connection from Composer to OpenSearch storage, a connector server needs to be installed and configured.
See [Manage Connectors and Connector Servers](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701042404749-Manage-Connectors-and-Connector-Servers) for general instructions and [Connect to OpenSearch](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701011633805-Connect-to-OpenSearch) for details specific to the OpenSearch connector.

After setting up the connector, create data sources that specify the necessary connection information and identify the data you want to use. See [Manage Data Sources](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701068934669-Manage-Data-Sources) for more information. After you set up your data sources, create [dashboards](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701076467981-Create-Dashboards) and [visuals](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701179894541-Create-and-Add-Visuals-to-the-Visual-Gallery) from from the data in these data sources. See [Create Dashboards](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701076467981-Create-Dashboards).

For information on securing your OpenSearch environment, see [https://docs.opensearch.org/docs/2.19/install-and-configure/configuring-opensearch/security-settings/](https://docs.opensearch.org/docs/2.19/install-and-configure/configuring-opensearch/security-settings/ "https://docs.opensearch.org/docs/2.19/install-and-configure/configuring-opensearch/security-settings/").

This section covers the following topics:

* [Composer OpenSearch Connector Feature Support](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701044572813-Composer-OpenSearch-Connector-Feature-Support)
* [Connect to OpenSearch](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701011633805-Connect-to-OpenSearch)
* [Connect to OpenSearch Using Amazon Web Services Authentication](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701011525645-Connect-to-OpenSearch-Using-Amazon-Web-Services-Authentication)
* [OpenSearch Data Source Configuration Notes](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701026691597-OpenSearch-Data-Source-Configuration-Notes)
* [Distinct Counts and Percentiles in OpenSearch](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701044503949-Distinct-Counts-and-Percentiles-in-OpenSearch)
* [Tokenization in OpenSearch](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43700995805069-Tokenization-in-OpenSearch)
* [OpenSearch Connector IP Address Data Type Support](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701090973581-OpenSearch-Connector-IP-Address-Data-Type-Support)
* [OpenSearch Last Value Processing](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701091011597-OpenSearch-Last-Value-Processing)
* [OpenSearch Composite Aggregation](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701044429709-OpenSearch-Composite-Aggregation)
* [OpenSearch Source Document Storage Configurations](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701011897101-OpenSearch-Source-Document-Storage-Configurations)
* [OpenSearch Inner Hits Configuration Property](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701011792013-OpenSearch-Inner-Hits-Configuration-Property)
