---
title: "Enable Data Sharpening and Configure Its Defaults"
id: 34932836726541
section: "Manipulate Data In The Composer 25 Data Store"
product: "Logi Composer v25"
url: https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932836726541-Enable-Data-Sharpening-and-Configure-Its-Defaults
updated_at: 2026-05-26T22:09:54Z
---

# Enable Data Sharpening and Configure Its Defaults

# Enable Data Sharpening and Configure Its Defaults

To enable and configure Data Sharpening for a data source configuration, you need to enable the time settings in the data source's settings page. Specifically, a playable time field must be specified in the Global Settings tab of the data source configuration. However, Cloudera Impala data sources require additional configuration as described in [Enable Data Sharpening for Cloudera Impala Data Sources](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932735320461-Enable-Data-Sharpening-for-Cloudera-Impala-Data-Sources).

**Configure Data Sharpening in a data source configuration**

1. Log into Composer (either as an administrator or as a user who has been assigned to a group with [data source management privileges](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932577846157-Group-Privilege-Reference)).
2. Select **Sources** on the [UI menu](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933143886477-The-Composer-UI-Menu) (![](https://logi-composer-v25.insightsoftware.com/hc/article_attachments/46167940996109)) or the [top-level navigation menu](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933120256397-The-Top-Level-Navigation-Banner), or select the **Sources** box on the [Home page](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933063528717-Home-Page). The [Sources](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932895238669-Data-Sources-Page) page appears.
3. In the table on the Sources page, locate and select the data source configuration you want to edit.
4. Select the **Global Settings** tab. The time bar, search, and Data Sharpening settings for the data source appears.

   ![](https://logi-composer-v25.insightsoftware.com/hc/article_attachments/46167930881421)
5. Make sure **Time Bar** is enabled to access Data Sharpening settings. If Time Bar is disabled, you can't configure Data Sharpening settings. For more information about time bar default settings, see [Configure Time Bar Defaults](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932879958669-Configure-Time-Bar-Defaults).
6. Slide the **Prefer Sharpening** switch to the right to enable Data Sharpening for the data source.
7. Optionally, use the **Max Queries** slider to specify the maximum number of queries used for Data Sharpening. The default maximum is 10 queries.
8. When your changes are complete, select **Save Settings** to save your changes.
