---
title: "ReportConnectionParam"
id: 12528282333207
section: "System Reference"
category: "Izenda"
url: https://devnet.logianalytics.com/hc/en-us/articles/12528282333207-ReportConnectionParam
updated_at: 2023-02-19T08:37:04Z
---

# ReportConnectionParam

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

# ReportConnectionParam

| Field | NULL | Description | Note |
| --- | --- | --- | --- |
| **categories**  array of objects |  | An array of [ReportCategoryParam](https://devnet.logianalytics.com/hc/en-us/articles/12528297815575-ReportCategoryParam) objects. |  |

Inherited fields:

## ReportParam

| Field | NULL | Description | Note |
| --- | --- | --- | --- |
| **id**  string (GUID) |  | The id. |  |
| **name**  string |  | The name. |  |

**Sample**:

```
{"categories":[{"querySourceNames":["Employees"],"id":"860cab58-d90a-4d6d-9251-ec45c067f6b9","name":"dbo"}],"id":"5963219c-5243-4b6f-9042-b27ca9cbc5ec","name":"Retail"}
```
