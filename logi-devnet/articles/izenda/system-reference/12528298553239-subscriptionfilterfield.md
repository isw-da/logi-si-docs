---
title: "SubscriptionFilterField"
id: 12528298553239
section: "System Reference"
category: "Izenda"
url: https://devnet.logianalytics.com/hc/en-us/articles/12528298553239-SubscriptionFilterField
updated_at: 2023-02-23T16:45:02Z
---

# SubscriptionFilterField

# SubscriptionFilterField

| Field | NULL | Description | Note |
| --- | --- | --- | --- |
| **filterFieldId** string (GUID) |  | The id of the filter field |  |
| **value** string |  | The filter value |  |
| **operatorId** string (GUID) | Y | The id of the operator |  |
| **operatorSetting** string |  | The operator setting |  |
| **subscriptionId** string (GUID) | Y | The id of the subscription |  |
| **position** integer |  | The position in the list |  |
| **filterField** object |  | A [FilterField](https://devnet.logianalytics.com/hc/en-us/articles/12528281659159-FilterField) object |  |

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
