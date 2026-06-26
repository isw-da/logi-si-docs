---
title: "Update a Scheduled  Dashboard Report"
id: 43701047401869
section: "Use Dashboards and Visuals in Composer 26"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701047401869-Update-a-Scheduled-Dashboard-Report
updated_at: 2026-05-29T14:11:16Z
---

# Update a Scheduled  Dashboard Report

# Update a Scheduled Dashboard Report

After you create a scheduled dashboard report, you can go back and make updates as you wish. This topic describes how you can update a scheduled dashboard report.

**Update a scheduled dashboard report**

1. Log in as an administrator or a user with the **Create Scheduled Reports** [privilege](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701005611789-Group-Privilege-Reference).
2. Select **Library** on the [top-level navigation banner](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701115577869-The-Top-Level-Navigation-Banner) or select **Dashboard** on the [Home page](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701136935821-Home-Page). The [library](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701047640717-Use-the-Library-for-Dashboards) opens, displaying dashboards in a table (list) format.
3. Locate the dashboard in the library list containing the scheduled dashboard report you want to update.
4. Select the schedule icon (![](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46243240542349)) in the associated **Schedule** column. The Scheduled Reports dialog box displays.

   ![Use this dialog box to schedule reports for you and other users.](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46242708619533 "Scheduled Reports")

   Scheduled dashboard reports for this dashboard that have already been defined appear on the left side of the dialog.
5. Select the scheduled dashboard report that you want on the left side of the Scheduled Reports dialog box. Composer displays the settings.
6. Update the settings for the report on the right side of the Scheduled Reports dialog.

   | Field | Description |
   | --- | --- |
   | Name | Specify a name for the scheduled report definition. |
   | Delivery Method | Select a format for delivery.  * EMAIL (default): deliver to recipients by email. * FILE\_DROP ([if enabled in your environment](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701053868173-Server-Level-Variables#scheduled-report)): deliver to recipients (users defined in your Composer environment only) at the [defined SFTP location](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701077034381--Scheduled-Dashboard-Report-Properties#sftp.host). |
   | Format | Select a format for the scheduled report using the arrows in the **Format** selection box. PDF, PNG, and Data (XLSX) > Raw Data or Dat a (XLSX) > Visual Data formats are supported.  **Note:** When you export raw data from your visuals to XLSX, numeric fields are exported as numbers. Dates are exported as dates in ISO 8601 format. |
   | To | The **To** text box contains your user name. Add more recipients here by typing their name or email address in this box. You must have at least one name in this field.  * As you type in characters, existing user accounts are searched and defined users that match are shown. See [Manage Users](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701051820941-Manage-Users). * You can also set up user attributes and use the Recipient Rules API to specify who your users can see in the recipients list, and select from those users who to send the report to. See [Configure Recipient Rules](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701065872269-Configure-Recipient-Rules). * Add users without user accounts to the recipients list: type in their full email address, then select add (add icon) to include them in the list. Non-Logi Composer user recipients are granted the same security based on the report scheduler's user attributes for interpolation, row and column security (if defined), and filtering.  **Important:**    If you do not want to allow external users to receive scheduled dashboard reports, you can work with technical support to disable this in your environment. See[Scheduled Dashboard Report Prerequisites](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701047328013-Scheduled-Dashboard-Report-Prerequisites). See [Scheduled Dashboard Report Prerequisites](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701047328013-Scheduled-Dashboard-Report-Prerequisites) for information about Mail properties that you might need. |
   | Subject | Specify a subject for the email that will be sent containing the scheduled dashboard report. By default, a subject of **<dashboard-name> Schedule Report** is used. |
   | Message | Optionally provide a message for the email. |
   | Frequency | Select a frequency for the scheduled dashboard report using the arrows in the Frequency selection box. Frequencies of **Run Once**, **Days**, **Daily**, **Weekly**, and **Monthly** are supported. Depending on the frequency you select, additional fields appear. |
   | Run on the | This field only appears if the **Days**, **Weekly**, or **Monthly** frequencies are selected.  * Select one or more available days of the week for **Days**. * Select one day of the week for **Weekly**. * Select a date for **Monthly**. Options range from `1` to `31` and will run on that date, if available, each month. |
   | Run Time | This field only appears if the **Days**, **Daily**, **Weekly**, or **Monthly** frequencies are selected. Specify the hour and minute of the day at which the scheduled dashboard report should be generated and sent. Type the hour of the day on the left side of the colon and the minute of the day on the right side of the colon. Use the arrows in the box to the far right to select AM or PM. |
   | From | This field only appears if the **Days**, **Daily**, **Weekly**, or **Monthly** frequencies are selected. Select the starting date for the scheduled dashboard report. Click in the box to bring up a calendar in which you can select the date. |
   | To | This field only appears if the **Days**, **Daily**, **Weekly**, or **Monthly** frequencies are selected. Select the ending date for the scheduled dashboard report. Click in the box to bring up a calendar in which you can select the date. |
   | Date | This field only appears if you select the **Run Once** frequency. Select the date for the scheduled dashboard report. Click in the box to bring up a calendar with in you can select the date. |
   | Run Now | Slide the **Run Now** switch on (to the right) to send the scheduled dashboard report immediately. By default, this switch is off (on the left).  You can enable **Run Now** simultaneously with any other **Frequency** selected. The report will be delivered immediately and at the specified **Frequency**. For example, if you select **Run Once** and switch on **Run Now** you will get your report two times. |

   **Note:** 
   Only the report scheduler can see the non-Composer users included in the recipient list.
7. Select **Save** to save the scheduled dashboard report.
