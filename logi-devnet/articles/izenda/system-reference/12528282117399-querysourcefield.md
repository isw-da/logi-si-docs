---
title: "QuerySourceField"
id: 12528282117399
section: "System Reference"
category: "Izenda"
url: https://devnet.logianalytics.com/hc/en-us/articles/12528282117399-QuerySourceField
updated_at: 2023-02-23T16:14:10Z
---

# QuerySourceField

# QuerySourceField

| Field | NULL | Description | Note |
| --- | --- | --- | --- |
| **alias** string |  | The alias entered by user |  |
| **allowDistinct** boolean |  | Does the data type allow distinct select or not |  |
| **approval** boolean |  | Is the change approved |  |
| **calculatedTree** object |  | The calculated tree |  |
| **categoryName** string |  | The name of the [query source category](https://devnet.logianalytics.com/hc/en-us/articles/12528224699927-Glossary#term-query-source-category) |  |
| **checked** boolean  New in version 3.11.0. |  | Is the field checked for some operations or not (like for PII/Data Security) |  |
| **dataType** string |  | The data type of the field |  |
| **existed** boolean |  | Exist flag |  |
| **expression** string |  | The calculated expression in case this is a calculated field |  |
| **expressionFields** array of objects | Y | An array of [ReportField](https://devnet.logianalytics.com/hc/en-us/articles/12528297944471-ReportField) objects |  |
| **extendedProperties** string |  | The extended properties (for stored procedures and functions) |  |
| **filterable** boolean |  | Is the field selected to be filterable in report |  |
| **filteredValue** string |  | The filter value in json format - when the field is a stored procedure parameter |  |
| **filterStatus** integer  New in version 2.14.0. |  | The status of filter lookup key-value  * 0: valid lookup (default state) * 1: invalid query source * 2: invalid database connection * 4: lookup key is a Tenant Field * 8: lookup key is invisible * 16: display value is a Tenant Field * 32: display value is invisible  **Note:** If multiple errors occur at the same time, system will return the sum of error code. |  |
| **fullName** string |  | The fully-qualified name of the field |  |
| **functionName** string |  | Place-holder |  |
| **groupPosition** integer |  | The group position |  |
| **hasAggregatedFunction** boolean |  | Whether this calculated field contains an aggregated function |  |
| **hasFilterLookup** boolean  New in version 2.14.0. |  | Whether this field has filter lookup setting or not |  |
| **inaccessible** boolean |  | Whether this is inaccessible |  |
| **indeterminate** boolean |  | * true if 0 < numOfCheckedChilds < numOfChilds * false if not |  |
| **isCalculated** boolean |  | Is this a calculated field |  |
| **isCheck** boolean |  | Whether this is selected in workspace for copying |  |
| **isParameter** boolean |  | Is this a stored procedure parameter (or a normal field) |  |
| **izendaDataType** string |  | The mapped data type of the field |  |
| **matchedTenant** boolean |  | Is this query source field hidden from view because it is a tenant field (in Tenant Field setting), and current Show Tenant Field setting is false.  See also  Update\_settings\_in\_Security\_Additive\_Fields\_group |  |
| **name** string |  | The name of the query source field |  |
| **numOfCheckedChilds** integer |  | The number of selected children |  |
| **numOfChilds** integer |  | The number of children |  |
| **originalAlias** string |  | The original alias |  |
| **originalId** string (GUID) |  | The original id of the field - in case this field is cloned from a physical field |  |
| **originalName** string |  | The original name of the field - in case this field is cloned from a physical field |  |
| **parentId** string (GUID) | Y | The id of the parent of the parent query source |  |
| **physicalChange** integer |  | Has the field changed   * 0 = None * 1 = Added * 2 = Modified * 3 = Deleted |  |
| **position** integer |  | The ordinal position of the field inside the query source |  |
| **querySource** object |  | The parent [QuerySource](https://devnet.logianalytics.com/hc/en-us/articles/12528297595799-QuerySource) object |  |
| **querySourceId** string (GUID) |  | The id of the parent query source |  |
| **querySourceName** string |  | The name of the parent query source |  |
| **reportId** string (GUID) | Y | The id of the parent report - in case this is a calculated field |  |
| **type** integer |  | * 0 = Field * 1 = Parameter |  |
| **visible** boolean |  | Is the field selected to be visible in report |  |

Inherited fields:

## Entity

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

**Sample**:

```
{"id":"04ff2dc5-df20-48e3-bae8-443b400b0b89","name":"CustomerTypeID","alias":"CTypeID","dataType":"nchar","visible":true,"filterable":true,"deleted":false,"querySourceId":"9fa90af2-5329-44ac-a753-50c27f9d6fd5","parentId":null,"children":null,"modified":"2016-04-07T04:51:17","filteredValue":"{}","type":0,"position":0,"extendedProperties":"{\"PrimaryKey\":true}","physicalChange":0,"approval":0,"existed":false,"matchedTenant":false}
```
