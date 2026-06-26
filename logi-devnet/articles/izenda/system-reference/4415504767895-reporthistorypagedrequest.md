---
title: "ReportHistoryPagedRequest"
id: 4415504767895
section: "System Reference"
category: "Izenda"
url: https://devnet.logianalytics.com/hc/en-us/articles/4415504767895-ReportHistoryPagedRequest
updated_at: 2021-12-10T03:09:24Z
---

# ReportHistoryPagedRequest

# ReportHistoryPagedRequest

| Field | NULL | Description | Note |
| --- | --- | --- | --- |
| **reportId**  string (GUID) | Y | The id of the report if available |  |
| **categoryId**  string (GUID) | Y | The id of the category if available | Inherited from [ReportPagedRequest](https://devnet.logianalytics.com/hc/en-us/articles/4415492860439-ReportPagedRequest) |
| **subCategoryId**  string (GUID) | Y | The id of the sub-category if available | Inherited from [ReportPagedRequest](https://devnet.logianalytics.com/hc/en-us/articles/4415492860439-ReportPagedRequest) |
| **timestampOffset**  real number |  | The timestamp offset. See [User Setup](https://devnet.logianalytics.com/hc/en-us/articles/4415512108183-User-Setup). | Inherited from [ReportPagedRequest](https://devnet.logianalytics.com/hc/en-us/articles/4415492860439-ReportPagedRequest) |

Inherited fields:

## PagedRequest

| Field | NULL | Description | Note |
| --- | --- | --- | --- |
| **tenantId**  string (GUID) | Y | The id of the tenant |  |
| **criteria**  array of objects |  | An array of [SearchCriteria](https://devnet.logianalytics.com/hc/en-us/articles/4415512052759-SearchCriteria) objects |  |
| **sortOrders**  array of objects |  | An array of [SortOrder](https://devnet.logianalytics.com/hc/en-us/articles/4415512056215-SortOrder) objects |  |
| **parentIds**  array of strings (GUIDs) |  | Ids of the parents |  |
| **pageIndex**  integer |  | The index of the page | Inherited from [PagingInfo](https://devnet.logianalytics.com/hc/en-us/articles/4415504741143-PagingInfo) |
| **pageSize**  integer |  | The size of the page | Inherited from [PagingInfo](https://devnet.logianalytics.com/hc/en-us/articles/4415504741143-PagingInfo) |
| **total**  integer |  | The total number of rows | Inherited from [PagingInfo](https://devnet.logianalytics.com/hc/en-us/articles/4415504741143-PagingInfo) |
| **skipItems**  integer |  | Skip items | Inherited from [PagingInfo](https://devnet.logianalytics.com/hc/en-us/articles/4415504741143-PagingInfo) |
| **isLastPage**  boolean |  | Whether this is the last page | Inherited from [PagingInfo](https://devnet.logianalytics.com/hc/en-us/articles/4415504741143-PagingInfo) |

**PagedRequest Sample**:

```
{"criteria":[{"key":"All","value":"","operation":1}],"pageIndex":1,"pageSize":10,"sortOrders":[{"key":"shareWith","descending":true}]}
```

**ReportHistoryPagedRequest Sample**:

```
{"reportId":"41023c5b-3fe5-4a62-8ecf-7aae8974f63f","tenantId":null,"criteria":[{"key":"All","value":"","operation":1}],"pageIndex":1,"pageSize":10,"sortOrders":[{"key":"version","descending":true}]}
```
