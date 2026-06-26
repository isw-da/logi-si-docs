---
title: "Connecting to an SMPTP Server"
id: 4419723144471
section: "Use Logi Studio/SSRM - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419723144471-Connecting-to-an-SMPTP-Server
updated_at: 2022-04-01T09:26:37Z
---

# Connecting to an SMPTP Server

# Connecting to an SMPTP Server

The basic connection for sending an email is managed by the Connection.SMTP element, and requires that you have an SMTP server set up. Many web servers include an SMTP server, though it may not be installed by default along with the web server. Ensure that you have an SMTP server installed and properly configured.

![](https://devnet.logianalytics.com/hc/article_attachments/4419699888919/sendsms_02.png)![](https://devnet.logianalytics.com/hc/article_attachments/4419707060631/sendsms_02a.png)  

As shown above, the **Connection.SMTP** element is added beneath the Connections element in the \_Settings definition and its attributes are configured as appropriate for the SMTP server.

The following attributes are available for Connection.SMTP:

| Attribute | Description |
| --- | --- |
| ID | (Required) A unique element identifier. |
| SMTP Authentication Account | Specifies the account name to be used to login to the SMTP server. |
| SMTP Authentication Method | Specifies the method to be used to authenticate the login. Values can be:  *0* = None (the default) *1* = Login *2* = Use Cram-MD5 challenge-response authentication *3* = Use TLS/SSL encrypted communications. May require use of SMTP Port = *587* |
| SMTP Authentication Password | Specifies the account password to be used to login to the SMTP server. |
| SMTP Connection Timeout | Specifies the amount of time, in seconds, before the request to connect to the SMTP server is presumed to have failed. Default: *30 seconds* |
| SMTP EHLO Domain | Specifies an alternate EHLO domain name to be sent to the server. |
| SMTP Port | Specifies the port used by the SMTP server. Default: *25* TLS/SSL Authentication may require port *587* |
| SMTP Server | (Required) Specifies The computer name or IP address of the SMTP server. |
