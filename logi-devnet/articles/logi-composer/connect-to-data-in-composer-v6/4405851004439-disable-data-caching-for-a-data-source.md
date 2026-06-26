---
title: "Disable Data Caching for a Data Source"
id: 4405851004439
section: "Connect to Data in Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405851004439-Disable-Data-Caching-for-a-Data-Source
updated_at: 2021-09-21T01:27:59Z
---

# Disable Data Caching for a Data Source

# Disable Data Caching for a Data Source

The Composer data cache is a temporary storage area containing the aggregated data from your data sources. Two caches are supported: the visual (visual data) cache and the metadata (field statistics) cache. By default, caching is enabled for all data sources using both caches. However, you can disable all caching if your data source is constantly being updated, or you do not want to allocate the required RAM or if the performance of your data source is so high you do not need to store the aggregated queries.

To disable data caching:

1. Make sure you are logged in as a Composer administrator.
2. Select **Sources** on the [UI menu](https://devnet.logianalytics.com/hc/en-us/articles/4405859444119-The-Composer-UI-Menu) (![](https://devnet.logianalytics.com/hc/article_attachments/4406743720343/hamburger.png)). The [Data Sources](https://devnet.logianalytics.com/hc/en-us/articles/4405851037719-Sources-Page) page appears.
3. In the My Data Sources table on the [Data Sources](https://devnet.logianalytics.com/hc/en-us/articles/4405851037719-Sources-Page) page, locate and select the row displaying the data source configuration for which you want result set caching stopped.

   The data source configuration wizard starts.
4. Select the Tables or Indices tab. See [*Tables/Indices Tab*](https://devnet.logianalytics.com/hc/en-us/articles/4405859323287-Tables-Indices-Tab).
5. Turn the **Caching** switch OFF (to the left) at the bottom of the tab.
6. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4406743833239/save-white-btn.png) to save the data source configuration and close the wizard.

   Data caching in both caches is disabled for the data source configuration.  Data will be freshly loaded into the Composer cache the next time it is requested from the data source.
