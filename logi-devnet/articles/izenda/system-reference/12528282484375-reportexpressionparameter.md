---
title: "ReportExpressionParameter"
id: 12528282484375
section: "System Reference"
category: "Izenda"
url: https://devnet.logianalytics.com/hc/en-us/articles/12528282484375-ReportExpressionParameter
updated_at: 2023-02-19T08:37:08Z
---

# ReportExpressionParameter

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

# ReportExpressionParameter

| Field | NULL | Description | Note |
| --- | --- | --- | --- |
| **expression**  string |  | The expression |  |
| **izendaDataType**  string |  | The Izenda data type |  |
| **querySourceFieldId**  string (GUID) | Y | The id of the query source field |  |

Inherited fields:

## ReportParameter

| Field | NULL | Description | Note |
| --- | --- | --- | --- |
| **reportKey**  object |  | A [ReportKey](https://devnet.logianalytics.com/hc/en-us/articles/12528282642071-ReportKey) object |  |
| **previewRecord**  integer |  | The numer of records to preview |  |
| **relationShipIds**  array of string (GUID) |  | The array of the relationship Ids |  |
| **validateReportDataSource**  boolean |  | Whether to validate report data source or not | New in version 2.6.8. |

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

**Sample**:

```
{"reportKey":{"key":"e40d635c-c90f-45f7-bf7a-5750db7ef9cf"},"expression":"[Northwind].[dbo].[Products].[UnitsInStock] * [Northwind].[dbo].[Products].[UnitPrice]"}
```
