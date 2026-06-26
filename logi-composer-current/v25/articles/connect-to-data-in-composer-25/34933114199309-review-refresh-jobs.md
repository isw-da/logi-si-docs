---
title: "Review Refresh Jobs"
id: 34933114199309
section: "Connect to Data in Composer 25"
product: "Logi Composer v25"
url: https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933114199309-Review-Refresh-Jobs
updated_at: 2026-05-26T22:09:12Z
---

# Review Refresh Jobs

# Review Refresh Jobs

Administrators can monitor data source refresh jobs using the Console of Refreshing Jobs. Data on this page automatically refreshes every 15 seconds.

**Access the Console of Refreshing Jobs**

1. Log in as a Composer administrator.
2. Select **Console** on the [UI menu](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933143886477-The-Composer-UI-Menu) (![](https://logi-composer-v25.insightsoftware.com/hc/article_attachments/46167896718605)). The Console of Refreshing Jobs page appears. It shows a table of refresh jobs that are in progress or that have completed.

Refresh jobs are identified in the table by the data source configuration name. The columns in this work area include:

| Column | Description |
| --- | --- |
| Data Source | The name of the data source configuration to which the job applies. |
| Job Type | The type of refresh job that was run. Possible types are **Source Refresh** (the data source metadata and all fields were refreshed) and **Field Refresh** (an individual field was refreshed). Field refresh jobs also identify the field that was refreshed in the job type (for example, **Field Refresh [condition\_code]** indicates that the `condition_code` field was refreshed). |
| Status | The status of the job.  Possible statuses include:   * **Complete**: The job completed successfully. * **In Progress**: The job is running or is scheduled to be run. * **Incomplete**: The job only partially completed. For example, the minimum and maximum values were successfully refreshed, but the distinct values were not refreshed. * **Failed**: The job could not run or could not be completed due to some error in the system     For example, there may be connection problems with the data store. Select the arrow to view details on the issues that occurred while running the job. |
| Last Finished | The date and time when the most recent job completed. |
| Next Run | The date and time when the next job is scheduled. |
| Job History | Select  in this column to list all the completed refresh jobs of the selected refresh job type that have been run for the selected data source. The list appears on a pop-up dialog. The dialog shows the start time, finish time and status of the refresh jobs. |

By default, the table is sorted in order by the Last Finished date and time. You can sort the table by selecting any of the following column headings: **Data Source**, **Job Type**, **Status**, or **Last Finished**. If you select a heading once, the table data sorts in reverse lexicographical order by the selected column heading. Select the heading a second time to sort the data in lexicographical order. The table sort order is automatically reset to the default order every time the table is refreshed.

You can filter the list using any of the column headings. Select the filter icon ![](https://logi-composer-v25.insightsoftware.com/hc/article_attachments/46167047515533) in the column heading to select for specify an appropriate filter on a pop-up dialog. For example, the pop-up dialog for the Data Source column allows you to select data sources you want to see in the list.
