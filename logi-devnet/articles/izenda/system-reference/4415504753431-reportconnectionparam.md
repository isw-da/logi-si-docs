---
title: "ReportConnectionParam"
id: 4415504753431
section: "System Reference"
category: "Izenda"
url: https://devnet.logianalytics.com/hc/en-us/articles/4415504753431-ReportConnectionParam
updated_at: 2021-12-10T03:09:15Z
---

# ReportConnectionParam

# ReportConnectionParam

| Field | NULL | Description | Note |
| --- | --- | --- | --- |
| **categories**  array of objects |  | An array of [ReportCategoryParam](https://devnet.logianalytics.com/hc/en-us/articles/4415504751255-ReportCategoryParam) objects. |  |

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
