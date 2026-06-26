---
title: "Global Event: OnExceptionThrown"
id: 5281583292311
section: "Extensibility"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281583292311-Global-Event-OnExceptionThrown
updated_at: 2022-05-03T22:08:13Z
---

# Global Event: OnExceptionThrown

# Global Event: OnExceptionThrown

**OnExceptionThrown** is called when an application exception is thrown in the user interface. Generally used to pass additional or different information to the log file. For more information, see [Accessing the Log File](https://devnet.logianalytics.com/hc/en-us/articles/5281647183383-Accessing-the-Log-File).

## Signature

For custom code, the `args[]` array is structured as follows:

0. the `System.Exception` object
1. the `WebReports.Api.Common.Logger` object — provides write access to the log file
2. string of JSON data with the AJAX arguments which can provide more information in the log regarding the users requests which resulted in the exception being thrown.

For .NET Assemblies the method signature is as follows:

```
bool EventHandlerName(SessionInfo sessionInfo, Exception exception, Logger logger, string jsonArgs)
```

## Expected Return

The **OnExceptionThrown** event expects a Boolean return value. When *true*, logging of the exception is stopped.
