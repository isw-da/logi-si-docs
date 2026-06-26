---
title: "Trigger Refresh Jobs"
id: 4405851159063
section: "Connect to Data in Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405851159063-Trigger-Refresh-Jobs
updated_at: 2021-09-21T01:29:30Z
---

# Trigger Refresh Jobs

# Trigger Refresh Jobs

Composer maintains data source metadata and, optionally, a cached result set of the data from the data store for each data source configuration you define. When you initially connect to your data store using a data source configuration, a sampling of the data is collected to determine:

* Distinct values for all fields with attribute field types
* The minimum and maximum values for all fields with number or integer field types

Composer administrators can define refresh jobs for this cached data. The following table identifies the types of refresh jobs that are currently supported, the triggers for the jobs, and the activities that occur when the job is run.

| Refresh Type | Trigger | Activities |
| --- | --- | --- |
| Source Refresh | An initial connection to a data source is saved. See [*Define a Data Source Configuration*](https://devnet.logianalytics.com/hc/en-us/articles/4405859320727-Define-a-Data-Source-Configuration). | The Composer cache is cleared and the minimum and maximum values for non-attribute fields and distinct values for attribute fields are refreshed. |
| Changes to the [Tables](https://devnet.logianalytics.com/hc/en-us/articles/4405859323287-Tables-Indices-Tab) or [Fields](https://devnet.logianalytics.com/hc/en-us/articles/4405851026455-Fields-Tab) tab in the data source configuration are saved. See [*Edit a Data Source Configuration*](https://devnet.logianalytics.com/hc/en-us/articles/4405851024663-Edit-a-Data-Source-Configuration). |
| The scheduled refresh time (set on the [Refresh](https://devnet.logianalytics.com/hc/en-us/articles/4405859322007-Refresh-Tab) tab in the data source configuration) occurs. See [*Set Up a Data Source Refresh Job*](https://devnet.logianalytics.com/hc/en-us/articles/4405851158167-Set-Up-a-Data-Source-Refresh-Job). |
| Field Refresh | One of the refresh options on a data source configuration's [*Fields Tab*](https://devnet.logianalytics.com/hc/en-us/articles/4405851026455-Fields-Tab) tab is selected.   * To refresh the entire list of fields in a data source configuration, access the [Fields](https://devnet.logianalytics.com/hc/en-us/articles/4405851026455-Fields-Tab) tab and select  underneath the field table. This triggers a manual refresh of all the field data. * To refresh a specific field in a data source, access the [Fields](https://devnet.logianalytics.com/hc/en-us/articles/4405851026455-Fields-Tab) tab and select  in the **Statistics** column for the field you want to refresh. This triggers an immediate manual refresh for the selected field. The status of the refresh appears in the field table cell. | The minimum and maximum for non-attribute fields and distinct values for attribute fields are refreshed. |

The status of refresh jobs can be reviewed on the Console of Refreshing Jobs. See [*Review Refresh Jobs*](https://devnet.logianalytics.com/hc/en-us/articles/4405851155095-Review-Refresh-Jobs).
