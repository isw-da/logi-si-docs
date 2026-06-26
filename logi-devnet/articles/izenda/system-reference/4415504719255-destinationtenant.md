---
title: "DestinationTenant"
id: 4415504719255
section: "System Reference"
category: "Izenda"
url: https://devnet.logianalytics.com/hc/en-us/articles/4415504719255-DestinationTenant
updated_at: 2021-12-10T03:08:42Z
---

# DestinationTenant

# DestinationTenant

| Field | NULL | Description | Note |
| --- | --- | --- | --- |
| **id**  string (GUID) | Y | The id of the tenant if available |  |
| **tenantId**  string |  | The user-defined tenant id |  |
| **roleMappings**  array of objects |  | An array of [RoleMapping](https://devnet.logianalytics.com/hc/en-us/articles/4415492880023-RoleMapping) objects |  |
| **databaseMappings**  array of objects |  | An array of [DatabaseMapping](https://devnet.logianalytics.com/hc/en-us/articles/4415511991319-DatabaseMapping) objects |  |
| **overwrite**  object |  | An [Overwrite](https://devnet.logianalytics.com/hc/en-us/articles/4415492824087-Overwrite) object |  |
| **lineNumber**  integer |  | The line number of the item in config xml file |  |
