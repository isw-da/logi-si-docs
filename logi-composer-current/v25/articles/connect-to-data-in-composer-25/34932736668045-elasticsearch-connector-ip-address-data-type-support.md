---
title: "Elasticsearch Connector IP Address Data Type Support"
id: 34932736668045
section: "Connect to Data in Composer 25"
product: "Logi Composer v25"
url: https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932736668045-Elasticsearch-Connector-IP-Address-Data-Type-Support
updated_at: 2026-05-26T22:06:36Z
---

# Elasticsearch Connector IP Address Data Type Support

# Elasticsearch Connector IP Address Data Type Support

The IP Address data type is supported for Elasticsearch data connectors. Fields of this type are treated as ATTRIBUTEs and can be used in:

* An Elasticsearch text search box. When searching via the text search, Composer also supports the CIDR notation for IP addresses as described in the Elasticsearch documentation (<https://www.elastic.co/guide/en/elasticsearch/reference/current/ip.html>).
* The Group By selection box.
* Filters, although Composer does not support CIDR notation in filters for an IP address field. An exact match is required.
* Row-level expressions. In row-level expressions, Composer treats IP addresses as strings and expect an exact match.
