---
title: "Configure Default Table Settings"
id: 4405859542295
section: "Use Dashboards and Visuals in Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405859542295-Configure-Default-Table-Settings
updated_at: 2021-09-21T01:30:14Z
---

# Configure Default Table Settings

# Configure Default Table Settings

To configure default table settings for a data source configuration:

1. Edit the appropriate data source configuration. See [*Edit a Data Source Configuration*](https://devnet.logianalytics.com/hc/en-us/articles/4405851024663-Edit-a-Data-Source-Configuration).
2. Select the [Visuals](https://devnet.logianalytics.com/hc/en-us/articles/4405859325591-Visuals-Tab) tab in the data source configuration wizard.
3. On the **Standard** subtab of the [Visuals](https://devnet.logianalytics.com/hc/en-us/articles/4405859325591-Visuals-Tab) tab, select **Table**.

   If you want to be able to display the data collected by this data source configuration as a table, make sure the **Table** checkbox is selected.

   Default table settings appear on the right side of the page.
4. Configure the default settings as follows:

   | Setting | Description |
   | --- | --- |
   | Columns | Select data fields to show as columns in the table. By default, all fields are selected. The fields available are all the data fields that can be seen in the visual. If a field is selected as a table column, it cannot also be specifically selected as a grouped column. |
   | Grouped Columns | Select data fields that should be grouped in the table. By default, no fields are selected. The fields available are all the data fields that can be seen in the visual. If a field is selected for grouping, it is automatically selected for the table and cannot be specifically selected as a table column. |
   | Metrics | [Metrics](https://devnet.logianalytics.com/hc/en-us/articles/4405859309975-Metrics) in the data are listed in this section showing their default aggregation settings. To change the default aggregation for a metric, select the metric and then select the aggregation method you want used for that field in tables. Aggregation methods vary, depending on how the metric is created in Composer. See [*Metrics*](https://devnet.logianalytics.com/hc/en-us/articles/4405859309975-Metrics). Valid aggregation methods include SUM, AVG, MIN, MAX, LAST VALUE, and DISTINCT COUNT. See [*Metric Aggregation Functions*](https://devnet.logianalytics.com/hc/en-us/articles/4405851021975-Metric-Aggregation-Functions). |
   | Rows per Fetch | Specify the number of rows of data that are fetched each time the data source configuration fetches data from the associated data store. Valid values are integers ranging from 100 to 100000. |
5. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4406747382679/save-white-btn_40x23.png) or ![](https://devnet.logianalytics.com/hc/article_attachments/4406743731095/finish-btn_42x22.png), as appropriate.
