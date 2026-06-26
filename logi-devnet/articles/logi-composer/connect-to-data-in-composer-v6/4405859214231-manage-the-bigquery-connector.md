---
title: "Manage the BigQuery Connector"
id: 4405859214231
section: "Connect to Data in Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405859214231-Manage-the-BigQuery-Connector
updated_at: 2021-11-10T22:39:59Z
---

# Manage the BigQuery Connector

# Manage the BigQuery Connector

The Composer BigQuery connector lets you access the data available in Google BigQuery storage using the Composer client. The Composer BigQuery connector supports the current version of this software as a microservice (SaaS) product.

The Composer BigQuery connector is a cloud connector that connects to Google BigQuery via the BigQuery API. See *Manage Connectors and Connector Servers* for general instructions and [*Connect to BigQuery*](#Connecti) for details specific to the BigQuery connector.

After the connector has been set up, you can create data source configurations that specify the necessary connection information and identify the data you want to use. See [*Manage Data Source Configurations*](https://devnet.logianalytics.com/hc/en-us/articles/4405851027479-Manage-Data-Source-Configurations) for more information. After data sources are configured, they can be used to create dashboards and visuals from your data. See [*Create Dashboards*](https://devnet.logianalytics.com/hc/en-us/articles/4405859261207-Create-Dashboards).

## Composer Feature Support

BigQuery connector support for specific [Composer features](https://devnet.logianalytics.com/hc/en-us/articles/4405859170583-Connector-Feature-Support) is shown in the following table.

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
| [Kerberos Authentication](https://devnet.logianalytics.com/hc/en-us/articles/4405859461271-Configure-Kerberos-Single-Sign-On-SSO-Settings) | N/A | |
| [Last Value](https://devnet.logianalytics.com/hc/en-us/articles/4405859174295-Last-Value) | **Y** | |
| [Live Mode and Playback](https://devnet.logianalytics.com/hc/en-us/articles/4405851191447-Live-Mode-and-Historical-Playback) | **Y** | |
| [Multivalued Fields](https://devnet.logianalytics.com/hc/en-us/articles/4405859175319-Multivalued-Fields) | N/A | |
| [Nested Fields](https://devnet.logianalytics.com/hc/en-us/articles/4405851022871-Support-of-Nested-Data-Structures-in-Composer) | N/A | |
| [Partitions](https://devnet.logianalytics.com/hc/en-us/articles/4405859176343-Partitions) | **Y** | |
| [Pushdown Joins for Fusion Data Sources](https://devnet.logianalytics.com/hc/en-us/articles/4405859358487-Optimize-Joins) | **Y** | |
| [Schemas](https://devnet.logianalytics.com/hc/en-us/articles/4405859177367-Schemas) | **Y** | |
| [Text Search](https://devnet.logianalytics.com/hc/en-us/articles/4405859178391-Text-Search) | N/A | |
| [TLS](https://devnet.logianalytics.com/hc/en-us/articles/4405859179671-TLS) | N/A | |
| [User Delegation](https://devnet.logianalytics.com/hc/en-us/articles/4405859193111-Enable-User-Delegation) | **N** | |
| [Wild Card Filters](https://devnet.logianalytics.com/hc/en-us/articles/4405851071383-Apply-Wild-Card-Filters-to-a-Visual-or-Dashboard) | **Y** | |
| [Wild Card Filters, Case-Insensitive Mode](https://devnet.logianalytics.com/hc/en-us/articles/4405851071383-Apply-Wild-Card-Filters-to-a-Visual-or-Dashboard) | **Y** | |
| [Wild Card Filters, Case-Sensitive Mode](https://devnet.logianalytics.com/hc/en-us/articles/4405851071383-Apply-Wild-Card-Filters-to-a-Visual-or-Dashboard) | **Y** | |

## Connect to BigQuery

When connecting to BigQuery, provide the following information:

* Key Path: you have to specify the absolute path to the file that must be available for the connector.
* Public Project IDs.

For more information about these values, refer to Google BigQuery's documentation.

### Authorize the BigQuery Connection

To authorize the BigQuery connection, you need to create a security key for it. Before you can create the security key, you must access or create a BigQuery microservice account.

To create a BigQuery microservice account, perform the following steps:

1. Login to your Google API Console.
2. Select the required project from the list.
3. Make sure that current account is linked to a billing account. To check this, select the ![](https://devnet.logianalytics.com/hc/article_attachments/4406747448087/google-api-console-menu_17x15.png)icon and then select **Billing**.
4. On the API Manager page, select **Credentials**:

   ![](https://devnet.logianalytics.com/hc/article_attachments/4406743913111/bigquery-selecting-credentials-menu_152x135.png)
5. On the Credentials page, select **Manage service accounts**.
6. On the Service Accounts page, select **Create Service Account** and specify the following:

   * Service account name
   * Role - grant this microservice account role based access to the project. From the list, select the **BigQuery** category and then select **BigQuery Data Viewer** and **BigQuery User** roles.
   * Service account ID

   ![](https://devnet.logianalytics.com/hc/article_attachments/4406743913751/bigquery-create-service-account_230x208.png)
7. Select **Create**.

After you have created an account, create a security key for it.

To create a security key:

1. On the **Service Accounts** page, find the required account.
2. From the menu, select **Create key**.
3. In the Create private key dialog, select **JSON** for the key type and select **Create**. The local copy of the key is saved on your computer.

   For more information, see the following Google resources: [BigQuery Introduction to Authentication](https://cloud.google.com/bigquery/docs/authentication/) and [Using OAuth 2.0 for Server to Server Applications](https://developers.google.com/identity/protocols/oauth2/service-account).
4. Move the file with the key to the server, on which the connector is running.
