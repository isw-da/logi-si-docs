---
title: "Scheduler Results and Logging"
id: 4419715557143
section: "Reports - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419715557143-Scheduler-Results-and-Logging
updated_at: 2022-07-17T02:23:01Z
---

# Scheduler Results and Logging

# Scheduler Results and Logging

The Scheduler service can write out two types of information about its attempts to run tasks: **results files** and an **operational log**.

The results file contains details about the parameters passed to the targeted Process task, time stamps, a final status, and any error message passed through the Logi Server Engine.

Operational logs contain lower-level details about the internal operations of the web service itself and any errors it encounters. Whether there will be *any* logging and the amount of detail in the log depends on the "logging level" specified in the Scheduler's \_Settings.lgx file.

In addition, the Scheduler updates a scheduled task's database record after each run attempt. For example, the success or failure of each Scheduler task's last attempted run is written in its database record in the "WasSuccessfulLastRun" column, and the fully-qualified path and filename of the results file generated for each run attempt is written to the "TaskResults" column. This allows easy programmatic access to run attempt results from within reports, using DataLayer.Scheduler, and
can also be very helpful in diagnosing problems.

## Results Files

As mentioned above, a results file will be created for each run attempt. These are .xml text files and are stored in:
(Windows .NET) C:\Program Files\LogiXML IES Dev\LogiXML Scheduler Service\Log  
(Windows Java)C:\Program Files\LogiXML IES Dev\LogiXML Scheduler Service Java\Log  
(Linux/UNIX) <installFolder>/Log

A typical results file name is: rdSchedulerTask-8-d55cadb8-e243-437d-8587-d190417bdcb2.xml

![](https://devnet.logianalytics.com/hc/article_attachments/7522770228759/usingsched_08.png)

The example above shows the XML data in a results file. The contents will vary and may include an error message. These files can be read using a Logi report definition for the purpose of displaying task run status information (this is how the Scheduler Console sample app gets its task status).

![](https://devnet.logianalytics.com/hc/article_attachments/7522725232151/criticalicon.png) Results files are small, typically about 800 bytes, but they will accumulate over time and may consume excessive server storage if ignored. It's the developer's or server administrator's responsibility to manage these files.

## Error Notifications

You now have the option to receive automated email notifications when a Scheduler report errors. Developers have the flexibility to define their own custom logic for error handling. If the Scheduler service has access to @Session error messages, the developer can use that to write a custom logic accordingly.

This feature can be enabled by adding the constant "SchedulerErrorEmail" in application \_Settings. The value of this constant is the admin's email address; however, multiple addresses are supported, separated by ";". If there is no constant or the value is empty, this function is disabled.

![](https://devnet.logianalytics.com/hc/article_attachments/7522725179159/noteicon.png) If the receiving email address is invalid, the error will be also logged in Scheduler task log file and the error message email will not be sent.

The first smtp connection in application \_Settings is used to send an error message email. If there is no smtp connection, an error will be logged in the Scheduler task log file.

You can customize error message email content (send and receive email address, subject, body) by creating DMF rdWeb1/\_SupportFiles/rdSchedulerEmail\_DMF.xml Initial content can be customized like this:

<ScheduleMods>

<SetAttribute XPath="." AttributeName="EmailSubject" Value="Failed to schedule task" />

<SetAttribute XPath="." AttributeName="EmailBody" Value="Error message: " />

<SetAttribute XPath="." AttributeName="FromEmailAddress" Value="" />

<SetAttribute XPath="." AttributeName="ToEmailAddress" Value="" />

</ScheduleMods>

The following template points to the above-mentioned DMF file: rdTemplate/rdEmail/rdSchedulerErrorEmailTemplate.lgx

## Operational Log

As mentioned above, if the Scheduler's settings file is so configured, operational details will be written to a log.The log is:(Windows .NET) The Windows Event Log   
(Windows Java)C:\Program Files\LogiXML IES Dev\LogiXML Scheduler Service Java\Log\LogiScheduler.log  
(Linux/UNIX) <installFolder>/Log/LogiScheduler.log

The Java log file, "LogiScheduler.log", is a text file written using the [Apache Log4j 2 Logging Library](http://logging.apache.org/log4j/2.x/index.html) and it can be viewed with any generic text reader or log viewer tool. ![](https://devnet.logianalytics.com/hc/article_attachments/7522725232151/criticalicon.png) You must update to Log4j v2.15 to mitigate this 0 day vulnerability. For more information about this vulnerability, refer to [this statement](https://devnet.logianalytics.com/hc/en-us/articles/4415781801751).

![](https://devnet.logianalytics.com/hc/article_attachments/7522761850263/usingsched_09.png)

The Windows Event Log, shown above, can be viewed using the **Event Viewer** administrative tool, and entries are listed in Applications and Service Logs, under "Logi Info".

You can automate the cleanup of scheduler logs by adding three attributes to the scheduler settings file:

1. rdCleanUpSchedulerLog: This attribute enables or disables Scheduler Log Clean up. The default value of this constant is "False", no clean up of Scheduler Logs. To automate clean up, set this value to "True".
2. rdSchedulerLogCleanupInterval: Set this attribute to specify the time, in minutes, between clean ups. Default value is 5 minutes. It's triggered by scheduler pings, not by the Info Engine.
3. rdSchedulerLogLifespan: The minimum file age, in minutes, before a file qualifies to be deleted when the clean up runs. The default value of this attribute is *60* and the unit of measurement is minute.
