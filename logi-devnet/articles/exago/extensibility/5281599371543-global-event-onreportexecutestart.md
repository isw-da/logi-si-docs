---
title: "Global Event: OnReportExecuteStart"
id: 5281599371543
section: "Extensibility"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281599371543-Global-Event-OnReportExecuteStart
updated_at: 2022-05-03T22:08:12Z
---

# Global Event: OnReportExecuteStart

# Global Event: OnReportExecuteStart

The **OnReportExecuteStart** Event occurs at the beginning of the report execution cycle. This Event could be used to check and modify properties of a report and log or stop execution.

This event is called for all report executions, including those via:

* Execution in the web app process (remote execution disabled)
* Remote execution
* Scheduled execution (including those using the **Scheduler Queue**)
* Batch scheduled executions
* [REST — GetExecute](https://devnet.logianalytics.com/hc/en-us/articles/5281630138647-REST-GetExecute)

## Signature

For custom code the args array is structured as follows:

args[] is empty.

For .NET Assemblies the method signature is as follows:

```
string EventHandlerName(SessionInfo sessionInfo)
```

## Expected Return

The OnReportExecuteStart Event expects a string to be returned. Based on the return string there are three possible results.

* **Null / White space** — If the string is null or white space then the report execution will continue as expected.
* **LanguageId** — If the string matches the id of any element in the language files then the string of that language element will be displayed as a message to the user and the report execution will terminate. For more information see [Multi-Language Support](https://devnet.logianalytics.com/hc/en-us/articles/5281604247447-Multi-Language-Support).
* **Other** — If the string does not match the id of any element in the language files then the returned value will be displayed as a message to the user and the report execution will terminate.

## Notes

The report being executed can be accessed through the sessionInfo object by using `sessionInfo.Report`.
