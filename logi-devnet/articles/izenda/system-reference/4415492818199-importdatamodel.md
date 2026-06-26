---
title: "ImportDataModel"
id: 4415492818199
section: "System Reference"
category: "Izenda"
url: https://devnet.logianalytics.com/hc/en-us/articles/4415492818199-ImportDataModel
updated_at: 2021-12-10T03:08:54Z
---

# ImportDataModel

# ImportDataModel

| Field | NULL | Description | Note |
| --- | --- | --- | --- |
| **DataModelFileId**  string |  | The id of \*.bidm file uploaded to the server using the external API ([Import & Export](https://devnet.logianalytics.com/hc/en-us/articles/4415512083095-Import-Export)) |  |
| **DestinationTenants**  array of objects |  | An array of [ImportDataModelTenant](https://devnet.logianalytics.com/hc/en-us/articles/4415512011543-ImportDataModelTenant) objects |  |

**Sample**:

```
{"DataModelFileId":"4ba9b973-629b-458b-94fc-f901dba49852_DatamodelofSystemtenant","DestinationTenants":[{"Name":"YourDestinationTenantName","Mappings":[{"FromConnectionName":"Northwind","FromSchemaName":"dbo","ToConnectionName":"Northwind","ToSchemaName":"dbo"}]}]}
```
