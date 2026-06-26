---
title: "Update a Scheduled Dashboard Report"
id: 4405850988439
section: "Use Dashboards and Visuals in Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405850988439-Update-a-Scheduled-Dashboard-Report
updated_at: 2021-09-21T01:27:48Z
---

# Update a Scheduled Dashboard Report

# Update a Scheduled Dashboard Report

You can update a scheduled dashboard report.

To update a scheduled dashboard report:

1. Log into Composer as an administrator or a user with the **Can Create Scheduled Reports**[privilege](https://devnet.logianalytics.com/hc/en-us/articles/4405859114647-Group-Privilege-Reference). The [Home page](https://devnet.logianalytics.com/hc/en-us/articles/4405851121559-Home-Page) appears.
2. Select **Library** on the [top-level navigation banner](https://devnet.logianalytics.com/hc/en-us/articles/4405851152407-The-Top-Level-Navigation-Banner) or select **Dashboard** on the [Home page](https://devnet.logianalytics.com/hc/en-us/articles/4405851121559-Home-Page). The [dashboard library](https://devnet.logianalytics.com/hc/en-us/articles/4405859273751-Use-the-Dashboard-Library) appears.
3. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4406743873943/list-view.png) to view the dashboard library in list view.
4. Locate the dashboard in the dashboard library list containing the scheduled dashboard report you want to update.
5. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4406743712407/dashboard-schedule.png) in the associated **Schedule** column. The Scheduled Reports dialog appears.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4406747439767/dash-sched_576x413.png)

   Scheduled dashboard reports for this dashboard that have already been defined appear on the left side of the dialog. A message appears on the dialog if none have been defined.
6. Select the scheduled dashboard report that you want to modify on the left side of the Scheduled Reports dialog. The settings for the report appear on the right side of the dialog.
7. Update the settings for the report on the right side of the Scheduled Reports dialog.

   | Field | Description |
   | --- | --- |
   | Name | Specify a name for the scheduled dashboard report definition. |
   | Format | Select a format for the scheduled dashboard report using the arrows in the **Format** selection box. PDF and PNG formats are supported. |
   | Send report to me | Slide the **Send report to me** switch on (to the right) to have the report sent to you only. Slide it off (to the left) to specify a list of recipients for the scheduled dashboard report. |
   | To | This field only appears if the **Send report to me** switch is off (to the left). Specify at least one recipient. See [*Scheduled Dashboard Report Prerequisites*](https://devnet.logianalytics.com/hc/en-us/articles/4405859269911-Scheduled-Dashboard-Report-Prerequisites) for information about JavaMail properties that might be needed. |
   | Subject | Specify a subject for the email that will be sent containing the scheduled dashboard report. By default, a subject of **<dashboard-name> Schedule Report** is used. |
   | Message | Optionally provide a message for the email. |
   | Frequency | Select a frequency for the scheduled dashboard report using the arrows in the Frequency selection box. Frequencies of **Daily**, **Weekly**, **Monthly**, and **Run Once** are supported. Depending on the frequency you select, additional fields appear. |
   | Run Time | This field only appears if the **Daily**, **Weekly**, or **Monthly** frequencies are selected. Specify the hour and minute of the day at which the scheduled dashboard report should be generated and sent. Type the hour of the day on the left side of the colon and the minute of the day on the right side of the colon. Use the arrows in the box to the far right to select AM or PM. |
   | From | This field only appears if the **Daily**, **Weekly**, or **Monthly** frequencies are selected. Select the starting date for the scheduled dashboard report. Click in the box to bring up a calendar with which you can select the date. |
   | To | This field only appears if the **Daily**, **Weekly**, or **Monthly** frequencies are selected. Select the ending date for the scheduled dashboard report. Click in the box to bring up a calendar with which you can select the date. |
   | Run on the | This field only appears if the **Weekly** or **Monthly** frequencies are selected. When **Weekly** is selected, use the arrows in this selection box to select the day of the week on which the scheduled dashboard report should run (Sunday, Monday, Tuesday, etc.). When **Monthly** is selected, use the arrows in this selection box to select the date in the month on which the scheduled dashboard report should run (valid values range from 1 through 31). |
   | Date | This field only appears if you select the **Run Once** frequency. Select the date for the scheduled dashboard report. Click in the box to bring up a calendar with which you can select the date. |
   | Run Now | Slide the **Run Now** switch on (to the right) to send the scheduled dashboard report immediately. By default, this switch is off (on the left).  You can enable **Run Now** simultaneously with any other **Frequency** selected. The report will be delivered immediately and at the specified **Frequency**. For example, if you select **Run Once** and switch on **Run Now** you will get your report two times. |
8. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4406743874839/save-blue-supervisor-btn_65x22.png) to save the scheduled dashboard report. The updates are saved.
