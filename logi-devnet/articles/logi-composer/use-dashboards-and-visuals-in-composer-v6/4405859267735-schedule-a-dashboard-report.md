---
title: "Schedule a Dashboard Report"
id: 4405859267735
section: "Use Dashboards and Visuals in Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405859267735-Schedule-a-Dashboard-Report
updated_at: 2021-09-21T01:27:48Z
---

# Schedule a Dashboard Report

# Schedule a Dashboard Report

You can regularly generate and share a scheduled dashboard report with other users.

To generate a scheduled dashboard report:

1. Log into Composer as an administrator or a user with the **Can Create Scheduled Reports**[privilege](https://devnet.logianalytics.com/hc/en-us/articles/4405859114647-Group-Privilege-Reference). The [Home page](https://devnet.logianalytics.com/hc/en-us/articles/4405851121559-Home-Page) appears.
2. Select **Library** on the [top-level navigation banner](https://devnet.logianalytics.com/hc/en-us/articles/4405851152407-The-Top-Level-Navigation-Banner) or select **Dashboard** on the [Home page](https://devnet.logianalytics.com/hc/en-us/articles/4405851121559-Home-Page). The [dashboard library](https://devnet.logianalytics.com/hc/en-us/articles/4405859273751-Use-the-Dashboard-Library) appears.
3. Locate the dashboard in the dashboard library list for which you want to generate a scheduled dashboard report.
4. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4406743712407/dashboard-schedule.png) in the associated **Schedule** column. The Scheduled Reports dialog appears.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4406747439767/dash-sched_576x413.png)

   Scheduled dashboard reports for this dashboard that have already been defined appear on the left side of the dialog. A message appears on the dialog if none have been defined.
5. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4406743877015/new-sched_87x21.png).
6. Supply values for the following fields on the Scheduled Reports dialog.

   | Field | Description |
   | --- | --- |
   | Name | Specify a name for the scheduled dashboard report definition. |
   | Format | Select a format for the scheduled dashboard report using the arrows in the **Format** selection box. PDF and PNG formats are supported. |
   | Send report to me | Slide the **Send report to me** switch on (to the right) to have the report sent to you only. Slide it off (to the left) to specify a list of recipients for the scheduled dashboard report. |
   | To | This field only appears if the **Send report to me** switch is off (to the left). Specify at least one recipient; more than one can be specified. User names must be defined in Composer. See [*Manage User Definitions*](https://devnet.logianalytics.com/hc/en-us/articles/4405859120023-Manage-User-Definitions).  To specify a user, simply start typing the user name or the user's email (if the email is provided in the Composer user definition) and Composer will provide a list of user names that match your specification. Select one from the list.  To add a second user, simply repeat the process.  See [*Scheduled Dashboard Report Prerequisites*](https://devnet.logianalytics.com/hc/en-us/articles/4405859269911-Scheduled-Dashboard-Report-Prerequisites) for information about JavaMail properties that might be needed. |
   | Subject | Specify a subject for the email that will be sent containing the scheduled dashboard report. By default, a subject of **<dashboard-name> Schedule Report** is used. |
   | Message | Optionally provide a message for the email. |
   | Frequency | Select a frequency for the scheduled dashboard report using the arrows in the Frequency selection box. Frequencies of **Daily**, **Weekly**, **Monthly**, and **Run Once** are supported. Depending on the frequency you select, additional fields appear. |
   | Run Time | This field only appears if the **Daily**, **Weekly**, or **Monthly** frequencies are selected. Specify the hour and minute of the day at which the scheduled dashboard report should be generated and sent. Type the hour of the day on the left side of the colon and the minute of the day on the right side of the colon. Use the arrows in the box to the far right to select AM or PM. |
   | From | This field only appears if the **Daily**, **Weekly**, or **Monthly** frequencies are selected. Select the starting date for the scheduled dashboard report. Click in the box to bring up a calendar with which you can select the date. |
   | To | This field only appears if the **Daily**, **Weekly**, or **Monthly** frequencies are selected. Select the ending date for the scheduled dashboard report. Click in the box to bring up a calendar with which you can select the date. |
   | Run on the | This field only appears if the **Weekly** or **Monthly** frequencies are selected. When **Weekly** is selected, use the arrows in this selection box to select the day of the week on which the scheduled dashboard report should run (Sunday, Monday, Tuesday, etc.). When **Monthly** is selected, use the arrows in this selection box to select the date in the month on which the scheduled dashboard report should run (valid values range from 1 through 31). |
   | Date | This field only appears if you select the **Run Once** frequency. Select the date for the scheduled dashboard report. Click in the box to bring up a calendar with which you can select the date. |
   | Run Now | Slide the **Run Now** switch on (to the right) to send the scheduled dashboard report immediately. By default, this switch is off (on the left).  You can enable **Run Now** simultaneously with any other **Frequency** selected. The report will be delivered immediately and at the specified **Frequency**. For example, if you select **Run Once** and switch on **Run Now** you will get your report two times. |
7. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4406743874839/save-blue-supervisor-btn_65x22.png) to save the scheduled dashboard report. The name of the scheduled dashboard report appears in the list on the left of the Scheduled Reports dialog.
