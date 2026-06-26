---
title: "RelationshipBase"
id: 4415504748311
section: "System Reference"
category: "Izenda"
url: https://devnet.logianalytics.com/hc/en-us/articles/4415504748311-RelationshipBase
updated_at: 2021-12-10T03:09:10Z
---

# RelationshipBase

# RelationshipBase

| Field | NULL | Description | Note |
| --- | --- | --- | --- |
| **joinQuerySourceName**  string |  | The alias/name of the query source containing the relationship |  |
| **joinQuerySourceId**  string (GUID) |  | The id of the query source containing the relationship |  |
| **joinFieldId**  string (GUID) | Y | The id of the referencing field |  |
| **joinFieldType**  string |  | Place-holder |  |
| **foreignQuerySourceName**  string |  | The alias/name of the query source referenced by the relationship |  |
| **foreignQuerySourceId**  string (GUID) |  | The id of the query source referenced by the relationship |  |
| **foreignFieldId**  string (GUID) | Y | The id of the field referenced by the relationship |  |
| **foreignFieldType**  string |  | Place-holder |  |
| **joinFieldName**  string |  | The alias/name of the referencing field |  |
| **foreignFieldName**  string |  | The alias/name of the field referenced by the relationship |  |
| **joinDataSourceCategoryId**  string (GUID) |  | The id of the category of the query source containing the relationship |  |
| **joinDataSourceCategoryName**  string |  | The name of the category of the query source containing the relationship |  |
| **foreignDataSourceCategoryId**  string (GUID) |  | The id of the category of the query source referenced by the relationship |  |
| **foreignDataSourceCategoryName**  string |  | The name of the category of the query source referenced by the relationship |  |
| **comparisonOperator**  string |  | The comparison operator |  |

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
