---
title: "OpenSearch Connector IP Address Data Type Support"
id: 43701090973581
section: "Connect to Data in Composer 26"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701090973581-OpenSearch-Connector-IP-Address-Data-Type-Support
updated_at: 2026-05-29T14:07:51Z
---

# OpenSearch Connector IP Address Data Type Support

# OpenSearch Connector IP Address Data Type Support

The IP Address data type is supported for OpenSearch data connectors. Fields of this type are treated as ATTRIBUTEs and can be used in:

* An OpenSearch text search box. When searching via the text search, Composer also supports the CIDR notation for IP addresses.
* The Group By selection box.
* Filters, although Composer does not support CIDR notation in filters for an IP address field. An exact match is required.
* Row-level expressions. In row-level expressions, Composer treats IP addresses as strings and expect an exact match.

**Important:** If you are connecting to OpenSearch versions earlier than 2.x, use the [Elasticsearch 7 connector](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701025911309-Manage-the-Elasticsearch-Connector).
