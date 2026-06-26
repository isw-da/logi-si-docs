---
title: "Global Event: OnScheduledReportComplete"
id: 5281622290839
section: "Extensibility"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281622290839-Global-Event-OnScheduledReportComplete
updated_at: 2022-05-03T22:08:10Z
---

# Global Event: OnScheduledReportComplete

# Global Event: OnScheduledReportComplete

The **OnScheduledReportComplete** server event occurs when a scheduled report execution completes, regardless of whether it was successful or not. It precedes creation of the output file. The schedule job object is passed in the args array so the job can be examined for potential errors.

## Signature

For custom code the args array is structured as follows:

`args[]` contains one argument, a SchedulerJob object representing the completed scheduled execution.

For .NET Assemblies the method signature is as follows:

```
bool EventHandlerName(SessionInfo sessionInfo, SchedulerJob job)
```

## Expected Return

The OnScheduledReportComplete server event expects a Boolean return value to indicate whether to create the report output for the job. Returns **TRUE** if the report output should be created, returns **FALSE** if the report output should not be created.
