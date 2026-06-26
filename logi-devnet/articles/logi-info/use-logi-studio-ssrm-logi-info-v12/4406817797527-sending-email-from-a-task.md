---
title: "Sending Email from a Task"
id: 4406817797527
section: "Use Logi Studio/SSRM - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817797527-Sending-Email-from-a-Task
updated_at: 2022-04-06T06:08:16Z
---

# Sending Email from a Task

# Sending Email from a Task

A process task also gives you the ability to send email messages, separately or in bulk.

![](https://devnet.logianalytics.com/hc/article_attachments/4417563115415/workproctask_22.png)

An example in [Running Datalayer and Data Table Rows](https://devnet.logianalytics.com/hc/en-us/articles/4406822481687-Running-Datalayer-and-Data-Table-Rows) demonstrated one method of sending out a mass mailing, but there's a second method you may want to use instead.

1. Add a **Procedure.Send Mail** element to your task, as shown above, and set its attributes as desired to configure the message to be sent. ![](https://devnet.logianalytics.com/hc/article_attachments/4417583587863/noteicon.png) The actual message (the "Email Body") can be formatted as *Plain Text* or *HTML*. Use @Data tokens to reference the data values that will be coming from your data source.
2. Beneath it, add a **Bulk Email Data Layer** element, which iterates through its child datalayer rows.
3. Beneath it, add an appropriate datalayer element to retrieve the data with the addressing information. If possible, use a query that includes a filter to eliminate records that have Null email addresses.  
     
     
   ![](https://devnet.logianalytics.com/hc/article_attachments/4417575561751/workproctask_23.png)
4. Optionally, add one or more **Attachment** elements beneath the Procedure.Send Mail element. Set its **Filename** attribute to the fully-qualified file path and file name of the file to be attached. ![](https://devnet.logianalytics.com/hc/article_attachments/4417583587863/noteicon.png) The @Function token for your application folder can be used here, as shown above. Set the **Display Name** attribute to the text that you wish to appear identifying the attachment in the recipient's mail reader.   
     
   Keep in mind that your mail server may impose restrictions on the *size* of file attachments.

![](https://devnet.logianalytics.com/hc/article_attachments/4417583587863/noteicon.png) Procedure.Send Mail element supports TLS/SSL encryption, allowing, for example, GMail to be used as an SMTP server. Set the related **Connection.SMTP** element's **SMTP Authentication Method** attribute to *3* to invoke this, and its **SMTP Port** attribute may need to be set to *587*.

![](https://devnet.logianalytics.com/hc/article_attachments/4417575435927/notev12.7base.png)When sending email from a Java application to an older SMTP server, attachments with long file names (> 60 chars.) result in a split name that cannot be clicked to be viewed by the recipient. To solve this, keep attachment names short, or add this JVM option:

-Dmail.mime.encodeparameters=false

![](https://devnet.logianalytics.com/hc/article_attachments/4417562936855/criticalicon.png) Sending out thousands of emails may have an impact on your network bandwidth and your email server performance, so use caution before "opening the floodgates" and sending out a zillion messages!

DevNet includes a [sample application](https://devnet.logianalytics.com/hc/en-us/articles/360050373673-Send-Email-Sample-Application) that demonstrates the use of a process task to send email.
