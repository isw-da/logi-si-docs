---
title: "SystemVariablePagedRequest"
id: 12528283266967
section: "System Reference"
category: "Izenda"
url: https://devnet.logianalytics.com/hc/en-us/articles/12528283266967-SystemVariablePagedRequest
updated_at: 2023-02-19T08:37:44Z
---

# SystemVariablePagedRequest

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

# SystemVariablePagedRequest

| Field | NULL | Description | Note |
| --- | --- | --- | --- |
| **reportingType**  integer |  | The reporting type   * 1 = Report * 2 = Dashboard * 0 = Both |  |

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

**SystemVariablePagedRequest Sample**:

```
{"reportingType":0,"pageIndex":1,"pageSize":10,"sortOrders":[{"key":"name","descending":true}],"criteria":[]}
```
