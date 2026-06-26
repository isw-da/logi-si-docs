---
title: "RelationshipPagedRequest"
id: 4415492839191
section: "System Reference"
category: "Izenda"
url: https://devnet.logianalytics.com/hc/en-us/articles/4415492839191-RelationshipPagedRequest
updated_at: 2021-12-10T03:09:11Z
---

# RelationshipPagedRequest

# RelationshipPagedRequest

| Field | NULL | Description | Note |
| --- | --- | --- | --- |
| **querySourceId**  string (GUID) | Y | The id of the query source |  |
| **objectId**  string (GUID) | Y | The id of the object in draft to load from    Put null here to load from the database |  |
| **relationshipOrders**  array of objects |  | An array of [RelationshipOrder](https://devnet.logianalytics.com/hc/en-us/articles/4415492838167-RelationshipOrder) objects |  |
| **querySources**  array of objects |  | An array of [ReportSelectedQuerySource](https://devnet.logianalytics.com/hc/en-us/articles/4415492874647-ReportSelectedQuerySource) objects |  |
| **selectedDataSourceChanged**  boolean |  | Whether selected data source has changed |  |
| **modifiedRelationships**  string (GUID)  New in version 2.16.0. | Y | The newly added or modified relationships | Use for retrieve the newly added/modified relationships in Datta Model > Relationships |
| **includeDisabledRelationships**  boolean  New in version 3.10.0. |  | Indictates whether disabled relationships should be included or not |  |

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

**RelationshipPagedRequest Sample**:

```
{"querySourceId":null,"tenentId":"","criteria":[{"key":"All","value":"","operation":1}],"pageIndex":1,"pageSize":1,"sortOrders":[{"key":"DatabaseName","descending":true}],"includeDisabledRelationships":true}
```
