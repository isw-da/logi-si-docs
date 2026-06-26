---
title: "Clear the Cache for a Data Source Configuration"
id: 4405859313815
section: "Connect to Data in Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405859313815-Clear-the-Cache-for-a-Data-Source-Configuration
updated_at: 2021-09-21T01:28:14Z
---

# Clear the Cache for a Data Source Configuration

# Clear the Cache for a Data Source Configuration

You can manually clear the cache for a data source configuration if you are an administrator or a user granted the **Can Administer Sources**[privilege](https://devnet.logianalytics.com/hc/en-us/articles/4405859114647-Group-Privilege-Reference) or a user with **read**[permission](https://devnet.logianalytics.com/hc/en-us/articles/4405859328535-About-Data-Source-Permissions) for the data source. Both the visual (visual data) cache and the metadata (field statistics) cache are cleared.

To clear the cache for a data source configuration:

1. Make sure you are logged in as a Composer administrator or a user granted the **Can Administer Sources**[privilege](https://devnet.logianalytics.com/hc/en-us/articles/4405859114647-Group-Privilege-Reference), or a user with **read**[permission](https://devnet.logianalytics.com/hc/en-us/articles/4405859328535-About-Data-Source-Permissions) for the data source.
2. Select **Sources** on the [UI menu](https://devnet.logianalytics.com/hc/en-us/articles/4405859444119-The-Composer-UI-Menu) (![](https://devnet.logianalytics.com/hc/article_attachments/4406743720343/hamburger.png)) or the [top-level navigation menu](https://devnet.logianalytics.com/hc/en-us/articles/4405851152407-The-Top-Level-Navigation-Banner), or select the **Sources** box on the [Home page](https://devnet.logianalytics.com/hc/en-us/articles/4405851121559-Home-Page). The [Sources](https://devnet.logianalytics.com/hc/en-us/articles/4405851037719-Sources-Page) page appears.
3. In the table on the Sources page, locate the row displaying the data source configuration with the cache you want to clear.
4. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4406743809431/clear-cache-btn_30x31.png) in the **Clear Cache** column of the table.

   All caches are cleared for the data source configuration. Data is freshly loaded into the Composer cache the next time it is requested from the data source. For more information about data caching or to disable it, see [*How Composer Caches Data*](https://devnet.logianalytics.com/hc/en-us/articles/4405859286935-How-Composer-Caches-Data).

![](https://devnet.logianalytics.com/hc/article_attachments/4406747382295/noteicon.jpg) You can force Composer to bypass the visual cache and query the underlying data source by selecting **Refresh Data** on a Composer dashboard menu.
