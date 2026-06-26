---
title: "Set Up a Data Source Refresh Job"
id: 4405851158167
section: "Connect to Data in Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405851158167-Set-Up-a-Data-Source-Refresh-Job
updated_at: 2021-09-21T01:29:30Z
---

# Set Up a Data Source Refresh Job

# Set Up a Data Source Refresh Job

Data source refresh jobs are defined on the Refresh tab of a data source configuration. Only one refresh job can be defined for a data source, however you can manually trigger refresh jobs on the [Fields](https://devnet.logianalytics.com/hc/en-us/articles/4405851026455-Fields-Tab) tab of the data source configuration. See [*Trigger Refresh Jobs*](https://devnet.logianalytics.com/hc/en-us/articles/4405851159063-Trigger-Refresh-Jobs).

A refresh job requires you to specify a schedule for the job and, optionally, identify fields for the refresh.

The following refresh job schedule options are available:

* **No Schedule**: By default, this option is selected for a data source. It indicates that an initial data source refresh job is run after the data source has been successfully created and saved. After that, no additional refreshes of the data occur, although you can manually trigger a refresh of the field data. See [*Trigger Refresh Jobs*](https://devnet.logianalytics.com/hc/en-us/articles/4405851159063-Trigger-Refresh-Jobs).
* **Periodically**: Select this option to define a refresh job that runs at standard periods.
* **Advanced**: Select this option to define a refresh job using cron expressions. Use this option to define refresh jobs that run on a more complicated schedule.

In addition to the refresh job schedule options, you can select specific fields for the refresh job.

For specific instructions, see one of the following topics:

* [*Configure a Periodic Refresh Job*](https://devnet.logianalytics.com/hc/en-us/articles/4405859445527-Configure-a-Periodic-Refresh-Job)
* [*Configure an Advanced Refresh Job*](https://devnet.logianalytics.com/hc/en-us/articles/4405851156247-Configure-an-Advanced-Refresh-Job)
* [*Identify Specific Fields for a Refresh Job*](https://devnet.logianalytics.com/hc/en-us/articles/4405851157271-Identify-Specific-Fields-for-a-Refresh-Job)
