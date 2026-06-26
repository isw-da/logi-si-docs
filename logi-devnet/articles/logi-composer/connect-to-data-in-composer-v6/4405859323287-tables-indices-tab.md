---
title: "Tables/Indices Tab"
id: 4405859323287
section: "Connect to Data in Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405859323287-Tables-Indices-Tab
updated_at: 2021-09-21T01:28:17Z
---

# Tables/Indices Tab

# Tables/Indices Tab

![](https://devnet.logianalytics.com/hc/article_attachments/4406747425303/tables-tab_576x254.png)

Use the Tables or Indices tab in the data source configuration wizard to select the data table you want to use for this data source configuration. The name of this tab varies, depending on the data source you select.

![](https://devnet.logianalytics.com/hc/article_attachments/4406747382295/noteicon.jpg) You must be logged in as an administrator or as a user with the [group privilege](https://devnet.logianalytics.com/hc/en-us/articles/4405859114647-Group-Privilege-Reference)**Can Create new Data Sources** to see the Tables/Indices tab of the data source configuration wizard.

![](https://devnet.logianalytics.com/hc/article_attachments/4406747382295/noteicon.jpg) For flat file data connectors, the Connection tab is replaced with a Data tab and there is no Tables or Indices tab.

The structure and options on this tab vary by data source. The following general structure is used:

* In the left column of the tab, select a schema, index, table, or collection to use for the data source configuration. In some cases, you can select **All** to select all schemas for the configuration.
* In the upper half of the right column, a Field table shows you the fields you can select from the schema, index, table, or collection that should be used for the configuration.
* In the lower half of the right column, the Preview section shows a preview of the first ten records in the data you have selected.

Different options appear on this tab for different data sources types. The options include the following, but may not be available for every data source:

* **Custom SQL** — If you want to use specific fields from the table, you can write an SQL query to select them. If you select this option, the Field table in the upper half of the right column becomes an editing pane that you can use to write the SQL query.

  ![](https://devnet.logianalytics.com/hc/article_attachments/4406743739159/criticalicon.gif) Custom SQL queries are a powerful tool for performing complex data queries. However, be careful when creating custom SQL queries because it is easy to define a heavy query or a query that may overwhelm your database. Use this feature carefully.

  Variables (specified as custom user attributes) can be inserted in custom SQL. See [*Specify Custom User Attributes*](https://devnet.logianalytics.com/hc/en-us/articles/4405850862359-Specify-Custom-User-Attributes). In addition, you can use a vertical bar (|) in the SQL to separate the custom attribute name from a default value used for user definitions that do not have the custom user attribute defined. For example, the following custom SQL uses the value of the `state` customer user attribute to filter data source data for records from whatever state the user's `state` custom user attribute is set to. If a `state` custom user attribute is not defined for a user, a default of Alabama is used.

  ```
  SELECT * FROM Orders WHERE state = '${User.state|Alabama}'
  ```
* **Caching** — Use this switch to indicate whether Composer should cache the aggregated results of queries from this source. This controls both the visual cache (visual data) and the metadata cache (field statistics). See [*How Composer Caches Data*](https://devnet.logianalytics.com/hc/en-us/articles/4405859286935-How-Composer-Caches-Data).
* **Lookup Values** — If you are using Solr, Cloudera Search, or Elasticsearch data sources, you can use this switch to refresh the distinct values in the metadata store. Otherwise, the data source is queried directly each time.
* **Enable Filter by Type** — For Elasticsearch data sources, you can select this checkbox to filter the available indices by type. When you select this checkbox,
* **Request Handler** — For Cloudera Search and Solr data sources, you can use this box at the top of the Field table to specify a request handler plug-in that defines the logic used when executing a search request.

Select ![](https://devnet.logianalytics.com/hc/article_attachments/4406743833879/next-btn.png) to proceed to the [*Fields Tab*](https://devnet.logianalytics.com/hc/en-us/articles/4405851026455-Fields-Tab) in the data source configuration wizard. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4406743834135/back-btn.png) to return to the previous tab (either the [*Connection Tab*](https://devnet.logianalytics.com/hc/en-us/articles/4405851023767-Connection-Tab) or the [*General Tab*](https://devnet.logianalytics.com/hc/en-us/articles/4405859318039-General-Tab), depending on the privileges assigned to your user account and on the type of connection selected for the data source).
