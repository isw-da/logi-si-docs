---
title: "How Composer Caches Data"
id: 4405859286935
section: "Connect to Data in Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405859286935-How-Composer-Caches-Data
updated_at: 2021-09-21T01:27:58Z
---

# How Composer Caches Data

# How Composer Caches Data

Composer uses a visual cache to enhance performance in scenarios where large numbers of users are concurrently viewing the same shared visuals. A metadata cache is also used to store field statistics.

Cached data is shared between users only if they have the same data access permissions and security context.

When caching is enabled, Composer does not requery the data source to obtain the data unless the cache is cleared or unless a refresh schedule is defined in the data source configuration. See [*Refresh Tab*](https://devnet.logianalytics.com/hc/en-us/articles/4405859322007-Refresh-Tab) and [*Trigger Refresh Jobs*](https://devnet.logianalytics.com/hc/en-us/articles/4405851159063-Trigger-Refresh-Jobs).

By default, data caching is enabled for all data sources.
The Composer cache stores all the results of aggregated requests from your data source. When a visual is created the request is first sent to the Composer cache. If the required results are found in the data cache, they are applied to your visual.

If the required results are not found in the Composer data cache, the data flow is as follows:

1. The request is sent to the Composer cache.
2. When the required results are *not* found in the Composer data cache, the request is sent to the data source.
3. The results from the data source are sent to the Composer data cache and stored there.
4. The visual displays the requested data.

Review the following links to learn how you can control Composer data caching.

* [*Clear the Cache for a Data Source Configuration*](https://devnet.logianalytics.com/hc/en-us/articles/4405859313815-Clear-the-Cache-for-a-Data-Source-Configuration)
* [*Disable Data Caching for a Data Source*](https://devnet.logianalytics.com/hc/en-us/articles/4405851004439-Disable-Data-Caching-for-a-Data-Source)
* [*Trigger Refresh Jobs*](https://devnet.logianalytics.com/hc/en-us/articles/4405851159063-Trigger-Refresh-Jobs)

![](https://devnet.logianalytics.com/hc/article_attachments/4406747382295/noteicon.jpg) You can force Composer to bypass the cache and to query the underlying data source by selecting **Refresh All** from a Composer dashboard menu.
