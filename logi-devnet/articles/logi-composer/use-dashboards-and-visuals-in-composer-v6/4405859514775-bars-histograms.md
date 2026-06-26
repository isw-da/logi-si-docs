---
title: "Bars: Histograms"
id: 4405859514775
section: "Use Dashboards and Visuals in Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405859514775-Bars-Histograms
updated_at: 2021-09-21T01:30:00Z
---

# Bars: Histograms

# Bars: Histograms

Histograms require only one metric (number or integer). The metric data range is divided into intervals and the metric values that fall within each interval are counted. The histogram plots the value counts (Volume) against the metric intervals.

Histograms are supported only by data sources that use Composer [connectors](https://devnet.logianalytics.com/hc/en-us/articles/4405859436055-Composer-Data-Connector-Reference) that support the calculations necessary for histogram visuals with integer values.

Support for this feature by Composer connectors is shown in the following table.

**Key:****Y** - Supported; **N** - Not Supported; N/A - not applicable

| Connector | Supported? | |
| --- | --- | --- |
| [Amazon Redshift](https://devnet.logianalytics.com/hc/en-us/articles/4405859198103-Manage-the-Amazon-Redshift-Connector) | **Y** | |
| [Amazon S3](https://devnet.logianalytics.com/hc/en-us/articles/4405850929943-Manage-the-Amazon-S3-Connector) | **Y** | |
| [Apache Drill](https://devnet.logianalytics.com/hc/en-us/articles/4405850930839-Manage-the-Apache-Drill-Connector) | **Y** | |
| [Apache Phoenix](https://devnet.logianalytics.com/hc/en-us/articles/4405859202839-Manage-the-Apache-Phoenix-Connector) | **Y** | |
| [Apache Phoenix Query Server (QS)](https://devnet.logianalytics.com/hc/en-us/articles/4405859202839-Manage-the-Apache-Phoenix-Connector) | **Y** | |
| [Apache Solr](https://devnet.logianalytics.com/hc/en-us/articles/4405850931735-Manage-the-Apache-Solr-Connector) | **Y** | |
| [BigQuery](https://devnet.logianalytics.com/hc/en-us/articles/4405859214231-Manage-the-BigQuery-Connector) | **Y** | |
| [Cloudera Impala](https://devnet.logianalytics.com/hc/en-us/articles/4405850938647-Manage-the-Impala-Connector) | **Y** | |
| [Cloudera Search](https://devnet.logianalytics.com/hc/en-us/articles/4405859219863-Manage-the-Cloudera-Search-Connector) | **N** | |
| [Couchbase](https://devnet.logianalytics.com/hc/en-us/articles/4405859220887-Manage-the-Couchbase-Connector) | **Y** | |
| [Dremio](https://devnet.logianalytics.com/hc/en-us/articles/4405859221911-Manage-the-Dremio-Connector) | **Y** | |
| [Elasticsearch 6.0](https://devnet.logianalytics.com/hc/en-us/articles/4405850940439-Manage-the-Elasticsearch-Connector) | **Y** | |
| [Elasticsearch 7.0](https://devnet.logianalytics.com/hc/en-us/articles/4405850940439-Manage-the-Elasticsearch-Connector) | **Y** | |
| [Flat File](https://devnet.logianalytics.com/hc/en-us/articles/4405850954647-Upload-a-Flat-File-into-Composer) | **Y** | |
| [HDFS](https://devnet.logianalytics.com/hc/en-us/articles/4405859226903-Manage-the-HDFS-Connector) | **Y** | |
| [Hive](https://devnet.logianalytics.com/hc/en-us/articles/4405850956695-Manage-the-Hive-Connector) | **Y** | |
| [MemSQL](https://devnet.logianalytics.com/hc/en-us/articles/4405859228567-Manage-the-MemSQL-Connector) | **Y** | |
| [Microsoft SQL Server](https://devnet.logianalytics.com/hc/en-us/articles/4405859229975-Manage-the-Microsoft-SQL-Server-Connector) | **Y** | |
| [MongoDB](https://devnet.logianalytics.com/hc/en-us/articles/4405850957591-Manage-the-MongoDB-Connector) | **N** | |
| [MySQL](https://devnet.logianalytics.com/hc/en-us/articles/4405850958487-Manage-the-MySQL-Connector) | **Y** | |
| [Oracle](https://devnet.logianalytics.com/hc/en-us/articles/4405850959383-Manage-the-Oracle-Connector) | **Y** | |
| [PostgreSQL](https://devnet.logianalytics.com/hc/en-us/articles/4405850960279-Manage-the-PostgreSQL-Connector) | **Y** | |
| [Presto](https://devnet.logianalytics.com/hc/en-us/articles/4405859231639-Manage-the-Presto-Connector) | **Y** | |
| [Real Time Sales](https://devnet.logianalytics.com/hc/en-us/articles/4405850962071-Manage-the-Real-Time-Sales-Demo-Source) | **Y** | |
| [SAP Hana](https://devnet.logianalytics.com/hc/en-us/articles/4405859232791-Manage-the-SAP-Hana-Connector) | **Y** | |
| [SAP IQ](https://devnet.logianalytics.com/hc/en-us/articles/4405850963095-Manage-the-SAP-IQ-Connector) | **Y** | |
| [Snowflake](https://devnet.logianalytics.com/hc/en-us/articles/4405859234199-Manage-the-Snowflake-Connector) | **Y** | |
| [Spark SQL](https://devnet.logianalytics.com/hc/en-us/articles/4405850963991-Manage-the-Spark-SQL-Connector) | **Y** | |
| [Teradata](https://devnet.logianalytics.com/hc/en-us/articles/4405859235607-Manage-the-Teradata-Connector) | **Y** | |
| [TIBCO DV](https://devnet.logianalytics.com/hc/en-us/articles/4405850965783-Manage-the-TIBCO-Data-Virtualization-TDV-Connector) | **Y** | |
| [Upload API](https://devnet.logianalytics.com/hc/en-us/articles/4405859140247-Use-the-Upload-API) | **Y** | |
| [Vertica](https://devnet.logianalytics.com/hc/en-us/articles/4405850966679-Manage-the-Vertica-Connector) | **Y** | |

Data from Fusion data sources can be used in histograms.

This topic describes:

* [*Configure Default Histogram Settings for a Data Source*](#Configur)
* [*Configure Settings for a Specific Histogram*](#Configur3)
* [*Configure Colors for a Specific Histogram*](#Configur2)

## Configure Default Histogram Settings for a Data Source

To configure default histogram settings for a data source configuration:

1. Edit the appropriate data source configuration. See [*Edit a Data Source Configuration*](https://devnet.logianalytics.com/hc/en-us/articles/4405851024663-Edit-a-Data-Source-Configuration).
2. Select the [Visuals](https://devnet.logianalytics.com/hc/en-us/articles/4405859325591-Visuals-Tab) tab in the data source configuration wizard.
3. On the **Standard** subtab of the [Visuals](https://devnet.logianalytics.com/hc/en-us/articles/4405859325591-Visuals-Tab) tab, select **Bars: Histogram**.

   If you want to be able to display the data collected by this data source configuration as a histogram, make sure the **Bars:Histogram** checkbox is selected.

   Default histogram settings appear on the right side of the page.
4. Configure the default settings as follows:

   | Setting | Description |
   | --- | --- |
   | Group By | Select the attribute by which the data should be grouped. |
   | Number of bars | Specify the number of bars:  * **Auto** - if you select this option, the bins for all your data set will be built and corresponding bars will be displayed. * **Limit to** - specify the maximum number of bars to be displayed on your visual. * **Bar interval** - specify the bar interval for your visual. |
   | Axis values | Specify the types of values to be shown on the visual:  * **Absolute** - select this option if you want to see the exact values. * **Relative** - select this option if you want to see the values in %. |
   | Show Cumulative Line | Select this checkbox if you want the cumulative line to be displayed on your visual. |
   | Cumulative Line Color | Select the color for the cumulative line on your visual. |
   | Bins Color | Select the color for the bins on the visual. |
5. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4406747382679/save-white-btn_40x23.png).

## Configure Settings for a Specific Histogram

To change the settings for a specific histogram:

1. Edit the histogram you want to modify. See [*Edit Visuals*](https://devnet.logianalytics.com/hc/en-us/articles/4405859570839-Edit-Visuals).
2. If you are editing the visual in a dashboard, select **Edit Visual** from the [visual drop-down menu](https://devnet.logianalytics.com/hc/en-us/articles/4405851254295-Use-the-Visual-Menu). The [sidebar menu](https://devnet.logianalytics.com/hc/en-us/articles/4405859578391-Use-the-Visual-Sidebar-Menu) for the visual appears.

   If you are editing the visual from the Visual Gallery, the sidebar appears to the right of the visual.
3. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4406747383319/sidebar-chtsettings.png) on the [sidebar menu](https://devnet.logianalytics.com/hc/en-us/articles/4405859578391-Use-the-Visual-Sidebar-Menu). The Histogram Settings sidebar for the visual appears.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4406747393175/bar-histogram-settings_192x312.png)
4. Alter the settings as needed:

   | Setting | Description |
   | --- | --- |
   | Number of Bars | Specify the number of bars:  * **Auto** - if you select this option, the bins for all your data set will be built and corresponding bars will be displayed. * **Limit to** - specify the maximum number of bars to be displayed on your visual. * **Bar interval** - specify the bar interval for your visual. |
   | Labels | Slide the **Append Absolute Values**, and **Append Relative Values** sliders on (to the right) to enable these label options. |
5. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4406743710231/dash-save.png) to save the dashboard and the visual with its updated settings.

## Configure Colors for a Specific Histogram

To specify the color settings for a specific histogram using the Color sidebar:

1. Edit the visual you want to modify. See [*Edit Visuals*](https://devnet.logianalytics.com/hc/en-us/articles/4405859570839-Edit-Visuals).
2. If you are editing the visual in a dashboard, select **Edit Visual** from the [visual drop-down menu](https://devnet.logianalytics.com/hc/en-us/articles/4405851254295-Use-the-Visual-Menu). The [sidebar menu](https://devnet.logianalytics.com/hc/en-us/articles/4405859578391-Use-the-Visual-Sidebar-Menu) for the visual appears. If you are editing the visual from the Visual Gallery, the sidebar appears to the right of the visual.

   Select ![](https://devnet.logianalytics.com/hc/article_attachments/4406743709975/sidebar-color.png) on the [sidebar menu](https://devnet.logianalytics.com/hc/en-us/articles/4405859578391-Use-the-Visual-Sidebar-Menu). The Color sidebar for the visual appears.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4406743738263/color-bar-hist2_288x193.png)
3. Configure the color settings as described below. Supported color specifications are described in [*Specify Colors*](https://devnet.logianalytics.com/hc/en-us/articles/4405859162903-Specify-Colors).

   | Setting | Description |
   | --- | --- |
   | Bins Color | Select the color for the bins on the visual. |
   | Cumulative Line Color | Select the color for the cumulative line on your visual. |
4. Close the Color sidebar and the color settings are dynamically applied to the visual.
5. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4406743710231/dash-save.png) to save the dashboard and the visual with its updated settings.
