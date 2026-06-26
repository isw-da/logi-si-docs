---
title: "Manage the Apache Solr Connector"
id: 34932743530125
section: "Connect to Data in Composer 25"
product: "Logi Composer v25"
url: https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932743530125-Manage-the-Apache-Solr-Connector
updated_at: 2026-05-26T22:06:36Z
---

# Manage the Apache Solr Connector

# Manage the Apache Solr Connector

The Composer Apache Solr connector lets you access the data available in your Apache Solr databases using the Composer client. The Composer Apache Solr connector supports Apache Solr versions 7.4 through 8.4.

Before you can establish a connection from Composer to an Apache Solr database, a connector server needs to be installed, configured and enabled.
See [Manage Connectors and Connector Servers](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932741363981-Manage-Connectors-and-Connector-Servers) for general instructions and [Connect to Apache Solr](#Connecti) for details specific to the Apache Solr connector.

After setting up the connector, create data sources that specify the necessary connection information and identify the data you want to use. See [Manage Data Sources](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932941009037-Manage-Data-Sources) for more information. After you set up your data sources, create [dashboards](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932763355021-Create-Dashboards) and [visuals](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933273224589-Create-and-Add-Visuals-to-the-Visual-Gallery) from from the data in these data sources. See [Create Dashboards](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932763355021-Create-Dashboards).

## Feature Support

Connector support for specific  [features](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932704861453-Connector-Feature-Support) is shown in the following table.

**Key:** **Y** - Supported; **N** - Not Supported; N/A - not applicable

| Feature | Supported? | | | Notes |
| --- | --- | --- | --- | --- |
| [Admin-Defined Functions](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932796673933-Admin-Defined-Functions) | **N** | | |  |
| [Box Plots](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933208692493-Box-Plots) | **Y** | | |  |
| [Custom SQL Queries](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932704947213-Custom-SQL-Queries) | **N** | | | If you need to access a BigQuery partition, explicitly include an alias for the built in partition column in your select clause, such as `select *, _PARTITIONTIME as pt from projectId.datasetId.tableId`. |
| [Derived Fields (Row-Level Expressions)](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932839148813-Maintain-Derived-Fields) | **N** | | |  |
| [Distinct Counts](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932867905037-Distinct-Counts) | **Y** | | |  |
| [Fast Distinct Values](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932715069197-Fast-Distinct-Values) | **Y** | | |  |
| [Group By Multiple Fields](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932715164173-Group-By-Multiple-Fields) | **Y** | | |  |
| [Group By Time](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932690999309-Group-By-Time) | **Y** | | |  |
| [Group By UNIX Time](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932730700429-Group-By-UNIX-Time) | **Y** | | |  |
| [Histogram Floating Point Values](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932708132109-Histogram-Floating-Point-Values) | **N** | | |  |
| [Histograms](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933212496141-Bars-Histograms) | **Y** | | |  |
| [Kerberos Authentication](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933139627149-Configure-Kerberos-Single-Sign-On-SSO-Settings) | **Y** | | |  |
| [Last Value](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932730888205-Last-Value) | **N** | | |  |
| [Live Mode and Playback](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933163012621-Live-Mode-and-Historical-Playback) | **Y** | | |  |
| [Multivalued Fields](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932715662093-Multivalued-Fields) | **N** | | | The Apache Solr JSON API does not support metrics by multivalued fields. |
| [Nested Fields](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932861225357-Support-of-Nested-Data-Structures-in-Composer) | **N** | | |  |
| [Partitions](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932715778445-Partitions) | N/A | | |  |
| [Pushdown Joins for Fusion Data Sources](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932963077133-Optimize-Joins) | **N** | | |  |
| [Schemas](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932691729805-Schemas) | N/A | | |  |
| [Text Search](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932739827853-Text-Search) | **Y** | | | You can sort keyword searches by Best Match and Most Recent (when you select a preferred time field from the source). Filter your search results by selecting fields in the Filter modal. Select **Clear All** to clear filtered search results. |
| [TLS](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932692004749-TLS) | **N** | | |  |
| [User Delegation](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932742695053-Enable-User-Delegation) | **Y** | | |  |
| [Wildcard Filters](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932977272717-Apply-Wildcard-Filters-to-a-Visual-Filter-Snippet-or-Dashboard) | **Y** | | |  |
| [Wildcard Filters, Case-Insensitive Mode](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932723779981-Wildcard-Case-Insensitive-Filters) | **N** | | | Case-sensitivity cannot be enforced. Consequently, neither case-sensitive or case-insensitive wildcard filters are supported. |
| [Wildcard Filters, Case-Sensitive Mode](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932692417677-Wildcard-Case-Sensitive-Filters) | **N** | | | Case-sensitivity cannot be enforced. Consequently, neither case-sensitive or case-insensitive wildcard filters are supported. |

In addition, Apache Solr supports the Request Handler field on the Tables/Indices tab of the [data source configuration](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932941009037-Manage-Data-Sources). You can use this box at the top of the Field table on the Tables/Indices tab to specify a request handler plug-in that defines the logic used when executing a search request.

For Kerberos authentication instructions, see [Connect to Apache Solr Data Stores That Use Kerberos Authentication](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932695429773-Connect-to-Apache-Solr-Data-Stores-That-Use-Kerberos-Authentication). For instructions on using user delegation with the Apache Solr connector, see [Configure User Delegation for the Apache Solr Connector](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932719394061-Configure-User-Delegation-for-the-Apache-Solr-Connector).

## Connect to Apache Solr

You can configure the Composer Apache Solr connector to connect to a kerberized Apache Solr data store. For more information, see [Connect to Apache Solr Data Stores That Use Kerberos Authentication](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932695429773-Connect-to-Apache-Solr-Data-Stores-That-Use-Kerberos-Authentication).

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

**Note:** 
Fields of time groupings with low time granularity may cause loading time issues for the data source.
