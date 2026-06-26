---
title: "Modifying Default Email Template"
id: 4415492643607
section: "Developer Guide"
category: "Izenda"
url: https://devnet.logianalytics.com/hc/en-us/articles/4415492643607-Modifying-Default-Email-Template
updated_at: 2022-01-25T14:40:52Z
---

# Modifying Default Email Template

# Modifying Default Email Template

This article describes how to change the default footer in emails for Schedules and Subscriptions. The default templates can be found under API/EmailTemplates. Before modifying the templates, please take note of the below:

![../_images/Settings_Schedule_Scope.PNG](https://devnet.logianalytics.com/hc/article_attachments/4415511692823/settings_schedule_scope.png)

## Change the Default Footer in Emails

Note

The following steps cover modifying the template for the “Link” delivery method for schedules and subscriptions. Modifying the template of other delivery methods can be done by changing its respective file.

1. In Windows explorer, navigate to API/EmailTemplates/en-US/Report/Schedule/Inside. Modify the “Link.xml” file to include the desired text (e.g. Add “Have a nice day” to the end of the email body).
2. In Windows explorer, navigate to API/EmailTemplates/en-US/Report/Schedule/Outside. Modify the “Link.xml” file to include the desired text.
3. In Windows explorer, navigate to API/EmailTemplates/en-US/Report/Subscription. Modify the “Link.xml” file to include the desired text.

   > * Sample template for “Link.xml”:
   >
   > ```
   > <?xml version="1.0" encoding="utf-8" ?><Body><![CDATA[    Please find the report link below. Have a nice day.    <br/>    <br/>    {reportLink}    <br/>    <br/>    Regards,    <br/>    {currentUserName}]]></Body>
   > ```
4. Reset IIS and clear your browser cache.
5. Navigate to Izenda and select a report in the Report List
6. Add a scheduled instance (link) to the report and observe the email body. If the “External User” permission is unchecked, this reflects our change in step 1. Otherwise, this reflects our change in step 2.
7. Add a subscription (link) to the report and observe the email body. This reflects our change from step 3.

   > [![../_images/Custom_Email_Footer.PNG](https://devnet.logianalytics.com/hc/article_attachments/4415492420887/custom_email_footer_500x495.png)](https://devnet.logianalytics.com/hc/article_attachments/4415504312855/custom_email_footer.png)
