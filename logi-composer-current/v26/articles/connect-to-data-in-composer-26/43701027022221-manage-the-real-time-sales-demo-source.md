---
title: "Manage the Real Time Sales Demo Source"
id: 43701027022221
section: "Connect to Data in Composer 26"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701027022221-Manage-the-Real-Time-Sales-Demo-Source
updated_at: 2026-05-29T14:07:52Z
---

# Manage the Real Time Sales Demo Source

# Manage the Real Time Sales Demo Source

A demo data source called Real Time Sales (RTS) is included as part of the Composer installation package. This data generator simulates a real-time data stream; allowing users to interact with and explore Composer's capabilities without the need to connect to a data source. However, this demo source, by default, is not available in the Composer Client and must be manually activated. This topic walks you through how to enable and disable the demo source.
The current version of the RTS connector is 2.3.232.

**Note:** 
A known issue with real-time streaming sources such as this demo source exists. If such sources are left enabled for an extended period of time, 'Out of Memory' errors may occur in the Composer Server. To avoid this problem, disable such sources when not in use.

Before you can establish a connection from Composer to RTS, a data source configuration for the demo source needs to be enabled and set up.
See [Enable the Real Time Sales Demo Source](#Enabling) and [Set Up the Real Time Sales Demo Source](#Setting). To manage the availability for RTS, see [Manage Connectors and Connector Servers](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701042404749-Manage-Connectors-and-Connector-Servers).

After setting up the connector, create data sources that specify the necessary connection information and identify the data you want to use. See [Manage Data Sources](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701068934669-Manage-Data-Sources) for more information. After you set up your data sources, create [dashboards](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701076467981-Create-Dashboards) and [visuals](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701179894541-Create-and-Add-Visuals-to-the-Visual-Gallery) from from the data in these data sources. See [Create Dashboards](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701076467981-Create-Dashboards).

## Feature Support

Real Time Sales Demo support for specific  [features](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43700992759565-Connector-Feature-Support) is shown in the following table.

**Key:** **Y** - Supported; **N** - Not Supported; N/A - not applicable

| Feature | Supported? |
| --- | --- |
| [Admin-Defined Functions](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701029797901-Admin-Defined-Functions) | N/A |
| [Box Plots](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701211727885-Box-Plots) | **Y** |
| [Custom SQL Queries](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701041493645-Custom-SQL-Queries) | N/A |
| [Derived Fields (Row-Level Expressions)](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701078705933-Maintain-Derived-Fields) | N/A |
| [Distinct Counts](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701030916365-Distinct-Counts) | **Y** |
| [Fast Distinct Values](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701008284941-Fast-Distinct-Values) | N/A |
| [Group By Multiple Fields](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701054799373-Group-By-Multiple-Fields) | **Y** |
| [Group By Time](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701054819213-Group-By-Time) | **Y** |
| [Group By UNIX Time](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701041642381-Group-By-UNIX-Time) | **N** |
| [Histogram Floating Point Values](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701041703437-Histogram-Floating-Point-Values) | **Y** |
| [Histograms](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701211617293-Bars-Histograms) | **Y** |
| [Kerberos Authentication](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701208766477-Configure-Kerberos-Single-Sign-On-SSO-Settings) | N/A |
| [Last Value](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701008456845-Last-Value) | **Y** |
| [Live Mode and Playback](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701210493837-Live-Mode-and-Historical-Playback) | **Y** |
| [Multivalued Fields](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43700993039117-Multivalued-Fields) | N/A |
| [Nested Fields](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701068575501-Support-of-Nested-Data-Structures-in-Composer) | N/A |
| [Partitions](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701024301709-Partitions) | N/A |
| [Pushdown Joins for Fusion Data Sources](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701134208269-Optimize-Joins) | N/A |
| [Schemas](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701038566797-Schemas) | **Y** |
| [Text Search](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701041900045-Text-Search) | N/A |
| [TLS](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43700993160717-TLS) | N/A |
| [User Delegation](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701039382541-Enable-User-Delegation) | N/A |
| [Wildcard Filters](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701071787533-Apply-Wildcard-Filters-to-a-Visual-Filter-Snippet-or-Dashboard) | **Y** |
| [Wildcard Filters, Case-Insensitive Mode](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701038723341-Wildcard-Case-Insensitive-Filters) | **Y** |
| [Wildcard Filters, Case-Sensitive Mode](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43700993286669-Wildcard-Case-Sensitive-Filters) | **Y** |

## Enable the Real Time Sales Demo Source

To enable the Real Time Sales demo source, use an automated script that activates the demo source in the Composer client. This script, labeled `create-rts.sh`, is included as part of the installation package. However, the script needs to be run from the Linux prompt, so administrative access to your Linux server is necessary.

RTS is installed in your server as part of the
 [installation process](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701072793997-Install-Composer). However, if an
[alternative installation method](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701072353933-Alternative-Installation-Options) was used to manually install each Composer component, you should first confirm whether the RTS package was included during the installation efforts.

More specifically, running the automated RTS script will do the following (in the Composer Client):

1. Add the RTS connector server details in the Composer Client (using port 8108).
2. Define the connection type for the RTS demo source.
3. Create the connection and generate the RTS icon in the Data Source page.

## Set Up the Real Time Sales Demo Source

To set up the RTS demo source, take the following steps:

1. Log out of the Composer client and close the browser window.
2. Access the Linux prompt and log into your Composer Server (via Secure Shell or SSH).
3. From your Linux prompt, run the RTS script:

   sudo /opt/zoomdata/lib/create-rts.sh -a admin:<YourAdminPassword>
   -s supervisor:<YourSupervisorPassword>

## Enable RTS After Upgrading Composer

If you are upgrading your Composer Server to the current release version, that version's RTS demo source is deleted during the process and the current version is installed. You need to activate RTS following the same steps outlined above.

## Disable the Real Time Sales Demo Data Source

To disable the Real Time Sales demo source, do the following:

* Log in as an admin user.
* Select the
  **Connectors** tab.
* Go to the **Connectors** list in the bottom half of the Connectors page.
* Locate the **RTS** connector in the Connectors list.
* Clear the checkbox in the **Enabled** column associated with the RTS connector.
