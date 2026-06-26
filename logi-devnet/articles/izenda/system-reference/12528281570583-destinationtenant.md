---
title: "DestinationTenant"
id: 12528281570583
section: "System Reference"
category: "Izenda"
url: https://devnet.logianalytics.com/hc/en-us/articles/12528281570583-DestinationTenant
updated_at: 2023-02-23T16:11:34Z
---

# DestinationTenant

# DestinationTenant

| Field | NULL | Description | Note |
| --- | --- | --- | --- |
| **id** string (GUID) | Y | The id of the tenant if available |  |
| **tenantId** string |  | The user-defined tenant id |  |
| **roleMappings** array of objects |  | An array of [RoleMapping](https://devnet.logianalytics.com/hc/en-us/articles/12528283059479-RoleMapping) objects |  |
| **databaseMappings** array of objects |  | An array of [DatabaseMapping](https://devnet.logianalytics.com/hc/en-us/articles/12528296875671-DatabaseMapping) objects |  |
| **overwrite** object |  | An [Overwrite](https://devnet.logianalytics.com/hc/en-us/articles/12528297493143-Overwrite) object |  |
| **lineNumber** integer |  | The line number of the item in config xml file |  |
