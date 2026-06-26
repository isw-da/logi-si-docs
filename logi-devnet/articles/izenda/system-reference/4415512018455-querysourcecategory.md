---
title: "QuerySourceCategory"
id: 4415512018455
section: "System Reference"
category: "Izenda"
url: https://devnet.logianalytics.com/hc/en-us/articles/4415512018455-QuerySourceCategory
updated_at: 2021-12-10T03:09:04Z
---

# QuerySourceCategory

# QuerySourceCategory

| Field | NULL | Description | Note |
| --- | --- | --- | --- |
| **id**  string (GUID) |  | The id |  |
| **name**  string |  | The name |  |
| **parentCategoryId**  string (GUID) | Y | The id of the parent category |  |
| **connectionId**  string (GUID) |  | The id of the connection |  |
| **querySources**  array of objects |  | An array of [QuerySource](https://devnet.logianalytics.com/hc/en-us/articles/4415512017303-QuerySource) objects |  |
| **childs**  array of objects |  | An array of [QuerySourceCategory](#) objects |  |
| **connection**  object |  | A [Connection](https://devnet.logianalytics.com/hc/en-us/articles/4415504700055-Connection) object |  |
| **physicalChange**  integer |  | The change state |  |
| **existed**  boolean |  | Exist flag |  |
| **deleted**  boolean |  | Whether this has been deleted |  |
| **checked**  boolean |  | Whether this is checked on workspace for copying purpose |  |
| **totalTableChildNodes**  integer |  | The number of child nodes that are tables |  |
| **totalTableCheckedNodes**  integer |  | The number of selected for copying child nodes that are tables |  |
| **totalStoredProcedureChildNodes**  integer |  | The number of child nodes that are stored procedures |  |
| **totalStoredProcedureCheckedNodes**  integer |  | The number of selected for copying child nodes that are stored procedures |  |
| **totalViewChildNodes**  integer |  | The number of child nodes that are views |  |
| **totalViewCheckedNodes**  integer |  | The number of selected for copying child nodes that are views |  |
| **totalFunctionChildNodes**  integer |  | The number of child nodes that are functions |  |
| **totalFunctionCheckedNodes**  integer |  | The number of selected for copying child nodes that are functions |  |
