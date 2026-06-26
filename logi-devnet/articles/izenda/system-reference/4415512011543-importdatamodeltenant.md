---
title: "ImportDataModelTenant"
id: 4415512011543
section: "System Reference"
category: "Izenda"
url: https://devnet.logianalytics.com/hc/en-us/articles/4415512011543-ImportDataModelTenant
updated_at: 2021-12-10T03:08:56Z
---

# ImportDataModelTenant

# ImportDataModelTenant

| Field | NULL | Description | Note |
| --- | --- | --- | --- |
| **Name**  string |  | The name of the destination tenant |  |
| **Mappings**  array of objects |  | An array of [ImportDataModelMapping](https://devnet.logianalytics.com/hc/en-us/articles/4415512010391-ImportDataModelMapping) objects |  |

**Sample**:

```
{"Name":"YourDestinationTenantName","Mappings":[{"FromConnectionName":"Northwind","FromSchemaName":"dbo","ToConnectionName":"Northwind","ToSchemaName":"dbo"}]}
```
