---
title: "Disable Data Caching for a Data Source"
id: 34932820958733
section: "Connect to Data in Composer 25"
product: "Logi Composer v25"
url: https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932820958733-Disable-Data-Caching-for-a-Data-Source
updated_at: 2026-05-26T22:09:45Z
---

# Disable Data Caching for a Data Source

# Disable Data Caching for a Data Source

The Composer data cache is a temporary storage area containing the aggregated data from your data sources. Two caches are supported: the visual (visual data) cache and the metadata (field statistics) cache. By default, caching is enabled for all data sources using both caches. However, you can disable all caching if your data source is constantly being updated, or you do not want to allocate the required RAM or if the performance of your data source is so high you do not need to store the aggregated queries.

**Disable data caching**

1. Make sure you are logged in as a user with the **Administer Sources** [privilege](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932577846157-Group-Privilege-Reference), or a user with **read** and **write** [permission](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932915596173-About-Source-Permissions) for the data source.
2. Select **Sources** on the [UI menu](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933143886477-The-Composer-UI-Menu) (![](https://logi-composer-v25.insightsoftware.com/hc/article_attachments/46167924070029)). The [Data Sources](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932895238669-Data-Sources-Page) page appears.
3. On the [Sources](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932895238669-Data-Sources-Page) page, locate and select the data source configuration you want to edit. The Source Creation work area opens.
4. Select the **Cache** tab. All the fields from your data source are listed.

   ![](https://logi-composer-v25.insightsoftware.com/hc/article_attachments/46167352418061)
5. Disable (toggle off) **Data Cache**. Data caching is disabled for the data source configuration. Data will be freshly loaded into the Composer cache the next time it is requested from the data source.
6. Optionally, Disable (toggle off) **Statistics Cache**. Field metadata caching is disabled for the data source configuration.  Data will be freshly loaded into the Composer cache the next time it is requested from the data source. Data will be freshly loaded into the Composer cache the next time it is requested from the data source.

   If you have [set up refresh jobs](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933150390285-Set-Up-a-Data-Source-Refresh-Job) for this data source, a warning appears that the jobs are disabled and the schedule deleted for this data source. Select **Ok** to continue disabling Statistics Cache and delete the schedule.
7. Exit the source data configuration when you've finished making your changes.
