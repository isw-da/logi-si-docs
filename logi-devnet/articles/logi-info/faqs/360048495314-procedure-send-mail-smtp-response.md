---
title: "Procedure.Send Mail SMTP response"
id: 360048495314
section: "FAQs"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/360048495314-Procedure-Send-Mail-SMTP-response
updated_at: 2020-07-27T22:25:12Z
---

# Procedure.Send Mail SMTP response

**Question:**

My scheduled reports aren't being delivered, and Logi info is not returning an error. How do I troubleshoot?

**Answer:**Procedure.Send Mail doesn't return error messages if the SMTP server rejects the email or if the SMTP connection fails.

If there are no errors in the Info application logs, check the SMTP log files if available. Some SMTP servers change the character encoding of the attachments. This may inflate the file size causing the file to exceed the attachment limit even if export file we see in rdDownload doesn't exceed the size limit. For example, an example SMTP server, SmarterMail increases the attachment size roughly 35-40% ([link](https://portal.smartertools.com/kb/a3113/set-maximum-email-message-size-for-outbound-and-inbound-messages.aspx)).

**Further Reading**

SmarterMail: <https://portal.smartertools.com/kb/a3113/set-maximum-email-message-size-for-outbound-and-inbound-messages.aspx>
