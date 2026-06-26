---
title: "Set Up a Data Source Refresh Job"
id: 34933150390285
section: "Connect to Data in Composer 25"
product: "Logi Composer v25"
url: https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933150390285-Set-Up-a-Data-Source-Refresh-Job
updated_at: 2026-05-26T22:07:56Z
---

# Set Up a Data Source Refresh Job

# Set Up a Data Source Refresh Job

Data source refresh jobs are defined on the Cache tab of a data source configuration. Only one refresh job can be defined for a data source, however you can manually trigger refresh jobs on the [Cache](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932891391629-Cache-Tab) tab of the data source configuration. See [Trigger Refresh Jobs](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933145070861-Trigger-Refresh-Jobs).

A refresh job requires you to specify a schedule for the job and, optionally, identify fields for the refresh.

By default, no data refresh jobs are scheduled for a data source. Select **Schedule Refresh Settings** on the Cache tab to set up Periodic or Advanced refresh jobs. An initial data source refresh job is run after the data source has been successfully created and saved. After that, no additional refreshes of the data occur, although you can manually trigger a refresh of the field data. See [Trigger Refresh Jobs](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933145070861-Trigger-Refresh-Jobs).

* **Periodic**: Select this option to define a refresh job that runs at standard periods.
* **Advanced**: Select this option to define a refresh job using cron expressions. Use this option to define refresh jobs that run on a more complicated schedule.

In addition to the refresh job schedule options, you can select specific fields for the refresh job.

For specific instructions, see one of the following topics:

* [Configure a Periodic Refresh Job](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933144425997-Configure-a-Periodic-Refresh-Job)
* [Configure an Advanced Refresh Job](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933114491533-Configure-an-Advanced-Refresh-Job)
* [Identify Specific Fields for a Refresh Job](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933144813965-Identify-Specific-Fields-for-a-Refresh-Job)
