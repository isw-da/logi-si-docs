---
title: "Manage the Amazon Redshift Connector"
id: 4405859198103
section: "Connect to Data in Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405859198103-Manage-the-Amazon-Redshift-Connector
updated_at: 2021-09-21T01:27:14Z
---

# Manage the Amazon Redshift Connector

# Manage the Amazon Redshift Connector

The Composer Amazon Redshift connector lets you access the data available in Amazon Redshift storage using the Composer client. The Composer Amazon Redshift connector supports Amazon Redshift version 1.0.

Before you can establish a connection from Composer to Amazon Redshift storage, a connector server needs to be installed and configured.
See [*Manage Connectors and Connector Servers*](https://devnet.logianalytics.com/hc/en-us/articles/4405859186199-Manage-Connectors-and-Connector-Servers) for general instructions and [*Connect to Amazon Redshift*](#Conn) for details specific to the Amazon Redshift connector.

After the connector has been set up, you can create data source configurations that specify the necessary connection information and identify the data you want to use. See [*Manage Data Source Configurations*](https://devnet.logianalytics.com/hc/en-us/articles/4405851027479-Manage-Data-Source-Configurations) for more information. After data sources are configured, they can be used to create dashboards and visuals from your data. See [*Create Dashboards*](https://devnet.logianalytics.com/hc/en-us/articles/4405859261207-Create-Dashboards).

## Composer Feature Support

Amazon Redshift connector support for specific [Composer features](https://devnet.logianalytics.com/hc/en-us/articles/4405859170583-Connector-Feature-Support) is shown in the following table.

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
| [Partitions](https://devnet.logianalytics.com/hc/en-us/articles/4405859176343-Partitions) | N/A | |
| [Pushdown Joins for Fusion Data Sources](https://devnet.logianalytics.com/hc/en-us/articles/4405859358487-Optimize-Joins) | **Y** | |
| [Schemas](https://devnet.logianalytics.com/hc/en-us/articles/4405859177367-Schemas) | **Y** | |
| [Text Search](https://devnet.logianalytics.com/hc/en-us/articles/4405859178391-Text-Search) | N/A | |
| [TLS](https://devnet.logianalytics.com/hc/en-us/articles/4405859179671-TLS) | **Y** | |
| [User Delegation](https://devnet.logianalytics.com/hc/en-us/articles/4405859193111-Enable-User-Delegation) | **N** | |
| [Wild Card Filters](https://devnet.logianalytics.com/hc/en-us/articles/4405851071383-Apply-Wild-Card-Filters-to-a-Visual-or-Dashboard) | **Y** | |
| [Wild Card Filters, Case-Insensitive Mode](https://devnet.logianalytics.com/hc/en-us/articles/4405851071383-Apply-Wild-Card-Filters-to-a-Visual-or-Dashboard) | **Y** | |
| [Wild Card Filters, Case-Sensitive Mode](https://devnet.logianalytics.com/hc/en-us/articles/4405851071383-Apply-Wild-Card-Filters-to-a-Visual-or-Dashboard) | **Y** | |

![](https://devnet.logianalytics.com/hc/article_attachments/4406747382295/noteicon.jpg) Amazon
Redshift returns whole numbers for aggregates on columns of type DECIMAL and NUMERIC types which have a 0 scale (in other words, 0 decimal places).

## Connect to Amazon Redshift

### Verify the MTU Size of Composer

Before you can establish a connection between Amazon Redshift and Composer, you must verify that the size of the maximum transmission unit (MTU) on your Composer server is set to 1500.

The MTU size determines the maximum size, in bytes, of a packet that can be transferred in one Ethernet frame over your network connection. If your MTU size is too large for the connection, you might experience incomplete query results, your query might hang, or the connection might be dropped altogether. For more information, see this AWS documentation link: <https://docs.aws.amazon.com/redshift/latest/mgmt/connecting-drop-issues.html>.

To review the MTU value, use the `ip` command:

```
$ ip addr show eth0
```

If you need to edit the MTU value and set the size to 1500, use the following `ip` command:

```
$ ip link set dev eth0 mtu 1500
```

### Configure and Reference the JDBC Driver

The Amazon Redshift connector requires a JDBC driver to be configured before you connect. You can download the driver from the vendor's site. If you are upgrading, keep in mind you need to configure the JDBC driver- see [*Upgrade Composer*](https://devnet.logianalytics.com/hc/en-us/articles/4405859509271-Upgrade-Composer). For more information, see [*Add a JDBC Driver*](https://devnet.logianalytics.com/hc/en-us/articles/4405859376919-Add-a-JDBC-Driver). The JDBC Driver for Redshift has more than one jar file that needs to be downloaded: be sure to place the files in the same location to avoid any issues.

When setting up your Amazon Redshift connection, you need to specify the JDBC URL. You can find the URL on the
**Configuration** tab of a cluster under
**Cluster Database Properties**. The format varies slightly based on the type of database being connected. For Amazon Redshift, use the following format:
`jdbc:redshift://HOSTNAME:PORT/DATABASE_NAME`. If authentication has been set up, provide the user name and password
