---
title: "Global Event: OnReportFailValidation"
id: 5281622228759
section: "Extensibility"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281622228759-Global-Event-OnReportFailValidation
updated_at: 2022-05-03T22:08:09Z
---

# Global Event: OnReportFailValidation

# Global Event: OnReportFailValidation

The **OnReportFailValidation** server event occurs when a user attempts to edit or run a report which has errors. When a user edits a report which fails validation, a message dialog shows the user the list of errors with the report. This server event can be used to customize the error messages.

## Signature

For custom code the args array is structured as follows:

args[] contains one argument, the list of ValidationErrors. A ValidationError is an object containing an enum for the error type, and two strings for more detailed message information about the error. The message strings can be a text string or a language file id element.

For .NET Assemblies the method signature is as follows:

```
string EventHandlerName(SessionInfo sessionInfo, List<ValidationErrors> errorList)
```

## Expected Return

The OnReportFailValidation server event expects a List<ValidationErrors> return object.

The list of error types is as follows:

DataObjectNotFound,  
SortDataFieldNotFound,  
FilterDataFieldNotFound,  
LinkedDataFieldNotFound,  
MinMaxFilterDataFieldNotFound,  
JoinDataObjectNotFound,  
JoinNotFound,  
JoinDataFieldNotFound,  
ChartDataFieldNotFound,  
MapDataFieldNotFound,  
CellDataFieldNotFound,  
RowGroupNameNotFound,  
RowGroupFormulaNameNotFound,  
ChartCellIdNotFound,  
MapCellIdNotFound,  
MergedCellsAcrossSections,  
CrossTabIdNotFound,  
CrossTabCellIdNotFound,  
ColumnSortByFieldNotFound,  
ChildReportNotFound,  
ExpressViewColumnMissingEntity,  
ExpressViewColumnMissingField,  
ExpressViewGroupMissingField,  
ExpressViewFilterMissingField,  
ExpressViewChartMissingField,  
None
