---
title: "Manage the Spark SQL Connector"
id: 34932799029901
section: "Connect to Data in Composer 25"
product: "Logi Composer v25"
url: https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932799029901-Manage-the-Spark-SQL-Connector
updated_at: 2026-05-26T22:06:44Z
---

# Manage the Spark SQL Connector

# Manage the Spark SQL Connector

The Composer Spark SQL connector lets you access the data available in Spark SQL databases using the Composer client. The Composer Spark SQL connector supports Spark SQL versions 2.3 through 3.0.

Before you can establish a connection from Composer to Spark SQL storage, a connector server needs to be installed and configured.
See [Manage Connectors and Connector Servers](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932741363981-Manage-Connectors-and-Connector-Servers) for general instructions and [Connect to Spark SQL](#Connecti) for details specific to the Spark SQL connector.

After setting up the connector, create data sources that specify the necessary connection information and identify the data you want to use. See [Manage Data Sources](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932941009037-Manage-Data-Sources) for more information. After you set up your data sources, create [dashboards](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932763355021-Create-Dashboards) and [visuals](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933273224589-Create-and-Add-Visuals-to-the-Visual-Gallery) from from the data in these data sources. See [Create Dashboards](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932763355021-Create-Dashboards).

## Feature Support

Connector support for specific  [features](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932704861453-Connector-Feature-Support) is shown in the following table.

**Key:** **Y** - Supported; **N** - Not Supported; N/A - not applicable

| Feature | Supported? | | | Notes |
| --- | --- | --- | --- | --- |
| [Admin-Defined Functions](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932796673933-Admin-Defined-Functions) | **Y** | | |  |
| [Box Plots](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933208692493-Box-Plots) | **Y** | | |  |
| [Custom SQL Queries](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932704947213-Custom-SQL-Queries) | **Y** | | | If you need to access a BigQuery partition, explicitly include an alias for the built in partition column in your select clause, such as `select *, _PARTITIONTIME as pt from projectId.datasetId.tableId`. |
| [Derived Fields (Row-Level Expressions)](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932839148813-Maintain-Derived-Fields) | **Y** | | |  |
| [Distinct Counts](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932867905037-Distinct-Counts) | **Y** | | |  |
| [Fast Distinct Values](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932715069197-Fast-Distinct-Values) | N/A | | |  |
| [Group By Multiple Fields](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932715164173-Group-By-Multiple-Fields) | **Y** | | |  |
| [Group By Time](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932690999309-Group-By-Time) | **Y** | | |  |
| [Group By UNIX Time](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932730700429-Group-By-UNIX-Time) | **Y** | | |  |
| [Histogram Floating Point Values](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932708132109-Histogram-Floating-Point-Values) | **Y** | | |  |
| [Histograms](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933212496141-Bars-Histograms) | **Y** | | |  |
| [Kerberos Authentication](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933139627149-Configure-Kerberos-Single-Sign-On-SSO-Settings) | **Y** | | | To enable Kerberos authentication, see [Connect to Spark SQL Sources on a Kerberized HDP Cluster](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932768085773-Connect-to-Spark-SQL-Sources-on-a-Kerberized-HDP-Cluster). |
| [Last Value](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932730888205-Last-Value) | **Y** | | |  |
| [Live Mode and Playback](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933163012621-Live-Mode-and-Historical-Playback) | **Y** | | |  |
| [Multivalued Fields](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932715662093-Multivalued-Fields) | N/A | | |  |
| [Nested Fields](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932861225357-Support-of-Nested-Data-Structures-in-Composer) | N/A | | |  |
| [Partitions](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932715778445-Partitions) | **Y** | | |  |
| [Pushdown Joins for Fusion Data Sources](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932963077133-Optimize-Joins) | **Y** | | |  |
| [Schemas](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932691729805-Schemas) | **Y** | | |  |
| [Text Search](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932739827853-Text-Search) | N/A | | |  |
| [TLS](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932692004749-TLS) | **N** | | |  |
| [User Delegation](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932742695053-Enable-User-Delegation) | **N** | | |  |
| [Wildcard Filters](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932977272717-Apply-Wildcard-Filters-to-a-Visual-Filter-Snippet-or-Dashboard) | **Y** | | |  |
| [Wildcard Filters, Case-Insensitive Mode](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932723779981-Wildcard-Case-Insensitive-Filters) | **Y** | | |  |
| [Wildcard Filters, Case-Sensitive Mode](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932692417677-Wildcard-Case-Sensitive-Filters) | **Y** | | |  |

## Connect to Spark SQL

When establishing a connection to Spark SQL, you need to provide the following information when setting up the partition settings.

Configure the partition settings. For the partitioned fields you can select one of the following options:

* **No**
* **Date**  - this option is available for the Time field type. If you select this option, the list of the partitioned columns will be displayed in the Configure column.

Numeric and time-based fields can be edited using the Fields tab:

* Numeric type Number - ability to select a default aggregation function
* Time fields - ability to define the default time pattern and granularity; if the time field provides granularities of hour, minute and second, then a
  time zone
  label may be applied.

When you create a data source, the specific number of distinct values for the attribute fields are saved in Composer depending on the data sample from your data set. You can filter the data on your visual by these values. While editing a data source, if you want to use all distinct values in the filter (that is from whole data source), select **Refresh** in the
**Statistics** column.
