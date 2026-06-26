---
title: "Configuring Default Pivot Table Settings"
id: 4402537930519
section: "Use Dashboards and Visuals in Composer v5"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4402537930519-Configuring-Default-Pivot-Table-Settings
updated_at: 2021-09-15T02:22:59Z
---

# Configuring Default Pivot Table Settings

# Configuring Default Pivot Table Settings

To configure default pivot table settings for a data source configuration:

1. Edit the appropriate data source configuration. See [*Editing a Data Source Configuration*](https://devnet.logianalytics.com/hc/en-us/articles/4402537781143-Editing-a-Data-Source-Configuration).
2. Select the [Visuals](https://devnet.logianalytics.com/hc/en-us/articles/4402537788695-Visuals-Tab) tab in the data source configuration wizard.
3. On the **Standard** subtab of the [Visuals](https://devnet.logianalytics.com/hc/en-us/articles/4402537788695-Visuals-Tab) tab, select **Pivot Table**.

   If you want to be able to display the data collected by this data source configuration as a pivot table, make sure the **Pivot Table** checkbox is selected.

   Default pivot table settings appear on the right side of the page.
4. Configure the default settings as follows:

   | Setting | Description |
   | --- | --- |
   | Cell Limit | Specifies the maximum number of cells of data that can be returned for a pivot table. The default is 1,000,000 cells.  This setting regulates the quantity of data returned in a pivot table and can reduce the risk of performance problems with your browser. When the data returned from a query exceeds this setting, an error message displays. |
   | Column Limit | Specifies the maximum number of columns of data that can be returned for a pivot table. The default is 4000 columns.  This setting regulates the quantity of data returned in a pivot table and can reduce the risk of performance problems with your browser. When the data returned from a query exceeds this setting, an error message displays. |
   | Metrics | Select the default measurement metrics and corresponding functions, if required, that should be used.  By default **Volume** is selected. You can also define the default aggregation function used for the metric values: SUM, AVG, MAX, MIN, or (for some data sources) LAST VALUE. See [*Available Metric Functions*](https://devnet.logianalytics.com/hc/en-us/articles/4402537777687-Available-Metric-Functions). |
   | Metric Direction | Select **Rows** if you want the metrics listed in rows. Select **Columns** if you want the metrics listed in columns. |
   | Row Attributes | Select the default row attributes on which the table is based. |
   | Column Attributes | Select the column attributes for the table. |
   | Rows per Page | Select the number of rows per page. |
5. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4406763898903/save-white-btn_40x23.png).
