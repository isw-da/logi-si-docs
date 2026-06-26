---
title: "Report Designer/Schedule"
id: 4415512103447
section: "User Guide"
category: "Izenda"
url: https://devnet.logianalytics.com/hc/en-us/articles/4415512103447-Report-Designer-Schedule
updated_at: 2021-12-10T03:10:37Z
---

# Report Designer/Schedule

# Report Designer/Schedule

The **Report Designer/Schedule** page allows users to

* View scheduled deliveries
* Add, copy, and remove schedules

## Methods of Delivering Scheduled Reports

| Delivery Method | Recipient Options | Delivery Options | Sending Location | Applied Filters |
| --- | --- | --- | --- | --- |
| Subscription | Self (Current User) | * Scheduled Alert * Scheduled Reporting Item | * Subscription Button in Report Viewer * Subscription Button in Report List | Configured in Subscription Scheduler window |
| Scheduled | All Users, Others and Self | * Scheduled Alert * Scheduled Reporting Item | * Schedule Tab in Report Designer | Configured in Report Scheduler window |
| Instant Delivery | All Users, Others and Self | * Instantly delivered report via email | * Email Button in Report Viewer * Email Button in Report List | Currently configured filters in report |

## View Schedule List

1. In Report Designer, click Schedule in the left menu.
2. Summaries of existing schedules are listed together with delivery
   options.
3. Each schedule can be edited, copied or deleted using the icons in
   Action field.
4. New schedule can be added using the Add Schedule button above the
   list.

[![../_images/Report_Schedule_List.png](https://devnet.logianalytics.com/hc/article_attachments/4415504498327/report_schedule_list_950x177.png)](https://devnet.logianalytics.com/hc/article_attachments/4415511834775/report_schedule_list.png)

Note: To delete multiple schedules at the same time, tick the checkbox in front of them then click the delete icon above the list (that looks like a waste basket).

## Search for Schedules

1. Select a field to search in from the drop-down, default is All.
2. Enter a partial text and click the search icon (🔍).
3. Only matching schedules will be displayed.

![../_images/Report_Schedule_Search.png](https://devnet.logianalytics.com/hc/article_attachments/4415492584855/report_schedule_search_348x161.png)

## Add a Schedule

Click the Add Schedule button above the list
to open the Add Schedule pop-up.

1. Enter a name for this schedule.
2. In Schedule tab:

   1. Select Scheduling Type:
      * Scheduled Alert: delivered only if report has data at scheduled time.
      * Scheduled Reporting Item: delivered regardless whether it has
        data or not at scheduled time.
   2. Select desired time zone.
   3. Select a start date in the future.
   4. Enter the start time (some common values can be quickly selected
      from the pre-defined list).
   5. Select a common recurrence period from the list, or select Custom
      Recurrence to define a different one.

   [![../_images/Report_Add_Schedule_pop-up_Schedule.png](https://devnet.logianalytics.com/hc/article_attachments/4415511835287/report_add_schedule_pop-up_schedule_600x389.png)](https://devnet.logianalytics.com/hc/article_attachments/4415511835031/report_add_schedule_pop-up_schedule.png)
3. In Delivery tab, select:

   * “Email” Delivery Type: send the report to the email address of
     selected users.
     1. Select Delivery Method: email a **Link**, email an
        **Attachment**, or email with **Embedded HTML** body.
     2. Customize the default template if necessary.
   * “File Location” Delivery Type: save the report as a file.
     1. Delivery Method is Send to disk.
     2. Select the Export File Type: PDF, Word Doc, Excel or CSV.

   [![../_images/Report_Add_Schedule_pop-up_Delivery.png](https://devnet.logianalytics.com/hc/article_attachments/4415511835799/report_add_schedule_pop-up_delivery_600x389.png)](https://devnet.logianalytics.com/hc/article_attachments/4415511835543/report_add_schedule_pop-up_delivery.png)
4. Optionally re-select values for report filters.

   [![../_images/Report_Add_Schedule_pop-up_Filter_Value_Selection.png](https://devnet.logianalytics.com/hc/article_attachments/4415504499095/report_add_schedule_pop-up_filter_value_selection_600x390.png)](https://devnet.logianalytics.com/hc/article_attachments/4415504498839/report_add_schedule_pop-up_filter_value_selection.png)
5. Click OK to close Add Schedule pop-up.
6. Click Save at the top to save the Report.
