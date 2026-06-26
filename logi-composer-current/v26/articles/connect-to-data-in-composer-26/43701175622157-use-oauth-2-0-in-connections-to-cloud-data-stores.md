---
title: "Use OAuth 2.0 in Connections to Cloud Data Stores"
id: 43701175622157
section: "Connect to Data in Composer 26"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701175622157-Use-OAuth-2-0-in-Connections-to-Cloud-Data-Stores
updated_at: 2026-05-29T14:09:23Z
---

# Use OAuth 2.0 in Connections to Cloud Data Stores

# Use OAuth 2.0 in Connections to Cloud Data Stores

You can leverage existing authorization rules of BigQuery and Snowflake data sources by enabling OAuth 2.0 for these connectors in Logi Composer. Users access the connected data stores, using their personalized credentials, and receive access to the data following the security rules of your data source.

## Feature Support

Use OAuth to connect to these supported data sources:

* [Connect to BigQuery](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701009802509-Manage-the-BigQuery-Connector#Connecti)
* [Connect to Snowflake](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701074814989-Manage-the-Snowflake-Connector#Connecti)

To avoid frequent authentication requests for users, Logi Composer operates with long-lived tokens and preemptively refreshes the tokens when they are close to expiration.

**Note:** 
Scheduled source refresh is not available when you use OAuth 2.0 authentication.
