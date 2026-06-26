---
title: "Clear the Cache for a Data Source Configuration"
id: 34932890108045
section: "Connect to Data in Composer 25"
product: "Logi Composer v25"
url: https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932890108045-Clear-the-Cache-for-a-Data-Source-Configuration
updated_at: 2026-05-26T22:09:46Z
---

# Clear the Cache for a Data Source Configuration

# Clear the Cache for a Data Source Configuration

You can manually clear the cache for a data source configuration if you are a user granted the **Administer Sources** [privilege](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932577846157-Group-Privilege-Reference) or a user with **write** [permission](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932915596173-About-Source-Permissions) for the data source. Both the visual (visual data) cache and the metadata (field statistics) cache are cleared.

**Clear the cache for a data source configuration**

1. Log in as a user with the **Administer Sources** [privilege](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932577846157-Group-Privilege-Reference), or a user with **write** [permission](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932915596173-About-Source-Permissions) for the data source.
2. Select **Sources** on the [UI menu](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933143886477-The-Composer-UI-Menu) (![](https://logi-composer-v25.insightsoftware.com/hc/article_attachments/46167916702093)) or the [top-level navigation menu](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933120256397-The-Top-Level-Navigation-Banner), or select the **Sources** box on the [Home page](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933063528717-Home-Page). The [Sources](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932895238669-Data-Sources-Page) page appears.
3. In the table on the Sources page, locate the row displaying the data source configuration with the cache you want to clear.
4. Select the Clear Cache button in the **Actions** column of the table. The Cache Cleanup work area opens.

   ![cache cleanup dialog box](https://logi-composer-v25.insightsoftware.com/hc/article_attachments/46167304787469 "cache cleanup dialog box")
5. If available, select **[Data Cache](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932891391629-Cache-Tab#datacache)** to clear the query results from visuals.
6. If available, select **[Statistics Cache](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932891391629-Cache-Tab#stasticscache)** to clear the cache of field statisticsdata such as min, max, and distinct values numbers.

   **Note:** 
   Control the availability of caching options on the [Cache tab](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932891391629-Cache-Tab) of a data source.
7. Select **Ok** to clear your selected caches for this data source. The data is freshly loaded into the Composer cache the next time it is requested from the data source. For more information about data caching or to disable it, see [How Composer Caches Data](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932848587917-How-Composer-Caches-Data).

**Note:** 
If a [Custom Range](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932906721933-Manage-Fields#Custom) has been defined for a field, the minimum and maximum fields used in filters remains unchanged by the action of refreshing the source data.

**Note:** 
You can force Composer to bypass and update the cache to query the underlying data source by selecting **Refresh** from a Composer dashboard menu.
