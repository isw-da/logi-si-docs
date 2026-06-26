---
title: "Enable Data Sharpening and Configure Its Defaults"
id: 4405851007127
section: "Manipulate Data in Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405851007127-Enable-Data-Sharpening-and-Configure-Its-Defaults
updated_at: 2021-12-13T00:27:59Z
---

# Enable Data Sharpening and Configure Its Defaults

# Enable Data Sharpening and Configure Its Defaults

To enable and configure Data Sharpening for a data source configuration, you need to enable the time settings in the data source's settings page. Specifically, a playable time field must be specified in the Global Default Settings on the Visuals tab of the data source configuration. However, Cloudera Impala data sources require additional configuration as described in [*Enable Data Sharpening for Cloudera Impala Data Sources*](https://devnet.logianalytics.com/hc/en-us/articles/4405859217687-Enable-Data-Sharpening-for-Cloudera-Impala-Data-Sources).

To configure Data Sharpening in a data source configuration:

1. Log into Composer (either as an administrator or as a user who has been assigned to a group with [data source management privileges](https://devnet.logianalytics.com/hc/en-us/articles/4405859114647-Group-Privilege-Reference)).
2. Select **Sources** on the [UI menu](https://devnet.logianalytics.com/hc/en-us/articles/4405859444119-The-Composer-UI-Menu) (![](https://devnet.logianalytics.com/hc/article_attachments/4406743720343/hamburger.png)) or the [top-level navigation menu](https://devnet.logianalytics.com/hc/en-us/articles/4405851152407-The-Top-Level-Navigation-Banner), or select the **Sources** box on the [Home page](https://devnet.logianalytics.com/hc/en-us/articles/4405851121559-Home-Page). The [Sources](https://devnet.logianalytics.com/hc/en-us/articles/4405851037719-Sources-Page) page appears.
3. Select your data source to start the data source configuration wizard.
4. Select the **Visuals** tab.
5. Select the **Global Default Settings**. The time bar, search, and Data Sharpening settings for the data source appear.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4406747434647/ds-global-defaults_288x518.png)
6. Make sure **Enable Timebar** is switched on. This enables the Data Sharpening settings. If this is switched off, you cannot configure Data Sharpening settings. For more information about time bar default settings, see [*Configure Time Bar Defaults*](https://devnet.logianalytics.com/hc/en-us/articles/4405859324311-Configure-Time-Bar-Defaults).
7. Slide the **Prefer Sharpening** switch to the right to enable Data Sharpening for the data source.
8. Optionally, use the **Max Queries** slider to specify the maximum number of queries used for Data Sharpening. The default maximum is 10 queries.
9. Select **Finish** or **Save** to save your data source configuration.
