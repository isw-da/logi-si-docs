---
title: "Manage the Apache Phoenix Connector"
id: 4405859202839
section: "Connect to Data in Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405859202839-Manage-the-Apache-Phoenix-Connector
updated_at: 2021-09-21T01:27:14Z
---

# Manage the Apache Phoenix Connector

# Manage the Apache Phoenix Connector

The Composer Apache Phoenix connector lets you access the data available in your Apache Phoenix storage using the Composer client. The Composer Apache Phoenix connector supports Apache Phoenix version 4.7 and Apache Phoenix Query Server 4.7. Apache Phoenix v4.5 requires a separate download. To obtain a connector for Apache Phoenix 4.4, contact [Technical Support](https://devnet.logianalytics.com/hc/en-us/articles/4405859363351-Contact-Technical-Support).

Before you can establish a connection from Composer to Apache Phoenix, a Composer connector server for it needs to be installed, configured and enabled.
See [*Manage Connectors and Connector Servers*](https://devnet.logianalytics.com/hc/en-us/articles/4405859186199-Manage-Connectors-and-Connector-Servers) for general instructions and [*Connect to Apache Phoenix*](#Connecti) for details specific to the Apache Phoenix and Apache Phoenix Query Server connectors.

After the connector has been set up, you can create data source configurations that specify the necessary connection information and identify the data you want to use. See [*Manage Data Source Configurations*](https://devnet.logianalytics.com/hc/en-us/articles/4405851027479-Manage-Data-Source-Configurations) for more information. After data sources are configured, they can be used to create dashboards and visuals from your data. See [*Create Dashboards*](https://devnet.logianalytics.com/hc/en-us/articles/4405859261207-Create-Dashboards).

## Composer Feature Support

Apache Phoenix and Apache Phoenix Query Server connector support for specific [Composer features](https://devnet.logianalytics.com/hc/en-us/articles/4405859170583-Connector-Feature-Support) is shown in the following table.

**Key:** **Y** - Supported; **N** - Not Supported; N/A - not applicable

| Feature | Supported? | | | Notes |
| --- | --- | --- | --- | --- |
| [Admin-Defined Functions](https://devnet.logianalytics.com/hc/en-us/articles/4405850995991-Admin-Defined-Functions) | **Y** | | |  |
| [Box Plots](https://devnet.logianalytics.com/hc/en-us/articles/4405859517207-Box-Plots) | **N** | | |  |
| [Custom SQL Queries](https://devnet.logianalytics.com/hc/en-us/articles/4405859171735-Custom-SQL-Queries) | **Y** | | |  |
| [Derived Fields (Row-Level Expressions)](https://devnet.logianalytics.com/hc/en-us/articles/4405859299479-Maintain-Derived-Fields) | **Y** | | | Apache Phoenix and Apache Phoenix Query Server connectors support row-level expressions (derived fields) with the following limitations:   * The filter IS NULL does not work properly on grouped fields. * The LOCATE [text row-level function](https://devnet.logianalytics.com/hc/en-us/articles/4405851020183-Text-Functions) only supports a constant as a argument. * A COALESCE [conditional row-level function](https://devnet.logianalytics.com/hc/en-us/articles/4405851017239-Conditional-Functions) specified with and empty argument does not work properly. * If the CASE [conditional row-level function](https://devnet.logianalytics.com/hc/en-us/articles/4405851017239-Conditional-Functions) returns a null value as a an argument of another function, a NullPointerException may occur. * The LPAD and RPAD [text row-level functions](https://devnet.logianalytics.com/hc/en-us/articles/4405851020183-Text-Functions) are not supported. |
| [Distinct Counts](https://devnet.logianalytics.com/hc/en-us/articles/4405859300503-Enable-Distinct-Counts) | **Y** | | |  |
| [Fast Distinct Values](https://devnet.logianalytics.com/hc/en-us/articles/4405850912279-Fast-Distinct-Values) | N/A | | |  |
| [Group By Multiple Fields](https://devnet.logianalytics.com/hc/en-us/articles/4405850913303-Group-By-Multiple-Fields) | **Y** | | |  |
| [Group By Time](https://devnet.logianalytics.com/hc/en-us/articles/4405850914199-Group-By-Time) | **Y** | | |  |
| [Group By UNIX Time](https://devnet.logianalytics.com/hc/en-us/articles/4405850915095-Group-By-UNIX-Time) | **Y** | | |  |
| [Histogram Floating Point Values](https://devnet.logianalytics.com/hc/en-us/articles/4405850915991-Histogram-Floating-Point-Values) | **Y** | | |  |
| [Histograms](https://devnet.logianalytics.com/hc/en-us/articles/4405859514775-Bars-Histograms) | **Y** | | |  |
| [Kerberos Authentication](https://devnet.logianalytics.com/hc/en-us/articles/4405859461271-Configure-Kerberos-Single-Sign-On-SSO-Settings) | **Y****N** | | | Apache Phoenix supports Kerberos, but Apache Phoenix Query Server does not. For more information, see [*Enable Kerberos Authentication for Apache Phoenix Connectors*](https://devnet.logianalytics.com/hc/en-us/articles/4405850933527-Enable-Kerberos-Authentication-for-Apache-Phoenix-Connectors). |
| [Last Value](https://devnet.logianalytics.com/hc/en-us/articles/4405859174295-Last-Value) | **N** | | |  |
| [Live Mode and Playback](https://devnet.logianalytics.com/hc/en-us/articles/4405851191447-Live-Mode-and-Historical-Playback) | **Y** | | |  |
| [Multivalued Fields](https://devnet.logianalytics.com/hc/en-us/articles/4405859175319-Multivalued-Fields) | N/A | | |  |
| [Nested Fields](https://devnet.logianalytics.com/hc/en-us/articles/4405851022871-Support-of-Nested-Data-Structures-in-Composer) | N/A | | |  |
| [Partitions](https://devnet.logianalytics.com/hc/en-us/articles/4405859176343-Partitions) | N/A | | |  |
| [Pushdown Joins for Fusion Data Sources](https://devnet.logianalytics.com/hc/en-us/articles/4405859358487-Optimize-Joins) | **N** | | |  |
| [Schemas](https://devnet.logianalytics.com/hc/en-us/articles/4405859177367-Schemas) | **Y** | | |  |
| [Text Search](https://devnet.logianalytics.com/hc/en-us/articles/4405859178391-Text-Search) | N/A | | |  |
| [TLS](https://devnet.logianalytics.com/hc/en-us/articles/4405859179671-TLS) | **Y** | | |  |
| [User Delegation](https://devnet.logianalytics.com/hc/en-us/articles/4405859193111-Enable-User-Delegation) | **N** | | |  |
| [Wild Card Filters](https://devnet.logianalytics.com/hc/en-us/articles/4405851071383-Apply-Wild-Card-Filters-to-a-Visual-or-Dashboard) | **Y** | | |  |
| [Wild Card Filters, Case-Insensitive Mode](https://devnet.logianalytics.com/hc/en-us/articles/4405851071383-Apply-Wild-Card-Filters-to-a-Visual-or-Dashboard) | **Y** | | |  |
| [Wild Card Filters, Case-Sensitive Mode](https://devnet.logianalytics.com/hc/en-us/articles/4405851071383-Apply-Wild-Card-Filters-to-a-Visual-or-Dashboard) | **Y** | | |  |

## Connect to Apache Phoenix

For Apache Phoenix, specify the JDBC URL in the following format:

```
jdbc:phoenix:<zk_quorum>:<zk_port>:<zk_hbase_path>
```

where:

* `<zk_quorum>` is a comma separated list of the ZooKeeper servers
* `<zk_port>` is the ZooKeeper port
* `<zk_hbase_path>` is the path used by HBase to stop information about the instance

For Apache Phoenix Query Server, specify the JDBC URL in the following format:

```
jdbc:phoenix:thin:url=<scheme>://<server-hostname>:<port>
```

where:

* `<scheme>` is a transport protocol for communication with the server
* `<server-hostname>` is the name of the host offering the microservice
* `<port>` is the port number on which the host is listening
