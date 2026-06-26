---
title: "ReportSavingParameter"
id: 12528282939799
section: "System Reference"
category: "Izenda"
url: https://devnet.logianalytics.com/hc/en-us/articles/12528282939799-ReportSavingParameter
updated_at: 2023-02-19T08:37:27Z
---

# ReportSavingParameter

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

# ReportSavingParameter

| Field | NULL | Description | Note |
| --- | --- | --- | --- |
| **saveAs**  boolean |  | Is this saved as new report |  |
| **report**  object |  | A [ReportDefinition](https://devnet.logianalytics.com/hc/en-us/articles/12528297929111-ReportDefinition) object |  |
| **section**  integer |  | The report section   * 0 = All * 1 = DataSource * 2 = Fields * 3 = CalculatedField |  |
| **tenantId**  string (GUID) | Y | The id of the tenant |  |
| **ignoreCheckChange**  boolean |  | Is the check for report changes ignored |  |
| **ignoreCheckName**  boolean |  | Is the check for report name ignored |  |
| **insertWithAssignedId**  boolean |  | Whether to use the populated report id in **report** object to insert |  |
| **overrideCalculatedFields**  boolean |  | Whether to override calculated fields |  |
| **reportState**  integer |  | * 0 = Posted - Report is posted from client * 1 = Saved - Get report from database * 2 = Draft - Get report from draft |  |
| **isSavingReport**  boolean |  | Whether report is saving or not | Only validate report data source when saving report (isSavingReport = true)  New in version 2.6.8. |

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
{"reportKey":{"key":null,"modified":null},"section":0,"saveAs":false,"ignoreCheckChange":false,"report":{"name":"","type":"Templates","previewRecord":10,"advancedMode":true,"allowNulls":false,"isDistinct":false,"reportDataSource":[{"aliasId":"479be129-338d-45f1-b216-1d95957fe2c8_Order Details","querySourceId":"479be129-338d-45f1-b216-1d95957fe2c8","querySourceName":"Order Details","selected":true},{"aliasId":"54852be4-5584-4c23-ae5d-4197724059e1_Orders","querySourceId":"54852be4-5584-4c23-ae5d-4197724059e1","querySourceName":"Orders","selected":true}],"reportRelationship":[{"tempId":"16d3b9bf-86cb-45fa-b33d-53e3e2a8a042","joinConnectionId":"db19bb46-ffa3-45fd-b205-0dad305fdf98","foreignConnectionId":"db19bb46-ffa3-45fd-b205-0dad305fdf98","joinQuerySourceId":"479be129-338d-45f1-b216-1d95957fe2c8","joinQuerySourceName":"Order Details","joinDataSourceCategoryName":"","foreignDataSourceCategoryName":"","foreignQuerySourceId":"54852be4-5584-4c23-ae5d-4197724059e1","foreignQuerySourceName":"Orders","joinFieldId":"a0011b48-ef08-45fe-b044-abc68442cd17","joinFieldName":"OrderID","foreignFieldId":"3caf9c17-abd7-4119-809d-2c3debb8eb37","foreignFieldName":"OrderID","alias":"","systemRelationship":true,"joinType":"Inner","parentRelationshipId":"c55d696b-f25d-4a6f-a951-7a4e6e532c98","position":null,"relationshipKeyJoins":[],"selectedForeignAlias":"54852be4-5584-4c23-ae5d-4197724059e1_Orders","id":"16d3b9bf-86cb-45fa-b33d-53e3e2a8a052","state":1,"validationKey":"c55d696b-f25d-4a6f-a951-7a4e6e532c98","relationshipPosition":0,"invalidAlias":null,"hidden":false,"level":1}],"reportPart":[]},"expandedLevel":0,"filters":[]}
```
