---
title: "FilterOperatorGroup"
id: 12528297213207
section: "System Reference"
category: "Izenda"
url: https://devnet.logianalytics.com/hc/en-us/articles/12528297213207-FilterOperatorGroup
updated_at: 2023-02-23T16:51:47Z
---

# FilterOperatorGroup

# FilterOperatorGroup

| Field | NULL | Description | Note |
| --- | --- | --- | --- |
| **name** string |  | The name of the operator group |  |
| **defaultOperatorId** string (GUID) | Y | The id of the default operator of the group |  |

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
