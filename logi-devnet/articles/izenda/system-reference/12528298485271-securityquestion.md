---
title: "SecurityQuestion"
id: 12528298485271
section: "System Reference"
category: "Izenda"
url: https://devnet.logianalytics.com/hc/en-us/articles/12528298485271-SecurityQuestion
updated_at: 2023-02-19T08:37:37Z
---

# SecurityQuestion

[Skip To Main Content](#)

Account

Settings

---

Logout

* placeholder

Account

Settings

---

Logout

Filter: 

* All Files

Submit Search

# SecurityQuestion

| Field | NULL | Description | Note |
| --- | --- | --- | --- |
| **tenantId**  string (GUID) | Y | The id of the tenant |  |
| **question**  string |  | The question |  |
| **orderNumber**  integer |  | The order of the question |  |

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
{"tenantId":null,"question":"What is the first and last name of your first boyfriend or girlfriend?","orderNumber":1,"id":"5784ece5-d2e7-42b1-89bb-859737b7b2a9","state":0,"deleted":false,"inserted":true,"version":1,"created":null,"createdBy":null,"modified":null,"modifiedBy":null}
```
