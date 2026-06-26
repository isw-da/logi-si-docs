---
title: "Scheduling Report Distribution "
id: 4419715453079
section: "Elements - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419715453079-Scheduling-Report-Distribution
updated_at: 2022-07-17T02:23:34Z
---

# Scheduling Report Distribution 

# Scheduling Report Distribution

When report bookmarks are being used and the appropriate ReportCenter Item attributes have been set to allow scheduling, two icons will appear at the end of each bookmark menu link:

![](https://devnet.logianalytics.com/hc/article_attachments/7522758091671/rptcenter_06.png)

These icons allow users to **rename** or **remove** the bookmark, or **schedule** report distribution, as shown above.

![](https://devnet.logianalytics.com/hc/article_attachments/7522745474327/_newplus.jpg) New for 14.1 Upon removing a bookmark, Info generates a confirmation dialog box that lists the time and date the bookmark is set to run and asks if you still want to delete the bookmark:

![](https://devnet.logianalytics.com/hc/article_attachments/7522774044439/delete_bookmark_confirmatoin_442x199.jpg)

To proceed, select **OK**. Otherwise, select **Cancel**.

When the **Schedule** icon is selected, the modal dialog box shown below, is displayed and the user can fill-in appropriate information:

![](https://devnet.logianalytics.com/hc/article_attachments/7522784767255/report_center_time_zone_schedule_516x614.png)

Multiple addresses can be entered in the "To:" field by separating them with commas or semi-colons.

![](https://devnet.logianalytics.com/hc/article_attachments/7522774430103/noteicon.jpg) Report developers can set a default time zone for reports using TMFs.

The child element **Email List** can be used with ReportCenter Menu to make it easier for a user to enter email addresses by showing an auto-complete list for the To: text box in the form shown above. The email addresses come from a column ina datalayer added beneath Email List. Specify the name of that column in the Email List element's **Email Column Name** attribute.

At the designated time, the Logi Scheduler will run the report, export it in the specified format and attach it to an email (for PDF and Excel formats) or embed it in an email (Web Mail format), and send the email using the first (top-most) **Connection.SMTP**
element found in the \_Settings definition. This enables an administrator
to switch SMTP servers without having to change report schedules. The developer, of course, controls which export formats are available using a ReportCenter Item attribute.

If it's supported by your browser,
an **HTML5** feature called "local storage" will be used to automatically store the email
addresses you enter, preserve them between sessions, and provide them back to
you in a list for selection in subsequent sessions. If your browser doesn't
support this feature, or if it's turned off in your browser options, obviously
the element won't be able to provide the list of addresses for re-use.
