---
title: "QuerySourceFieldPagedRequest"
id: 4415512019991
section: "System Reference"
category: "Izenda"
url: https://devnet.logianalytics.com/hc/en-us/articles/4415512019991-QuerySourceFieldPagedRequest
updated_at: 2021-12-10T03:09:06Z
---

# QuerySourceFieldPagedRequest

# QuerySourceFieldPagedRequest

| Field | NULL | Description | Note |
| --- | --- | --- | --- |
| **querySource**  object |  | The parent [QuerySource](https://devnet.logianalytics.com/hc/en-us/articles/4415512017303-QuerySource) object |  |

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

**QuerySourceFieldPagedRequest Sample**:

```
{"querySource":{"id":"9fa90af2-5329-44ac-a753-50c27f9d6fd5","type":"Table"},"criteria":[],"tenantId":null,"pageIndex":1,"pageSize":1,"sortOrders":[{"key":"Alias","descending":true}]}
```
