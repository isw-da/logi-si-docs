---
title: "SaveConnectionStatus"
id: 12528283080471
section: "System Reference"
category: "Izenda"
url: https://devnet.logianalytics.com/hc/en-us/articles/12528283080471-SaveConnectionStatus
updated_at: 2023-02-19T08:37:34Z
---

# SaveConnectionStatus

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

# SaveConnectionStatus

| Field | NULL | Description | Note |
| --- | --- | --- | --- |
| **connectionId**  string (GUID) | Y | The id of the connection |  |

Inherited fields:

## OperationResult

| Field | NULL | Description | Note |
| --- | --- | --- | --- |
| **success**  boolean |  | Is the operation successful |  |
| **messages**  array of objects |  | An array of [ModelError](https://devnet.logianalytics.com/hc/en-us/articles/12528297464471-ModelError) objects |  |
| **data**  object |  | A dynamic object to store additional data |  |

**Sample**:

```
{"success":true,"data":"4e2d54c8-20e7-437f-a5ce-43e963c763a2"}
```

**Sample**:

```
{"success":true,"connectionId":"f5180bc0-7c07-48db-b672-e66a5adde027","connectionErrors":[]}
```
