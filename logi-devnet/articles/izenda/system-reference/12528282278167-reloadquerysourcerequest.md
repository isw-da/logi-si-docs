---
title: "ReloadQuerySourceRequest"
id: 12528282278167
section: "System Reference"
category: "Izenda"
url: https://devnet.logianalytics.com/hc/en-us/articles/12528282278167-ReloadQuerySourceRequest
updated_at: 2023-02-19T08:37:02Z
---

# ReloadQuerySourceRequest

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

# ReloadQuerySourceRequest

| Field | NULL | Description | Note |
| --- | --- | --- | --- |
| **querySourceId**  string (GUID) |  | The query source id |  |
| **postedParameters**  array of objects |  | An array of [QuerySourceField](https://devnet.logianalytics.com/hc/en-us/articles/12528282117399-QuerySourceField) objects |  |

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

**ReloadQuerySourceRequest Sample**:

```
{"querySourceId":"0cd0f186-48f1-47a9-9975-1f2bded3a5cc","postedParameters":[{"id":"8ccfac80-c883-446b-948d-18568dc4d173","name":"@OrderID","filteredValue":{"type":"1","databaseName":"Northwind","databaseId":"f7d00fd9-bfb4-40ae-b25a-61007781b196","querySourceName":"dbo.Order Details","querySourceId":"000e6c8a-89fd-4b38-8d6a-1b891c180daa","lookupKeyQuerySourceFieldName":"OrderID","lookupKeyQuerySourceFieldId":"a0acf5b0-4e47-49d6-af73-c953408df3ef","displayQuerySourceFieldName":"OrderID","displayQuerySourceFieldId":"a0acf5b0-4e47-49d6-af73-c953408df3ef","userDefinedValues":[]}}],"sortOrders":[{"key":"ColumnName","descending":true}]}
```
