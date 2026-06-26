---
title: "Global Event: OnDataFieldsRetrieved"
id: 5281613541655
section: "Extensibility"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281613541655-Global-Event-OnDataFieldsRetrieved
updated_at: 2022-05-03T22:08:14Z
---

# Global Event: OnDataFieldsRetrieved

# Global Event: OnDataFieldsRetrieved

The **OnDataFieldsRetrieved** Event occurs after Data Fields are retrieved for a specific Data Object. This event is commonly used to change the order Data Fields are displayed in the Data Menu of the Report Designer.

## Signature

For custom code the arguments array is structured as follows:

`args[]` contains three objects:

0. a `System.Data.DataTable` containing the names and metadata of the Data Fields
1. the Data Object as a `WebReports.Api.Reports.Entity` object
2. a reference to a `WebReports.Api.Data.DataObjectBase` object which calls the event.

For .NET Assemblies the method signature is as follows:

```
DataTable EventHandlerName(SessionInfo sessionInfo, DataTable originalDataFields, Entity dataObject, DataObjectBase eventCaller)
```

## Notes

The DataTable being being passed to the event in the first argument has already applied Column Metadata.

## Expected Return

Expects a System.Data.DataTable return value, which represents the modified data.
