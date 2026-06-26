---
title: "Manage the Snowflake Connector"
id: 4405859234199
section: "Connect to Data in Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405859234199-Manage-the-Snowflake-Connector
updated_at: 2021-09-21T01:27:30Z
---

# Manage the Snowflake Connector

# Manage the Snowflake Connector

The Composer Snowflake connector lets you access the data available in Snowflake storage using the Composer client. The Composer Snowflake connector supports whatever Snowflake version is currently available in the cloud.

Before you can establish a connection from Composer to Snowflake storage, a connector server needs to be installed and configured.
See [*Manage Connectors and Connector Servers*](https://devnet.logianalytics.com/hc/en-us/articles/4405859186199-Manage-Connectors-and-Connector-Servers) for general instructions and [*Connect to Snowflake*](#Connecti) for details specific to the Snowflake connector.

After the connector has been set up, you can create data source configurations that specify the necessary connection information and identify the data you want to use. See [*Manage Data Source Configurations*](https://devnet.logianalytics.com/hc/en-us/articles/4405851027479-Manage-Data-Source-Configurations) for more information. After data sources are configured, they can be used to create dashboards and visuals from your data. See [*Create Dashboards*](https://devnet.logianalytics.com/hc/en-us/articles/4405859261207-Create-Dashboards).

## Composer Feature Support

Snowflake connector support for specific [Composer features](https://devnet.logianalytics.com/hc/en-us/articles/4405859170583-Connector-Feature-Support) is shown in the following table.

**Key:** **Y** - Supported; **N** - Not Supported; N/A - not applicable

| Feature | Supported? | |
| --- | --- | --- |
| [Admin-Defined Functions](https://devnet.logianalytics.com/hc/en-us/articles/4405850995991-Admin-Defined-Functions) | **Y** | |
| [Box Plots](https://devnet.logianalytics.com/hc/en-us/articles/4405859517207-Box-Plots) | **Y** | |
| [Custom SQL Queries](https://devnet.logianalytics.com/hc/en-us/articles/4405859171735-Custom-SQL-Queries) | **Y** | |
| [Derived Fields (Row-Level Expressions)](https://devnet.logianalytics.com/hc/en-us/articles/4405859299479-Maintain-Derived-Fields) | **Y** | |
| [Distinct Counts](https://devnet.logianalytics.com/hc/en-us/articles/4405859300503-Enable-Distinct-Counts) | **Y** | |
| [Fast Distinct Values](https://devnet.logianalytics.com/hc/en-us/articles/4405850912279-Fast-Distinct-Values) | N/A | |
| [Group By Multiple Fields](https://devnet.logianalytics.com/hc/en-us/articles/4405850913303-Group-By-Multiple-Fields) | **Y** | |
| [Group By Time](https://devnet.logianalytics.com/hc/en-us/articles/4405850914199-Group-By-Time) | **Y** | |
| [Group By UNIX Time](https://devnet.logianalytics.com/hc/en-us/articles/4405850915095-Group-By-UNIX-Time) | **Y** | |
| [Histogram Floating Point Values](https://devnet.logianalytics.com/hc/en-us/articles/4405850915991-Histogram-Floating-Point-Values) | **Y** | |
| [Histograms](https://devnet.logianalytics.com/hc/en-us/articles/4405859514775-Bars-Histograms) | **Y** | |
| [Kerberos Authentication](https://devnet.logianalytics.com/hc/en-us/articles/4405859461271-Configure-Kerberos-Single-Sign-On-SSO-Settings) | **N** | |
| [Last Value](https://devnet.logianalytics.com/hc/en-us/articles/4405859174295-Last-Value) | **Y** | |
| [Live Mode and Playback](https://devnet.logianalytics.com/hc/en-us/articles/4405851191447-Live-Mode-and-Historical-Playback) | **Y** | |
| [Multivalued Fields](https://devnet.logianalytics.com/hc/en-us/articles/4405859175319-Multivalued-Fields) | N/A | |
| [Nested Fields](https://devnet.logianalytics.com/hc/en-us/articles/4405851022871-Support-of-Nested-Data-Structures-in-Composer) | N/A | |
| [Partitions](https://devnet.logianalytics.com/hc/en-us/articles/4405859176343-Partitions) | **N** | |
| [Pushdown Joins for Fusion Data Sources](https://devnet.logianalytics.com/hc/en-us/articles/4405859358487-Optimize-Joins) | **Y** | |
| [Schemas](https://devnet.logianalytics.com/hc/en-us/articles/4405859177367-Schemas) | **Y** | |
| [Text Search](https://devnet.logianalytics.com/hc/en-us/articles/4405859178391-Text-Search) | N/A | |
| [TLS](https://devnet.logianalytics.com/hc/en-us/articles/4405859179671-TLS) | **Y** | |
| [User Delegation](https://devnet.logianalytics.com/hc/en-us/articles/4405859193111-Enable-User-Delegation) | **N** | |
| [Wild Card Filters](https://devnet.logianalytics.com/hc/en-us/articles/4405851071383-Apply-Wild-Card-Filters-to-a-Visual-or-Dashboard) | **Y** | |
| [Wild Card Filters, Case-Insensitive Mode](https://devnet.logianalytics.com/hc/en-us/articles/4405851071383-Apply-Wild-Card-Filters-to-a-Visual-or-Dashboard) | **Y** | |
| [Wild Card Filters, Case-Sensitive Mode](https://devnet.logianalytics.com/hc/en-us/articles/4405851071383-Apply-Wild-Card-Filters-to-a-Visual-or-Dashboard) | **Y** | |

## Connect to Snowflake

The version 3.12.11 JDBC driver is included with the Snowflake connector, but you can download a newer version from <https://repo1.maven.org/maven2/net/snowflake/snowflake-jdbc/>. See [*Add a JDBC Driver*](https://devnet.logianalytics.com/hc/en-us/articles/4405859376919-Add-a-JDBC-Driver).

When setting up a connection to Snowflake, you need to provide the following:

* The name of the connection
* The JDBC URL.
* Each Snowflake connection must be associated with a database. It may be the database specified in the JDBC URL or the default data base of the connecting user (when no database is specified in the JDBC URL).
* The username and password. Only simple username and password authentication is supported.

Snowflake officially supports each of its client versions for a minimum of two years: <https://docs.snowflake.net/manuals/release-notes/requirements.html#support-policy>. If the JDBC driver is not updated for two years, the Snowflake connector may stop working. Composer regularly updates the JDBC driver, however if you do not update your Snowflake connector for a long time, you may encounter problems. If this happens, you can manually update the JDBC driver yourself. Composer provides it in `/opt/zoomdata/lib/edc-snowflake`.

## Snowflake Time Field Conversion

The Composer Snowflake connector converts date-time fields with data types of TIMESTAMP\_TZ (a Snowflake data type) to Coordinated Universal Time (UTC) format. The connector also sets the session timezone to UTC format, which means that all Snowflake fields that use the Snowflake local timezone data type TIMESTAMP\_LTZ are also converted to UTC format.

## Configure the Snowflake Clustering Depth Threshold

Snowflake does not have an index, but supports micro-partitions and clustering keys instead. It uses a clustering depth for a table column to indicate whether the clustering state of the column has improved or deteriorated as a result of data changes in the table. A value of 1.0 for the clustering depth indicates that the column is fully clustered. A higher clustering depth indicates that the Snowflake table is not optimally clustered. See [Understanding Snowflake Table Structures](https://docs.snowflake.com/en/user-guide/tables-micro-partitions.html).

To define playability of date or numeric fields, the Composer Snowflake connector uses the relative clustering depth of these fields in relation to the total number of partitions in the table, computed as a percentage using the following formula:

```
AverageClusteringDepth / MAX(TotalPartitionCount, 100) * 100
```

If the relative clustering depth of a field is equal to or less than a set threshold value, it is considered to be playable. The default clustering depth threshold is 10%, but can be changed by changing the following Snowflake configuration property in the Snowflake properties file (`edc-snowflake.properties`):

```
snowflake.metadata-detection.fast-range-queries.max-clustering-depth-percent=<nnn>
```

See [*Connector Properties and Property Files*](https://devnet.logianalytics.com/hc/en-us/articles/4405850892439-Connector-Properties-and-Property-Files).

The clustering depth threshold allows Composer to enable playback and live mode for all fields that are optimally clustered and disable it for all fields that are not. Adjust the threshold value or recluster your Snowflake tables to better handle intermediate cases.
