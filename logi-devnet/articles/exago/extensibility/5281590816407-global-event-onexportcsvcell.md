---
title: "Global Event: OnExportCsvCell"
id: 5281590816407
section: "Extensibility"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281590816407-Global-Event-OnExportCsvCell
updated_at: 2022-05-03T22:08:14Z
---

# Global Event: OnExportCsvCell

# Global Event: OnExportCsvCell

Called prior to exporting a CSV cell for the purpose of overriding the standard export results. If the server event is defined, it is called for every visible cell in a report on CSV export. Allows for customizing cell contents on a cell-by-cell basis.

## Signature

For custom code the args array is structured as follows:

args[] is contains two objects: The first argument args[0] is the Cell object in its entirety, which contains a variety of cell attribute information including row and col indices, cell type, format, convenience flags, linked report data, etc. The second argument args[1] provides the raw text of the cell as a string.

For .NET Assemblies the method signature is as follows:

```
string EventHandlerName(SessionInfo sessionInfo, Cell cell, string rawCellText)
```

## Expected Return

The event expects a string or null return value. If null is returned, the event will interpret this as a flag indicating that no custom CSV data is being provided, and to return the report’s CSV output. If a string is returned (including an empty string), the cell will output the string as provided, overriding the report data for that cell.
