---
title: "Configure an Advanced Refresh Job"
id: 43701160844045
section: "Connect to Data in Composer 26"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701160844045-Configure-an-Advanced-Refresh-Job
updated_at: 2026-05-29T14:10:31Z
---

# Configure an Advanced Refresh Job

# Configure an Advanced Refresh Job

Using cron expressions, you can specify a more complicated schedule for refresh jobs for the data cached for a data source configuration.

**Configure an advanced refresh job for a data source configuration using a cron expression**

1. Log in as a user with the **Administer Sources** [privilege](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701005611789-Group-Privilege-Reference), or a user with **read** and **write** [permission](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701101615373-About-Source-Permissions) for the data source.
2. Select **Sources** on the [UI menu](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701160499853-The-Composer-UI-Menu) (![](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46243193170701)). The [Sources](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701081381901-Data-Sources-Page) page appears.
3. On the [Sources](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701081381901-Data-Sources-Page) page, locate and select the data source configuration you want to edit. The Source Creation work area opens.
4. Select the **Cache** tab, then enable enable **Schedule Refresh Settings** and select **Advanced** in the pop up. The settings work area for an Advanced refresh job appear.

   ![use the work area to scheudule the refresh settings for your data by creating your own Cron Expression](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46242401359373 "Schedule Refresh Settings Advanced work area")
5. In the box provided, enter a cron expression that sets the schedule using a string of six fields, each separated by a blank space. The format for the cron expression is:

   <seconds> <minutes> <hours> <days of the month> <months> <days of the week>

   The standard values supported by each field include:

   | Field | Allowed Values | Additional Characters |
   | --- | --- | --- |
   | <seconds> | 0-59 | , - \* / |
   | <minutes> | 0-59 | , - \* / |
   | <hours> | 0-23 | , - \* / |
   | <days of the month> | 1-31 | , - \* / ? L W |
   | <months> | 1-12 or Jan-Dec | , - \* / |
   | <days of the week> | 1-7 or Sun-Sat | , - \* / ? L W # |

   When creating the cron expression, keep the following requirements in mind:

   * Specifying `<seconds>` is optional, but defaults to zero seconds, which ensures that only one refresh job is run. If you specify seconds, the refresh job is rerun after that number of seconds has elapsed.
   * Either the `<days of the month>` or `<days of the week>` field is needed, but both should not be specified. If one of these fields is marked with an asterisk (\*), the other is automatically set to a question mark in the cron expression. In addition, an error is returned if you try to specify both of these fields.

     **Note:** 
     If you save an existing data source configuration that has both fields specified, no error is returned, but warnings are written to the log when Composer starts.
   * Names for the `<month>` and `<days of the week>` fields are not case sensitive. For example, `FRI` and `fri` are both acceptable formats.

   Special characters that can be specified are described in the table below.

   | Special Character | What It Means |
   | --- | --- |
   | \* | All values. Represents all the values within the specified field. In the following example, an asterisk is used in the <minutes> field, indicating that the job will run every minute:  0 \* 0 0 0 0 |
   | ? | No specific value. Used as a placeholder when no value is needed in the field. In the following example, the <months> field value is 6 (June) and the <days of the week> field value is a question mark, indicating that job runs in June, regardless of the day of the week:  0 0 0 0 6 ? |
   | - | Used to specify a range of values. For example, specifying `3-6` in the <hours> field (as shown in the following example) means the job will run at 3:00, 4:00, 5:00 and 6:00 am:  0 0 3-6 0 0 0 |
   | , | Used to specify a series of values. Use the comma to identify all the values for the field. In the following example, a comma is used in the <days of the week> field to run the job on Wednesdays, Thursdays, and Fridays:  0 0 0 0 0 Wed,Thur,Fri |
   | / | Used to specify the starting time value and the incremental increase of time. In the following example, specifying 0/5 in the <minutes> field means that the job runs immediately and then every 5 minutes.  0 0/5 0 0 0 0 |
   | L | Last. Used only in the <days of the month> and <days of the week> fields.  When this character is used standalone, it indicates the last day of the month or the last day of the week (Saturday).  However, when it is used with a value (such as 5L) in the <days of the month> field, it means the last Friday of the month (5 is Friday, L indicates the last Friday).  0 0 0 5L 0 0 |
   | W | Weekday. Used only in the <days of the month> and <days of the week> fields.  Identifies the weekday closest to the given day. For example, 15W means the closest weekday to the 15th of the month. The following results are possible:  * If the 15th falls on a Saturday, the result returned would be Friday the 14th * If the 15th falls on a Sunday, the result is Monday the 16th * If the 15th falls on a weekday, that specific day is returned. |
   | # | Number sign. Used only with the <days of the week> field.  Identifies the specific day of the month. For example, both `Wed#2` and `3#2` identify the second Wednesday of the month.  0 0 0 0 0 Wed#2 |

   The following table provides some cron expression examples:

   | cron Expression | Meaning |
   | --- | --- |
   | 0 0 12 \* \* ? | Noon every day |
   | 0 30 20 ? \* \* | 8:30 p.m. every night |
   | 0 0/10 17 \* \* ? | Every 10 minutes starting at 5 p.m. and ending at 5:50 p.m., every day |
   | 0 15-30 20 \* \* ? | Every minute starting at 8:15 p.m. and ending at 8:30 p.m., every day |
   | 0 45 20 ? \* Mon,Wed,Fri | 8:45 p.m. every Monday, Wednesday and Friday |
   | 0 0 20 3/3 \* ? | 8 p.m. every 3 days in every month, starting on the third day of the month |
6. Select **Save** to save your changes, then exit the source data configuration when you've finished defining your periodic refresh jobs. A summary of the configuration appears below **Schedule Refresh Settings.**

**Note:** 
If you disable **Schedule Refresh Settings**, any schedule you had set up previously is deleted.

Select the Schedule Refresh menu button to quickly enable or disable scheduled refreshing for all fields. This is available only if you have enabled **Schedule Refresh Settings** and defined a frequency.
