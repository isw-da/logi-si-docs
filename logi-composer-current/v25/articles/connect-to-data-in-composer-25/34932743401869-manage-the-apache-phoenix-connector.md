---
title: "Manage the Apache Phoenix Connector"
id: 34932743401869
section: "Connect to Data in Composer 25"
product: "Logi Composer v25"
url: https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932743401869-Manage-the-Apache-Phoenix-Connector
updated_at: 2026-05-26T22:06:33Z
---

# Manage the Apache Phoenix Connector

# Manage the Apache Phoenix Connector

The Composer Apache Phoenix connector lets you access the data available in your Apache Phoenix storage using the Composer client. The Composer Apache Phoenix connector supports Apache Phoenix version 4.7 and Apache Phoenix Query Server 4.7. Apache Phoenix v4.5 requires a separate download. To obtain a connector for Apache Phoenix 4.4, contact [Technical Support](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932980712461-Contact-Technical-Support).

Before you can establish a connection from Composer to Apache Phoenix, a Composer connector server for it needs to be installed, configured and enabled.
See [Manage Connectors and Connector Servers](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932741363981-Manage-Connectors-and-Connector-Servers) for general instructions and [Connect to Apache Phoenix](#Connecti) for details specific to the Apache Phoenix and Apache Phoenix Query Server connectors.

After setting up the connector, create data sources that specify the necessary connection information and identify the data you want to use. See [Manage Data Sources](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932941009037-Manage-Data-Sources) for more information. After you set up your data sources, create [dashboards](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932763355021-Create-Dashboards) and [visuals](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933273224589-Create-and-Add-Visuals-to-the-Visual-Gallery) from from the data in these data sources. See [Create Dashboards](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932763355021-Create-Dashboards).

## Feature Support

Connector support for specific  [features](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932704861453-Connector-Feature-Support) is shown in the following table.

**Key:** **Y** - Supported; **N** - Not Supported; N/A - not applicable

| Feature | Supported? | | | Notes |
| --- | --- | --- | --- | --- |
| [Admin-Defined Functions](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932796673933-Admin-Defined-Functions) | **Y** | | |  |
| [Box Plots](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933208692493-Box-Plots) | **N** | | |  |
| [Custom SQL Queries](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932704947213-Custom-SQL-Queries) | **Y** | | | If you need to access a BigQuery partition, explicitly include an alias for the built in partition column in your select clause, such as `select *, _PARTITIONTIME as pt from projectId.datasetId.tableId`. |
| [Derived Fields (Row-Level Expressions)](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932839148813-Maintain-Derived-Fields) | **Y** | | | Apache Phoenix and Apache Phoenix Query Server connectors support row-level expressions (derived fields) with the following limitations:   * The filter IS NULL does not work properly on grouped fields. * The LOCATE [text row-level function](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932874867597-Text-Functions) only supports a constant as a argument. * A COALESCE [conditional row-level function](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932874388621-Conditional-Functions) specified with and empty argument does not work properly. * If the CASE [conditional row-level function](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932874388621-Conditional-Functions) returns a null value as a an argument of another function, a NullPointerException may occur. * The LPAD and RPAD [text row-level functions](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932874867597-Text-Functions) are not supported. |
| [Distinct Counts](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932867905037-Distinct-Counts) | **Y** | | |  |
| [Fast Distinct Values](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932715069197-Fast-Distinct-Values) | N/A | | |  |
| [Group By Multiple Fields](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932715164173-Group-By-Multiple-Fields) | **Y** | | |  |
| [Group By Time](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932690999309-Group-By-Time) | **Y** | | |  |
| [Group By UNIX Time](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932730700429-Group-By-UNIX-Time) | **Y** | | |  |
| [Histogram Floating Point Values](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932708132109-Histogram-Floating-Point-Values) | **Y** | | |  |
| [Histograms](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933212496141-Bars-Histograms) | **Y** | | |  |
| [Kerberos Authentication](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933139627149-Configure-Kerberos-Single-Sign-On-SSO-Settings) | **Y** / **N** | | | Apache Phoenix supports Kerberos, but Apache Phoenix Query Server does not. For more information, see [Enable Kerberos Authentication for Apache Phoenix Connectors](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932719212429-Enable-Kerberos-Authentication-for-Apache-Phoenix-Connectors). |
| [Last Value](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932730888205-Last-Value) | **N** | | |  |
| [Live Mode and Playback](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933163012621-Live-Mode-and-Historical-Playback) | **Y** | | |  |
| [Multivalued Fields](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932715662093-Multivalued-Fields) | N/A | | |  |
| [Nested Fields](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932861225357-Support-of-Nested-Data-Structures-in-Composer) | N/A | | |  |
| [Partitions](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932715778445-Partitions) | N/A | | |  |
| [Pushdown Joins for Fusion Data Sources](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932963077133-Optimize-Joins) | **N** | | |  |
| [Schemas](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932691729805-Schemas) | **Y** | | |  |
| [Text Search](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932739827853-Text-Search) | N/A | | |  |
| [TLS](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932692004749-TLS) | **Y** | | |  |
| [User Delegation](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932742695053-Enable-User-Delegation) | **N** | | |  |
| [Wildcard Filters](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932977272717-Apply-Wildcard-Filters-to-a-Visual-Filter-Snippet-or-Dashboard) | **Y** | | |  |
| [Wildcard Filters, Case-Insensitive Mode](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932723779981-Wildcard-Case-Insensitive-Filters) | **Y** | | |  |
| [Wildcard Filters, Case-Sensitive Mode](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932692417677-Wildcard-Case-Sensitive-Filters) | **Y** | | |  |

## Connect to Apache Phoenix

For Apache Phoenix, specify the JDBC URL in the following format:

jdbc:phoenix:<zk\_quorum>:<zk\_port>:<zk\_hbase\_path>

where:

* `<zk_quorum>` is a comma separated list of the ZooKeeper servers
* `<zk_port>` is the ZooKeeper port
* `<zk_hbase_path>` is the path used by HBase to stop information about the instance

For Apache Phoenix Query Server, specify the JDBC URL in the following format:

jdbc:phoenix:thin:url=<scheme>://<server-hostname>:<port>

where:

* `<scheme>` is a transport protocol for communication with the server
* `<server-hostname>` is the name of the host offering the microservice
* `<port>` is the port number on which the host is listening
