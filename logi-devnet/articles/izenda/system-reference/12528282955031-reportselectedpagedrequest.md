---
title: "ReportSelectedPagedRequest"
id: 12528282955031
section: "System Reference"
category: "Izenda"
url: https://devnet.logianalytics.com/hc/en-us/articles/12528282955031-ReportSelectedPagedRequest
updated_at: 2023-02-19T08:37:28Z
---

# ReportSelectedPagedRequest

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

# ReportSelectedPagedRequest

| Field | NULL | Description | Note |
| --- | --- | --- | --- |
| **querySources**  array of objects |  | An array of [ReportSelectedQuerySource](https://devnet.logianalytics.com/hc/en-us/articles/12528282988823-ReportSelectedQuerySource) objects |  |

Inherited fields:

# ReportPagedRequest

| Field | NULL | Description | Note |
| --- | --- | --- | --- |
| **categoryId**  string (GUID) | Y | The id of the category if available |  |
| **subCategoryId**  string (GUID) | Y | The id of the sub-category if available |  |
| **isGlobal**  boolean | Y | Whether to load global reports |  |
| **timestampOffset**  real number |  | The timestamp offset. See [User Setup](https://devnet.logianalytics.com/hc/en-us/articles/12528284610839-User-Setup). |  |
| **excludeIds**  array of strings (GUIDs) |  | The list of report ids to exclude |  |

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

**ReportPagedRequest Sample**:

```
{"subcategoryid":null,"categoryId":null,"tenantId":null,"pageSize":10,"pageIndex":1,"sortOrders":[{"key":"reportname","descending":true}],"criteria":[{"key":"reportName","value":"test","operation":1}]}
```

**ReportSelectedPagedRequest Sample**:

```
{"querySources":[{"querySourceId":"39e2a9b9-3be3-4b8b-ae86-0823ecb3c533","selected":true}],"tenantId":null,"criteria":null,"pageIndex":1,"pageSize":10,"sortOrders":null}
```
