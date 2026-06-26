---
title: "Debugging Discovery v3.0"
id: 4406817354519
section: "Developer Tools - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817354519-Debugging-Discovery-v3-0
updated_at: 2022-04-06T06:10:42Z
---

# Debugging Discovery v3.0

# Debugging Discovery v3.0

The services that support Discovery v3.0,
**Logi Application Service** and **Logi Data Service**, have their
own logs which can be useful for debugging. Assuming a default
installation location, the logs are located in:

C:\LogiAnalytics\Discovery\platform\logs

There are a variety of log files but focus on the two for the services:
logiApplicationService.yyyymmdd.log
and
logiDataService.log. The files are created using Log4j and can be easily viewed with
Notepad++ or many other free log viewers.
![](https://devnet.logianalytics.com/hc/article_attachments/4417562936855/criticalicon.png) You must update to Log4j v2.15 to mitigate this 0 day vulnerability. For more information about this vulnerability, refer to [this statement](https://devnet.logianalytics.com/hc/en-us/articles/4415781801751).

Debugging can be turned on and off in this settings file:

C:\LogiAnalytics\Discovery\platform\settings\logiApplicationService.json

By default, all information, warning, and error messages are logged:

{  
 "disableSchemaValidation": false,  
 "logiApplicationService": {  
 "description": "Platform
logiApplicationService Configuration",  
"logLevel": "debug",  
 "corsOriginWhiteList": "\*",  
 "accessTokenGracePeriod": 120,  
 "system": {  
 "pollingIntervalSeconds":
15,  
 "pollingTimeoutMinutes":
-1  
 },

In the file, change the "logLevel" value from "error"
to "debug", as shown above, to enable debug logging. You'll need
to stop and restart the two services after editing the settings file.

Status 201 [DEBUG] - 2018-01-11T08:07:05-0500 - Response Received
(521bbef0-f6d0-11e7-86ba-97facc95ecaa)

An example log debug entry is shown above.
