---
title: "Scheduled Dashboard Report Properties"
id: 4402552775959
section: "Use Dashboards and Visuals in Composer v5"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4402552775959-Scheduled-Dashboard-Report-Properties
updated_at: 2021-09-15T02:20:59Z
---

# Scheduled Dashboard Report Properties

# Scheduled Dashboard Report Properties

Specific properties control the behavior of scheduled dashboard reports. These properties are stored in `zoomdata.properties`.

| Property | Required? | Description |
| --- | --- | --- |
| `dashboard.scheduling.screenshot.png.height` | No | Identifies the height (in pixels) of the screenshot PNG file that will be sent. The default is 720 pixels. |
| `dashboard.scheduling.screenshot.png.width` | No | Identifies the width (in pixels) of the screenshot PNG file that will be sent. The default is 1280 pixels. |
| `dashboard.scheduling.screenshot.timeout` | No | Specifies the timeout (in seconds) to take a screenshot for a dashboard email report. The default is 60 seconds.  Note: The time specified by this property must be less than or equal to the time set by the `screenshot.service.http.client.read.timeout.milliseconds` property. If you increase the value of this property, make sure that you increase the value of the `screenshot.service.http.client.read.timeout.milliseconds property` accordingly. Bear in mind that this property is specified in seconds, but the `screenshot.service.http.client.read.timeout.milliseconds` property is specified in milliseconds. |
| `mail.from` | Yes | Specifies the email address identifying where the email comes from. |
| `mail.login` | Yes | Specifies the email login to use to access the mail server. |
| `mail.password` | Yes | Specifies the password associated with the email login identified in the `mail.login` property. |
| `screenshot.service.http.client.connect.timeout.milliseconds` | No | Specifies the number of milliseconds that can elapse before Composer stops trying to connect to the screenshot microservice client. The default is 10000 milliseconds. |
| `screenshot.service.http.client.read.timeout.milliseconds` | No | Specifies the number of milliseconds that can elapse before Composer stops trying to read from the screenshot microservice client. The default is 60000 milliseconds.  Note: If you increase the time set by the `dashboard.scheduling.screenshot.timeout` property, make sure that you increase the value of this property as well. The total time set by `screenshot.service.http.client.read.timeout.milliseconds` should always be greater than or equal to the time set by the `dashboard.scheduling.screenshot.timeout` property. Bear in mind that this property is specified in milliseconds, but the `dashboard.scheduling.screenshot.timeout` property is specified in seconds. |
| `screenshot.service.http.client.write.timeout.milliseconds` | No | Specifies the number of milliseconds that can elapse before Composer stops trying to write to the screenshot microservice client. The default is 60000 milliseconds. |

In addition, JavaMail properties should be added to the `zoomdata.properties` file to identify the mail server and other mail properties required to use that server to send the scheduled dashboard (for example, `mail.smtp.auth, mail.smtp.host`, `mail.smtp.port`, `mail.imap.host`, and `mail.imap.port`). Composer supports both IMAP and SMTP protocols. Complete descriptions of IMAP and SMTP protocol JavaMail properties can be found at these links:

* IMAP: <https://javaee.github.io/javamail/docs/api/com/sun/mail/imap/package-summary.html>
* SMTP: <https://javaee.github.io/javamail/docs/api/com/sun/mail/smtp/package-summary.html>

For information about the properties in the `zoomdata.properties` file, see [*zoomdata.properties Properties*](https://devnet.logianalytics.com/hc/en-us/articles/4402552734615-zoomdata-properties-Properties).

Log messages related to dashboard report scheduling are stored in the `zoomdata.log`[log file](https://devnet.logianalytics.com/hc/en-us/articles/4402537842071-Composer-Log-Files).
