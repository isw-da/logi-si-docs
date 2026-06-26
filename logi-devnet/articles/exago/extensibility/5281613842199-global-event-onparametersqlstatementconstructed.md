---
title: "Global Event: OnParameterSqlStatementConstructed"
id: 5281613842199
section: "Extensibility"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281613842199-Global-Event-OnParameterSqlStatementConstructed
updated_at: 2022-05-03T22:08:11Z
---

# Global Event: OnParameterSqlStatementConstructed

# Global Event: OnParameterSqlStatementConstructed

Called after a parameter dropdown object is constructed. Allows for modifying the object SQL.

## Signature

For custom code the args array is structured as follows:

args[] contains one object, the SQL string passed to the server to construct the parameter dropdown.

For .NET Assemblies the method signature is as follows:

```
string EventHandlerName(SessionInfo sessionInfo, string sqlStatement)
```

## Expected Return

The event expects a string return value: The (modified) SQL statement to be passed to the server to construct the parameter dropdown.
