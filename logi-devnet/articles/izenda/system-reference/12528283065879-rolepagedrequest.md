---
title: "RolePagedRequest"
id: 12528283065879
section: "System Reference"
category: "Izenda"
url: https://devnet.logianalytics.com/hc/en-us/articles/12528283065879-RolePagedRequest
updated_at: 2023-02-19T08:37:33Z
---

# RolePagedRequest

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

# RolePagedRequest

| Field | NULL | Description | Note |
| --- | --- | --- | --- |
| **roletId**  string (GUID) | Y | The id of the report if available |  |
| **userModeType**  integer |  | The mode type   - 0 = All   - 1 = Access   - 2 = Schedule |  |
| **roleVirtualNode**  an array of object |  | An array of [RoleVirtualNode](https://devnet.logianalytics.com/hc/en-us/articles/12528298434583-RoleVirtualNode) objects |  |

Inherited fields:

## PagedRequest

| Field | NULL | Description | Note |
| --- | --- | --- | --- |
| **tenantId**  string (GUID) | Y | The id of the tenant |  |
| **criteria**  array of objects |  | An array of [SearchCriteria](https://devnet.logianalytics.com/hc/en-us/articles/12528283106455-SearchCriteria) objects |  |
| **sortOrders**  array of objects |  | An array of [SortOrder](https://devnet.logianalytics.com/hc/en-us/articles/12528298506903-SortOrder) objects |  |
| **parentIds**  array of strings (GUIDs) |  | Ids of the parents |  |
| **pageIndex**  integer |  | The index of the page | Inherited from [PagingInfo](https://devnet.logianalytics.com/hc/en-us/articles/12528297527575-PagingInfo) |
| **pageSize**  integer |  | The size of the page | Inherited from [PagingInfo](https://devnet.logianalytics.com/hc/en-us/articles/12528297527575-PagingInfo) |
| **total**  integer |  | The total number of rows | Inherited from [PagingInfo](https://devnet.logianalytics.com/hc/en-us/articles/12528297527575-PagingInfo) |
| **skipItems**  integer |  | Skip items | Inherited from [PagingInfo](https://devnet.logianalytics.com/hc/en-us/articles/12528297527575-PagingInfo) |
| **isLastPage**  boolean |  | Whether this is the last page | Inherited from [PagingInfo](https://devnet.logianalytics.com/hc/en-us/articles/12528297527575-PagingInfo) |

**PagedRequest Sample**:

```
{"criteria":[{"key":"All","value":"","operation":1}],"pageIndex":1,"pageSize":10,"sortOrders":[{"key":"shareWith","descending":true}]}
```

**RolePagedRequest Sample**:

```
{"roleId":"db8693f7-3d5a-41d7-a888-8a1dfaad31b4","tenantId":null,"skipItems":1,"pageSize":6,"parentIds":["5329b0cc-37a1-49c7-9271-a870a480db5c"],"criteria":[{"key":"name","value":"Anna"}]}
```
