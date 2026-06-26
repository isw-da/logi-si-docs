---
title: "OpenSearch Connector IP Address Data Type Support"
id: 37515123321357
section: "Connect to Data in Composer 25"
product: "Logi Composer v25"
url: https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/37515123321357-OpenSearch-Connector-IP-Address-Data-Type-Support
updated_at: 2026-05-26T22:05:56Z
---

# OpenSearch Connector IP Address Data Type Support

# OpenSearch Connector IP Address Data Type Support

The IP Address data type is supported for OpenSearch data connectors. Fields of this type are treated as ATTRIBUTEs and can be used in:

* An OpenSearch text search box. When searching via the text search, Composer also supports the CIDR notation for IP addresses.
* The Group By selection box.
* Filters, although Composer does not support CIDR notation in filters for an IP address field. An exact match is required.
* Row-level expressions. In row-level expressions, Composer treats IP addresses as strings and expect an exact match.

**Important:** If you are connecting to OpenSearch versions earlier than 2.x, use the [Elasticsearch 7 connector](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932728155405-Manage-the-Elasticsearch-Connector).
