---
title: "DashboardPartFilterField"
id: 4415511990295
section: "System Reference"
category: "Izenda"
url: https://devnet.logianalytics.com/hc/en-us/articles/4415511990295-DashboardPartFilterField
updated_at: 2021-12-10T03:08:32Z
---

# DashboardPartFilterField

# DashboardPartFilterField

| Field | NULL | Description | Note |
| --- | --- | --- | --- |
| **filterFieldId**  string (GUID) |  | The id of the filter field |  |
| **value**  string |  | The value of the filter field |  |
| **operatorId**  string (GUID) | Y | The id of the operator |  |
| **operatorSetting**  string |  | The operator setting |  |
| **displayName**  string |  | The display name |  |
| **dashboardPartId**  string (GUID) |  | The id of the dashboard part |  |
| **filterField**  object |  | A [ReportFilterField](https://devnet.logianalytics.com/hc/en-us/articles/4415504761879-ReportFilterField) object |  |
| **position**  integer |  | The position in the list of filters |  |
| **dataType**  string |  | The data type |  |
| **required**  boolean |  | Is this required |  |

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
