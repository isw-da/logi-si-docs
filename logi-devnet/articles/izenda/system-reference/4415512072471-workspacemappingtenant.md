---
title: "WorkspaceMappingTenant"
id: 4415512072471
section: "System Reference"
category: "Izenda"
url: https://devnet.logianalytics.com/hc/en-us/articles/4415512072471-WorkspaceMappingTenant
updated_at: 2021-12-10T03:10:06Z
---

# WorkspaceMappingTenant

# WorkspaceMappingTenant

| Field | NULL | Description | Note |
| --- | --- | --- | --- |
| **workspaceMappingId**  string (GUID) | Y | The id of the workspace mapping |  |
| **tenantId**  string (GUID) |  | The id of the tenant |  |

Inherited fields:

## Entity

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
{"isDirty":false,"workspaceMappingId":null,"tenantId":"468af427-ebe6-433d-97f3-aacd0c5a8e50","tenantName":"","id":null,"state":0,"inserted":true,"version":null,"created":null,"createdBy":null,"modified":null,"modifiedBy":null}
```
