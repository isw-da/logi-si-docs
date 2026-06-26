---
title: "How Composer Caches Data"
id: 43701078034061
section: "Connect to Data in Composer 26"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701078034061-How-Composer-Caches-Data
updated_at: 2026-05-29T14:11:10Z
---

# How Composer Caches Data

# How Composer Caches Data

Composer uses a visual cache to enhance performance in scenarios where large numbers of users are concurrently viewing the same shared visuals. A metadata cache is also used to store field statistics. This cached data is shared between users only if they have the same data access permissions and security context.

Caching is enabled by default for all data sources. Composer does not re-query the data source for data unless you manually clear the cache, or define a refresh schedule. See [Cache Tab](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701085337997-Cache-Tab) and [Trigger Refresh Jobs](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701192120205-Trigger-Refresh-Jobs).

Available cache settings and options include:

* **Data Cache**: Composer caches query results and common cached data for multiple visuals that use this source. When you create a visual that uses this source, the first data request is sent to the Composer cache. Composer returns the cached data, if available.

  If the data is not available in the cache, Composer next queries the data source. The results are returned and stored in the cache, and the visual displays the returned data.
* **Statistics Cache**: When enabled, field metadata, such as minimum, maximum, and distinct values numbers are cached. This toggle also controls the availability of the Field Statistics Configuration option and scheduled refresh settings.
* **Field Statistics Configuration**: When enabled, you can enable or disable caching and scheduling for individual fields, or manually refresh the cached data for individual fields. Fields that include a statistics override that prevents refreshing are indicated by an exclamation point in a triangle.

![](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46243239400077)

* **Schedule Refresh Settings**: Enable and define Periodic or Advanced refreshing of fields with **Schedule Refresh** enabled. If you disable Schedule Refresh Settings, any schedule you had set up previously is deleted.

**Note:** 
If a [Custom Range](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701116424973-Manage-Fields#Custom) has been defined for a field, the minimum and maximum fields used in filters remain unchanged when you refresh source data. These fields are shown with cache actions disabled on the [Cache tab](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701085337997-Cache-Tab).

You can refresh the entire data source, all the fields in a data source, or select fields in a data source. For more information, see:

* [Clear the Cache for a Data Source Configuration](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701080340493-Clear-the-Cache-for-a-Data-Source-Configuration)
* [Disable Data Caching for a Data Source](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701077994381-Disable-Data-Caching-for-a-Data-Source)
* [Trigger Refresh Jobs](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701192120205-Trigger-Refresh-Jobs)

**Note:** 
You can force Composer to bypass the cache and to query the underlying data source by selecting **Refresh All** from a Composer dashboard menu.
