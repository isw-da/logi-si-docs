---
title: "Trigger Refresh Jobs"
id: 43701192120205
section: "Connect to Data in Composer 26"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701192120205-Trigger-Refresh-Jobs
updated_at: 2026-05-29T14:10:31Z
---

# Trigger Refresh Jobs

# Trigger Refresh Jobs

Composer maintains data source metadata and, optionally, a cached result set of the data from the data store for each data source configuration you define. When you initially connect to your data store using a data source configuration, a sampling of the data is collected to determine:

* Distinct values for all fields with ATTRIBUTE and NUMBER field types.
* The minimum and maximum values for all fields with number or time data types for which [Custom Ranges](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701116424973-Manage-Fields#Custom) have not been defined.

Composer administrators can define refresh jobs for this cached data. The following table identifies the types of refresh jobs that are currently supported, the triggers for the jobs, and the activities that occur when the job is run.

| Refresh Type | Trigger | Activities |
| --- | --- | --- |
| Source Refresh | An initial connection to a data source is saved. See [Define a Source](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701080450061-Define-a-Source). | The Composer cache is cleared and the minimum and maximum values for non-attribute fields and distinct values for attribute and number fields are refreshed. |
| Changes to the [Source Creation Tab](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701080568205-Source-Creation-Tab) or [Fields](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701116424973-Manage-Fields) tab in the data source configuration are saved. See [Edit a Data Source](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701116405261-Edit-a-Data-Source). |
| The scheduled refresh time (set on the [Cache](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701085337997-Cache-Tab "Cache tab") tab in the data source configuration) occurs. See [Set Up a Data Source Refresh Job](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701140447885-Set-Up-a-Data-Source-Refresh-Job). |
| Field Refresh | * To refresh the entire list of fields in a data source configuration, access the [Cache](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701085337997-Cache-Tab) tab and select the refresh () button for Manual Refresh in the table heading to trigger a manual refresh for all fields. This triggers a manual refresh of all the field data. * To refresh a specific field in a data source, access the [Cache](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701085337997-Cache-Tab) tab and select the Manual Refresh button () for the field you want to refresh. This triggers an immediate manual refresh for the selected field. | The minimum and maximum for non-attribute fields and distinct values for attribute and number fields are refreshed. |
| After Cache Cleanup | When a user selects an available Cache Cleanup option from the Actions column for a data source on the [Sources](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701081381901-Data-Sources-Page) page.  See [Clear the Cache for a Data Source Configuration](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701080340493-Clear-the-Cache-for-a-Data-Source-Configuration). | The data is freshly loaded into the Composer cache the next time it is requested from the data source. |

**Note:** 
If a [Custom Range](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701116424973-Manage-Fields#Custom) has been defined for a field, the minimum and maximum fields used in filters remain unchanged when you refresh source data. These fields are shown with cache actions disabled on the [Cache tab](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701085337997-Cache-Tab).

**Note:** 
When you add a new field to a data source, the scheduled refresh is not enabled for the new fields by default. Quickly enable scheduled refresh for all fields using the bulk update option in the [Schedule Refresh menu on the Cache](#schedulerefresh) tab, or enable each field for scheduled refresh manually on the Cache tab.

The status of refresh jobs can be reviewed on the Console of Refreshing Jobs. See [Review Refresh Jobs](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701140188173-Review-Refresh-Jobs).
