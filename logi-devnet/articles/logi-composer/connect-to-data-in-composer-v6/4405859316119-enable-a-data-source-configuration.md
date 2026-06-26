---
title: "Enable a Data Source Configuration"
id: 4405859316119
section: "Connect to Data in Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405859316119-Enable-a-Data-Source-Configuration
updated_at: 2021-09-21T01:28:13Z
---

# Enable a Data Source Configuration

# Enable a Data Source Configuration

You can enable a data source configuration that was disabled in a previous version of Composer. Data source configurations must be enabled to be used for visuals.

![](https://devnet.logianalytics.com/hc/article_attachments/4406747382295/noteicon.jpg) Data source configurations can no longer be disabled. Once they are enabled, they cannot be disabled by anyone. You can control access to a data source configuration using data source [permissions](https://devnet.logianalytics.com/hc/en-us/articles/4405859328535-About-Data-Source-Permissions), [row](https://devnet.logianalytics.com/hc/en-us/articles/4405859333655-Restrict-Access-to-Data-Using-Row-Security) and [column](https://devnet.logianalytics.com/hc/en-us/articles/4405851034007-Restrict-Access-to-Fields-Using-Column-Security) data source restrictions, or by [deleting](https://devnet.logianalytics.com/hc/en-us/articles/4405859314967-Delete-a-Data-Source-Configuration) the data source from the system. The **Enabled** column on the Sources page was deprecated in Composer 6.9 and will be removed in a future release.

To enable a data source configuration:

1. Make sure you are logged in as a Composer administrator or a user who has been granted the **Can Administer Sources**[privilege](https://devnet.logianalytics.com/hc/en-us/articles/4405859114647-Group-Privilege-Reference) or a user with **Write** permission for the data source.
2. Select **Sources** on the [UI menu](https://devnet.logianalytics.com/hc/en-us/articles/4405859444119-The-Composer-UI-Menu) (![](https://devnet.logianalytics.com/hc/article_attachments/4406743720343/hamburger.png)) or the top-level navigation menu. The [Sources](https://devnet.logianalytics.com/hc/en-us/articles/4405851037719-Sources-Page) page appears.
3. In the table on the Sources page, locate the row displaying the data source configuration you want to enable.
4. Slide the switch in the **Enabled** column to the right for the configuration. The data source configuration is enabled.
