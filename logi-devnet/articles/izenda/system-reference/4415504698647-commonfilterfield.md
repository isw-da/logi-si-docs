---
title: "CommonFilterField"
id: 4415504698647
section: "System Reference"
category: "Izenda"
url: https://devnet.logianalytics.com/hc/en-us/articles/4415504698647-CommonFilterField
updated_at: 2021-12-10T03:08:24Z
---

# CommonFilterField

# CommonFilterField

| Field | NULL | Description | Note |
| --- | --- | --- | --- |
| **name**  string |  | The common name |  |
| **displayName**  string |  | The display name |  |
| **value**  string |  | The value |  |
| **operatorId**  string (GUID) | Y | The id of the operator |  |
| **operatorSetting**  string |  | The operator setting |  |
| **dataType**  string |  | The data type |  |
| **dashboardId**  string (GUID) | Y | The id of the dashboard |  |
| **position**  integer |  | The position in the list of filters |  |
| **cascading**  boolean |  | Whether common filter field will be cascaded |  |
| **sortType**  string |  | The sort type |  |
| **filterFields**  array of objects |  | An array of dynamic objects |  |

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
{"name":"042a04a3-dfe1-4ef9-bd27-1b657886f02e-ShipCountry","displayName":"ShipCountry","value":"","operatorId":"042a04a3-dfe1-4ef9-bd27-1b657886f02e","operatorSetting":"","dataType":null,"dashboardId":"70193a58-5752-48b7-bd0b-018a430087ec","position":1,"cascading":false,"sortType":null,"filterFields":[{"filterFieldId":"e5698682-3118-41ba-94e4-985955fc2f2f","dashboardPartId":"00000000-0000-0000-0000-000000000000"},{"filterFieldId":"9baaf9a0-5e65-45c2-b8e5-1cdb8ad5a021","dashboardPartId":"00000000-0000-0000-0000-000000000000"}],"id":"32bf178c-eeac-473a-bc0e-3d4c4096bb13","state":0,"deleted":false,"inserted":true,"version":1,"created":"2017-01-10T03:35:23.803","createdBy":"John Doe","modified":"2017-01-10T03:35:23.803","modifiedBy":"John Doe"}
```
