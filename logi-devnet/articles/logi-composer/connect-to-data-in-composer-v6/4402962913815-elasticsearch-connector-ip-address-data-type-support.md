---
title: "Elasticsearch Connector IP Address Data Type Support"
id: 4402962913815
section: "Connect to Data in Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4402962913815-Elasticsearch-Connector-IP-Address-Data-Type-Support
updated_at: 2021-08-07T17:30:00Z
---

# Elasticsearch Connector IP Address Data Type Support

# Elasticsearch Connector IP Address Data Type Support

The IP Address data type is supported for Elasticsearch data connectors. Fields of this type are treated as ATTRIBUTEs and can be used in:

* An Elasticsearch text search box. When searching via the text search, Composer also supports the CIDR notation for IP addresses as described in the Elasticsearch documentation (<https://www.elastic.co/guide/en/elasticsearch/reference/current/ip.html>).
* The Group By selection box.
* Filters, although Composer does not support CIDR notation in filters for an IP address field. An exact match is required.
* Row-level expressions. In row-level expressions, Composer treats IP addresses as strings and expect an exact match.
