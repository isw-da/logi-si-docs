---
title: "ReportSelectedQuerySourceResult"
id: 4415504783639
section: "System Reference"
category: "Izenda"
url: https://devnet.logianalytics.com/hc/en-us/articles/4415504783639-ReportSelectedQuerySourceResult
updated_at: 2021-12-10T03:09:38Z
---

# ReportSelectedQuerySourceResult

# ReportSelectedQuerySourceResult

| Field | NULL | Description | Note |
| --- | --- | --- | --- |
| **result**  array of objects |  | An array of [ReportSelectedQuerySourceDetail](https://devnet.logianalytics.com/hc/en-us/articles/4415492875543-ReportSelectedQuerySourceDetail) objects |  |
| **relatedQuerySources**  array of objects |  | An array of [ReportSelectedQuerySource](https://devnet.logianalytics.com/hc/en-us/articles/4415492874647-ReportSelectedQuerySource) objects |  |
| **pageIndex**  integer |  | The index of the page | Inherited from [PagedResult](https://devnet.logianalytics.com/hc/en-us/articles/4415492825879-PagedResult) |
| **pageSize**  integer |  | The size of the page | Inherited from [PagedResult](https://devnet.logianalytics.com/hc/en-us/articles/4415492825879-PagedResult) |
| **total**  integer |  | The total number of rows | Inherited from [PagedResult](https://devnet.logianalytics.com/hc/en-us/articles/4415492825879-PagedResult) |

**Sample**:

```
{"relatedQuerySources":[{"querySourceId":"39e2a9b9-3be3-4b8b-ae86-0823ecb3c533","isNew":false,"physicalChange":0,"selected":false},{"querySourceId":"c25dc1d3-8066-4fe2-9adb-179060780088","isNew":false,"physicalChange":0,"selected":false},{"querySourceId":"2c26efb2-9ff8-43ea-bcc7-6f1063e1f635","isNew":false,"physicalChange":0,"selected":false}],"result":[{"id":"39e2a9b9-3be3-4b8b-ae86-0823ecb3c533","category":null,"databaseName":"Northwind","schemaName":"dbo","dataObject":"CustomerCustomerDemo","dataObjectType":"Table"}],"total":1,"pageIndex":1,"pageSize":10}
```
