---
title: "Elasticsearch Connector IP Address Data Type Support"
id: 43700995024653
section: "Connect to Data in Composer 26"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43700995024653-Elasticsearch-Connector-IP-Address-Data-Type-Support
updated_at: 2026-05-29T14:07:39Z
---

# Elasticsearch Connector IP Address Data Type Support

# Elasticsearch Connector IP Address Data Type Support

The IP Address data type is supported for Elasticsearch data connectors. Fields of this type are treated as ATTRIBUTEs and can be used in:

* An Elasticsearch text search box. When searching via the text search, Composer also supports the CIDR notation for IP addresses as described in the Elasticsearch documentation (<https://www.elastic.co/guide/en/elasticsearch/reference/current/ip.html>).
* The Group By selection box.
* Filters, although Composer does not support CIDR notation in filters for an IP address field. An exact match is required.
* Row-level expressions. In row-level expressions, Composer treats IP addresses as strings and expect an exact match.
