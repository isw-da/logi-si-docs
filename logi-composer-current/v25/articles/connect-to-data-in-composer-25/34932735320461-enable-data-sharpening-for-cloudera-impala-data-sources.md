---
title: "Enable Data Sharpening for Cloudera Impala Data Sources"
id: 34932735320461
section: "Connect to Data in Composer 25"
product: "Logi Composer v25"
url: https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932735320461-Enable-Data-Sharpening-for-Cloudera-Impala-Data-Sources
updated_at: 2026-05-26T22:10:13Z
---

# Enable Data Sharpening for Cloudera Impala Data Sources

# Enable Data Sharpening for Cloudera Impala Data Sources

Data Sharpening works with certain partitioned Impala data sources. The partitioned field should be a time-based attribute and in a supported time format (for example, yyyy-MM-dd). Follow the steps below to set up Data Sharpening for an Impala data source.

**Configure Data Sharpening for a Cloudera Impala data source configuration:**

1. Log into Composer (either as an administrator or as a user who has been assigned to a group with [data source management privileges](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932577846157-Group-Privilege-Reference)).
2. Select **Sources** on the [UI menu](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933143886477-The-Composer-UI-Menu) (![](https://logi-composer-v25.insightsoftware.com/hc/article_attachments/46167957946765)) or the [top-level navigation menu](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933120256397-The-Top-Level-Navigation-Banner), or select the **Sources** box on the [Home page](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933063528717-Home-Page). The [Sources](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932895238669-Data-Sources-Page) page appears.
3. Select the appropriate data source configuration to edit it, then access the [Fields tab](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932906721933-Manage-Fields) of the data source.
4. Locate and select the time field you want to use as the driving time field. Select an appropriate time granularity in the **Data Details** section of the **Settings** side bar menu, then **Save** your changes. Consider the 10% rule to ensure Data Sharpening runs when you want it to. See [When Data Sharpening Occurs](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932849324685-When-Data-Sharpening-Occurs) for more information.
5. Select the **Global Settings** tab, and enable **Time Bar** if not enabled to access the data sharpening settings. See [Configure Time Bar Defaults](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932879958669-Configure-Time-Bar-Defaults).
6. Select the time field you want to use as the driving time field in thedrop-downfor **Default Time Attribute**.
7. Enable the **Prefer Sharpening** toggle to enable sharpening and sharpening settings.
8. Optionally, use the **Max Queries** slider to specify the maximum number of queries used for Data Sharpening. The default maximum is 10 queries.
9. When your changes are complete, select **Save Settings** to save your changes.
