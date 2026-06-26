---
title: "Configure Search Box Defaults"
id: 4405851028503
section: "Connect to Data in Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405851028503-Configure-Search-Box-Defaults
updated_at: 2021-09-21T01:28:17Z
---

# Configure Search Box Defaults

# Configure Search Box Defaults

The search box is available for [Apache Solr](https://devnet.logianalytics.com/hc/en-us/articles/4405850931735-Manage-the-Apache-Solr-Connector), [Cloudera Search](https://devnet.logianalytics.com/hc/en-us/articles/4405859219863-Manage-the-Cloudera-Search-Connector), and [Elasticsearch](https://devnet.logianalytics.com/hc/en-us/articles/4405850940439-Manage-the-Elasticsearch-Connector) data sources and is enabled by default for visuals created using these sources. It allows you to enter keywords to quickly filter the data. You can disable the search box, if needed, in the data source configuration.

## Disable the Search Box

To disable the search box:

1. Make sure you are logged in as a Composer administrator or as a user assigned to a group that can edit data source configurations.
2. Select **Sources** on the [UI menu](https://devnet.logianalytics.com/hc/en-us/articles/4405859444119-The-Composer-UI-Menu) (![](https://devnet.logianalytics.com/hc/article_attachments/4406743720343/hamburger.png)) or the [top-level navigation menu](https://devnet.logianalytics.com/hc/en-us/articles/4405851152407-The-Top-Level-Navigation-Banner), or select the **Sources** box on the [Home page](https://devnet.logianalytics.com/hc/en-us/articles/4405851121559-Home-Page). The [Sources](https://devnet.logianalytics.com/hc/en-us/articles/4405851037719-Sources-Page) page appears.
3. In the table on the Sources page, locate and select the data source configuration you want to edit. Make sure you select a data source that supports the Search feature (see above). The data source configuration wizard appears.
4. Select the [Visuals tab](https://devnet.logianalytics.com/hc/en-us/articles/4405859325591-Visuals-Tab) in the data source configuration wizard.
5. Select the **Global Default Settings** bar on the [Visuals tab](https://devnet.logianalytics.com/hc/en-us/articles/4405859325591-Visuals-Tab), if it is not already selected.
6. Select **Disable** in the **Search Feature** box on the tab.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4406743834647/search-feature_217x52.png)

   ![](https://devnet.logianalytics.com/hc/article_attachments/4406747382295/noteicon.jpg) The availability of this setting depends on the data source you have selected. The Search feature is available for [Apache Solr](https://devnet.logianalytics.com/hc/en-us/articles/4405850931735-Manage-the-Apache-Solr-Connector), [Cloudera Search](https://devnet.logianalytics.com/hc/en-us/articles/4405859219863-Manage-the-Cloudera-Search-Connector), and [Elasticsearch](https://devnet.logianalytics.com/hc/en-us/articles/4405850940439-Manage-the-Elasticsearch-Connector) data sources.
7. When your changes are complete, select ![](https://devnet.logianalytics.com/hc/article_attachments/4406743760663/save-white-btn_43x25.png), ![](https://devnet.logianalytics.com/hc/article_attachments/4406743761431/save-next-btn_82x25.png), or ![](https://devnet.logianalytics.com/hc/article_attachments/4406743731095/finish-btn_42x22.png) (depending on the tab) to save the data source configuration and close the wizard.

## Enable the Search Box

To enable the search box:

1. Make sure you are logged in as a Composer administrator or as a user assigned to a group that can edit data source configurations.
2. Select **Sources** on the [UI menu](https://devnet.logianalytics.com/hc/en-us/articles/4405859444119-The-Composer-UI-Menu) (![](https://devnet.logianalytics.com/hc/article_attachments/4406743720343/hamburger.png)) or the top-level navigation menu. The [Sources](https://devnet.logianalytics.com/hc/en-us/articles/4405851037719-Sources-Page) page appears.
3. In the table on the Sources page, locate and select the data source configuration you want to edit. Make sure you select a data source that supports the Search feature (see above). The data source configuration wizard appears.
4. Select the [Visuals tab](https://devnet.logianalytics.com/hc/en-us/articles/4405859325591-Visuals-Tab) in the data source configuration wizard.
5. Select the **Global Default Settings** bar on the [Visuals tab](https://devnet.logianalytics.com/hc/en-us/articles/4405859325591-Visuals-Tab), if it is not already selected. The search box settings appears with the time bar settings on the right side of the tab.
6. Select **Enable** in the **Search Feature** box on the tab.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4406743834647/search-feature_217x52.png)

   ![](https://devnet.logianalytics.com/hc/article_attachments/4406747382295/noteicon.jpg) The availability of this setting depends on the data source you have selected. The Search feature is available for [Apache Solr](https://devnet.logianalytics.com/hc/en-us/articles/4405850931735-Manage-the-Apache-Solr-Connector), [Cloudera Search](https://devnet.logianalytics.com/hc/en-us/articles/4405859219863-Manage-the-Cloudera-Search-Connector), and [Elasticsearch](https://devnet.logianalytics.com/hc/en-us/articles/4405850940439-Manage-the-Elasticsearch-Connector) data sources.
7. When your changes are complete, select ![](https://devnet.logianalytics.com/hc/article_attachments/4406743833239/save-white-btn.png), ![](https://devnet.logianalytics.com/hc/article_attachments/4406743834903/save-next-btn.png), or ![](https://devnet.logianalytics.com/hc/article_attachments/4406743835287/finish-btn.png) (depending on the tab) to save the data source configuration and close the wizard.
