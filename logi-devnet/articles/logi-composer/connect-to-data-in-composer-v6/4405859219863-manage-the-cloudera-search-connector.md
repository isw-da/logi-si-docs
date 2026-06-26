---
title: "Manage the Cloudera Search Connector"
id: 4405859219863
section: "Connect to Data in Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405859219863-Manage-the-Cloudera-Search-Connector
updated_at: 2021-09-21T01:27:20Z
---

# Manage the Cloudera Search Connector

# Manage the Cloudera Search Connector

Composer supports Cloudera Search version 4.10 - 7.4.

Before you can establish a connection from Composer to Cloudera Search storage, a connector server needs to be installed and configured.
See [*Manage Connectors and Connector Servers*](https://devnet.logianalytics.com/hc/en-us/articles/4405859186199-Manage-Connectors-and-Connector-Servers) for general instructions and [*Connect to Cloudera Search*](#Connecti) for details specific to the Cloudera Search connector.

After the connector has been set up, you can create data source configurations that specify the necessary connection information and identify the data you want to use. See [*Manage Data Source Configurations*](https://devnet.logianalytics.com/hc/en-us/articles/4405851027479-Manage-Data-Source-Configurations) for more information. After data sources are configured, they can be used to create dashboards and visuals from your data. See [*Create Dashboards*](https://devnet.logianalytics.com/hc/en-us/articles/4405859261207-Create-Dashboards).

## Composer Feature Support

Cloudera Search connector support for specific [Composer features](https://devnet.logianalytics.com/hc/en-us/articles/4405859170583-Connector-Feature-Support) is shown in the following table.

**Key:** **Y** - Supported; **N** - Not Supported; N/A - not applicable

| Feature | Supported? | | | Notes |
| --- | --- | --- | --- | --- |
| [Admin-Defined Functions](https://devnet.logianalytics.com/hc/en-us/articles/4405850995991-Admin-Defined-Functions) | **N** | | |  |
| [Box Plots](https://devnet.logianalytics.com/hc/en-us/articles/4405859517207-Box-Plots) | **N** | | | The Apache Solr versions prior to 5.3 used by Cloudera Search do not have the percentile aggregations required for box plots built in. |
| [Custom SQL Queries](https://devnet.logianalytics.com/hc/en-us/articles/4405859171735-Custom-SQL-Queries) | N/A | | |  |
| [Derived Fields (Row-Level Expressions)](https://devnet.logianalytics.com/hc/en-us/articles/4405859299479-Maintain-Derived-Fields) | **N** | | |  |
| [Distinct Counts](https://devnet.logianalytics.com/hc/en-us/articles/4405859300503-Enable-Distinct-Counts) | **Y** | | |  |
| [Fast Distinct Values](https://devnet.logianalytics.com/hc/en-us/articles/4405850912279-Fast-Distinct-Values) | **Y** | | |  |
| [Group By Multiple Fields](https://devnet.logianalytics.com/hc/en-us/articles/4405850913303-Group-By-Multiple-Fields) | **N** | | |  |
| [Group By Time](https://devnet.logianalytics.com/hc/en-us/articles/4405850914199-Group-By-Time) | **N** | | |  |
| [Group By UNIX Time](https://devnet.logianalytics.com/hc/en-us/articles/4405850915095-Group-By-UNIX-Time) | **N** | | |  |
| [Histogram Floating Point Values](https://devnet.logianalytics.com/hc/en-us/articles/4405850915991-Histogram-Floating-Point-Values) | **N** | | |  |
| [Histograms](https://devnet.logianalytics.com/hc/en-us/articles/4405859514775-Bars-Histograms) | **N** | | |  |
| [Kerberos Authentication](https://devnet.logianalytics.com/hc/en-us/articles/4405859461271-Configure-Kerberos-Single-Sign-On-SSO-Settings) | **Y** | | |  |
| [Last Value](https://devnet.logianalytics.com/hc/en-us/articles/4405859174295-Last-Value) | **N** | | |  |
| [Live Mode and Playback](https://devnet.logianalytics.com/hc/en-us/articles/4405851191447-Live-Mode-and-Historical-Playback) | **Y** | | |  |
| [Multivalued Fields](https://devnet.logianalytics.com/hc/en-us/articles/4405859175319-Multivalued-Fields) | **Y** | | |  |
| [Nested Fields](https://devnet.logianalytics.com/hc/en-us/articles/4405851022871-Support-of-Nested-Data-Structures-in-Composer) | **N** | | |  |
| [Partitions](https://devnet.logianalytics.com/hc/en-us/articles/4405859176343-Partitions) | N/A | | |  |
| [Pushdown Joins for Fusion Data Sources](https://devnet.logianalytics.com/hc/en-us/articles/4405859358487-Optimize-Joins) | **N** | | |  |
| [Schemas](https://devnet.logianalytics.com/hc/en-us/articles/4405859177367-Schemas) | N/A | | |  |
| [Text Search](https://devnet.logianalytics.com/hc/en-us/articles/4405859178391-Text-Search) | **Y** | | |  |
| [TLS](https://devnet.logianalytics.com/hc/en-us/articles/4405859179671-TLS) | **Y** | | |  |
| [User Delegation](https://devnet.logianalytics.com/hc/en-us/articles/4405859193111-Enable-User-Delegation) | **Y** | | |  |
| [Wild Card Filters](https://devnet.logianalytics.com/hc/en-us/articles/4405851071383-Apply-Wild-Card-Filters-to-a-Visual-or-Dashboard) | **Y** | | |  |
| [Wild Card Filters, Case-Insensitive Mode](https://devnet.logianalytics.com/hc/en-us/articles/4405851071383-Apply-Wild-Card-Filters-to-a-Visual-or-Dashboard) | **N** | | | Case-sensitivity cannot be enforced. Consequently, neither case-sensitive or case-insensitive wild card filters are supported. |
| [Wild Card Filters, Case-Sensitive Mode](https://devnet.logianalytics.com/hc/en-us/articles/4405851071383-Apply-Wild-Card-Filters-to-a-Visual-or-Dashboard) | **N** | | | Case-sensitivity cannot be enforced. Consequently, neither case-sensitive or case-insensitive wild card filters are supported. |

In addition, Cloudera Search supports the Request Handler field on the [Tables/Indices](https://devnet.logianalytics.com/hc/en-us/articles/4405859323287-Tables-Indices-Tab) tab of the [data source configuration](https://devnet.logianalytics.com/hc/en-us/articles/4405851027479-Manage-Data-Source-Configurations). You can use this box at the top of the Field table on the Tables/Indices tab to specify a request handler plug-in that defines the logic used when executing a search request.

## Connect to Cloudera Search

When establishing a connection to a new Cloudera Search server, you need to provide the following:

* The connection name
* The Base URL
