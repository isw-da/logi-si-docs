---
title: "Update a Scheduled  Report"
id: 43701047401869
section: "Use Dashboards, Reports  and Visuals in Composer 26"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701047401869-Update-a-Scheduled-Report
updated_at: 2026-08-26T07:10:35Z
---

# Update a Scheduled  Report

# Update a Scheduled Report

**Note:** In this release, when your admin enables the Enhanced Experience user interface, you will see changes to workflows you may have used in previous releases.

After you [create](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701093791245-Schedule-a-Self-Service-Report-or-Dashboard-Report) a dashboard or self service report schedule, you can go back and make updates as you wish. This topic describes how you can update a scheduled report.

**Update a scheduled report**

1. Log in as an administrator or a user with the **Create Scheduled Reports** [privilege](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701005611789-Group-Privilege-Reference).
2. Select the **Discovery Board** card on your home page or **Library** from the main menu, then the **Reports** or **Dashboards** tab in the library. The library displays your items in a table (list) format.
3. Locate the report or dashboard you want.
4. Select the schedule icon in the associated **Schedule** column. The Scheduled Reports dialog box displays.

   ![Use this work area to schedule or update self service and dashboard reports](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/48418006424461 "Scheduled Reports dialog")

   Scheduled reports for this item that have already been defined appear on the left side of the dialog.
5. Select the scheduled report that you want on the left side of the Scheduled Reports dialog box. Composer displays the settings.
6. Update the settings for the report on the right side of the Scheduled Reports dialog.

   | Field | Description |
   | --- | --- |
   | Name | Specify a name for the scheduled report definition. |
   | Delivery Method | Select a format for delivery.  * EMAIL (default): deliver to recipients by email. * FILE\_DROP ([if enabled in your environment](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701053868173-Server-Level-Variables#scheduled-report)): deliver to recipients (users defined in your Composer environment only) at the [defined SFTP location](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701077034381--Scheduled-Report-Properties#sftp.host). |
   | Format | Select a format for the scheduled report using the arrows in the **Format** selector field.  * For dashboard reports, select from PDF, PNG, and XLSX format. * For self service reports, select from PDF and XLSX format. For more information on formatted PDF and XLSX options, see [Export Your Self Service Report](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/46982018753165-Create-Self-Service-Reports#Export2) and [Page Size and Orientation](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/46982018753165-Create-Self-Service-Reports#Page). **Note:** When you export raw data from your visuals to XLSX, numeric fields are exported as numbers. Dates are exported as dates in ISO 8601 format. |
   | To | The **To** text box contains your user name. Add more recipients here by typing their name or email address (if enabled in your environment) in this field. You must have at least one name in this field.  * As you type in characters, existing user accounts are searched and defined users that match are shown. See [Manage Users](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701051820941-Manage-Users). * You can also set up user attributes and use the Recipient Rules API to specify who your users can see in the recipients list, and select from those users who to send the report to. See [Configure Recipient Rules](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701065872269-Configure-Recipient-Rules). * Add users without user accounts to the recipients list: type in their full email address, then select the add icon to include them in the list. Non-Logi Composer user recipients are granted the same security based on the report scheduler's user attributes for interpolation, row and column security (if defined), and filtering.  **Important:**    If you do not want to allow external users to receive scheduled dashboard reports, you can work with technical support to disable this in your environment. See[Scheduled Self Service Reports and Dashboard Report Prerequisites](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701047328013-Scheduled-Self-Service-Reports-and-Dashboard-Report-Prerequisites). See [Scheduled Self Service Reports and Dashboard Report Prerequisites](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701047328013-Scheduled-Self-Service-Reports-and-Dashboard-Report-Prerequisites) for information about Mail properties that you might need. |
   | Subject | Specify a subject for the email that will be sent containing the scheduled dashboard report. By default, a subject of **<dashboard-or-report-name> Schedule Report** is used. |
   | Message | Optionally provide a message for the email. |
   | Frequency | Select a frequency for the scheduled dashboard report using the arrows in the Frequency selection box. Frequencies of **Run Once**, **Daily**, **Days**, **Weekly**, **Monthly** and **Periodically** are supported. Depending on the frequency you select, additional fields appear.  After selecting a Frequency, you can define the appropriate frequency options:  * **Run Once** - Select a **Date** and **Timezone** to run and deliver the report once. * **Daily** - Select a **Run Time**, **Timezone**, then a **From** and **To** date to define the time span to run and deliver the report daily. * **Days** - Select one or more **Day(s)** of the week, a **Run Time**, **Timezone**, then a **From** and **To** date to define the time span to run and deliver the report on the selected day or days. * **Weekly** - Select a day of the week from **Run on the** options, a **Run Time**, **Timezone**, then a **From** and **To** date to define the time span to run and deliver this report once weekly. * **Monthly** - Select a **Day** of the month, a **Run Time**, **Timezone**, then a **From** and **To** date to define the time span to run and deliver this report once monthly. * **Periodically** - Select one or more **Month(s)**, a **Day** of the month or months, a **Run Time**, **Timezone**, then a **From** and **To** date to define the time span to run and deliver this report once a month for the selected periodic months. |
   | |  |  | | --- | --- | | Date | This field only appears if you select the **Run Once** frequency.  Select the date for the scheduled dashboard report. Click in the box to bring up a calendar with in you can select the date. | |
   | |  |  | | --- | --- | | Day(s) | This field only appears if the **Days** frequency is selected. Sunday is added by default.  Enter one or more days of the week to run this schedule, or select the **x** next to a day to remove. | |
   | |  |  | | --- | --- | | Run on the | This field only appears if the **Weekly** frequency is selected.  Select one day of the week for **Weekly** to run and deliver this report on the selected day of the week. | |
   | |  |  | | --- | --- | | Month(s) | This field only appears if the **Periodically** frequency is selected.  January is added by default. Enter one or more months of the year to run this schedule, or select the **x** next to a month to remove. | |
   | |  |  | | --- | --- | | Day | This field only appears if the **Monthly** or **Periodically** frequency is selected.  1 is selected by default. Options range from `1` to `31` and will run on that date, if available, each month. | |
   | |  |  | | --- | --- | | Run Time | This field appears for all frequencies except **Run Once**.  Specify the hour and minute of the day at which the scheduled dashboard report should be generated and sent. Type the hour of the day on the left side of the colon and the minute of the day on the right side of the colon. Use the arrows in the box to the far right to select AM or PM. | |
   | Timezone | Default selection is UTC; select a time zone for this schedule to run and deliver this report.  If you select a timezone other than UTC, the schedule respects the appropriate standard and seasonal time rules. |
   | From | This field appears for all frequencies except **Run Once**.  Select the starting date for the scheduled dashboard report. Click in the box to bring up a calendar in which you can select the date. |
   | To | This field appears for all frequencies except **Run Once**.  Select the ending date for the scheduled dashboard report. Click in the box to bring up a calendar in which you can select the date. |
   | Run Now | Slide the **Run Now** switch on (to the right) to send the scheduled dashboard report immediately. By default, this switch is off (on the left).  You can enable **Run Now** simultaneously with any other **Frequency** selected. The report will be run and delivered immediately and at the specified **Frequency**. For example, if you select **Run Once** and switch on **Run Now** you will get your report two times when you **Save** your schedule. |

   **Note:** 
   Only the report scheduler can see the non-Composer users included in the recipient list.
7. Select **Save** to save the scheduled report.
