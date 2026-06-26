---
title: "Manage the Impala Connector"
id: 43701025595405
section: "Connect to Data in Composer 26"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701025595405-Manage-the-Impala-Connector
updated_at: 2026-05-29T14:11:29Z
---

# Manage the Impala Connector

# Manage the Impala Connector

The Composer Cloudera Impala™ connector allows you to visualize huge volumes of data stored in their Hadoop cluster in real time and with no ETL.
Composer supports Impala versions 3.2 - 3.4.

Before you can establish a connection from Composer to Cloudera Impala storage, a connector server needs to be installed and configured.
See [Manage Connectors and Connector Servers](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701042404749-Manage-Connectors-and-Connector-Servers) for general instructions and [Connect to Impala](#Connecti) for details specific to the Cloudera Impala connector.

After setting up the connector, create data sources that specify the necessary connection information and identify the data you want to use. See [Manage Data Sources](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701068934669-Manage-Data-Sources) for more information. After you set up your data sources, create [dashboards](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701076467981-Create-Dashboards) and [visuals](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701179894541-Create-and-Add-Visuals-to-the-Visual-Gallery) from from the data in these data sources. See [Create Dashboards](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701076467981-Create-Dashboards).

This topic describes:

* [Feature Support](#featuresupport)
* [Impala Authentication](#Impala)
* [Connect to Impala](#Connecti)
* [Impala Table Settings](#Tables)

See also:

* [Work With Distinct Counts on Cloudera Impala](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701043213709-Work-With-Distinct-Counts-on-Cloudera-Impala)
* [Enable Data Sharpening for Cloudera Impala Data Sources](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701025623565-Enable-Data-Sharpening-for-Cloudera-Impala-Data-Sources)

## Feature Support

Connector support for specific  [features](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43700992759565-Connector-Feature-Support) is shown in the following table.

**Key:** **Y** - Supported; **N** - Not Supported; N/A - not applicable

| Feature | Supported? | | | Notes |
| --- | --- | --- | --- | --- |
| [Admin-Defined Functions](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701029797901-Admin-Defined-Functions) | **Y** | | |  |
| [Box Plots](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701211727885-Box-Plots) | **Y** | | |  |
| [Custom SQL Queries](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701041493645-Custom-SQL-Queries) | **Y** | | | If you need to access a BigQuery partition, explicitly include an alias for the built in partition column in your select clause, such as `select *, _PARTITIONTIME as pt from projectId.datasetId.tableId`. |
| [Derived Fields (Row-Level Expressions)](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701078705933-Maintain-Derived-Fields) | **Y** | | |  |
| [Distinct Counts](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701030916365-Distinct-Counts) | **Y** | | | Cloudera Impala connectors can receive only a single distinct count field in a query. |
| [Fast Distinct Values](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701008284941-Fast-Distinct-Values) | N/A | | |  |
| [Group By Multiple Fields](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701054799373-Group-By-Multiple-Fields) | **Y** | | |  |
| [Group By Time](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701054819213-Group-By-Time) | **Y** | | |  |
| [Group By UNIX Time](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701041642381-Group-By-UNIX-Time) | **Y** | | |  |
| [Histogram Floating Point Values](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701041703437-Histogram-Floating-Point-Values) | **Y** | | |  |
| [Histograms](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701211617293-Bars-Histograms) | **Y** | | |  |
| [Kerberos Authentication](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701208766477-Configure-Kerberos-Single-Sign-On-SSO-Settings) | **Y** | | |  |
| [Last Value](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701008456845-Last-Value) | **Y** | | |  |
| [Live Mode and Playback](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701210493837-Live-Mode-and-Historical-Playback) | **Y** | | |  |
| [Multivalued Fields](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43700993039117-Multivalued-Fields) | N/A | | |  |
| [Nested Fields](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701068575501-Support-of-Nested-Data-Structures-in-Composer) | N/A | | |  |
| [Partitions](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701024301709-Partitions) | **Y** | | |  |
| [Pushdown Joins for Fusion Data Sources](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701134208269-Optimize-Joins) | **Y** | | |  |
| [Schemas](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701038566797-Schemas) | **Y** | | |  |
| [Text Search](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701041900045-Text-Search) | N/A | | |  |
| [TLS](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43700993160717-TLS) | **Y** | | |  |
| [User Delegation](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701039382541-Enable-User-Delegation) | **Y** | | |  |
| [Wildcard Filters](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701071787533-Apply-Wildcard-Filters-to-a-Visual-Filter-Snippet-or-Dashboard) | **Y** | | |  |
| [Wildcard Filters, Case-Insensitive Mode](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701038723341-Wildcard-Case-Insensitive-Filters) | **Y** | | |  |
| [Wildcard Filters, Case-Sensitive Mode](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43700993286669-Wildcard-Case-Sensitive-Filters) | **Y** | | |  |

The Cloudera Impala connector also supports Progress reporting. Progress reporting support allows the connector to report the progress of a running query. On the UI, this shows as **Reading *nn*%** in the upper left corner of a visual.

## Impala Authentication

Support is provided for passing along credentials for users with access privileges to Impala source. Delegation allows for Impala queries to be issued with the privileges from a specified user. This is available in the Connection page and is set as the **Do As User** list.
See [Enable User Delegation](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701039382541-Enable-User-Delegation) and [Apply User Delegation to a Connection](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701039356557-Apply-User-Delegation-to-a-Connection).

## Connect to Impala

When setting up an Impala connection, you need to provide the following.

1. Specify the JDBC URL. You can connect to your Impala data source using either simple user
   credentials authentication or Kerberos authentication with optional SSL encryption. Refer to
   [Connecting to Impala on Kerberized CDH](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701043234957-Connect-to-a-Kerberized-CDH-Cluster) or [Connecting to Impala with TLS (SSL)](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701025646093-Connect-to-Impala-with-TLS-SSL-Enabled) for more details on the configuration.

   Composer enables you to connect either to a single Impala node or to multiple nodes within a cluster.
   To connect to a single Impala node, specify a JDBC URL in the following format:

   jdbc:hive2://<impala\_host>:<port>/;auth=noSas​l

   To connect to multiple Impala nodes, specify the required JDBC URLs separated by commas. The URLs will be used in a round-robin fashion. Keep in mind that such a connection will be valid as long as there is at least one available node. If all the nodes can not be reached, then the connection won't be validated.
2. If Impala authentication has been set up, provide a user name and password.
3. To allow for Impala user delegation, select the appropriate custom user attribute from the **Do As User** drop-down list (set up by the Composer supervisor or administrator).
   This basically allows Composer to pass along credentials for the specified user with access rights to Impala. See [Enable User Delegation](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701039382541-Enable-User-Delegation) and [Apply User Delegation to a Connection](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701039356557-Apply-User-Delegation-to-a-Connection).
4. Select **Validate**. If successfully validated, the connection is saved.

## Impala Table Settings

Time-based fields can be configured for partitioning in an Impala [data source configuration](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701068934669-Manage-Data-Sources) using the **Partition** column on the Fields tab of the data source. The following options are available:

* No (partitioning to be done)
* Date - this option is available for the Time field type. If you select this option, the list of the partitioned columns will be displayed in the Configure column.

  ![](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46242734563469)
* Function - If you select this option, the list of the partitioned columns and supported MURMUR3\_HASH function will be displayed in the Configure column.

  ![](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46242724035341)

Numeric and time-based fields can be edited using the Fields tab:

* Numeric type Number - ability to select a default aggregation function
* Time fields - ability to define the default time pattern and granularity; if the time field provides granularities of hour, minute and second, then a
  time zone
  label may be applied.

Select the checkbox in the **Distinct Count** column for any fields if a distinct count is needed.
For more information, see [Work With Distinct Counts on Cloudera Impala](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701043213709-Work-With-Distinct-Counts-on-Cloudera-Impala).
