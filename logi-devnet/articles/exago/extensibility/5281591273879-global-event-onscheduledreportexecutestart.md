---
title: "Global Event: OnScheduledReportExecuteStart"
id: 5281591273879
section: "Extensibility"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281591273879-Global-Event-OnScheduledReportExecuteStart
updated_at: 2022-05-03T22:08:10Z
---

# Global Event: OnScheduledReportExecuteStart

# Global Event: OnScheduledReportExecuteStart

This server event is available in *v2018.1+*. The **OnScheduledReportExecuteStart** Event occurs at the beginning of the Report Execution process when run by a Scheduler Service. Occurs for any job run by a scheduler service, including scheduled executions, remote executions, and execution cache rebuilds. This Event could be used to check and modify properties of a report and log or stop execution.

## Signature

For custom code the args array is structured as follows:

`args[]` contains a **SchedulerJob** object at position 0, which can be used to access and modify properties of the active execution and schedule, including the report object, email and schedule information.

For .NET Assemblies the method signature is as follows:

```
string EventHandlerName(SessionInfo sessionInfo, SchedulerJob job)
```

## Expected Return

The **OnScheduledReportExecuteStart** Event expects a string to be returned. Based on the string returned there are three possible results:

* **Null / White space** – If the string is `null` or white space then the report execution will continue as expected.
* **LanguageId** – If the string matches the id of any element in the language files then the string of that language element will be displayed as a message to the user and the report execution will terminate. For more information see [Multi-Language Support](https://devnet.logianalytics.com/hc/en-us/articles/5281604247447-Multi-Language-Support).
* **Other –** If the string does not match the id of any element in the language files then the returned value will be displayed as a message to the user and the report execution will terminate.

## Notes

The report being executed can be accessed through the ScheduleJob object by using job.Report. The schedule information can be accessed through job.ScheduleInfo.
