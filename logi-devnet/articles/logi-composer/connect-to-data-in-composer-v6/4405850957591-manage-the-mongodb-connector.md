---
title: "Manage the MongoDB Connector"
id: 4405850957591
section: "Connect to Data in Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405850957591-Manage-the-MongoDB-Connector
updated_at: 2022-08-26T20:16:19Z
---

# Manage the MongoDB Connector

# Manage the MongoDB Connector

The Composer MongoDB connector lets you access the data available in MongoDB storage using the Composer client. The Composer MongoDB connector supports MongoDB versions 3.4 - 4.4.

The MongoDB connector supports MongoDB views.

Before you can establish a connection from Composer to MongoDB storage, a connector server needs to be installed and configured. See [*Manage Connectors and Connector Servers*](https://devnet.logianalytics.com/hc/en-us/articles/4405859186199-Manage-Connectors-and-Connector-Servers) for general instructions.

After the connector has been set up, you can create data source configurations that specify the necessary connection information and identify the data you want to use. See [*Manage Data Source Configurations*](https://devnet.logianalytics.com/hc/en-us/articles/4405851027479-Manage-Data-Source-Configurations) for more information. After data sources are configured, they can be used to create dashboards and visuals from your data. See [*Create Dashboards*](https://devnet.logianalytics.com/hc/en-us/articles/4405859261207-Create-Dashboards).

## Composer Feature Support

MongoDB connector support for specific [Composer features](https://devnet.logianalytics.com/hc/en-us/articles/4405859170583-Connector-Feature-Support) is shown in the following table.

**Key:** **Y** - Supported; **N** - Not Supported; N/A - not applicable

| Feature | Supported? | | |
| --- | --- | --- | --- |
| [Admin-Defined Functions](https://devnet.logianalytics.com/hc/en-us/articles/4405850995991-Admin-Defined-Functions) | **N** | | |
| [Box Plots](https://devnet.logianalytics.com/hc/en-us/articles/4405859517207-Box-Plots) | **N** | | |
| [Custom SQL Queries](https://devnet.logianalytics.com/hc/en-us/articles/4405859171735-Custom-SQL-Queries) | **N** | | |
| [Derived Fields (Row-Level Expressions)](https://devnet.logianalytics.com/hc/en-us/articles/4405859299479-Maintain-Derived-Fields) | **Y** | | |
| [Distinct Counts](https://devnet.logianalytics.com/hc/en-us/articles/4405859300503-Enable-Distinct-Counts) | **Y** | | |
| [Fast Distinct Values](https://devnet.logianalytics.com/hc/en-us/articles/4405850912279-Fast-Distinct-Values) | N/A | | |
| [Group By Multiple Fields](https://devnet.logianalytics.com/hc/en-us/articles/4405850913303-Group-By-Multiple-Fields) | **Y** | | |
| [Group By Time](https://devnet.logianalytics.com/hc/en-us/articles/4405850914199-Group-By-Time) | **Y** | | |
| [Group By UNIX Time](https://devnet.logianalytics.com/hc/en-us/articles/4405850915095-Group-By-UNIX-Time) | **N** | | |
| [Histogram Floating Point Values](https://devnet.logianalytics.com/hc/en-us/articles/4405850915991-Histogram-Floating-Point-Values) | **Y** | | |
| [Histograms](https://devnet.logianalytics.com/hc/en-us/articles/4405859514775-Bars-Histograms) | **N** | | |
| [Kerberos Authentication](https://devnet.logianalytics.com/hc/en-us/articles/4405859461271-Configure-Kerberos-Single-Sign-On-SSO-Settings) | **N** | | |
| [Last Value](https://devnet.logianalytics.com/hc/en-us/articles/4405859174295-Last-Value) | **N** | | |
| [Live Mode and Playback](https://devnet.logianalytics.com/hc/en-us/articles/4405851191447-Live-Mode-and-Historical-Playback) | **Y** | | |
| [Multivalued Fields](https://devnet.logianalytics.com/hc/en-us/articles/4405859175319-Multivalued-Fields) | **Y** | | |
| [Nested Fields](https://devnet.logianalytics.com/hc/en-us/articles/4405851022871-Support-of-Nested-Data-Structures-in-Composer) | **Y** | | |
| [Partitions](https://devnet.logianalytics.com/hc/en-us/articles/4405859176343-Partitions) | N/A | | |
| [Pushdown Joins for Fusion Data Sources](https://devnet.logianalytics.com/hc/en-us/articles/4405859358487-Optimize-Joins) | **N** | | |
| [Schemas](https://devnet.logianalytics.com/hc/en-us/articles/4405859177367-Schemas) | **Y** | | |
| [Text Search](https://devnet.logianalytics.com/hc/en-us/articles/4405859178391-Text-Search) | N/A | | |
| [TLS](https://devnet.logianalytics.com/hc/en-us/articles/4405859179671-TLS) | **Y** | | |
| [User Delegation](https://devnet.logianalytics.com/hc/en-us/articles/4405859193111-Enable-User-Delegation) | **N** | | |
| [Wild Card Filters](https://devnet.logianalytics.com/hc/en-us/articles/4405851071383-Apply-Wild-Card-Filters-to-a-Visual-or-Dashboard) | **Y** | | |
| [Wild Card Filters, Case-Insensitive Mode](https://devnet.logianalytics.com/hc/en-us/articles/4405851071383-Apply-Wild-Card-Filters-to-a-Visual-or-Dashboard) | **Y** | | |
| [Wild Card Filters, Case-Sensitive Mode](https://devnet.logianalytics.com/hc/en-us/articles/4405851071383-Apply-Wild-Card-Filters-to-a-Visual-or-Dashboard) | **Y** | | |

MongoDB connectors support [derived fields](https://devnet.logianalytics.com/hc/en-us/articles/4405859299479-Maintain-Derived-Fields) created using most [row-level functions](https://devnet.logianalytics.com/hc/en-us/articles/4405851021079-Supported-Row-Level-Functions), with the following exceptions:

* If you are running a version of MongoDB prior to version 4.0, the following [text row-level functions](https://devnet.logianalytics.com/hc/en-us/articles/4405851020183-Text-Functions) are not supported (these functions work for MongoDB version 4.0 and later):

  + TEXT\_TO\_NUM
  + TEXT\_TO\_TIME
  + LTRIM
  + RTRIM
* The following restrictions apply to MongoDB 3.4:

  + You cannot use a number field with a year pattern as a date field in a [row-level expression](https://devnet.logianalytics.com/hc/en-us/articles/4405859311511-Row-Level-Expressions).
  + [TIME\_ADD](https://devnet.logianalytics.com/hc/en-us/articles/4405859308823-Time-Functions) intervals cannot be specified for YEAR, QUARTER, or MONTH.
  + [TRUNCATE\_TIME](https://devnet.logianalytics.com/hc/en-us/articles/4405859308823-Time-Functions) cannot truncate date-time field values to YEAR or QUARTER granularities.

## Connect to MongoDB with Configured SSL

To connect to a MongoDB data store with configured SSL:

1. Add parameter `ssl=true` to your connection string. For example (replace `<mongodb_host>`, `<port>`, `<database>` with your values ):

   ```
   mongodb://<mongodb_host>:<port>/<database>?ssl=true
   ```
2. If your MongoDB data store is configured with a custom certificate, you should configure a truststore for the MongoDB connector:

   1. Copy a truststore to the machine on which the MongoDB connector is running.
   2. Add the following lines to file `/etc/zoomdata/edc-mongo.jvm`. Copy the file `edc-mongo.jvm` from the `/opt/zoomdata/conf` directory if a copy is not in `/etc/zoomdata/`.

      ```
      -Djavax.net.ssl.trustStore=<path_to_truststore>  
      -Djavax.net.ssl.trustStorePassword=<truststore_password>
      ```

      Replace:

      * `<path_to_truststore>` with an absolute path to your truststore
      * `<truststore_password>` with a password for your truststore
3. Restart the MongoDB connector microservice. See [*Restart Composer Microservices*](https://devnet.logianalytics.com/hc/en-us/articles/4405851094679-Restart-Composer-Microservices).
