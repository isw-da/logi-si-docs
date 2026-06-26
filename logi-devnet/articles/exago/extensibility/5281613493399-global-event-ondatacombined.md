---
title: "Global Event: OnDataCombined"
id: 5281613493399
section: "Extensibility"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281613493399-Global-Event-OnDataCombined
updated_at: 2022-05-03T22:08:13Z
---

# Global Event: OnDataCombined

# Global Event: OnDataCombined

The **OnDataCombined** Event allows the inspection and/or modification of the raw data set after retrieval from the Data Sources and initial combining within Exago. A common use of this event is to modify or blank sensitive data fields in a Report depending on the authorizations available to the user executing the report.

In *v2018.1* this event was extended to provide access to the active execution object, as well as the ability to modify report execution schema via the **SessionInfo** object. After modifying the execution schema, the method `Report.ReprocessAfterAlteration()` must be called in order to process the changes.

## Signature pre-v2018.1

For custom code the args array is structured as follows:

args[] contains a single DataTable of the combined data in position zero.

For .NET Assemblies the method signature is as follows:

```
DataTable EventHandlerName(SessionInfo sessionInfo, DataTable combinedData)
```

## Signature v2018.1+

For custom code the args array is structured as follows:

args[] contains a single DataTable of the combined data in position zero and the ActiveLocalExecution object in position one.

For .NET Assemblies the method signature is as follows:

```
DataTable EventHandlerName(SessionInfo sessionInfo, DataTable combinedData, ActiveLocalExecution execution)
```

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> The **ActiveLocalExecution** object is defined in the `WebReports.Api.Execute` namespace.

## Expected Return

The OnDataCombined Event expects a DataTable to be returned. The schema of the DataTable must match that of combinedData.

## Notes

In the DataTable, if a Data Object has an **Id** then that will be used as the column names, otherwise the database name will be used. Data Fields will always use their database names despite any **Column Metadata**.
