---
title: "Global Event: OnExecuteSqlStatementConstructed"
id: 5281613621399
section: "Extensibility"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281613621399-Global-Event-OnExecuteSqlStatementConstructed
updated_at: 2022-05-03T22:08:15Z
---

# Global Event: OnExecuteSqlStatementConstructed

# Global Event: OnExecuteSqlStatementConstructed

The **OnExecuteSqlStatementConstructed** Event occurs just before SQL is sent to the Data Source to retrieve data for report execution. This Event could be used to inspect, log or modify the SQL that is being used for report execution.

## Signature

For custom code the arguments array is structured as follows:

`args[]` contains:

0. a string representing the execution SQL
1. a `SqlObject` class wrapping the execution SQL string in position one.

For .NET Assemblies the method signature is as follows:

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> Include the `WebReports.Api.Data` namespace.

```
string EventHandlerName(SessionInfo sessionInfo, string executionSql, SqlObject sqlObject)
```

## Expected Return

The **OnExecuteSqlStatementConstructed** Event expects either a SQL string return, to override the default execution SQL, or null, in which case the execution will continue as normal.
