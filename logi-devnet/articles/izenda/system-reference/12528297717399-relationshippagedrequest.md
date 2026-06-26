---
title: "RelationshipPagedRequest"
id: 12528297717399
section: "System Reference"
category: "Izenda"
url: https://devnet.logianalytics.com/hc/en-us/articles/12528297717399-RelationshipPagedRequest
updated_at: 2023-02-19T08:37:00Z
---

# RelationshipPagedRequest

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

# RelationshipPagedRequest

| Field | NULL | Description | Note |
| --- | --- | --- | --- |
| **querySourceId**  string (GUID) | Y | The id of the query source |  |
| **objectId**  string (GUID) | Y | The id of the object in draft to load from    Put null here to load from the database |  |
| **relationshipOrders**  array of objects |  | An array of [RelationshipOrder](https://devnet.logianalytics.com/hc/en-us/articles/12528297710103-RelationshipOrder) objects |  |
| **querySources**  array of objects |  | An array of [ReportSelectedQuerySource](https://devnet.logianalytics.com/hc/en-us/articles/12528282988823-ReportSelectedQuerySource) objects |  |
| **selectedDataSourceChanged**  boolean |  | Whether selected data source has changed |  |
| **modifiedRelationships**  string (GUID)  New in version 2.16.0. | Y | The newly added or modified relationships | Use for retrieve the newly added/modified relationships in Datta Model > Relationships |
| **includeDisabledRelationships**  boolean  New in version 3.10.0. |  | Indictates whether disabled relationships should be included or not |  |

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

**RelationshipPagedRequest Sample**:

```
{"querySourceId":null,"tenentId":"","criteria":[{"key":"All","value":"","operation":1}],"pageIndex":1,"pageSize":1,"sortOrders":[{"key":"DatabaseName","descending":true}],"includeDisabledRelationships":true}
```
