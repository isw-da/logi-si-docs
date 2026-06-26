---
title: "ReportSelectedQuerySourceResult"
id: 12528283006231
section: "System Reference"
category: "Izenda"
url: https://devnet.logianalytics.com/hc/en-us/articles/12528283006231-ReportSelectedQuerySourceResult
updated_at: 2023-02-19T08:37:29Z
---

# ReportSelectedQuerySourceResult

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

# ReportSelectedQuerySourceResult

| Field | NULL | Description | Note |
| --- | --- | --- | --- |
| **result**  array of objects |  | An array of [ReportSelectedQuerySourceDetail](https://devnet.logianalytics.com/hc/en-us/articles/12528282999831-ReportSelectedQuerySourceDetail) objects |  |
| **relatedQuerySources**  array of objects |  | An array of [ReportSelectedQuerySource](https://devnet.logianalytics.com/hc/en-us/articles/12528282988823-ReportSelectedQuerySource) objects |  |
| **pageIndex**  integer |  | The index of the page | Inherited from [PagedResult](https://devnet.logianalytics.com/hc/en-us/articles/12528282006423-PagedResult) |
| **pageSize**  integer |  | The size of the page | Inherited from [PagedResult](https://devnet.logianalytics.com/hc/en-us/articles/12528282006423-PagedResult) |
| **total**  integer |  | The total number of rows | Inherited from [PagedResult](https://devnet.logianalytics.com/hc/en-us/articles/12528282006423-PagedResult) |

**Sample**:

```
{"relatedQuerySources":[{"querySourceId":"39e2a9b9-3be3-4b8b-ae86-0823ecb3c533","isNew":false,"physicalChange":0,"selected":false},{"querySourceId":"c25dc1d3-8066-4fe2-9adb-179060780088","isNew":false,"physicalChange":0,"selected":false},{"querySourceId":"2c26efb2-9ff8-43ea-bcc7-6f1063e1f635","isNew":false,"physicalChange":0,"selected":false}],"result":[{"id":"39e2a9b9-3be3-4b8b-ae86-0823ecb3c533","category":null,"databaseName":"Northwind","schemaName":"dbo","dataObject":"CustomerCustomerDemo","dataObjectType":"Table"}],"total":1,"pageIndex":1,"pageSize":10}
```
