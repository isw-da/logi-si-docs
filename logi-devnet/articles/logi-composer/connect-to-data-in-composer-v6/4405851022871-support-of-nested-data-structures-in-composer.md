---
title: "Support of Nested Data Structures in Composer"
id: 4405851022871
section: "Connect to Data in Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405851022871-Support-of-Nested-Data-Structures-in-Composer
updated_at: 2021-09-21T01:28:11Z
---

# Support of Nested Data Structures in Composer

# Support of Nested Data Structures in Composer

Composer supports aggregations for nested (or hierarchical) data structures for some data stores.

Support for this feature by Composer connectors is shown in the following table.

**Key:****Y** - Supported; **N** - Not Supported; N/A - not applicable

| Connector | Supported? | |
| --- | --- | --- |
| [Amazon Redshift](https://devnet.logianalytics.com/hc/en-us/articles/4405859198103-Manage-the-Amazon-Redshift-Connector) | N/A | |
| [Amazon S3](https://devnet.logianalytics.com/hc/en-us/articles/4405850929943-Manage-the-Amazon-S3-Connector) | N/A | |
| [Apache Drill](https://devnet.logianalytics.com/hc/en-us/articles/4405850930839-Manage-the-Apache-Drill-Connector) | N/A | |
| [Apache Phoenix](https://devnet.logianalytics.com/hc/en-us/articles/4405859202839-Manage-the-Apache-Phoenix-Connector) | N/A | |
| [Apache Phoenix Query Server (QS)](https://devnet.logianalytics.com/hc/en-us/articles/4405859202839-Manage-the-Apache-Phoenix-Connector) | N/A | |
| [Apache Solr](https://devnet.logianalytics.com/hc/en-us/articles/4405850931735-Manage-the-Apache-Solr-Connector) | **N** | |
| [BigQuery](https://devnet.logianalytics.com/hc/en-us/articles/4405859214231-Manage-the-BigQuery-Connector) | N/A | |
| [Cloudera Impala](https://devnet.logianalytics.com/hc/en-us/articles/4405850938647-Manage-the-Impala-Connector) | N/A | |
| [Cloudera Search](https://devnet.logianalytics.com/hc/en-us/articles/4405859219863-Manage-the-Cloudera-Search-Connector) | **N** | |
| [Couchbase](https://devnet.logianalytics.com/hc/en-us/articles/4405859220887-Manage-the-Couchbase-Connector) | N/A | |
| [Dremio](https://devnet.logianalytics.com/hc/en-us/articles/4405859221911-Manage-the-Dremio-Connector) | N/A | |
| [Elasticsearch 6.0](https://devnet.logianalytics.com/hc/en-us/articles/4405850940439-Manage-the-Elasticsearch-Connector) | **Y** | |
| [Elasticsearch 7.0](https://devnet.logianalytics.com/hc/en-us/articles/4405850940439-Manage-the-Elasticsearch-Connector) | **Y** | |
| [Flat File](https://devnet.logianalytics.com/hc/en-us/articles/4405850954647-Upload-a-Flat-File-into-Composer) | N/A | |
| [HDFS](https://devnet.logianalytics.com/hc/en-us/articles/4405859226903-Manage-the-HDFS-Connector) | N/A | |
| [Hive](https://devnet.logianalytics.com/hc/en-us/articles/4405850956695-Manage-the-Hive-Connector) | N/A | |
| [MemSQL](https://devnet.logianalytics.com/hc/en-us/articles/4405859228567-Manage-the-MemSQL-Connector) | N/A | |
| [Microsoft SQL Server](https://devnet.logianalytics.com/hc/en-us/articles/4405859229975-Manage-the-Microsoft-SQL-Server-Connector) | N/A | |
| [MongoDB](https://devnet.logianalytics.com/hc/en-us/articles/4405850957591-Manage-the-MongoDB-Connector) | **Y** | |
| [MySQL](https://devnet.logianalytics.com/hc/en-us/articles/4405850958487-Manage-the-MySQL-Connector) | N/A | |
| [Oracle](https://devnet.logianalytics.com/hc/en-us/articles/4405850959383-Manage-the-Oracle-Connector) | N/A | |
| [PostgreSQL](https://devnet.logianalytics.com/hc/en-us/articles/4405850960279-Manage-the-PostgreSQL-Connector) | N/A | |
| [Presto](https://devnet.logianalytics.com/hc/en-us/articles/4405859231639-Manage-the-Presto-Connector) | N/A | |
| [Real Time Sales](https://devnet.logianalytics.com/hc/en-us/articles/4405850962071-Manage-the-Real-Time-Sales-Demo-Source) | N/A | |
| [SAP Hana](https://devnet.logianalytics.com/hc/en-us/articles/4405859232791-Manage-the-SAP-Hana-Connector) | N/A | |
| [SAP IQ](https://devnet.logianalytics.com/hc/en-us/articles/4405850963095-Manage-the-SAP-IQ-Connector) | N/A | |
| [Snowflake](https://devnet.logianalytics.com/hc/en-us/articles/4405859234199-Manage-the-Snowflake-Connector) | N/A | |
| [Spark SQL](https://devnet.logianalytics.com/hc/en-us/articles/4405850963991-Manage-the-Spark-SQL-Connector) | N/A | |
| [Teradata](https://devnet.logianalytics.com/hc/en-us/articles/4405859235607-Manage-the-Teradata-Connector) | N/A | |
| [TIBCO DV](https://devnet.logianalytics.com/hc/en-us/articles/4405850965783-Manage-the-TIBCO-Data-Virtualization-TDV-Connector) | N/A | |
| [Upload API](https://devnet.logianalytics.com/hc/en-us/articles/4405859140247-Use-the-Upload-API) | N/A | |
| [Vertica](https://devnet.logianalytics.com/hc/en-us/articles/4405850966679-Manage-the-Vertica-Connector) | N/A | |

There are two ways to store nested structure:

1. Store all hierarchy as a single document, for example, in JSON format (nested documents).
2. Store hierarchy items as separate documents and additional info on hierarchical links internally (block join).

## Nested Documents

Hierarchical structure can be represented in JSON format. In MongoDB and Elasticsearch, storing such structures is supported.

Consider the following example. We need to store a hierarchy of divisions by country with two divisions in country. Also we need to store some general country information, for example, foundation year.

In this case, the following JSON is sent to the index document:

```
{
	"country":"Germany",
	"foundation year":2008,
	"divisions":[
		{
			"city":"Berlin",
			"sales":200,
			"manager":{
				"first name":"Robert",
				"last name":"Simmons",
				"years in company":4
				}
		},
		{
			"city":"Munich",
			"sales":200,
			"manager":{
				"first name":"Robert",
				"last name":"Simmons",
				"years in company":4
				}
		}
	]
}
```

In MongoDB, you can store such documents and then query them as is, without any restrictions. However, the performance may be slow if the document contains a lot of arrays.

In Elasticsearch, we recommend using the "nested" type for complex objects before the document is indexed.

## Block Join Support

There is another way to store hierarchical structures. All hierarchy items are stored as separate elements, with information about the hierarchical links stored internally. Apache Solr supports this approach.

Consider the following example. We need to store a hierarchy of divisions by country with two divisions in country. Also we need to store some general country information, for example, foundation year.

In this case, the following JSON is sent to the index document:

```
{   
	"country":"Germany",   
	"foundationYear":2008,   
	"_childDocuments_":[
		{
			"city":"Berlin",
			"sales":200,  
			"managerFirstName":"Robert",  
			"managerLastName":"Simmons",  
			"managerYearsInCompany":4  
		},
		{
			"city":"Munich",
			"sales":200,
			"managerFirstName":"Robert",
			"managerLastName":"Simmons",
			"managerYearsInCompany":4 
		}
	]
}
```

As a result, there are three documents in the index. Information on hierarchical linking of these objects is stored internally in Solr.

```
{
	"country":"Germany",
	"foundationYear":2008
},
{
	"city":"Berlin",
	"sales":200,
	"managerFirstName":"Robert",
	"managerLastName":"Simmons",
	"managerYearsInCompany":4
},
{
	"city":"Munich",
	"sales":200,
	"managerFirstName":"Robert",
	"managerLastName":"Simmons",
	"managerYearsInCompany":4
}
```

You must specify what fields are used in parent documents. To do this, you must select the checkbox in the
**Parent Field** column on the
**Fields** tab while
[creating](https://devnet.logianalytics.com/hc/en-us/articles/4405859320727-Define-a-Data-Source-Configuration) or [modifying](https://devnet.logianalytics.com/hc/en-us/articles/4405851024663-Edit-a-Data-Source-Configuration) the data source
configuration
.
