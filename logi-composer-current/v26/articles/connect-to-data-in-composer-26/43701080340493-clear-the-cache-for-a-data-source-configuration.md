---
title: "Clear the Cache for a Data Source Configuration"
id: 43701080340493
section: "Connect to Data in Composer 26"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701080340493-Clear-the-Cache-for-a-Data-Source-Configuration
updated_at: 2026-08-26T07:12:17Z
---

# Clear the Cache for a Data Source Configuration

# Clear the Cache for a Data Source Configuration

You can manually clear the cache for a data source configuration if you are a user granted the **Administer Sources** [privilege](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701005611789-Group-Privilege-Reference) or a user with **write** [permission](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701101615373-About-Source-Permissions) for the data source. Both the visual (visual data) cache and the metadata (field statistics) cache are cleared.

**Note:** In this release, when your admin enables the Enhanced Experience user interface, you will see changes to workflows you may have used in previous releases.

**Clear the cache for a data source configuration**

1. Log in as a user with the **Administer Sources** [privilege](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701005611789-Group-Privilege-Reference), or a user with **write** [permission](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701101615373-About-Source-Permissions) for the data source.
2. Select the **Sources** card on your home page or **Data Sources** from the main menu.. The [Sources](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701081381901-Data-Sources-Page) page appears.
3. In the table on the Sources page, locate the row displaying the data source configuration with the cache you want to clear.
4. Select the Clear Cache button in the **Actions** column of the table. The Cache Cleanup work area opens.

   ![cache cleanup dialog box](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/48418031075981 "cache cleanup dialog box")
5. If available, select **[Data Cache](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701085337997-Cache-Tab#datacache)** to clear the query results from visuals.
6. If available, select **[Statistics Cache](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701085337997-Cache-Tab#stasticscache)** to clear the cache of field statistics data such as min, max, and distinct values numbers.

   **Note:** 
   Control the availability of caching options on the [Cache tab](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701085337997-Cache-Tab) of a data source.
7. Select **Ok** to clear your selected caches for this data source. The data is freshly loaded into the Composer cache the next time it is requested from the data source. For more information about data caching or to disable it, see [How Composer Caches Data](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701078034061-How-Composer-Caches-Data).

**Note:** 
If a [Custom Range](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701116424973-Manage-Fields#Custom) has been defined for a field, the minimum and maximum fields used in filters remains unchanged by the action of refreshing the source data.

**Note:** 
You can force Composer to bypass and update the cache to query the underlying data source by selecting **Refresh** from a Composer dashboard menu.
