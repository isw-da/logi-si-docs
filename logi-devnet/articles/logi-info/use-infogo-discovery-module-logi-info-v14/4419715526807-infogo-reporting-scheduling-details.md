---
title: "InfoGo - Reporting Scheduling Details"
id: 4419715526807
section: "Use InfoGo/Discovery Module - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419715526807-InfoGo-Reporting-Scheduling-Details
updated_at: 2022-07-17T02:23:16Z
---

# InfoGo - Reporting Scheduling Details

# InfoGo - Reporting Scheduling Details

To schedule a report, you need to provide the delivery details and report generation frequency in the Schedule panel:

![](https://devnet.logianalytics.com/hc/article_attachments/7522765664535/schedule_time_zon.png)

Provide the following schedule details:

* **From** - Enter your email address (or the email address you want to appear as the "Sent From" address).
* **To** - Enter the email address of the report recipient. Separate multiple addresses with a semi-colon (";").

  + ![](https://devnet.logianalytics.com/hc/article_attachments/7522745474327/_newplus.jpg) New for 14.1 The characters accepted in the To, Cc, and Bcc fields are: **!#$%&'+-^`~**
* **Subject** - Enter a brief subject description.
* **Orientation** - Select the orientation for the report: Portrait or Landscape.
* **Message** - Enter the text of the email message, included when the PDF or Excel format option is chosen.
* **Schedule** - Select the **Start Time**, **Run On** date, and **Time Zone** to customize the delivery of the report. These options change depending on the initial selection and are described in more detail below.
* **Done** - Select **Done** to save the settings.

If you're editing a schedule, two more buttons display:

* **Run Now...** - Select **Run Now...** to generate and deliver the report immediately.
* **Remove...** - Select **Remove...** to remove this scheduled occurrence.

![](https://devnet.logianalytics.com/hc/article_attachments/7522755629847/noteicon.jpg) Schedules launched by the shared user are removed if their permission changes to "Read". Likewise, if the report or folder is unshared with that user, schedules launches by the shared user are also removed.

You can also click the **X** icon to close the panel, without saving any changes, at any time.

## Schedule Options: Once

This option generates and delivers the report exactly one time:

![](https://devnet.logianalytics.com/hc/article_attachments/7522749514007/date_picker_replacement.png)

* **Start Time** - Format must use the *24-hour* clock. You can select it from the Time Picker by clicking the **clock** icon (selected time can be made more exact by editing it once it's in the input control).
* **Start Date** - Format must be *YYYY-MM-DD*. You can select it from a Calendar by clicking the **calendar** icon.
* **Time Zone** - An optional feature to customize the time zone for report delivery. If your application has been configured for it, a default time zone displays. If not, select the **Time Zone** drop-down to set desired time zone.

![](https://devnet.logianalytics.com/hc/article_attachments/7522725179159/noteicon.png) The date picker highlights the current date (default), as well as the selected date.

## Schedule Options: Minutes, Hours, Daily

This option generates and delivers the report every X minutes, hours, or days:  

![](https://devnet.logianalytics.com/hc/article_attachments/7522751335319/minutes_hours_daily_time_zone.png)

* **Every** - Select the interval of minutes, hours, or days desired. Use caution if selecting minutes; repetitive short time intervals may impact server performance.
* **Start Time** - Format must use the *24-hour* clock. You can select it from the Time Picker by clicking the **clock** icon (selected time can be made more exact by editing it once it's in the input control).
* **Start Date** - Format must be *YYYY-MM-DD*. You can select it from a Calendar by clicking the **calendar** icon.
* **End Date** - An optional date for stopping the scheduled deliveries. Format must be *YYYY-MM-DD*. You can select it from a Calendar by clicking the **calendar** icon.
* **Time Zone** - An optional feature to customize the time zone for report delivery. If your application has been configured for it, a default time zone displays. If not, select the **Time Zone** drop-down to set desired time zone.

![](https://devnet.logianalytics.com/hc/article_attachments/7522725179159/noteicon.png) The date picker highlights the current date (default), as well as the selected date.

## Schedule Options: Weekly

This option generates and delivers the report at various weekly intervals, on specific days of the week:

![](https://devnet.logianalytics.com/hc/article_attachments/7522755893015/weekly_time_zone.png)

  

* **Every** - Select the interval of weeks desired.
* **Days** - Use the check boxes to specify the exact days desired.
* **Start Time** - Format must use the *24-hour* clock. You can select it from the Time Picker by clicking the **clock** icon (selected time can be made more exact by editing it once it's in the input control).
* **Start Date** - Format must be *YYYY-MM-DD*. You can select it from a Calendar by clicking the **calendar** icon.
* **End Date** - An optional date for stopping the scheduled deliveries. Format must be *YYYY-MM-DD*. You can select it from a Calendar by clicking the **calendar** icon.
* **Time Zone** - An optional feature to customize the time zone for report delivery. If your application has been configured for it, a default time zone displays. If not, select the **Time Zone** drop-down to set desired time zone.

![](https://devnet.logianalytics.com/hc/article_attachments/7522725179159/noteicon.png) The date picker highlights the current date (default), as well as the selected date.

## Schedule Options: Monthly

This option generates and delivers the report on specific days in specific months:  

![](https://devnet.logianalytics.com/hc/article_attachments/7522787465111/image-20220421-022137_538x450.png)

* **Day N of the Month** - Enter a specific day number, 1-31, for report delivery in each of the selected months. Ensure that the day number actually exists in each selected month (non-existent days will be skipped). - or -
* ![](https://devnet.logianalytics.com/hc/article_attachments/7522745474327/_newplus.jpg) New for 14.2**Last day of the month(s) -** Select for report delivery on the last day of each month. - or -
* **Nth Weekday** - Select first, second, third, fourth, or last specific day of the week for report delivery in each of the selected months.
* **Start Time** - Format must use the *24-hour* clock. You can select it from the Time Picker by clicking the **clock** icon (selected time can be made more exact by editing it once it's in the input control).
* **Start Date** - Format must be *YYYY-MM-DD*. You can select it from a Calendar by clicking the **calendar** icon.
* **End Date** - An optional date for stopping the scheduled deliveries. Format must be *YYYY-MM-DD*. You can select it from a Calendar by clicking the **calendar** icon.
* **Time Zone** - An optional feature to customize the time zone for report delivery. If your application has been configured for it, a default time zone displays. If not, select the **Time Zone** drop-down to set desired time zone.

![](https://devnet.logianalytics.com/hc/article_attachments/7522725179159/noteicon.png) The date picker highlights the current date (default), as well as the selected date.
