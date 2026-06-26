---
title: "RelationshipKeyJoin"
id: 12528282229527
section: "System Reference"
category: "Izenda"
url: https://devnet.logianalytics.com/hc/en-us/articles/12528282229527-RelationshipKeyJoin
updated_at: 2023-02-23T16:40:31Z
---

# RelationshipKeyJoin

# RelationshipKeyJoin

| Field | NULL | Description | Note |
| --- | --- | --- | --- |
| **relationshipId** string (GUID) |  | The id of the relationship |  |
| **operator** string |  | Either “And” or “Or” |  |
| **joinSourceAlias** string |  | The alias of the join query source |  |
| **specifictJoinFieldAlias** string |  | The alias to be used in query without generating a new one |  |
| **foreignSourceAlias** string |  | The alias of the foregin query source |  |
| **specifictForeignFieldAlias** string |  | The alias to be used in query without generating a new one |  |
| **position** integer |  | The position of the key join in the relationship |  |
| **tempId** string |  | The temporary id |  |
| **joinQuerySourceUniqueName** string |  | Unique name for join query source |  |
| **joinFieldUniqueName** string |  | Unique name for join field |  |
| **foreignQuerySourceUniqueName** string |  | Unique name for foreign query source |  |
| **foreignFieldUniqueName** string |  | Unique name for foreign field |  |
| **comparisonValue** string |  | The comparison value |  |
| **selectedJoinSourceAlias** string |  | `<joinQuerySourceId>_[<joinSourceAlias>|<joinQuerySourceName>]` |  |
| **selectedForeignSourceAlias** string |  | `<foreignQuerySourceId>_[<foreignSourceAlias>|<foreignQuerySourceName>]` |  |
| **convertedFromRelationshipId** string(GUID) | Y | The id of the relationship that converted to key join |  |

Inherited fields:

## RelationshipBase

| Field | NULL | Description | Note |
| --- | --- | --- | --- |
| **joinQuerySourceName** string |  | The alias/name of the query source containing the relationship |  |
| **joinQuerySourceId** string (GUID) |  | The id of the query source containing the relationship |  |
| **joinFieldId** string (GUID) | Y | The id of the referencing field |  |
| **joinFieldType** string |  | Place-holder |  |
| **foreignQuerySourceName** string |  | The alias/name of the query source referenced by the relationship |  |
| **foreignQuerySourceId** string (GUID) |  | The id of the query source referenced by the relationship |  |
| **foreignFieldId** string (GUID) | Y | The id of the field referenced by the relationship |  |
| **foreignFieldType** string |  | Place-holder |  |
| **joinFieldName** string |  | The alias/name of the referencing field |  |
| **foreignFieldName** string |  | The alias/name of the field referenced by the relationship |  |
| **joinDataSourceCategoryId** string (GUID) |  | The id of the category of the query source containing the relationship |  |
| **joinDataSourceCategoryName** string |  | The name of the category of the query source containing the relationship |  |
| **foreignDataSourceCategoryId** string (GUID) |  | The id of the category of the query source referenced by the relationship |  |
| **foreignDataSourceCategoryName** string |  | The name of the category of the query source referenced by the relationship |  |
| **comparisonOperator** string |  | The comparison operator |  |

Inherited fields:

### Entity

| Field | NULL | Description | Note |
| --- | --- | --- | --- |
| **id** string (GUID) |  | The id of this object  Example: `572bd576-8c92-4901-ab2a-b16e38144813` | Allow null incase insert a new entity |
| **state** integer |  | The entity state of this object   * 0 = None * 1 = Insert * 2 = Delete * 3 = Update |  |
| **deleted** boolean |  | Is this object deleted |  |
| **inserted** boolean |  | Is this object inserted |  |
| **version** string | Y | The version |  |
| **created** datetime in ISO 8601 format | Y | The created datetime |  |
| **createdBy** string |  | The creator |  |
| **modified** datetime in ISO 8601 format | Y | The modification datetime |  |
| **modifiedBy** string |  | The user who last modified this object |  |
