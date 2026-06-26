---
title: "ImportDataModelTenant"
id: 12528297374615
section: "System Reference"
category: "Izenda"
url: https://devnet.logianalytics.com/hc/en-us/articles/12528297374615-ImportDataModelTenant
updated_at: 2023-02-23T16:13:05Z
---

# ImportDataModelTenant

# ImportDataModelTenant

| Field | NULL | Description | Note |
| --- | --- | --- | --- |
| **Name** string |  | The name of the destination tenant |  |
| **Mappings** array of objects |  | An array of [ImportDataModelMapping](https://devnet.logianalytics.com/hc/en-us/articles/12528281813911-ImportDataModelMapping) objects |  |

**Sample**:

```
{"Name":"YourDestinationTenantName","Mappings":[{"FromConnectionName":"Northwind","FromSchemaName":"dbo","ToConnectionName":"Northwind","ToSchemaName":"dbo"}]}
```
