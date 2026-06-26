---
title: "WorkspaceTenant"
id: 12528283598999
section: "System Reference"
category: "Izenda"
url: https://devnet.logianalytics.com/hc/en-us/articles/12528283598999-WorkspaceTenant
updated_at: 2023-02-23T16:42:15Z
---

# WorkspaceTenant

# WorkspaceTenant

| Field | NULL | Description | Note |
| --- | --- | --- | --- |
| **workspaceId** string (GUID) | Y | The id of the workspace |  |
| **tenantId** string (GUID) | Y | The id of the tenant if available |  |
| **status** integer |  | The status of the workspace tenant   * 0 = Need Validated * 1 = Ready to Copy * 2 = Authentication Missing * 3 = Validation Error |  |
| **physicalDataModel** string |  | The physical data structure in json format |  |
| **sourceDataModel** string |  | The source data model in json format |  |
| **destinationHashCode** string |  | The hashcode of the tenant data model |  |

Inherited fields:

## Entity

| Field | NULL | Description | Note |
| --- | --- | --- | --- |
| **id** string (GUID) |  | The id of this object  Example: `572bd576-8c92-4901-ab2a-b16e38144813` | Allow null incase insert a new entity |
| **state** integer |  | The entity state of this object   * 0 = None * 1 = Insert * 2 = Delete * 3 = Update |  |
| **deleted** boolean |  | Is this object deleted |  |
| **inserted** boolean |  | Is this object inserted |  |
| **version** string | Y | The version |  |
| **created** datetime in ISO 8601 format | Y | The created datetime |  |
| **createdBy** string |  | The creator |  |
| **modified** datetime in ISO 8601 format | Y | The modification datetime |  |
| **modifiedBy** string |  | The user who last modified this object |  |
