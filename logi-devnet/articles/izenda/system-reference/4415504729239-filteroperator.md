---
title: "FilterOperator"
id: 4415504729239
section: "System Reference"
category: "Izenda"
url: https://devnet.logianalytics.com/hc/en-us/articles/4415504729239-FilterOperator
updated_at: 2021-12-10T03:08:50Z
---

# FilterOperator

# FilterOperator

| Field | NULL | Description | Note |
| --- | --- | --- | --- |
| **name**  string |  | The name of the operator |  |
| **operatorGroupId**  string (GUID) |  | The id of the parent operator group |  |
| **label**  string |  | The operator label |  |
| **allowParameter**  boolean |  | Whether operator can be used with parameter or not |  |

Inherited fields:

## Entity

| Field | NULL | Description | Note |
| --- | --- | --- | --- |
| **id**  string (GUID) |  | The id of this object   Example: `572bd576-8c92-4901-ab2a-b16e38144813` | Allow null incase insert a new entity |
| **state**  integer |  | The entity state of this object   * 0 = None * 1 = Insert * 2 = Delete * 3 = Update |  |a
| **deleted**  boolean |  | Is this object deleted |  |
| **inserted**  boolean |  | Is this object inserted |  |
| **version**  string | Y | The version |  |
| **created**  datetime in ISO 8601 format | Y | The created datetime |  |
| **createdBy**  string |  | The creator |  |
| **modified**  datetime in ISO 8601 format | Y | The modification datetime |  |
| **modifiedBy**  string |  | The user who last modified this object |  |
