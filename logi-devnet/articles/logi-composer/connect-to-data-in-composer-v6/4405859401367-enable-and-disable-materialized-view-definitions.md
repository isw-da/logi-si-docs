---
title: "Enable and Disable Materialized View Definitions"
id: 4405859401367
section: "Connect to Data in Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405859401367-Enable-and-Disable-Materialized-View-Definitions
updated_at: 2021-09-21T01:29:05Z
---

# Enable and Disable Materialized View Definitions

# Enable and Disable Materialized View Definitions

You can enable and disable materialized view definitions. When disabled, the stored query data for the materialized view is not used in visuals for the data source. Disabling a materialized view definition allows you to remove the effect of the definition without deleting it.

By default materialized view definitions are enabled when they are defined.

![](https://devnet.logianalytics.com/hc/article_attachments/4406743739159/criticalicon.gif) This is an experimental feature.

To disable a materialized view definition using the UI:

1. Make sure you are logged in as a Composer administrator or a user with the **Can Administer Sources** or the **Can Create new Data Sources**[privilege](https://devnet.logianalytics.com/hc/en-us/articles/4405859114647-Group-Privilege-Reference) and that you have [write permission for the data source](https://devnet.logianalytics.com/hc/en-us/articles/4405859328535-About-Data-Source-Permissions).
2. List the materialized views for the data source. See [*List Materialized View Definitions*](https://devnet.logianalytics.com/hc/en-us/articles/4405851113751-List-Materialized-View-Definitions).

   ![](https://devnet.logianalytics.com/hc/article_attachments/4406743777815/mat-view-list_576x447.png)
3. Locate the materialized view in the list of materialized view definitions and slide the switch in the **Enabled** column for the definition to the left (off).

   The definition is disabled.

To enable a materialized view definition using the UI:

1. Make sure you are logged in as a Composer administrator or a user with the **Can Administer Sources** or the **Can Create new Data Sources**[privilege](https://devnet.logianalytics.com/hc/en-us/articles/4405859114647-Group-Privilege-Reference).
2. List the materialized views for the data source. See [*List Materialized View Definitions*](https://devnet.logianalytics.com/hc/en-us/articles/4405851113751-List-Materialized-View-Definitions).

   ![](https://devnet.logianalytics.com/hc/article_attachments/4406743777815/mat-view-list_576x447.png)
3. Locate the materialized view in the list of materialized view definitions and slide the switch in the **Enabled** column for the definition to the right (on).

   The definition is enabled.
