---
title: "Global Event: OnReportSaveStart"
id: 5281605616279
section: "Extensibility"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281605616279-Global-Event-OnReportSaveStart
updated_at: 2022-05-03T22:08:11Z
---

# Global Event: OnReportSaveStart

# Global Event: OnReportSaveStart

The **OnReportSaveStart** Event occurs at the beginning of the save process for Advanced Reports, CrossTabs, Dashboards, Chained Reports and ExpressView.

Support for Dashboards and Chained Reports is available in *v2019.1.26*, *v2019.2.12* and *v2020.1.1*.

## Signature

For custom code the arguments array is structured as follows:

`args[]` is empty.

For .NET Assemblies the method signature is as follows:

```
string EventHandlerName(SessionInfo sessionInfo)
```

## Notes

The report being saved can be accessed through the sessionInfo object by using `sessionInfo.Report` for Advanced Reports, CrossTabs and ExpressViews. For Dashboards and Chained Reports, use `sessionInfo.ReportObject`.

## Expected Return

Expects a string return value. If null, the report will continue processing; if not null, represents the [Multi-Language Support](https://devnet.logianalytics.com/hc/en-us/articles/5281604247447-Multi-Language-Support), or string text to display to the user.
