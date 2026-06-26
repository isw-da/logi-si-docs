---
title: "Global Event: OnScheduledReportExecuteSuccess"
id: 5281591294615
section: "Extensibility"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281591294615-Global-Event-OnScheduledReportExecuteSuccess
updated_at: 2022-05-03T22:08:10Z
---

# Global Event: OnScheduledReportExecuteSuccess

# Global Event: OnScheduledReportExecuteSuccess

The **OnScheduledReportExecuteSuccess** event occurs when a scheduled report execution is finished. This event can be used to create an audit log of scheduled reports.

## Signature

For custom code the args array is structured as follows:

`args[]` is empty.

For .NET Assemblies the method signature is as follows:

```
bool EventHandlerName(SessionInfo sessionInfo)
```

## Expected Return

The **OnScheduledReportExecuteSuccess** Event expects a Boolean to be returned. Returning *True* will prevent the scheduled report from being sent. Returning *False* will allow the report schedule to proceed with processing.

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> This server event is called for remote execution of reports. However, the return value will be ignored as there is no email to be prevented.
