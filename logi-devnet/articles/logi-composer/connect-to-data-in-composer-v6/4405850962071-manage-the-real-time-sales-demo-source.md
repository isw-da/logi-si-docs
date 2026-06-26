---
title: "Manage the Real Time Sales Demo Source"
id: 4405850962071
section: "Connect to Data in Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405850962071-Manage-the-Real-Time-Sales-Demo-Source
updated_at: 2021-09-21T01:27:31Z
---

# Manage the Real Time Sales Demo Source

# Manage the Real Time Sales Demo Source

A demo data source called Real Time Sales (RTS) is included as part of the Composer installation package. This data generator simulates a real-time data stream; allowing users to interact with and explore Composer's capabilities without the need to connect to a data source. However, this demo source, by default, is not available in the Composer Client and must be manually activated. This topic walks you through how to enable and disable the demo source.

![](https://devnet.logianalytics.com/hc/article_attachments/4406747382295/noteicon.jpg) A known issue with real-time streaming sources such as this demo source exists. If such sources are left enabled for an extended period of time, 'Out of Memory' errors may occur in the Composer Server. To avoid this problem, disable such sources when not in use.

Before you can establish a connection from Composer to RTS, a data source configuration for the demo source needs to be enabled and set up.
See [*Enable the Real Time Sales Demo Source*](#Enabling) and [*Set Up the Real Time Sales Demo Source*](#Setting). To manage the availability for RTS, see [*Manage Connectors and Connector Servers*](https://devnet.logianalytics.com/hc/en-us/articles/4405859186199-Manage-Connectors-and-Connector-Servers).

After the connector has been set up, you can create data source configurations that specify the necessary connection information and identify the data you want to use. See [*Manage Data Source Configurations*](https://devnet.logianalytics.com/hc/en-us/articles/4405851027479-Manage-Data-Source-Configurations) for more information. After data sources are configured, they can be used to create dashboards and visuals from your data. See [*Create Dashboards*](https://devnet.logianalytics.com/hc/en-us/articles/4405859261207-Create-Dashboards).

## Composer Feature Support

Real Time Sales Demo support for specific [Composer features](https://devnet.logianalytics.com/hc/en-us/articles/4405859170583-Connector-Feature-Support) is shown in the following table.

**Key:** **Y** - Supported; **N** - Not Supported; N/A - not applicable

| Feature | Supported? | |
| --- | --- | --- |
| [Admin-Defined Functions](https://devnet.logianalytics.com/hc/en-us/articles/4405850995991-Admin-Defined-Functions) | N/A | |
| [Box Plots](https://devnet.logianalytics.com/hc/en-us/articles/4405859517207-Box-Plots) | **Y** | |
| [Custom SQL Queries](https://devnet.logianalytics.com/hc/en-us/articles/4405859171735-Custom-SQL-Queries) | **N** | |
| [Derived Fields (Row-Level Expressions)](https://devnet.logianalytics.com/hc/en-us/articles/4405859299479-Maintain-Derived-Fields) | N/A | |
| [Distinct Counts](https://devnet.logianalytics.com/hc/en-us/articles/4405859300503-Enable-Distinct-Counts) | **Y** | |
| [Fast Distinct Values](https://devnet.logianalytics.com/hc/en-us/articles/4405850912279-Fast-Distinct-Values) | N/A | |
| [Group By Multiple Fields](https://devnet.logianalytics.com/hc/en-us/articles/4405850913303-Group-By-Multiple-Fields) | **Y** | |
| [Group By Time](https://devnet.logianalytics.com/hc/en-us/articles/4405850914199-Group-By-Time) | **Y** | |
| [Group By UNIX Time](https://devnet.logianalytics.com/hc/en-us/articles/4405850915095-Group-By-UNIX-Time) | **N** | |
| [Histogram Floating Point Values](https://devnet.logianalytics.com/hc/en-us/articles/4405850915991-Histogram-Floating-Point-Values) | **Y** | |
| [Histograms](https://devnet.logianalytics.com/hc/en-us/articles/4405859514775-Bars-Histograms) | **Y** | |
| [Kerberos Authentication](https://devnet.logianalytics.com/hc/en-us/articles/4405859461271-Configure-Kerberos-Single-Sign-On-SSO-Settings) | N/A | |
| [Last Value](https://devnet.logianalytics.com/hc/en-us/articles/4405859174295-Last-Value) | **Y** | |
| [Live Mode and Playback](https://devnet.logianalytics.com/hc/en-us/articles/4405851191447-Live-Mode-and-Historical-Playback) | **Y** | |
| [Multivalued Fields](https://devnet.logianalytics.com/hc/en-us/articles/4405859175319-Multivalued-Fields) | N/A | |
| [Nested Fields](https://devnet.logianalytics.com/hc/en-us/articles/4405851022871-Support-of-Nested-Data-Structures-in-Composer) | N/A | |
| [Partitions](https://devnet.logianalytics.com/hc/en-us/articles/4405859176343-Partitions) | N/A | |
| [Pushdown Joins for Fusion Data Sources](https://devnet.logianalytics.com/hc/en-us/articles/4405859358487-Optimize-Joins) | N/A | |
| [Schemas](https://devnet.logianalytics.com/hc/en-us/articles/4405859177367-Schemas) | **Y** | |
| [Text Search](https://devnet.logianalytics.com/hc/en-us/articles/4405859178391-Text-Search) | N/A | |
| [TLS](https://devnet.logianalytics.com/hc/en-us/articles/4405859179671-TLS) | N/A | |
| [User Delegation](https://devnet.logianalytics.com/hc/en-us/articles/4405859193111-Enable-User-Delegation) | N/A | |
| [Wild Card Filters](https://devnet.logianalytics.com/hc/en-us/articles/4405851071383-Apply-Wild-Card-Filters-to-a-Visual-or-Dashboard) | **Y** | |
| [Wild Card Filters, Case-Insensitive Mode](https://devnet.logianalytics.com/hc/en-us/articles/4405851071383-Apply-Wild-Card-Filters-to-a-Visual-or-Dashboard) | **Y** | |
| [Wild Card Filters, Case-Sensitive Mode](https://devnet.logianalytics.com/hc/en-us/articles/4405851071383-Apply-Wild-Card-Filters-to-a-Visual-or-Dashboard) | **Y** | |

## Enable the Real Time Sales Demo Source

To enable the Real Time Sales demo source, use an automated script that activates the demo source in the Composer client. This script, labeled `create-rts.sh`, is included as part of the installation package. However, the script needs to be run from the Linux prompt, so administrative access to your Linux server is necessary.

RTS is installed in your server as part of the
[Composer installation process](https://devnet.logianalytics.com/hc/en-us/articles/4405859373719-Install-Composer). However, if an
[alternative installation method](https://devnet.logianalytics.com/hc/en-us/articles/4405851076887-Alternative-Installation-Options) was used to manually install each Composer component, you should first confirm whether the RTS package was included during the installation efforts.

More specifically, running the automated RTS script will do the following (in the Composer Client):

1. Add the RTS connector server details in the Composer Client (using port 8108).
2. Define the connection type for the RTS demo source.
3. Create the connection and generate the RTS icon in the Data Source page.

## Set Up the Real Time Sales Demo Source

To set up the RTS demo source, take the following steps:

1. Log out of the Composer client and close the browser window.
2. Access the Linux prompt and log into your Composer Server (via Secure Shell or SSH).
3. From your Linux prompt, run the RTS script:

   ```
   sudo /opt/zoomdata/lib/create-rts.sh -a admin:<YourAdminPassword> 
   -s supervisor:<YourSupervisorPassword>
   ```

## Enable RTS After Upgrading Composer

If you are upgrading your Composer Server to the current release version, that version's RTS demo source is deleted during the process and the current version is installed. You need to activate RTS following the same steps outlined above.

## Disable the Real Time Sales Demo Data Source

To disable the Real Time Sales demo source, do the following:

* Log in as the supervisor.
* Select the
  **Connectors** tab.
* Go to the **Connectors** list in the bottom half of the Connectors page.
* Locate the **RTS** connector in the Connectors list.
* Clear the checkbox in the **Enabled** column associated with the RTS connector.
