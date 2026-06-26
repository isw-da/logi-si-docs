---
title: "RolePagedRequest"
id: 4415492881047
section: "System Reference"
category: "Izenda"
url: https://devnet.logianalytics.com/hc/en-us/articles/4415492881047-RolePagedRequest
updated_at: 2021-12-10T03:09:42Z
---

# RolePagedRequest

# RolePagedRequest

| Field | NULL | Description | Note |
| --- | --- | --- | --- |
| **roletId**  string (GUID) | Y | The id of the report if available |  |
| **userModeType**  integer |  | The mode type   - 0 = All   - 1 = Access   - 2 = Schedule |  |
| **roleVirtualNode**  an array of object |  | An array of [RoleVirtualNode](https://devnet.logianalytics.com/hc/en-us/articles/4415504790167-RoleVirtualNode) objects |  |

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

**RolePagedRequest Sample**:

```
{"roleId":"db8693f7-3d5a-41d7-a888-8a1dfaad31b4","tenantId":null,"skipItems":1,"pageSize":6,"parentIds":["5329b0cc-37a1-49c7-9271-a870a480db5c"],"criteria":[{"key":"name","value":"Anna"}]}
```
