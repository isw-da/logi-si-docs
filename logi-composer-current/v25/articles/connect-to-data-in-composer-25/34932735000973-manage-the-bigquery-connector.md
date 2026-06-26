---
title: "Manage the BigQuery Connector"
id: 34932735000973
section: "Connect to Data in Composer 25"
product: "Logi Composer v25"
url: https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932735000973-Manage-the-BigQuery-Connector
updated_at: 2026-05-26T22:10:12Z
---

# Manage the BigQuery Connector

# Manage the BigQuery Connector

The Composer BigQuery connector lets you access the data available in Google BigQuery storage using the Composer client. The Composer BigQuery connector supports the current version of this software as a microservice (SaaS) product.

The Composer BigQuery connector is a cloud connector that connects to Google BigQuery via the BigQuery API. See [Manage Connectors and Connector Servers](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932741363981-Manage-Connectors-and-Connector-Servers) for general instructions and [Connect to BigQuery](#Connecti) for details specific to the BigQuery connector.

After setting up the connector, create data sources that specify the necessary connection information and identify the data you want to use. See [Manage Data Sources](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932941009037-Manage-Data-Sources) for more information. After you set up your data sources, create [dashboards](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932763355021-Create-Dashboards) and [visuals](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933273224589-Create-and-Add-Visuals-to-the-Visual-Gallery) from from the data in these data sources. See [Create Dashboards](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932763355021-Create-Dashboards).

## Feature Support

Connector support for specific  [features](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932704861453-Connector-Feature-Support) is shown in the following table.

**Key:** **Y** - Supported; **N** - Not Supported; N/A - not applicable

| Feature | Supported? |
| --- | --- |
| [Admin-Defined Functions](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932796673933-Admin-Defined-Functions) | **Y** |
| [Box Plots](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933208692493-Box-Plots) | **Y** |
| [Custom SQL Queries](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932704947213-Custom-SQL-Queries) | **Y** |
| [Derived Fields (Row-Level Expressions)](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932839148813-Maintain-Derived-Fields) | **Y** |
| [Distinct Counts](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932867905037-Distinct-Counts) | **Y** |
| [Fast Distinct Values](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932715069197-Fast-Distinct-Values) | N/A |
| [Group By Multiple Fields](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932715164173-Group-By-Multiple-Fields) | **Y** |
| [Group By Time](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932690999309-Group-By-Time) | **Y** |
| [Group By UNIX Time](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932730700429-Group-By-UNIX-Time) | **Y** |
| [Histogram Floating Point Values](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932708132109-Histogram-Floating-Point-Values) | **Y** |
| [Histograms](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933212496141-Bars-Histograms) | **Y** |
| [Kerberos Authentication](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933139627149-Configure-Kerberos-Single-Sign-On-SSO-Settings) | N/A |
| [Last Value](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932730888205-Last-Value) | **Y** |
| [Live Mode and Playback](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933163012621-Live-Mode-and-Historical-Playback) | **Y** |
| [Multivalued Fields](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932715662093-Multivalued-Fields) | N/A |
| [Nested Fields](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932861225357-Support-of-Nested-Data-Structures-in-Composer) | N/A |
| [Partitions](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932715778445-Partitions) | **Y** |
| [Pushdown Joins for Fusion Data Sources](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932963077133-Optimize-Joins) | **Y** |
| [Schemas](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932691729805-Schemas) | **Y** |
| [Text Search](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932739827853-Text-Search) | N/A |
| [TLS](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932692004749-TLS) | N/A |
| [User Delegation](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932742695053-Enable-User-Delegation) | **N** |
| [Wildcard Filters](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932977272717-Apply-Wildcard-Filters-to-a-Visual-Filter-Snippet-or-Dashboard) | **Y** |
| [Wildcard Filters, Case-Insensitive Mode](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932723779981-Wildcard-Case-Insensitive-Filters) | **Y** |
| [Wildcard Filters, Case-Sensitive Mode](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932692417677-Wildcard-Case-Sensitive-Filters) | **Y** |

## Connect to BigQuery

When connecting to BigQuery, provide the following information:

* Key Path:
  you have to specify the absolute path to the file that must be available for the connector.
* Public Project IDs.

For more information about these values, refer to Google BigQuery's documentation.

### Authorize the BigQuery Connection

To authorize the BigQuery connection, you need to create a security key for it. Before you can create the security key, you must access or create a BigQuery microservice account.

**Create a BigQuery microservice account**

1. Login to your Google API Console.
2. Select the required project from the list.
3. Make sure that current account is linked to a billing account. To check this, select the menu (![](https://logi-composer-v25.insightsoftware.com/hc/article_attachments/46167452157325)) icon and then select
   **Billing**.
4. On the API Manager page, select **Credentials**:

   ![](https://logi-composer-v25.insightsoftware.com/hc/article_attachments/46167426873229)
5. On the Credentials page, select **Manage service accounts**.
6. On the Service Accounts page, select **Create Service Account** and specify the following:

   * Service account name
   * Role - grant this microservice account role based access to the project. From the list, select the **BigQuery** category and then select **BigQuery Data Viewer** and **BigQuery User** roles.
   * Service account ID

   ![](https://logi-composer-v25.insightsoftware.com/hc/article_attachments/46167437559309)
7. Select **Create**.

After you have created an account, create a security key for it.

**Create a security key**

1. On the **Service Accounts** page, find the required account.
2. From the menu, select **Create key**.
3. In the Create private key dialog, select **JSON** for the key type and select **Create**. The local copy of the key is saved on your computer.

   For more information, see the following Google resource:
   [BigQuery Introduction to Authentication](https://cloud.google.com/bigquery/docs/authentication/).
4. Move the file with the key to the server, on which the connector is running.

## Connect to BigQuery Using OAuth

To create a BigQuery connection use one of the available authentication methods:

* Key authentication flow requires a security key to be generated at BigQuery and placed to the Logi Composer instance;
* OAuth 2.0 requires providing OAuth `client_id` and `client_secrets` generated for a user that will serve for data retrieval, such as an integration user. Users are asked to authenticate via a separate authentication form. Users provide their individual credentials when accessing the data retrieved using this connection.

If both authentication methods are selected, connection via OAuth will have higher priority over key authentication except for the scheduled overrides setup.

|  | Authentication Flow |  |
| --- | --- | --- |
| Key Path | Key Authentication | Absolute path to the key authentication file obtained from BigQuery and placed to Logi Composer instance. |
| Public Project Ids | List of public project IDs that will be queried for the data. |
| **OAuth 2.0 Enabled** | OAuth 2.0 | TRUE/FALSE |
| **Project Id** | Billing project ID that will be queried for the data.  **Note:**  Optional if keys authentication is used.  **Important:**  Mandatory if OAuth 2.0 connection is enabled. |
| **OAuth 2.0 Client Id** | `client_id`: Obtain from BigQuery.  See <https://cloud.google.com/bigquery/docs/authentication/end-user-installed>. |
| **OAuth 2.0 Client Secrets** | `client_secrets`: Obtain from BigQuery.  See <https://cloud.google.com/bigquery/docs/authentication/end-user-installed>. |

### Scheduled Override Options

To maintain Logi Composer's ability to perform scheduled operations such as scheduled dashboard reports, alerts notifications, and more when using OAuth 2.0 authentication flow, you can setup scheduled overrides with key authentication method by providing a key path.

Additional OAuth 2.0 parameters available for override, however, already have prepopulated BigQuery values and do not require manual editing:

* `OAUTH2.AUTHORIZATION_URI`
* `OAUTH2.TOKEN_URI`
* `OAUTH2.SCOPES`

**Note:** 
Scheduled source refresh is not available when you use OAuth 2.0 authentication.

To avoid frequent authentication requests for users, Logi Composer operates with long-lived tokens and preemptively refreshes the tokens when they are close to expiration.

**Important:** 
Users' OAuth sessions are terminated when the OAuth token is revoked, if the connection is deleted, or connection details are modified.
