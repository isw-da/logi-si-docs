---
title: "ReportDataSource"
id: 4415492850839
section: "System Reference"
category: "Izenda"
url: https://devnet.logianalytics.com/hc/en-us/articles/4415492850839-ReportDataSource
updated_at: 2021-12-10T03:09:16Z
---

# ReportDataSource

# ReportDataSource

| Field | NULL | Description | Note |
| --- | --- | --- | --- |
| **reportId**  string (GUID) | Y | The id of the report |  |
| **querySourceId**  string (GUID) | Y | The id of the query source |  |
| **querySourceUniqueName**  string |  | Unique name for the query source |  |
| **querySourceCategoryId**  string (GUID) | Y | The id of the schema |  |
| **connectionId**  string (GUID) | Y | The id of the connection |  |
| **selected**  boolean |  | Is this data source selected on the UI |  |

Inherited fields:

## Entity

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
