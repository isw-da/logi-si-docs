---
title: "GoogleAPISetting"
id: 12528297311639
section: "System Reference"
category: "Izenda"
url: https://devnet.logianalytics.com/hc/en-us/articles/12528297311639-GoogleAPISetting
updated_at: 2023-02-19T08:36:40Z
---

# GoogleAPISetting

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

# GoogleAPISetting

| Field | NULL | Description | Note |
| --- | --- | --- | --- |
| **useSystemConfiguration**  boolean |  | Whether inherit the setting from System or not |  |
| **googleAPIKey**  string |  | The Google Map API key |  |
| **useGEOCodingService**  boolean |  | Whether tenant can allowed to use GEOCoding Service or not |  |
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
{"useSystemConfiguration":false,"googleAPIKey":"The google api key","useGEOCodingService":true,"tenantId":null,"id":"e7798b61-3192-42dc-b0cd-7f7726cbfa69","state":0,"deleted":false,"inserted":true,"version":1,"created":"2019-09-03T07:45:33.0134920+07:00","createdBy":"System Admin","modified":"2019-09-03T07:45:33.0134920+07:00","modifiedBy":"System Admin"}
```
