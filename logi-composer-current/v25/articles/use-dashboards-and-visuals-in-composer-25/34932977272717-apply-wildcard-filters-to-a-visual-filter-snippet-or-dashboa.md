---
title: "Apply Wildcard Filters to a Visual, Filter Snippet, or Dashboard"
id: 34932977272717
section: "Use Dashboards and Visuals in Composer 25"
product: "Logi Composer v25"
url: https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932977272717-Apply-Wildcard-Filters-to-a-Visual-Filter-Snippet-or-Dashboard
updated_at: 2026-05-26T22:09:36Z
---

# Apply Wildcard Filters to a Visual, Filter Snippet, or Dashboard

# Apply Wildcard Filters to a Visual, Filter Snippet, or Dashboard

Wildcard filters are row-level filters you can use to filter the data on your dashboard visuals or filter snippets. Wildcard filters allow you to filter and analyze the data that matches specific combinations of character patterns.

**Note:** 
When working with multiple filter types on the same visual, row-level filters (including wildcard filters) are applied first to a visual, keyset filters are applied second, and group filters are applied last on the aggregated result set.

Many connectors support wildcard filters, but support for case-sensitivity in wildcard filters varies depending on the connector's data store.

Support for this feature by connector is shown in the following table.

**Key:****Y** - Supported; **N** - Not Supported; N/A - not applicable

| Connector | Supported? |
| --- | --- |
| [Amazon Redshift](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932733806989-Manage-the-Amazon-Redshift-Connector) | **Y** |
| [Amazon S3](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932743032461-Manage-the-Amazon-S3-Connector) | **Y** |
| [Apache Drill](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932734193677-Manage-the-Apache-Drill-Connector) | **Y** |
| [Apache Phoenix](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932743401869-Manage-the-Apache-Phoenix-Connector) | **Y** |
| [Apache Phoenix Query Server (QS)](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932743401869-Manage-the-Apache-Phoenix-Connector) | **Y** |
| [Apache Solr](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932743530125-Manage-the-Apache-Solr-Connector) | **Y** |
| [BigQuery](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932735000973-Manage-the-BigQuery-Connector) | **Y** |
| [Business Central Jet](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932747192973-Manage-the-Business-Central-Jet-Connector) | **Y** |
| [Cloudera Impala](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932744502541-Manage-the-Impala-Connector) | **Y** |
| [Cloudera Search](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932696536461-Manage-the-Cloudera-Search-Connector) | **Y** |
| [Couchbase](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932720313229-Manage-the-Couchbase-Connector) | **Y** |
| [Dremio](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932728091149-Manage-the-Dremio-Connector) | **Y** |
| [Elasticsearch 7.0](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932728155405-Manage-the-Elasticsearch-Connector) | **Y** |
| [Elasticsearch 8.0](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932728155405-Manage-the-Elasticsearch-Connector) | **Y** |
| [File Upload](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932721668365-Manage-File-Uploads) | **Y** |
| [HDFS](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932746629773-Manage-the-HDFS-Connector) | **Y** |
| [Hive](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932766095885-Manage-the-Hive-Connector) | **Y** |
| [Jira](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932766172941-Manage-the-Jira-Connector) | **Y** |
| [MemSQL](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932747006861-Manage-the-MemSQL-Connector) | **Y** |
| [Microsoft SQL Server](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932730176653-Manage-the-Microsoft-SQL-Server-Connector) | **Y** |
| [MongoDB](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932729901069-Manage-the-MongoDB-Connector) | **Y** |
| [MySQL](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932730297485-Manage-the-MySQL-Connector) | **Y** |
| [OpenSearch](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/37515138873485-Manage-the-OpenSearch-Connector) | **Y** |
| [Oracle](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932730448653-Manage-the-Oracle-Connector) | **Y** |
| [PostgreSQL](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932749503629-Manage-the-PostgreSQL-Connector) | **Y** |
| [Python](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932738470925-Manage-the-Python-Connector) | **Y** |
| [Real Time Sales](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932767352077-Manage-the-Real-Time-Sales-Demo-Source) | **Y** |
| [Salesforce](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932756901901-Manage-the-Salesforce-Connector) | **Y** |
| [SAP Hana](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932798573197-Manage-the-SAP-Hana-Connector) | **Y** |
| [SAP S/4HANA](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932767840781-Manage-the-SAP-S-4HANA-Connector) | **N** |
| [SAP IQ](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932757142925-Manage-the-SAP-IQ-Connector) | **Y** |
| [Spark SQL](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932799029901-Manage-the-Spark-SQL-Connector) | **Y** |
| [Snowflake](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932757334669-Manage-the-Snowflake-Connector) | **Y** |
| [Teradata](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932773152781-Manage-the-Teradata-Connector) | **Y** |
| [TIBCO DV](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932768245901-Manage-the-TIBCO-Data-Virtualization-TDV-Connector) | **Y** |
| [Trino](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932773334285-Manage-the-Trino-Connector) | **Y** |
| [File Upload (Upload API)](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932721668365-Manage-File-Uploads) | **Y** |
| [Vertica](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932768403725-Manage-the-Vertica-Connector) | **Y** |

See [Wildcard Case-Insensitive Filters](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932723779981-Wildcard-Case-Insensitive-Filters) and [Wildcard Case-Sensitive Filters](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932692417677-Wildcard-Case-Sensitive-Filters) to determine whether case-insensitive or case-sensitive wildcards are supported.

**Apply a wildcard filter**

1. Select the filter icon on the [visual](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932931145741-Apply-a-Row-Level-Filter-to-a-Visual-or-Filter-Snippet), filter snippet, or [dashboard](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932922987533-Apply-a-Row-Level-Filter-to-a-Dashboard) to access the appropriate filter sidebar.

   * To access the filter sidebar, select its filter icon ![](https://logi-composer-v25.insightsoftware.com/hc/article_attachments/46167913774989) or select **Settings** from the [menu](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933290868621-Use-the-Visual-Menu)![](https://logi-composer-v25.insightsoftware.com/hc/article_attachments/46167868978317) and then select ![](https://logi-composer-v25.insightsoftware.com/hc/article_attachments/46167913776397) on the [sidebar menu](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933295031181-Use-the-Visual-Sidebar-Menu).
   * To access the dashboard filter sidebar, select its filter icon ![](https://logi-composer-v25.insightsoftware.com/hc/article_attachments/46167913777165). The dashboard-level filter icon is available only when all the visuals are from the same data source.

   The Filters sidebar appears showing any filters that have been applied.
2. Select the Row tab. If the style of your visual is an arc gauge, KPI chart, table (raw data), histogram, or map markers chart, the Group tab is available, but you cannot create a group filter because all filters for these visual styles are row-level filters. If you are using the dashboard filters sidebar, the Group tab is not available.

   The Saved tab shows saved filters that you can apply to a dashboard, visual, or filter snippet. See [Maintain Saved Filters](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932976956941-Maintain-Saved-Filters).
3. On the Row tab, select the filter attribute you want to use from the list of available attributes. A second page with three tabs appears in the Filters sidebar.

   * The Value tab allows you to select a filter value for the attribute. See [Apply Row-Level Filters](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932930630157-Apply-Row-Level-Filters) for instructions on using a regular row-level filter.
   * The Wildcard tab allows you to specify a wildcard filter for the attribute. Continue following the steps in these instructions.
   * The Keyset tab allows you to select a keyset filter for the attribute. See [Use Keysets](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933047406605-Use-Keysets) for instructions on using keysets in a filter.

   You can also select the add icon ![add icon](https://logi-composer-v25.insightsoftware.com/hc/article_attachments/46167868980749 "add icon") to access the [Derived Field Editor](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932882620813-Derived-Field-Editor) or the [Custom Metrics Editor](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932820475405-Custom-Metrics-Editor) to create or modify derived fields and custom metrics to be used as filters. See [Access the Derived Field Editor from the Filters Sidebar](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932881853581-Access-the-Derived-Field-Editor-from-the-Filters-Sidebar) and [Access the Custom Metrics Editor from the Filters Sidebar](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932813600525-Access-the-Custom-Metrics-Editor-from-the-Filters-Sidebar).
4. Select the Wildcard tab to create a row-level wildcard filter.
5. Select an operator from the drop-down menu for the **Operator** box on the **Wildcard** tab.

   | Operator | Data is included in the visual... |
   | --- | --- |
   | Contains | When the data in the filter attribute you selected contains the wildcard string you will specify in the next step. |
   | Does Not Contain | When the data in the filter attribute you selected does *not* contain the wildcard string you will specify in the next step. |
   | Begins With | When the data in the filter attribute you selected begins with the wildcard string you will specify in the next step. |
   | Does Not Begin With | When the data in the filter attribute you selected does **not** begin with the wildcard string you will specify in the next step. |
   | Ends With | When the data in the filter attribute you selected ends with the wildcard string you will specify in the next step. |
   | Does Not End With | When the data in the filter attribute you selected does **not** end with the wildcard string you will specify in the next step. |
6. In the **Value** box, type a string of characters that represents the wildcard string for the filter. Data is included in the visual when the data in the filter field meets the condition set by this operator and the wildcard string you specify.
7. By default the **Case Sensitive** slider is on (selected). When this option is selected, the wildcard filter includes data in the visual only if the filter attribute data exactly matches both the value of the wildcard string and the case of the wildcard string value. Slide the option off if you do not care if the visual data exactly matches the case of the wildcard string.
8. If you want to specify another wildcard value, select the add icon ![add icon](https://logi-composer-v25.insightsoftware.com/hc/article_attachments/46167868980749 "add icon") next to the **Values** title on the Wildcard tab. Then repeat Steps 5-7 above for the new wildcard value. Multiple wildcard values are treated as OR operations. A record can meet the filter criteria specified by any of the wildcard values to be selected for filter processing.
9. Select **Apply**. If you create the filter at the dashboard level, it is applied to all the visuals in the dashboard. Otherwise, it is applied only to the selected (active) visual.
10. Optionally, repeat these steps to apply additional filters to the visual or dashboard.

See [Remove a Filter from a Visual, Filter Snippet or Dashboard](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932940279949-Remove-a-Filter-from-a-Visual-Filter-Snippet-or-Dashboard) for information on removing a wildcard filter from a visual or dashboard.
