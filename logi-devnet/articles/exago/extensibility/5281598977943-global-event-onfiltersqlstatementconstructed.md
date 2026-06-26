---
title: "Global Event: OnFilterSqlStatementConstructed"
id: 5281598977943
section: "Extensibility"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281598977943-Global-Event-OnFilterSqlStatementConstructed
updated_at: 2022-05-03T22:08:12Z
---

# Global Event: OnFilterSqlStatementConstructed

# Global Event: OnFilterSqlStatementConstructed

The **OnFilterSqlStatementConstructed** event occurs just before SQL is sent to the Data Source to retrieve data to populate a filter dropdown. This Event could be used to inspect, log or modify the SQL that is being used to populate the dropdown.

## Signature

For custom code the arguments array is structured as follows:

`args[]` contains:

0. a string representing the filter SQL

For .NET Assemblies the method signature is as follows:

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> Include the `WebReports.Api.Data` namespace.

```
string EventHandlerName(SessionInfo sessionInfo, string filtersSql, SqlObject sqlObject)
```

## Expected Return

The **OnFilterSqlStatementConstructed** Event expects a string value to be returned.

## Note

This Event will provide the SQL for the Filter Dropdown Object if that feature is being utilized. See [Data Objects](https://devnet.logianalytics.com/hc/en-us/articles/5281608202519-Data-Objects) for more information on [Filter Dropdown Objects](https://devnet.logianalytics.com/hc/en-us/articles/5281608202519-Data-Objects#Filter).
