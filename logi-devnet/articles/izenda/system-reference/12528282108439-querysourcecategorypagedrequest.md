---
title: "QuerySourceCategoryPagedRequest"
id: 12528282108439
section: "System Reference"
category: "Izenda"
url: https://devnet.logianalytics.com/hc/en-us/articles/12528282108439-QuerySourceCategoryPagedRequest
updated_at: 2023-02-23T16:13:58Z
---

# QuerySourceCategoryPagedRequest

# QuerySourceCategoryPagedRequest

| Field | NULL | Description | Note |
| --- | --- | --- | --- |
| **ConnectionId** string |  | The id of the [Connection](https://devnet.logianalytics.com/hc/en-us/articles/12528281159575-Connection) |  |

Inherited fields:

## PagedRequest

| Field | NULL | Description | Note |
| --- | --- | --- | --- |
| **tenantId** string (GUID) | Y | The id of the tenant |  |
| **criteria** array of objects |  | An array of [SearchCriteria](https://devnet.logianalytics.com/hc/en-us/articles/12528283106455-SearchCriteria) objects |  |
| **sortOrders** array of objects |  | An array of [SortOrder](https://devnet.logianalytics.com/hc/en-us/articles/12528298506903-SortOrder) objects |  |
| **parentIds** array of strings (GUIDs) |  | Ids of the parents |  |
| **pageIndex** integer |  | The index of the page | Inherited from [PagingInfo](https://devnet.logianalytics.com/hc/en-us/articles/12528297527575-PagingInfo) |
| **pageSize** integer |  | The size of the page | Inherited from [PagingInfo](https://devnet.logianalytics.com/hc/en-us/articles/12528297527575-PagingInfo) |
| **total** integer |  | The total number of rows | Inherited from [PagingInfo](https://devnet.logianalytics.com/hc/en-us/articles/12528297527575-PagingInfo) |
| **skipItems** integer |  | Skip items | Inherited from [PagingInfo](https://devnet.logianalytics.com/hc/en-us/articles/12528297527575-PagingInfo) |
| **isLastPage** boolean |  | Whether this is the last page | Inherited from [PagingInfo](https://devnet.logianalytics.com/hc/en-us/articles/12528297527575-PagingInfo) |

**PagedRequest Sample**:

```
{"criteria":[{"key":"All","value":"","operation":1}],"pageIndex":1,"pageSize":10,"sortOrders":[{"key":"shareWith","descending":true}]}
```

**QuerySourceCategoryPagedRequest Sample**:

```
{"ConnectionId":"2046c03b-3830-4385-9ac0-bdc95e92ea49","criteria":[],"tenantId":null,"pageIndex":1,"pageSize":1,"sortOrders":[{"key":"value","descending":false}]}
```
