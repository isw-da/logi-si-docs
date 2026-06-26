---
title: "Configure a Periodic Refresh Job"
id: 43701140257805
section: "Connect to Data in Composer 26"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701140257805-Configure-a-Periodic-Refresh-Job
updated_at: 2026-05-29T14:10:32Z
---

# Configure a Periodic Refresh Job

# Configure a Periodic Refresh Job

You can configure a periodic refresh job for the data cached for a data source configuration.

**Configure a periodic refresh job for a data source configuration**

1. Log in as a user with the **Administer Sources** [privilege](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701005611789-Group-Privilege-Reference), or a user with **read** and **write** [permission](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701101615373-About-Source-Permissions) for the data source.
2. Select **Sources** on the [UI menu](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701160499853-The-Composer-UI-Menu) (![](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46243181383437)). The [Sources](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701081381901-Data-Sources-Page) page appears.
3. On the [Sources](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701081381901-Data-Sources-Page) page, locate and select the data source configuration you want to edit. The Source Creation work area opens.
4. Select the **Cache** tab. All the fields from your data source are listed.

   ![use this work area to define data cache settings, statistics stash settings, schedule refresh settings, enable caching for fields, or manually refresh one or more fields.](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46243181383821 "Cache Tab work area")
5. Select to enable **Schedule Refresh Settings** and select **Periodic** in the pop up. The settings work area for a periodic refresh job appear.

   ![](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46242401563917)
6. Select the time interval for the job to be run using the
   **Frequency** list. Options **Daily**, **Weekly**, and **Monthly**. Depending on the **Runs** option you select, corresponding options become available in the
   **Run every** section:

   | Runs Selection | Run every Specification |
   | --- | --- |
   | Daily | Specify the time of day in **Run Time**, and a start and end date for daily runs at that time using the calendar options in **From** and **To**.  The first job runs on the date and time at which you save the data source.  Subsequent jobs continue daily until the last date and time occur. |
   | Weekly | Select the day of the week for the job to be run in **Run on**, time of day in **Run Time**, and a start and end date for weekly runs at the time using the calendar options in **From** and **To**.  The first job runs on the date and time at which you save the data source.  Subsequent jobs continue weekly until the last date and time occur. |
   | Monthly | Specify the number of months between job runs in **Run on**, time of day in **Run Time**, and a start and end date for monthly interval runs at the time using the calendar options in **From** and **To**.  The first job runs on the date and time at which you save the data source.  Subsequent jobs run at the **Run Time** time after the number of months you specify have passed.  For example, if you set your job to run every three months and the **Start on** time is April 4, 2024 at 5:00 a.m., the subsequent job runs on July 4, 2024 at 5:00 a.m. |
7. Select **Save** to save your changes, then exit the source data configuration when you've finished defining your periodic refresh jobs. A summary of the configuration appears below **Schedule Refresh Settings.**

**Note:** 
If you disable **Schedule Refresh Settings**, any schedule you had set up previously is deleted.

Select the Schedule Refresh menu button to quickly enable or disable scheduled refreshing for all fields. This is available only if you have enabled **Schedule Refresh Settings** and defined a frequency.
