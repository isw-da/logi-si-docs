---
title: "ReportFilterSetting"
id: 4415492856983
section: "System Reference"
category: "Izenda"
url: https://devnet.logianalytics.com/hc/en-us/articles/4415492856983-ReportFilterSetting
updated_at: 2021-12-10T03:09:22Z
---

# ReportFilterSetting

# ReportFilterSetting

| Field | NULL | Description | Note |
| --- | --- | --- | --- |
| **filterFields**  array of objects |  | An array of [ReportFilterField](https://devnet.logianalytics.com/hc/en-us/articles/4415504761879-ReportFilterField) objects |  |

Inherited fields:

## ReportFilter

| Field | NULL | Description | Note |
| --- | --- | --- | --- |
| **logic**  string |  | The filter logic (See [Build complex filter logic](https://devnet.logianalytics.com/hc/en-us/articles/4415492934039-Report-Designer-Design#build-complex-filter-logic)) |  |
| **visible**  boolean |  | Is the report filter displayed under report description |  |
| **reportId**  string (GUID) |  | The id of the report |  |

Inherited fields:

### Entity

| Field | NULL | Description | Note |
| --- | --- | --- | --- |
| **id**  string (GUID) |  | The id of this object   Example: `572bd576-8c92-4901-ab2a-b16e38144813` | Allow null incase insert a new entity |
| **state**  integer |  | The entity state of this object   * 0 = None * 1 = Insert * 2 = Delete * 3 = Update |  |
| **deleted**  boolean |  | Is this object deleted |  |
| **inserted**  boolean |  | Is this object inserted |  |
| **version**  string | Y | The version |  |
| **created**  datetime in ISO 8601 format | Y | The created datetime |  |
| **createdBy**  string |  | The creator |  |
| **modified**  datetime in ISO 8601 format | Y | The modification datetime |  |
| **modifiedBy**  string |  | The user who last modified this object |  |

**ReportFilterSetting Sample**:

```
{"status":0,"logic":null,"visible":false,"filterFields":[{"connectionName":"Northwind","querySourceCategoryName":"dbo","sourceFieldName":"ShipCountry","sourceFieldVisible":true,"sourceFieldFilterable":true,"sourceDataObjectName":"Orders","dataType":"Text","filterId":"00000000-0000-0000-0000-000000000000","querySourceFieldId":"d0f88020-8d3f-4f80-a1ac-0c187f87dfd3","querySourceType":"Table","querySourceId":"8fda0166-5f38-4ca1-ae20-9b6cab288f9d","relationshipId":null,"alias":"ShipCountry","position":1,"visible":false,"required":false,"cascading":true,"operatorId":"737307d1-1e5f-407f-889f-1b3c9a66dd6f","operatorSetting":null,"value":"'US'","sortType":"Unsorted","fontFamily":null,"fontSize":0,"textColor":null,"backgroundColor":null,"fontBold":false,"fontItalic":false,"fontUnderline":false,"id":"00000000-0000-0000-0000-000000000000","status":0,"modified":null,"dateTimeNow":"2016-06-13T07:23:25.9138114Z","isParameter":false,"sourceDataObjectFullName":"Northwind.dbo.Orders","selected":false}],"id":"00000000-0000-0000-0000-000000000000","reportId":"37e99389-fa8a-4f9f-9d03-f6362240c931"}
```
