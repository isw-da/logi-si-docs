---
title: "ReloadQuerySourceRequest"
id: 4415492842263
section: "System Reference"
category: "Izenda"
url: https://devnet.logianalytics.com/hc/en-us/articles/4415492842263-ReloadQuerySourceRequest
updated_at: 2021-12-10T03:09:13Z
---

# ReloadQuerySourceRequest

# ReloadQuerySourceRequest

| Field | NULL | Description | Note |
| --- | --- | --- | --- |
| **querySourceId**  string (GUID) |  | The query source id |  |
| **postedParameters**  array of objects |  | An array of [QuerySourceField](https://devnet.logianalytics.com/hc/en-us/articles/4415504743703-QuerySourceField) objects |  |

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

**ReloadQuerySourceRequest Sample**:

```
{"querySourceId":"0cd0f186-48f1-47a9-9975-1f2bded3a5cc","postedParameters":[{"id":"8ccfac80-c883-446b-948d-18568dc4d173","name":"@OrderID","filteredValue":{"type":"1","databaseName":"Northwind","databaseId":"f7d00fd9-bfb4-40ae-b25a-61007781b196","querySourceName":"dbo.Order Details","querySourceId":"000e6c8a-89fd-4b38-8d6a-1b891c180daa","lookupKeyQuerySourceFieldName":"OrderID","lookupKeyQuerySourceFieldId":"a0acf5b0-4e47-49d6-af73-c953408df3ef","displayQuerySourceFieldName":"OrderID","displayQuerySourceFieldId":"a0acf5b0-4e47-49d6-af73-c953408df3ef","userDefinedValues":[]}}],"sortOrders":[{"key":"ColumnName","descending":true}]}
```
