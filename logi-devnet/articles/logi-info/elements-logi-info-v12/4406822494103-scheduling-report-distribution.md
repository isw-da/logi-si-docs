---
title: "Scheduling Report Distribution"
id: 4406822494103
section: "Elements - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406822494103-Scheduling-Report-Distribution
updated_at: 2022-04-06T06:08:25Z
---

# Scheduling Report Distribution

# Scheduling Report Distribution

When report bookmarks are being used and the appropriate ReportCenter Item attributes have been set to allow scheduling, two icons will appear at the end of each bookmark menu link:

![](https://devnet.logianalytics.com/hc/article_attachments/4417563098647/rptcenter_06.png)

These icons allow users to **rename** or **remove** the bookmark, or **schedule** report distribution, as shown above.

![](https://devnet.logianalytics.com/hc/article_attachments/4417583745559/email_removed.png)

When the Schedule icon is clicked, the modal dialog box shown above, is displayed and the user can fill-in appropriate information.

Multiple addresses can be entered in the "To:" field by separating them with commas or semi-colons.

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
