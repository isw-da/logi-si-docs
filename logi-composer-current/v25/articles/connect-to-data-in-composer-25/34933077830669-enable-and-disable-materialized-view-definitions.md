---
title: "Enable and Disable Materialized View Definitions"
id: 34933077830669
section: "Connect to Data in Composer 25"
product: "Logi Composer v25"
url: https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933077830669-Enable-and-Disable-Materialized-View-Definitions
updated_at: 2026-05-26T22:09:22Z
---

# Enable and Disable Materialized View Definitions

# Enable and Disable Materialized View Definitions

**Note:** 
Materialized view functionality is disabled by default. To enable, [contact technical support](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932980712461-Contact-Technical-Support) for assistance.
The [Materialized Views API](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932682254861-Materialized-Views-API-Experimental) is deprecated and will be removed in a future release.

You can enable and disable individual materialized view definitions. When disabled, the stored query data for the materialized view is not used in visuals for the data source. Disabling a materialized view definition allows you to remove the effect of the definition without deleting it.

By default, individual materialized view definitions are enabled when they are defined.

**Important:** 
This is an experimental feature.

**Disable a materialized view definition using the UI**

1. Make sure you are logged in as a user with the **Administer Sources**  or the **Create New Data Sources**[privilege](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932577846157-Group-Privilege-Reference).
2. List the materialized views for the data source. See [List Materialized View Definitions](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933057267725-List-Materialized-View-Definitions).

   ![](https://logi-composer-v25.insightsoftware.com/hc/article_attachments/46167137030157)
3. Locate the materialized view in the list of materialized view definitions and slide the switch in the **Enabled** column for the definition to the left (off).

   The definition is disabled.

**Enable a materialized view definition using the UI**

1. Make sure you are logged in as a user with the **Administer Sources** or the **Create New Data Sources** [privilege](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932577846157-Group-Privilege-Reference).
2. List the materialized views for the data source. See [List Materialized View Definitions](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933057267725-List-Materialized-View-Definitions).

   ![](https://logi-composer-v25.insightsoftware.com/hc/article_attachments/46167137030157)
3. Locate the materialized view in the list of materialized view definitions and slide the switch in the **Enabled** column for the definition to the right (on).

   The definition is enabled.
