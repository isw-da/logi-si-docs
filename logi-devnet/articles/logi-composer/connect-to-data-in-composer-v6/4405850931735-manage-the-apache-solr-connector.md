---
title: "Manage the Apache Solr Connector"
id: 4405850931735
section: "Connect to Data in Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405850931735-Manage-the-Apache-Solr-Connector
updated_at: 2021-09-21T01:27:15Z
---

# Manage the Apache Solr Connector

# Manage the Apache Solr Connector

The Composer Apache Solr connector lets you access the data available in your Apache Solr databases using the Composer client. The Composer Apache Solr connector supports Apache Solr versions 7.4 through 8.4.

Before you can establish a connection from Composer to an Apache Solr database, a connector server needs to be installed, configured and enabled.
See [*Manage Connectors and Connector Servers*](https://devnet.logianalytics.com/hc/en-us/articles/4405859186199-Manage-Connectors-and-Connector-Servers) for general instructions and [*Connect to Apache Solr*](#Connecti) for details specific to the Apache Solr connector.

After the connector has been set up, you can create data source configurations that specify the necessary connection information and identify the data you want to use. See [*Manage Data Source Configurations*](https://devnet.logianalytics.com/hc/en-us/articles/4405851027479-Manage-Data-Source-Configurations) for more information. After data sources are configured, they can be used to create dashboards and visuals from your data. See [*Create Dashboards*](https://devnet.logianalytics.com/hc/en-us/articles/4405859261207-Create-Dashboards).

## Composer Feature Support

Apache Solr connector support for specific [Composer features](https://devnet.logianalytics.com/hc/en-us/articles/4405859170583-Connector-Feature-Support) is shown in the following table.

**Key:** **Y** - Supported; **N** - Not Supported; N/A - not applicable

| Feature | Supported? | | | Notes |
| --- | --- | --- | --- | --- |
| [Admin-Defined Functions](https://devnet.logianalytics.com/hc/en-us/articles/4405850995991-Admin-Defined-Functions) | **N** | | |  |
| [Box Plots](https://devnet.logianalytics.com/hc/en-us/articles/4405859517207-Box-Plots) | **Y** | | |  |
| [Custom SQL Queries](https://devnet.logianalytics.com/hc/en-us/articles/4405859171735-Custom-SQL-Queries) | N/A | | |  |
| [Derived Fields (Row-Level Expressions)](https://devnet.logianalytics.com/hc/en-us/articles/4405859299479-Maintain-Derived-Fields) | **N** | | |  |
| [Distinct Counts](https://devnet.logianalytics.com/hc/en-us/articles/4405859300503-Enable-Distinct-Counts) | **Y** | | |  |
| [Fast Distinct Values](https://devnet.logianalytics.com/hc/en-us/articles/4405850912279-Fast-Distinct-Values) | **Y** | | |  |
| [Group By Multiple Fields](https://devnet.logianalytics.com/hc/en-us/articles/4405850913303-Group-By-Multiple-Fields) | **Y** | | |  |
| [Group By Time](https://devnet.logianalytics.com/hc/en-us/articles/4405850914199-Group-By-Time) | **Y** | | |  |
| [Group By UNIX Time](https://devnet.logianalytics.com/hc/en-us/articles/4405850915095-Group-By-UNIX-Time) | **Y** | | |  |
| [Histogram Floating Point Values](https://devnet.logianalytics.com/hc/en-us/articles/4405850915991-Histogram-Floating-Point-Values) | **N** | | |  |
| [Histograms](https://devnet.logianalytics.com/hc/en-us/articles/4405859514775-Bars-Histograms) | **Y** | | |  |
| [Kerberos Authentication](https://devnet.logianalytics.com/hc/en-us/articles/4405859461271-Configure-Kerberos-Single-Sign-On-SSO-Settings) | **Y** | | |  |
| [Last Value](https://devnet.logianalytics.com/hc/en-us/articles/4405859174295-Last-Value) | **N** | | |  |
| [Live Mode and Playback](https://devnet.logianalytics.com/hc/en-us/articles/4405851191447-Live-Mode-and-Historical-Playback) | **Y** | | |  |
| [Multivalued Fields](https://devnet.logianalytics.com/hc/en-us/articles/4405859175319-Multivalued-Fields) | **N** | | | The Apache Solr JSON API does not support metrics by multivalued fields. |
| [Nested Fields](https://devnet.logianalytics.com/hc/en-us/articles/4405851022871-Support-of-Nested-Data-Structures-in-Composer) | **N** | | |  |
| [Partitions](https://devnet.logianalytics.com/hc/en-us/articles/4405859176343-Partitions) | N/A | | |  |
| [Pushdown Joins for Fusion Data Sources](https://devnet.logianalytics.com/hc/en-us/articles/4405859358487-Optimize-Joins) | **N** | | |  |
| [Schemas](https://devnet.logianalytics.com/hc/en-us/articles/4405859177367-Schemas) | N/A | | |  |
| [Text Search](https://devnet.logianalytics.com/hc/en-us/articles/4405859178391-Text-Search) | **Y** | | |  |
| [TLS](https://devnet.logianalytics.com/hc/en-us/articles/4405859179671-TLS) | **N** | | |  |
| [User Delegation](https://devnet.logianalytics.com/hc/en-us/articles/4405859193111-Enable-User-Delegation) | **Y** | | |  |
| [Wild Card Filters](https://devnet.logianalytics.com/hc/en-us/articles/4405851071383-Apply-Wild-Card-Filters-to-a-Visual-or-Dashboard) | **Y** | | |  |
| [Wild Card Filters, Case-Insensitive Mode](https://devnet.logianalytics.com/hc/en-us/articles/4405851071383-Apply-Wild-Card-Filters-to-a-Visual-or-Dashboard) | **N** | | | Case-sensitivity cannot be enforced. Consequently, neither case-sensitive or case-insensitive wild card filters are supported. |
| [Wild Card Filters, Case-Sensitive Mode](https://devnet.logianalytics.com/hc/en-us/articles/4405851071383-Apply-Wild-Card-Filters-to-a-Visual-or-Dashboard) | **N** | | | Case-sensitivity cannot be enforced. Consequently, neither case-sensitive or case-insensitive wild card filters are supported. |

In addition, Apache Solr supports the Request Handler field on the [Tables/Indices](https://devnet.logianalytics.com/hc/en-us/articles/4405859323287-Tables-Indices-Tab) tab of the [data source configuration](https://devnet.logianalytics.com/hc/en-us/articles/4405851027479-Manage-Data-Source-Configurations). You can use this box at the top of the Field table on the Tables/Indices tab to specify a request handler plug-in that defines the logic used when executing a search request.

For Kerberos authentication instructions, see [*Connect to Apache Solr Data Stores That Use Kerberos Authentication*](https://devnet.logianalytics.com/hc/en-us/articles/4405859207959-Connect-to-Apache-Solr-Data-Stores-That-Use-Kerberos-Authentication). For instructions on using user delegation with the Apache Solr connector, see [*Configure User Delegation for the Apache Solr Connector*](https://devnet.logianalytics.com/hc/en-us/articles/4405850934935-Configure-User-Delegation-for-the-Apache-Solr-Connector).

## Connect to Apache Solr

You can configure the Composer Apache Solr connector to connect to a kerberized Apache Solr data store. For more information, see [*Connect to Apache Solr Data Stores That Use Kerberos Authentication*](https://devnet.logianalytics.com/hc/en-us/articles/4405859207959-Connect-to-Apache-Solr-Data-Stores-That-Use-Kerberos-Authentication).

When establishing a connection to Apache Solr, you must provide the following information.

1. Select the hosting type: **Standalone** or **Cloud**.
2. Specify a Solr Base URL.
3. Specify the version of the Solr source that you are going to connect to in the following format:
   `<major>.<minor>.<patch>`. This field is optional.

   While connecting to Solr, Composer first checks its version. If the version is not available, Composer checks the version that you have specified in this field and attempts to connect that version.
4. If authentication has been set up, provide the user name and password.

## Dashboard and Visual Considerations

Distinct count and percentiles metrics return approximate values in Solr, due to the nature of the data source. The precision of the result returned by distinct count metric depends on the precision threshold setting (default value is 1000).

When you create a bar chart using an Apache Solr data source, you can search for a specific word or phrase using the search box at the top of the dashboard. The **Details** tab displays the results.

![](https://devnet.logianalytics.com/hc/article_attachments/4406747382295/noteicon.jpg) Fields of time groupings with low time granularity may cause loading time issues for the data source.
