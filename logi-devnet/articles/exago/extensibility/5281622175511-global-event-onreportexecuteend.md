---
title: "Global Event: OnReportExecuteEnd"
id: 5281622175511
section: "Extensibility"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281622175511-Global-Event-OnReportExecuteEnd
updated_at: 2022-05-03T22:08:10Z
---

# Global Event: OnReportExecuteEnd

# Global Event: OnReportExecuteEnd

The **OnReportExecuteEnd** Event occurs at the end of the Report Execution process. This Event could be used to track which report executions return data.

This event will be called for all report execution types, including those via:

* Execution in the web app process (remote execution disabled)
* Remote execution
* Scheduled execution (including those using the **Scheduler Queue**)
* Batch scheduled executions
* [REST — GetExecute](https://devnet.logianalytics.com/hc/en-us/articles/5281630138647-REST-GetExecute)

## Signature

For custom code the args array is structured as follows:

args[] contains a single Boolean indicating if Data qualified (True), or not (False).

For .NET Assemblies the method signature is as follows:

```
string EventHandlerName(SessionInfo sessionInfo, bool DataQualified)
```

## Expected Return

Anything can be returned to the OnReportExecuteEnd Event. Any return value will be ignored.
