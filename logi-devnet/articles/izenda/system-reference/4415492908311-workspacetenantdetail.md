---
title: "WorkspaceTenantDetail"
id: 4415492908311
section: "System Reference"
category: "Izenda"
url: https://devnet.logianalytics.com/hc/en-us/articles/4415492908311-WorkspaceTenantDetail
updated_at: 2021-12-10T03:10:08Z
---

# WorkspaceTenantDetail

# WorkspaceTenantDetail

| Field | NULL | Description | Note |
| --- | --- | --- | --- |
| **destinationConnections**  array of objects |  | An array of [Connection](https://devnet.logianalytics.com/hc/en-us/articles/4415504700055-Connection) objects. |  |
| **sourceConnections**  array of objects |  | An array of [Connection](https://devnet.logianalytics.com/hc/en-us/articles/4415504700055-Connection) objects. |  |
| **tenantName**  string |  | The name of the tenant |  |
| **tenantUniqueName**  string |  | The tenant unique name |  |

Inherited fields:

## WorkspaceTenant

| Field | NULL | Description | Note |
| --- | --- | --- | --- |
| **workspaceId**  string (GUID) | Y | The id of the workspace |  |
| **tenantId**  string (GUID) | Y | The id of the tenant if available |  |
| **status**  integer |  | The status of the workspace tenant   * 0 = Need Validated * 1 = Ready to Copy * 2 = Authentication Missing * 3 = Validation Error |  |
| **physicalDataModel**  string |  | The physical data structure in json format |  |
| **sourceDataModel**  string |  | The source data model in json format |  |
| **destinationHashCode**  string |  | The hashcode of the tenant data model |  |

Inherited fields:

### Entity

| Field | NULL | Description | Note |
| --- | --- | --- | --- |
| **id**  string (GUID) |  | The id of this object   Example: `572bd576-8c92-4901-ab2a-b16e38144813` | Allow null incase insert a new entity |
| **state**  integer |  | The entity state of this object   * 0 = None * 1 = Insert * 2 = Delete * 3 = Update |  |
| **deleted**  boolean |  | Is this object deleted |  |
| **inserted**  boolean |  | Is this object inserted |  |
| **version**  string | Y | The version |  |
| **created**  datetime in ISO 8601 format | Y | The created datetime |  |
| **createdBy**  string |  | The creator |  |
| **modified**  datetime in ISO 8601 format | Y | The modification datetime |  |
| **modifiedBy**  string |  | The user who last modified this object |  |

**Sample**:

```
{"destinationConnections":[],"sourceConnections":[],"tenantName":"Tenant 1","tenantUniqueName":"T1","workspaceId":"49d886bc-45be-4acf-8ebe-4de775546f8c","tenantId":"9ef4b0af-2485-4050-91b9-cf149d999afd","status":0,"id":null,"state":0,"inserted":true,"version":null,"created":null,"createdBy":null,"modified":null,"modifiedBy":null}
```
