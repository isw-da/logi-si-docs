---
title: "ExportDataModel"
id: 4415504724759
section: "System Reference"
category: "Izenda"
url: https://devnet.logianalytics.com/hc/en-us/articles/4415504724759-ExportDataModel
updated_at: 2021-12-10T03:08:47Z
---

# ExportDataModel

# ExportDataModel

| Field | NULL | Description | Note |
| --- | --- | --- | --- |
| **SourceTenant**  string |  | The name of the source tenant (or blank if it is System level). |  |
| **SelectedConnections**  array of objects |  | An array of [Connection](https://devnet.logianalytics.com/hc/en-us/articles/4415504700055-Connection) objects.  Note  It is enough to specify only the names of the Сonnector, Schema, and DataSource, as in the example below. |  |

**Sample**:

```
{"SourceTenant":"YourSourceTenantName","SelectedConnections":[{"Name":"Northwind","DBSource":{"QuerySources":[{"Name":"dbo","QuerySources":[{"Name":"Orders"},{"Name":"Order Details"}]}]}}]}
```
