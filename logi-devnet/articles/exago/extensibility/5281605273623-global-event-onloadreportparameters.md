---
title: "Global Event: OnLoadReportParameters"
id: 5281605273623
section: "Extensibility"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281605273623-Global-Event-OnLoadReportParameters
updated_at: 2022-05-03T22:08:13Z
---

# Global Event: OnLoadReportParameters

# Global Event: OnLoadReportParameters

The **OnLoadReportParameters** event passes a list of Parameter elements that can be reordered or modified before they are sent to the client for display. Called when report parameters are loaded, but before any processing has occurred. By default, parameters are sorted alphabetically by name.

## Signature

For custom code the args array is structured as follows:

`args[]` is contains one object, a list of Parameter elements.

For .NET Assemblies the method signature is as follows:

```
void EventHandlerName(SessionInfo sessionInfo, List<Parameter> parameters)
```

## Expected Return

The event has a void return value.
