---
title: "Data Connector Microservices"
id: 4405851116951
section: "Introduction to  Logi Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405851116951-Data-Connector-Microservices
updated_at: 2022-08-25T11:32:17Z
---

# Data Connector Microservices

# Data Connector Microservices

Composer offers the widest set of connectors for modern data stores deployed on-premises or in the cloud, such as Hadoop, NoSQL, search engines, and modern data warehouses. In addition to the set of standard, out-of-the-box, data connectors that Composer provides, you can create custom data connectors.

Composer's standard, out-of-the-box, data connectors are smart, leveraging the unique capabilities of each data platform to take advantage of query expressiveness and to optimize performance. For example, Composer's data connectors leverage:

* Data partitions in Impala and other similar sources
* Faceted search when querying an unstructured data search engine such as Elasticsearch or Solr
* Native APIs for NoSQL databases.

The data connectors use native APIs either in whole or in part to interact with the target data store. For some modern data platforms, all user interactions are converted to native API calls. For data stores that can be queried using SQL over a JDBC driver, the data connector uses SQL when available and native API calls when necessary. For example, a data store may support query cancellation, but its JDBC driver may not. Composer data connectors are smart enough to enrich the data interaction experience beyond standard off-the-shelf functionality.

Composer's microservices-based architecture allows your developers to build connectivity to proprietary data platforms or to data for which a native connector is not currently available. Custom connectors can also be smart by making full use of the Composer query engine, including its Data Sharpening and live mode functionality as well as enabling custom security features such as user delegation and Kerberos authentication.

Custom connectors can also be used to extend Composer data connectors with additional business rules. For example, a custom connector can implement the logic necessary to query specific tables based on the end user's group membership.

Each Composer data connector deploys as a standalone Thrift server running in its own Java processing space and registers with Consul and Composer's Service Monitor as a Composer microservice.

For complete information about Composer data connectors, see [*Connect Composer to Data Stores*](https://devnet.logianalytics.com/hc/en-us/articles/4405850922903-Connect-Composer-to-Data-Stores).
