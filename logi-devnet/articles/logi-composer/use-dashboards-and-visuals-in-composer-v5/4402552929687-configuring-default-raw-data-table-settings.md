---
title: "Configuring Default Raw Data Table Settings"
id: 4402552929687
section: "Use Dashboards and Visuals in Composer v5"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4402552929687-Configuring-Default-Raw-Data-Table-Settings
updated_at: 2021-09-15T02:23:04Z
---

# Configuring Default Raw Data Table Settings

# Configuring Default Raw Data Table Settings

To configure default raw data table settings for a data source configuration:

1. Edit the appropriate data source configuration. See [*Editing a Data Source Configuration*](https://devnet.logianalytics.com/hc/en-us/articles/4402537781143-Editing-a-Data-Source-Configuration).
2. Select the [Visuals](https://devnet.logianalytics.com/hc/en-us/articles/4402537788695-Visuals-Tab) tab in the data source configuration wizard.
3. On the **Standard** subtab of the [Visuals](https://devnet.logianalytics.com/hc/en-us/articles/4402537788695-Visuals-Tab) tab, select **Raw Data Table**.

   If you want to be able to display the data collected by this data source configuration as a raw data table, make sure the **Raw Data Table** checkbox is selected.

   Default raw data table settings appear on the right side of the page.
4. Configure the default settings as follows:

   | Setting | Description |
   | --- | --- |
   | Columns | Select data fields to show as columns in the table. By default, all fields are selected. The fields available are all the data fields that can be seen in the visual. |
   | Rows per Fetch | Specify the number of rows of data that are fetched each time the data source configuration fetches data from the associated data store. Valid values are integers ranging from 100 to 100000. |
5. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4406763898903/save-white-btn_40x23.png).
