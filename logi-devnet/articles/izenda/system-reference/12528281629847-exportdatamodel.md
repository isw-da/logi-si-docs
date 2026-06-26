---
title: "ExportDataModel"
id: 12528281629847
section: "System Reference"
category: "Izenda"
url: https://devnet.logianalytics.com/hc/en-us/articles/12528281629847-ExportDataModel
updated_at: 2023-02-23T16:11:44Z
---

# ExportDataModel

# ExportDataModel

| Field | NULL | Description | Note |
| --- | --- | --- | --- |
| **SourceTenant** string |  | The name of the source tenant (or blank if it is System level). |  |
| **SelectedConnections** array of objects |  | An array of [Connection](https://devnet.logianalytics.com/hc/en-us/articles/12528281159575-Connection) objects.  Note  It is enough to specify only the names of the Сonnector, Schema, and DataSource, as in the example below. |  |

**Sample**:

```
{"SourceTenant":"YourSourceTenantName","SelectedConnections":[{"Name":"Northwind","DBSource":{"QuerySources":[{"Name":"dbo","QuerySources":[{"Name":"Orders"},{"Name":"Order Details"}]}]}}]}
```
