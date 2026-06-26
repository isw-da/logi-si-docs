---
title: "Manage the Hive Connector"
id: 4405850956695
section: "Connect to Data in Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405850956695-Manage-the-Hive-Connector
updated_at: 2021-09-21T01:27:28Z
---

# Manage the Hive Connector

# Manage the Hive Connector

The Composer Hive connector lets you access the data available in Hive storage using the Composer client. It can connect to both Hive on Tez and Hive on Tez with LLAP, depending on the JDBC URL you provide (see [*Connect to Hive*](#Connecti) below). The Composer Hive connector supports Hive versions 2.1 through 3.1.

Before you can establish a connection from Composer to Hive storage, a connector server needs to be installed and configured.
See [*Manage Connectors and Connector Servers*](https://devnet.logianalytics.com/hc/en-us/articles/4405859186199-Manage-Connectors-and-Connector-Servers) for general instructions and [*Connect to Hive*](#Connecti) for details specific to the Hive connector.

After the connector has been set up, you can create data source configurations that specify the necessary connection information and identify the data you want to use. See [*Manage Data Source Configurations*](https://devnet.logianalytics.com/hc/en-us/articles/4405851027479-Manage-Data-Source-Configurations) for more information. After data sources are configured, they can be used to create dashboards and visuals from your data. See [*Create Dashboards*](https://devnet.logianalytics.com/hc/en-us/articles/4405859261207-Create-Dashboards).

## Composer Feature Support

Hive connector support for specific [Composer features](https://devnet.logianalytics.com/hc/en-us/articles/4405859170583-Connector-Feature-Support) is shown in the following table.

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
| [Kerberos Authentication](https://devnet.logianalytics.com/hc/en-us/articles/4405859461271-Configure-Kerberos-Single-Sign-On-SSO-Settings) | **Y** | |
| [Last Value](https://devnet.logianalytics.com/hc/en-us/articles/4405859174295-Last-Value) | **Y** | |
| [Live Mode and Playback](https://devnet.logianalytics.com/hc/en-us/articles/4405851191447-Live-Mode-and-Historical-Playback) | **Y** | |
| [Multivalued Fields](https://devnet.logianalytics.com/hc/en-us/articles/4405859175319-Multivalued-Fields) | N/A | |
| [Nested Fields](https://devnet.logianalytics.com/hc/en-us/articles/4405851022871-Support-of-Nested-Data-Structures-in-Composer) | N/A | |
| [Partitions](https://devnet.logianalytics.com/hc/en-us/articles/4405859176343-Partitions) | **Y** | |
| [Pushdown Joins for Fusion Data Sources](https://devnet.logianalytics.com/hc/en-us/articles/4405859358487-Optimize-Joins) | **Y** | |
| [Schemas](https://devnet.logianalytics.com/hc/en-us/articles/4405859177367-Schemas) | **Y** | |
| [Text Search](https://devnet.logianalytics.com/hc/en-us/articles/4405859178391-Text-Search) | N/A | |
| [TLS](https://devnet.logianalytics.com/hc/en-us/articles/4405859179671-TLS) | **Y** | |
| [User Delegation](https://devnet.logianalytics.com/hc/en-us/articles/4405859193111-Enable-User-Delegation) | **Y** | |
| [Wild Card Filters](https://devnet.logianalytics.com/hc/en-us/articles/4405851071383-Apply-Wild-Card-Filters-to-a-Visual-or-Dashboard) | **Y** | |
| [Wild Card Filters, Case-Insensitive Mode](https://devnet.logianalytics.com/hc/en-us/articles/4405851071383-Apply-Wild-Card-Filters-to-a-Visual-or-Dashboard) | **Y** | |
| [Wild Card Filters, Case-Sensitive Mode](https://devnet.logianalytics.com/hc/en-us/articles/4405851071383-Apply-Wild-Card-Filters-to-a-Visual-or-Dashboard) | **Y** | |

## Connect to Hive

To establish a connection to Hive, you must specify a JDBC URL on the Connection page of your Composer data source definition for the Hive connection.

* Specify the JDBC URL for Hive.
* If authentication has been set up, provide the user name and password.
* If required, specify the Hive/YARN queue name in the Queue Name box.
* Specify the server timezone. If the timezone of your Hive server is in UTC, leave the Server Timezone box blank. Otherwise, specify the timezone abbreviation in all caps for correct handling the time data (for example, EST, EDT, or CST).
* Select **Validate** to test the connection.

To connect to Hive LLAP, the JDBC URL you must specify is different. If you use Hortonworks Data Platform (HDP), you can copy the URL from Ambari. See <https://docs.cloudera.com/HDPDocuments/HDP3/HDP-3.1.4/performance-tuning/content/hive_connect_clients_to_llap.html>.

See also [*Connect to Hive Sources on A Kerberized HDP Cluster*](https://devnet.logianalytics.com/hc/en-us/articles/4405850955543-Connect-to-Hive-Sources-on-A-Kerberized-HDP-Cluster).

## Migrate Your Hive Connectors

In Zoomdata 3.7, the Hive on Tez connector was renamed Hive. If your installation used the Hive on Tez connector in releases prior to 3.7, you will have two connectors after the upgrade: Hive on Tez and Hive. The Hive on Tez connector is outdated and should not be used anymore.

To migrate your existing data source configurations and connections to use the new Hive connector:

1. Copy any configuration properties you had customized in the Hive on Tez connector's `edc-tez.properties` configuration file to the new Hive connector's `edc-hive.properties` configuration file. See [*Connector Properties and Property Files*](https://devnet.logianalytics.com/hc/en-us/articles/4405850892439-Connector-Properties-and-Property-Files).
2. Verify that the new Hive connector, with the `zoomdata-edc-hive` package name, is running and enabled. See [*Manage Connectors and Connector Servers*](https://devnet.logianalytics.com/hc/en-us/articles/4405859186199-Manage-Connectors-and-Connector-Servers).
3. Log into Composer as the supervisor.
4. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4406743720343/hamburger.png) to access the [supervisor menu](https://devnet.logianalytics.com/hc/en-us/articles/4405859441687-The-Composer-Supervisor-Menu) and then select **Connectors**. The Manage Connector Services page appears.
5. At the bottom of the Manage Connector Services page, in the Connectors table (not the Connector Servers table), locate and select the **Hive on Tez** connector. The Edit Hive on Tez Connector page appears.
6. Select the **Hive** connector from the drop-down list in the **Connector Server** field.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4406747382295/noteicon.jpg) The **User Attribute** checkboxes in the **Connector Parameters** list on the Edit Hive on Tez Connector page are cleared when you changed the **Connector Server** field. So, before you make this change, make note of which connector parameters were marked as User Attributes.
7. If any connector parameters listed on the Edit Hive on Tez Connector page had the **User Attribute** checkbox selected, select the checkbox again.
8. Select **Save**.
9. Disable the old Hive on Tez connector with the package name `zoomdata-edc-tez`. See [*Manage Connectors and Connector Servers*](https://devnet.logianalytics.com/hc/en-us/articles/4405859186199-Manage-Connectors-and-Connector-Servers).

Your existing data source configurations and connections will now work with the new Hive connector. The old Hive on Tez connector server can be deleted. See [*Manage Connectors and Connector Servers*](https://devnet.logianalytics.com/hc/en-us/articles/4405859186199-Manage-Connectors-and-Connector-Servers).

## Troubleshooting

If you run into a warning message that is displayed when you try to open a dashboard based on a Hive data source, see [*Resolve the Hive Timeout Warning Message*](https://devnet.logianalytics.com/hc/en-us/articles/4405859495191-Resolve-the-Hive-Timeout-Warning-Message).
