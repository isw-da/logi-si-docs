---
title: "Manage the Impala Connector"
id: 4405850938647
section: "Connect to Data in Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405850938647-Manage-the-Impala-Connector
updated_at: 2021-09-21T01:27:20Z
---

# Manage the Impala Connector

# Manage the Impala Connector

The Composer Cloudera Impala™ connector allows you to visualize huge volumes of data stored in their Hadoop cluster in real time and with no ETL.
Composer supports Impala versions 2.7 - 3.2.

Before you can establish a connection from Composer to Cloudera Impala storage, a connector server needs to be installed and configured.
See [*Manage Connectors and Connector Servers*](https://devnet.logianalytics.com/hc/en-us/articles/4405859186199-Manage-Connectors-and-Connector-Servers) for general instructions and [*Connect to Impala*](#Connecti) for details specific to the Cloudera Impala connector.

After the connector has been set up, you can create data source configurations that specify the necessary connection information and identify the data you want to use. See [*Manage Data Source Configurations*](https://devnet.logianalytics.com/hc/en-us/articles/4405851027479-Manage-Data-Source-Configurations) for more information. After data sources are configured, they can be used to create dashboards and visuals from your data. See [*Create Dashboards*](https://devnet.logianalytics.com/hc/en-us/articles/4405859261207-Create-Dashboards).

This topic describes:

* [*Composer Feature Support*](#featuresupport)
* [*Impala Authentication*](#Impala)
* [*Connect to Impala*](#Connecti)
* [*Impala Table Settings*](#Tables)

See also:

* [*Work with Distinct Counts on Cloudera Impala*](https://devnet.logianalytics.com/hc/en-us/articles/4405850937367-Work-with-Distinct-Counts-on-Cloudera-Impala)
* [*Enable Data Sharpening for Cloudera Impala Data Sources*](https://devnet.logianalytics.com/hc/en-us/articles/4405859217687-Enable-Data-Sharpening-for-Cloudera-Impala-Data-Sources)

## Composer Feature Support

Cloudera Impala connector support for specific [Composer features](https://devnet.logianalytics.com/hc/en-us/articles/4405859170583-Connector-Feature-Support) is shown in the following table.

**Key:** **Y** - Supported; **N** - Not Supported; N/A - not applicable

| Feature | Supported? | | | Notes |
| --- | --- | --- | --- | --- |
| [Admin-Defined Functions](https://devnet.logianalytics.com/hc/en-us/articles/4405850995991-Admin-Defined-Functions) | **Y** | | |  |
| [Box Plots](https://devnet.logianalytics.com/hc/en-us/articles/4405859517207-Box-Plots) | **Y** | | |  |
| [Custom SQL Queries](https://devnet.logianalytics.com/hc/en-us/articles/4405859171735-Custom-SQL-Queries) | **Y** | | |  |
| [Derived Fields (Row-Level Expressions)](https://devnet.logianalytics.com/hc/en-us/articles/4405859299479-Maintain-Derived-Fields) | **Y** | | |  |
| [Distinct Counts](https://devnet.logianalytics.com/hc/en-us/articles/4405859300503-Enable-Distinct-Counts) | **Y** | | | Cloudera Impala connectors can receive only a single distinct count field in a query. |
| [Fast Distinct Values](https://devnet.logianalytics.com/hc/en-us/articles/4405850912279-Fast-Distinct-Values) | N/A | | |  |
| [Group By Multiple Fields](https://devnet.logianalytics.com/hc/en-us/articles/4405850913303-Group-By-Multiple-Fields) | **Y** | | |  |
| [Group By Time](https://devnet.logianalytics.com/hc/en-us/articles/4405850914199-Group-By-Time) | **Y** | | |  |
| [Group By UNIX Time](https://devnet.logianalytics.com/hc/en-us/articles/4405850915095-Group-By-UNIX-Time) | **Y** | | |  |
| [Histogram Floating Point Values](https://devnet.logianalytics.com/hc/en-us/articles/4405850915991-Histogram-Floating-Point-Values) | **Y** | | |  |
| [Histograms](https://devnet.logianalytics.com/hc/en-us/articles/4405859514775-Bars-Histograms) | **Y** | | |  |
| [Kerberos Authentication](https://devnet.logianalytics.com/hc/en-us/articles/4405859461271-Configure-Kerberos-Single-Sign-On-SSO-Settings) | **Y** | | |  |
| [Last Value](https://devnet.logianalytics.com/hc/en-us/articles/4405859174295-Last-Value) | **Y** | | |  |
| [Live Mode and Playback](https://devnet.logianalytics.com/hc/en-us/articles/4405851191447-Live-Mode-and-Historical-Playback) | **Y** | | |  |
| [Multivalued Fields](https://devnet.logianalytics.com/hc/en-us/articles/4405859175319-Multivalued-Fields) | N/A | | |  |
| [Nested Fields](https://devnet.logianalytics.com/hc/en-us/articles/4405851022871-Support-of-Nested-Data-Structures-in-Composer) | N/A | | |  |
| [Partitions](https://devnet.logianalytics.com/hc/en-us/articles/4405859176343-Partitions) | **Y** | | |  |
| [Pushdown Joins for Fusion Data Sources](https://devnet.logianalytics.com/hc/en-us/articles/4405859358487-Optimize-Joins) | **Y** | | |  |
| [Schemas](https://devnet.logianalytics.com/hc/en-us/articles/4405859177367-Schemas) | **Y** | | |  |
| [Text Search](https://devnet.logianalytics.com/hc/en-us/articles/4405859178391-Text-Search) | N/A | | |  |
| [TLS](https://devnet.logianalytics.com/hc/en-us/articles/4405859179671-TLS) | **Y** | | |  |
| [User Delegation](https://devnet.logianalytics.com/hc/en-us/articles/4405859193111-Enable-User-Delegation) | **Y** | | |  |
| [Wild Card Filters](https://devnet.logianalytics.com/hc/en-us/articles/4405851071383-Apply-Wild-Card-Filters-to-a-Visual-or-Dashboard) | **Y** | | |  |
| [Wild Card Filters, Case-Insensitive Mode](https://devnet.logianalytics.com/hc/en-us/articles/4405851071383-Apply-Wild-Card-Filters-to-a-Visual-or-Dashboard) | **Y** | | |  |
| [Wild Card Filters, Case-Sensitive Mode](https://devnet.logianalytics.com/hc/en-us/articles/4405851071383-Apply-Wild-Card-Filters-to-a-Visual-or-Dashboard) | **Y** | | |  |

The Cloudera Impala connector also supports Progress reporting. Progress reporting support allows the connector to report the progress of a running query. On the UI, this shows as **Reading *nn*%** in the upper left corner of a visual.

## Impala Authentication

Support is provided for passing along credentials for users with access privileges to Impala source. Delegation allows for Impala queries to be issued with the privileges from a specified user. This is available in the Connection page and is set as the **Do As User** list.
See [*Enable User Delegation*](https://devnet.logianalytics.com/hc/en-us/articles/4405859193111-Enable-User-Delegation) and [*Apply User Delegation to a Connection*](https://devnet.logianalytics.com/hc/en-us/articles/4405850928919-Apply-User-Delegation-to-a-Connection).

## Connect to Impala

When setting up an Impala connection, you need to provide the following.

1. Specify the JDBC URL. You can connect to your Impala data source using either simple user
   credentials authentication or Kerberos authentication with optional SSL encryption. Refer to
   [Connecting to Impala on Kerberized CDH](https://devnet.logianalytics.com/hc/en-us/articles/4405859216407-Connect-to-a-Kerberized-CDH-Cluster)
   or [Connecting to Impala with TLS (SSL)](https://devnet.logianalytics.com/hc/en-us/articles/4405850939543-Connect-to-Impala-with-TLS-SSL-Enabled)
   for more details on the configuration.

   Composer enables you to connect either to a single Impala node or to multiple nodes within a cluster.
   To connect to a single Impala node, specify a JDBC URL in the following format:

   ```
   jdbc:hive2://<impala_host>:<port>/;auth=noSas​l
   ```

   To connect to multiple Impala nodes, specify the required JDBC URLs separated by commas. The URLs will be used in a round-robin fashion. Keep in mind that such a connection will be valid as long as there is at least one available node. If all the nodes can not be reached, then the connection won't be validated.
2. If Impala authentication has been set up, provide a user name and password.
3. To allow for Impala user delegation, select the appropriate custom user attribute from the **Do As User** drop-down list (set up by the Composer supervisor or administrator).
   This basically allows Composer to pass along credentials for the specified user with access rights to Impala. See [*Enable User Delegation*](https://devnet.logianalytics.com/hc/en-us/articles/4405859193111-Enable-User-Delegation) and [*Apply User Delegation to a Connection*](https://devnet.logianalytics.com/hc/en-us/articles/4405850928919-Apply-User-Delegation-to-a-Connection).
4. Select **Validate**. If successfully validated, the connection is saved.

## Impala Table Settings

Time-based fields can be configured for partitioning in an Impala [data source configuration](https://devnet.logianalytics.com/hc/en-us/articles/4405851027479-Manage-Data-Source-Configurations) using the **Partition** column on the Fields tab of the data source configuration wizard. The following options are available:

* No (partitioning to be done)
* Date - this option is available for the Time field type. If you select this option, the list of the partitioned columns will be displayed in the Configure column.

  ![](https://devnet.logianalytics.com/hc/article_attachments/4406743907607/impala-partitioned-date_288x83.png)
* Function - If you select this option, the list of the partitioned columns and supported MURMUR3\_HASH function will be displayed in the Configure column.

  ![](https://devnet.logianalytics.com/hc/article_attachments/4406743908119/impala-partitioned-function_192x56.png)

Numeric and time-based fields can be edited using the **Configure** column of the Fields tab:

* Numeric types including Number and Integer - ability to select a default aggregation function
* Time fields - ability to define the default time pattern and granularity; if the time field provides granularities of hour, minute and second, then a
  time zone
  label may be applied.

Select the checkbox in the **Distinct Count** column for any fields if a distinct count is needed.
For more information, see [*Work with Distinct Counts on Cloudera Impala*](https://devnet.logianalytics.com/hc/en-us/articles/4405850937367-Work-with-Distinct-Counts-on-Cloudera-Impala).
