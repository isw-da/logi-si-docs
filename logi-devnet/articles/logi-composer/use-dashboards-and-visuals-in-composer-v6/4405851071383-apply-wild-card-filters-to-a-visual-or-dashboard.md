---
title: "Apply Wild Card Filters to a Visual or Dashboard"
id: 4405851071383
section: "Use Dashboards and Visuals in Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405851071383-Apply-Wild-Card-Filters-to-a-Visual-or-Dashboard
updated_at: 2021-09-21T01:28:40Z
---

# Apply Wild Card Filters to a Visual or Dashboard

# Apply Wild Card Filters to a Visual or Dashboard

Wild card filters are row-level filters you can use to filter the data on your dashboard visuals. Wild card filters allow you to filter and analyze the data in a visual that matches specific combinations of character patterns.

![](https://devnet.logianalytics.com/hc/article_attachments/4406747382295/noteicon.jpg) When working with multiple filter types on the same visual, row-level filters (including wild card filters) are applied first to a visual, keyset filters are applied second, and group filters are applied last on the aggregated result set.

Many Composer connectors support wild card filters, but support for case-sensitivity in wild card filters varies depending on the connector's data store.

Support for this feature by Composer connectors is shown in the following table.

**Key:****Y** - Supported; **N** - Not Supported; N/A - not applicable

| Connector | Supported? | | |
| --- | --- | --- | --- |
| [Amazon Redshift](https://devnet.logianalytics.com/hc/en-us/articles/4405859198103-Manage-the-Amazon-Redshift-Connector) | **Y** | | |
| [Amazon S3](https://devnet.logianalytics.com/hc/en-us/articles/4405850929943-Manage-the-Amazon-S3-Connector) | **Y** | | |
| [Apache Drill](https://devnet.logianalytics.com/hc/en-us/articles/4405850930839-Manage-the-Apache-Drill-Connector) | **Y** | | |
| [Apache Phoenix](https://devnet.logianalytics.com/hc/en-us/articles/4405859202839-Manage-the-Apache-Phoenix-Connector) | **Y** | | |
| [Apache Phoenix Query Server (QS)](https://devnet.logianalytics.com/hc/en-us/articles/4405859202839-Manage-the-Apache-Phoenix-Connector) | **Y** | | |
| [Apache Solr](https://devnet.logianalytics.com/hc/en-us/articles/4405850931735-Manage-the-Apache-Solr-Connector) | **Y** | | |
| [BigQuery](https://devnet.logianalytics.com/hc/en-us/articles/4405859214231-Manage-the-BigQuery-Connector) | **Y** | | |
| [Cloudera Impala](https://devnet.logianalytics.com/hc/en-us/articles/4405850938647-Manage-the-Impala-Connector) | **Y** | | |
| [Cloudera Search](https://devnet.logianalytics.com/hc/en-us/articles/4405859219863-Manage-the-Cloudera-Search-Connector) | **Y** | | |
| [Couchbase](https://devnet.logianalytics.com/hc/en-us/articles/4405859220887-Manage-the-Couchbase-Connector) | **Y** | | |
| [Dremio](https://devnet.logianalytics.com/hc/en-us/articles/4405859221911-Manage-the-Dremio-Connector) | **Y** | | |
| [Elasticsearch 6.0](https://devnet.logianalytics.com/hc/en-us/articles/4405850940439-Manage-the-Elasticsearch-Connector) | **Y** | | |
| [Elasticsearch 7.0](https://devnet.logianalytics.com/hc/en-us/articles/4405850940439-Manage-the-Elasticsearch-Connector) | **Y** | | |
| [Flat File](https://devnet.logianalytics.com/hc/en-us/articles/4405850954647-Upload-a-Flat-File-into-Composer) | **Y** | | |
| [HDFS](https://devnet.logianalytics.com/hc/en-us/articles/4405859226903-Manage-the-HDFS-Connector) | **Y** | | |
| [Hive](https://devnet.logianalytics.com/hc/en-us/articles/4405850956695-Manage-the-Hive-Connector) | **Y** | | |
| [MemSQL](https://devnet.logianalytics.com/hc/en-us/articles/4405859228567-Manage-the-MemSQL-Connector) | **Y** | | |
| [Microsoft SQL Server](https://devnet.logianalytics.com/hc/en-us/articles/4405859229975-Manage-the-Microsoft-SQL-Server-Connector) | **Y** | | |
| [MongoDB](https://devnet.logianalytics.com/hc/en-us/articles/4405850957591-Manage-the-MongoDB-Connector) | **Y** | | |
| [MySQL](https://devnet.logianalytics.com/hc/en-us/articles/4405850958487-Manage-the-MySQL-Connector) | **Y** | | |
| [Oracle](https://devnet.logianalytics.com/hc/en-us/articles/4405850959383-Manage-the-Oracle-Connector) | **Y** | | |
| [PostgreSQL](https://devnet.logianalytics.com/hc/en-us/articles/4405850960279-Manage-the-PostgreSQL-Connector) | **Y** | | |
| [Presto](https://devnet.logianalytics.com/hc/en-us/articles/4405859231639-Manage-the-Presto-Connector) | **Y** | | |
| [Real Time Sales](https://devnet.logianalytics.com/hc/en-us/articles/4405850962071-Manage-the-Real-Time-Sales-Demo-Source) | **Y** | | |
| [SAP Hana](https://devnet.logianalytics.com/hc/en-us/articles/4405859232791-Manage-the-SAP-Hana-Connector) | **Y** | | |
| [SAP IQ](https://devnet.logianalytics.com/hc/en-us/articles/4405850963095-Manage-the-SAP-IQ-Connector) | **Y** | | |
| [Snowflake](https://devnet.logianalytics.com/hc/en-us/articles/4405859234199-Manage-the-Snowflake-Connector) | **Y** | | |
| [Spark SQL](https://devnet.logianalytics.com/hc/en-us/articles/4405850963991-Manage-the-Spark-SQL-Connector) | **Y** | | |
| [Teradata](https://devnet.logianalytics.com/hc/en-us/articles/4405859235607-Manage-the-Teradata-Connector) | **Y** | | |
| [TIBCO DV](https://devnet.logianalytics.com/hc/en-us/articles/4405850965783-Manage-the-TIBCO-Data-Virtualization-TDV-Connector) | **Y** | | |
| [Upload API](https://devnet.logianalytics.com/hc/en-us/articles/4405859140247-Use-the-Upload-API) | **Y** | | |
| [Vertica](https://devnet.logianalytics.com/hc/en-us/articles/4405850966679-Manage-the-Vertica-Connector) | **Y** | | |

See [*Wild Card Case-Insensitive Filters*](https://devnet.logianalytics.com/hc/en-us/articles/4405850916887-Wild-Card-Case-Insensitive-Filters) and [*Wild Card Case-Sensitive Filters*](https://devnet.logianalytics.com/hc/en-us/articles/4405850917783-Wild-Card-Case-Sensitive-Filters) to determine whether case-insensitive or case-sensitive wild cards are supported.

To apply a wild card filter to a visual or dashboard:

1. Select the filter icon on the [visual](https://devnet.logianalytics.com/hc/en-us/articles/4405851057431-Apply-a-Row-Level-Filter-to-a-Visual) or [dashboard](https://devnet.logianalytics.com/hc/en-us/articles/4405851056535-Apply-a-Row-Level-Filter-to-a-Dashboard) to access the appropriate filter sidebar.

   * To access the visual filter sidebar, select its filter icon (![](https://devnet.logianalytics.com/hc/article_attachments/4406743754263/filter-vis.png)) or select **Edit Visual** from the [visual menu](https://devnet.logianalytics.com/hc/en-us/articles/4405851254295-Use-the-Visual-Menu) (![](https://devnet.logianalytics.com/hc/article_attachments/4406743718551/three-dots-menu_19x11.png)) and then select ![](https://devnet.logianalytics.com/hc/article_attachments/4406743782935/sidebar-filter_20x21.png) on the [sidebar menu](https://devnet.logianalytics.com/hc/en-us/articles/4405859578391-Use-the-Visual-Sidebar-Menu).
   * To access the dashboard filter sidebar, select its filter icon (![](https://devnet.logianalytics.com/hc/article_attachments/4406743718807/filter-dash.png)). The dashboard-level filter icon is available only when all the visuals are from the same data source.

   The Filters sidebar appears showing any filters that have been applied.
2. Select the Row tab. If the style of your visual is an arc gauge, KPI chart, table (raw data), histogram, or map markers chart, the Group tab is available, but you cannot create a group filter because all filters for these visual styles are row-level filters. If you are using the dashboard filters sidebar, the Group tab is not available.

   The Saved tab shows saved filters that you can apply to a dashboard or visual. See [*Maintain Saved Filters*](https://devnet.logianalytics.com/hc/en-us/articles/4405851070359-Maintain-Saved-Filters).
3. On the Row tab, select the filter attribute you want to use from the list of available attributes. A second page with three tabs appears in the Filters sidebar.

   * The Value tab allows you to select a filter value for the attribute. See [*Apply Row-Level Filters*](https://devnet.logianalytics.com/hc/en-us/articles/4405851055639-Apply-Row-Level-Filters) for instructions on using a regular row-level filter.
   * The Wildcard tab allows you to specify a wild card filter for the attribute. Continue following the steps in these instructions.
   * The Keyset tab allows you to select a keyset filter for the attribute. See [*Use Keysets*](https://devnet.logianalytics.com/hc/en-us/articles/4405859392151-Use-Keysets) for instructions on using keysets in a filter.

   You can also select ![](https://devnet.logianalytics.com/hc/article_attachments/4406743717271/add.png) to access the [*Derived Field Editor*](https://devnet.logianalytics.com/hc/en-us/articles/4405851014551-Derived-Field-Editor) or the [*Custom Metrics Editor*](https://devnet.logianalytics.com/hc/en-us/articles/4405859284119-Custom-Metrics-Editor) to create or modify derived fields and custom metrics to be used as filters. See [*Access the Derived Field Editor from the Filters Sidebar*](https://devnet.logianalytics.com/hc/en-us/articles/4405859296663-Access-the-Derived-Field-Editor-from-the-Filters-Sidebar) and [*Access the Custom Metrics Editor from the Filters Sidebar*](https://devnet.logianalytics.com/hc/en-us/articles/4405851000727-Access-the-Custom-Metrics-Editor-from-the-Filters-Sidebar).
4. Select the Wildcard tab to create a row-level wild card filter.
5. Select an operator from the drop-down menu for the **Operator** box on the **Wildcard** tab.

   | Operator | Data is included in the visual... |
   | --- | --- |
   | Contains | When the data in the filter attribute you selected contains the wild card string you will specify in the next step. |
   | Does Not Contain | When the data in the filter attribute you selected does *not* contain the wild card string you will specify in the next step. |
   | Begins With | When the data in the filter attribute you selected begins with the wild card string you will specify in the next step. |
   | Does Not Begin With | When the data in the filter attribute you selected does **not** begin with the wild card string you will specify in the next step. |
   | Ends With | When the data in the filter attribute you selected ends with the wild card string you will specify in the next step. |
   | Does Not End With | When the data in the filter attribute you selected does **not** end with the wild card string you will specify in the next step. |
6. In the **Value** box, type a string of characters that represents the wild card string for the filter. Data is included in the visual when the data in the filter field meets the condition set by this operator and the wild card string you specify.
7. By default the **Case Sensitive** slider is on (selected). When this option is selected, the wild card filter includes data in the visual only if the filter attribute data exactly matches both the value of the wild card string and the case of the wild card string value. Slide the option off if you do not care if the visual data exactly matches the case of the wild card string.
8. If you want to specify another wild card value, select ![](https://devnet.logianalytics.com/hc/article_attachments/4406743717271/add.png) next to the **Values** title on the Wildcard tab. Then repeat Steps 5-7 above for the new wild card value. Multiple wild card values are treated as OR operations. A record can meet the filter criteria specified by any of the wildcard values to be selected for filter processing.
9. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4406743795351/apply1-btn_48x27.png). If you create the filter at the dashboard level, it is applied to all the visuals in the dashboard. Otherwise, it is applied only to the selected (active) visual.
10. Optionally, repeat these steps to apply additional filters to the visual or dashboard.

See [*Remove a Filter from a Visual or Dashboard*](https://devnet.logianalytics.com/hc/en-us/articles/4405851061911-Remove-a-Filter-from-a-Visual-or-Dashboard) for information on removing a wild card filter from a visual or dashboard.
