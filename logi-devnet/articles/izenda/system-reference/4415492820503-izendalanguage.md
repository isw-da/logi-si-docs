---
title: "IzendaLanguage"
id: 4415492820503
section: "System Reference"
category: "Izenda"
url: https://devnet.logianalytics.com/hc/en-us/articles/4415492820503-IzendaLanguage
updated_at: 2021-12-10T03:08:57Z
---

# IzendaLanguage

# IzendaLanguage

| Field | Description | Note |
| --- | --- | --- |
| **language**  string | The language |  |
| **cultureName**  string | The culture name |  |

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
{"language":"English - United States","cultureName":"en-US","id":"c6e7d7b5-4e15-44b7-9538-fd1ab38783f0","state":0,"deleted":false,"inserted":true,"version":null,"created":null,"createdBy":null,"modified":null,"modifiedBy":null}
```
