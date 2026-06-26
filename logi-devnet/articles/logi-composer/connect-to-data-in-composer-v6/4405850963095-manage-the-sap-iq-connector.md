---
title: "Manage the SAP IQ Connector"
id: 4405850963095
section: "Connect to Data in Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405850963095-Manage-the-SAP-IQ-Connector
updated_at: 2021-09-21T01:27:29Z
---

# Manage the SAP IQ Connector

# Manage the SAP IQ Connector

The Composer SAP IQ connector allows you to access the data stored within your [SAP IQ](https://help.sap.com/viewer/a898e08b84f21015969fa437e89860c8/16.1.3.0/en-US/7b5bd4e8cdcb4593aba6f2895572b0a9.html) database using the Composer client. The Composer connector supports SAP IQ version 16.

Before you can establish a connection from Composer to SAP IQ, a connector server needs to be installed, configured and enabled.
See [*Manage Connectors and Connector Servers*](https://devnet.logianalytics.com/hc/en-us/articles/4405859186199-Manage-Connectors-and-Connector-Servers) for general instructions and [*Connect to SAP IQ*](#Connecti) for details specific to the SAP IQ connector. If you elect to use Kerberos authentication, see [*Configure Kerberos Support for the SAP IQ Connector*](#Configur).

After the connector has been set up, you can create data source configurations that specify the necessary connection information and identify the data you want to use. See [*Manage Data Source Configurations*](https://devnet.logianalytics.com/hc/en-us/articles/4405851027479-Manage-Data-Source-Configurations) for more information. After data sources are configured, they can be used to create dashboards and visuals from your data. See [*Create Dashboards*](https://devnet.logianalytics.com/hc/en-us/articles/4405859261207-Create-Dashboards).

## Composer Feature Support

SAP IQ connector support for specific [Composer features](https://devnet.logianalytics.com/hc/en-us/articles/4405859170583-Connector-Feature-Support) is shown in the following table.

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
| [Partitions](https://devnet.logianalytics.com/hc/en-us/articles/4405859176343-Partitions) | **N** | |
| [Pushdown Joins for Fusion Data Sources](https://devnet.logianalytics.com/hc/en-us/articles/4405859358487-Optimize-Joins) | **N** | |
| [Schemas](https://devnet.logianalytics.com/hc/en-us/articles/4405859177367-Schemas) | **Y** | |
| [Text Search](https://devnet.logianalytics.com/hc/en-us/articles/4405859178391-Text-Search) | N/A | |
| [TLS](https://devnet.logianalytics.com/hc/en-us/articles/4405859179671-TLS) | **Y** | |
| [User Delegation](https://devnet.logianalytics.com/hc/en-us/articles/4405859193111-Enable-User-Delegation) | **N** | |
| [Wild Card Filters](https://devnet.logianalytics.com/hc/en-us/articles/4405851071383-Apply-Wild-Card-Filters-to-a-Visual-or-Dashboard) | **Y** | |
| [Wild Card Filters, Case-Insensitive Mode](https://devnet.logianalytics.com/hc/en-us/articles/4405851071383-Apply-Wild-Card-Filters-to-a-Visual-or-Dashboard) | **Y** | |
| [Wild Card Filters, Case-Sensitive Mode](https://devnet.logianalytics.com/hc/en-us/articles/4405851071383-Apply-Wild-Card-Filters-to-a-Visual-or-Dashboard) | **Y** | |

## Connect to SAP IQ

Make sure that the `jConnect` system objects were installed on your Sap IQ database instance (see <https://help.sap.com/viewer/a894a54d84f21015b142ffe773888f8c/16.1.3.0/en-US/3bd561266c5f10149e06d363dbe03486.html>).

The SAP IQ connector requires a JDBC driver to be configured before your data source configurations can use it. You can download the driver from the vendor's site. For information and steps, see [*Add a JDBC Driver*](https://devnet.logianalytics.com/hc/en-us/articles/4405859376919-Add-a-JDBC-Driver).

When setting up a connection to SAP IQ , you need to provide the following:

* The name of the connection
* The JDBC URL. The format for the JDBC URL must be as follows: `jdbc:sybase:Tds:<ipaddr>:<port>`. For example, `jdbc:sybase:Tds:10.1.2.3:2638/.`
* The username and password, if applicable.
* Optionally, the microservice principal name.
* Optionally, select **Request Kerberos Session** if Kerberos connection authentication will be used. See [*Configure Kerberos Support for the SAP IQ Connector*](#Configur) for more information.

## Configure Kerberos Support for the SAP IQ Connector

To configure Kerberos support for the connector:

1. Create or update the file named `/etc/zoomdata/edc-sapiq.properties`. If this file already exists, verify that the information below exists in the file:

   ```
   kerberos.krb5.conf.location=/etc/krb5.conf
     
   kerberos.service.account.authentication=true
     
   kerberos.service.account.principal=<yourcompany_principal>@KERBEROS.REALM
   kerberos.service.account.keytab.location=/etc/zoomdata/<yourcompany_principal>.keytab				
   ```
2. Restart the SAP IQ connector.
3. To connect to SAP IQ, use the following JDBC URL template:

   ```
   jdbc:sybase:Tds:host:port/?REQUEST_KERBEROS_SESSION=true&SERVICE_PRINCIPAL_NAME=sap_iq_database@PRINCIPAL.NAME
   ```
