---
title: "ImportDataModel"
id: 12528281803671
section: "System Reference"
category: "Izenda"
url: https://devnet.logianalytics.com/hc/en-us/articles/12528281803671-ImportDataModel
updated_at: 2023-02-23T16:12:20Z
---

# ImportDataModel

ImportDataModel

| Field | NULL | Description | Note |
| --- | --- | --- | --- |
| **DataModelFileId** string |  | The id of \*.bidm file uploaded to the server using the external API ([Import & Export](https://devnet.logianalytics.com/hc/en-us/articles/12528283799063-Import-Export)) |  |
| **DestinationTenants** array of objects |  | An array of [ImportDataModelTenant](https://devnet.logianalytics.com/hc/en-us/articles/12528297374615-ImportDataModelTenant) objects |  |

**Sample**:

```
{"DataModelFileId":"4ba9b973-629b-458b-94fc-f901dba49852_DatamodelofSystemtenant","DestinationTenants":[{"Name":"YourDestinationTenantName","Mappings":[{"FromConnectionName":"Northwind","FromSchemaName":"dbo","ToConnectionName":"Northwind","ToSchemaName":"dbo"}]}]}
```
