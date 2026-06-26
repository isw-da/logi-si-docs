---
title: "ReportFilterFieldPagedRequest"
id: 4415504762775
section: "System Reference"
category: "Izenda"
url: https://devnet.logianalytics.com/hc/en-us/articles/4415504762775-ReportFilterFieldPagedRequest
updated_at: 2021-12-10T03:09:20Z
---

# ReportFilterFieldPagedRequest

# ReportFilterFieldPagedRequest

| Field | NULL | Description | Note |
| --- | --- | --- | --- |
| **reportParameter**  object |  | A [ReportSavingParameter](https://devnet.logianalytics.com/hc/en-us/articles/4415512047639-ReportSavingParameter) object |  |
| **includeAll**  boolean |  | Whether paged result should include [ALL] |  |
| **includeBlank**  boolean |  | Whether paged result should include [BLANK] |  |

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

**ReportFilterFieldPagedRequest Sample**:

```
{"dashboardId":"a3243533-166d-4377-90eb-add25edf6563","criteria":[{"key":"All","value":"","operation":1}],"pageIndex":1,"pageSize":10,"sortOrders":[{"key":"shareWith","descending":true}]}
```
