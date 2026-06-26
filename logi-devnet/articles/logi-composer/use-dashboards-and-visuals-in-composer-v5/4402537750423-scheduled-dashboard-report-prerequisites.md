---
title: "Scheduled Dashboard Report Prerequisites"
id: 4402537750423
section: "Use Dashboards and Visuals in Composer v5"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4402537750423-Scheduled-Dashboard-Report-Prerequisites
updated_at: 2021-09-15T02:20:59Z
---

# Scheduled Dashboard Report Prerequisites

# Scheduled Dashboard Report Prerequisites

To schedule a dashboard report, you must be an administrator or assigned to a group with the **Can Create Scheduled Reports**[privilege](https://devnet.logianalytics.com/hc/en-us/articles/4402537668503-Group-Privilege-Reference).

In addition, JavaMail API properties should be added to the `zoomdata.properties` file to identify the mail server and other mail properties required to use that server to send the scheduled dashboard (for example, `mail.smtp.auth, mail.smtp.host`, `mail.smtp.port`, `mail.imap.host`, and `mail.imap.port`). Composer supports both IMAP and SMTP protocols. Complete descriptions of IMAP and SMTP protocol JavaMail properties can be found at these links:

* IMAP: <https://javaee.github.io/javamail/docs/api/com/sun/mail/imap/package-summary.html>
* SMTP: <https://javaee.github.io/javamail/docs/api/com/sun/mail/smtp/package-summary.html>

For information about the properties in the `zoomdata.properties` file, see [*zoomdata.properties Properties*](https://devnet.logianalytics.com/hc/en-us/articles/4402552734615-zoomdata-properties-Properties).

Finally, if you will be scheduling many concurrent dashboard reports, you should consider altering the memory configuration settings for the Composer installation and Screenshot service pool configuration settings. See [*Configuring Memory Settings*](https://devnet.logianalytics.com/hc/en-us/articles/4402537688471-Configuring-Memory-Settings) and [*Setting Up the Screenshot Microservice*](https://devnet.logianalytics.com/hc/en-us/articles/4402552835479-Setting-Up-the-Screenshot-Microservice).

Log messages related to dashboard report scheduling are stored in the `zoomdata.log`[log file](https://devnet.logianalytics.com/hc/en-us/articles/4402537842071-Composer-Log-Files).
