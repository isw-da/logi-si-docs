---
title: "FusionDataRequest"
id: 4415492814103
section: "System Reference"
category: "Izenda"
url: https://devnet.logianalytics.com/hc/en-us/articles/4415492814103-FusionDataRequest
updated_at: 2021-12-10T03:08:51Z
---

# FusionDataRequest

# FusionDataRequest

| Field | NULL | Description | Note |
| --- | --- | --- | --- |
| **userAction**  string |  | The user action, used for logging user behavior |  |
| **reportId**  string (GUID) | Y | The id of the report |  |
| **reportPartId**  string (GUID) | Y | The id of the report part |  |
| **dashboardId**  string (GUID) | Y | The id of the dashboard |  |
| **dashboardPartId**  string (GUID) | Y | The id of the dashboard part |  |
| **tenantId**  string (GUID) | Y | The id of the tenant |  |
| **expandedLevel**  integer |  | The expanded level |  |
| **filters**  array of objects |  | An array of [FilterItem](https://devnet.logianalytics.com/hc/en-us/articles/4415512000919-FilterItem) objects |  |
| **masterReportId**  string (GUID) | Y | The id of the master report |  |
| **inheritMasterReportFilter**  boolean |  | Whether to inherit filters from master report |  |
| **paging**  object |  | A [PagingInfo](https://devnet.logianalytics.com/hc/en-us/articles/4415504741143-PagingInfo) object |  |
| **overridingFilterValue**  object |  | A dynamic object to store filter values to override |  |
| **overridingFilterOperator**  object |  | A dynamic object to store filter operators to override |  |
| **sortOrders**  array of objects |  | An array of [SortParam](https://devnet.logianalytics.com/hc/en-us/articles/4415504794135-SortParam) objects |  |
| **loadDraft**  boolean |  | Whether to load report from draft |  |
| **loadAll**  boolean |  | Whether to load all records for exporting or printing |  |
| **loadDefaultData**  boolean |  | Whether to load default data for dashboard part |  |
| **ignoreCache**  boolean  New in version 3.3.0. | Y | Whether to load data from cache or retrieve directly from DB |  |

**Sample**:

```
{"dashboardPartId":"8f64491a-3c07-46c7-a224-f5f6a58a1e29","expandedLevel":-1}
```
