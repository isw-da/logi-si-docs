---
title: "ReportRelationshipResult"
id: 12528282910231
section: "System Reference"
category: "Izenda"
url: https://devnet.logianalytics.com/hc/en-us/articles/12528282910231-ReportRelationshipResult
updated_at: 2023-02-19T08:37:26Z
---

# ReportRelationshipResult

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

# ReportRelationshipResult

| Field | NULL | Description | Note |
| --- | --- | --- | --- |
| **result**  array of objects |  | An array of [Relationship](https://devnet.logianalytics.com/hc/en-us/articles/12528282213015-Relationship) objects |  |
| **hasRemovedRelationship**  boolean |  | True if this instance has removed relationship; otherwise, false |  |
| **pageIndex**  integer |  | The index of the page | Inherited from [PagedResult](https://devnet.logianalytics.com/hc/en-us/articles/12528282006423-PagedResult) |
| **pageSize**  integer |  | The size of the page | Inherited from [PagedResult](https://devnet.logianalytics.com/hc/en-us/articles/12528282006423-PagedResult) |
| **total**  integer |  | The total number of rows | Inherited from [PagedResult](https://devnet.logianalytics.com/hc/en-us/articles/12528282006423-PagedResult) |
| **skipItems**  integer |  | Skip items | Inherited from [PagedResult](https://devnet.logianalytics.com/hc/en-us/articles/12528282006423-PagedResult) |
| **isLastPage**  boolean |  | Whether this is the last page | Inherited from [PagedResult](https://devnet.logianalytics.com/hc/en-us/articles/12528282006423-PagedResult) |

**Sample**:

```
{"hasRemovedRelationship":false,"result":[{"joinConnectionId":"11d2c31c-e726-4f80-8621-2b4856fae1a5","foreignConnectionId":"11d2c31c-e726-4f80-8621-2b4856fae1a5","joinQuerySourceId":"65d587e2-71f9-4565-8ad8-e6f532398455","joinQuerySourceName":"Employees","joinDataSourceCategoryName":null,"joinDataSourceCategoryId":"00000000-0000-0000-0000-000000000000","foreignDataSourceCategoryName":null,"foreignDataSourceCategoryId":"00000000-0000-0000-0000-000000000000","foreignQuerySourceId":"65d587e2-71f9-4565-8ad8-e6f532398455","foreignQuerySourceName":"Employees","joinFieldId":"d198eb03-6dee-4e3d-bc08-4ab11f08d3bd","joinFieldName":"ReportsTo","foreignFieldId":"f661a585-b463-426c-8849-dc6921139f7c","foreignFieldName":"EmployeeID","alias":null,"systemRelationship":true,"joinType":"Inner","parentRelationshipId":"00000000-0000-0000-0000-000000000000","deleted":false,"position":null,"relationshipPosition":0,"relationshipKeyJoins":null,"reportId":"00000000-0000-0000-0000-000000000000","foreignAlias":null,"selectedForeignAlias":"65d587e2-71f9-4565-8ad8-e6f532398455_Employees","id":"65fe4ced-577c-4da5-97a0-5e2903a0a7ab","state":0,"modified":"2016-04-28T03:33:48.4200000+07:00","dateTimeNow":"2016-04-28T04:04:09.0399962Z"}],"total":1,"pageIndex":1,"pageSize":10}
```
