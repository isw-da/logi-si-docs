---
title: "ReportFilterField"
id: 4415504761879
section: "System Reference"
category: "Izenda"
url: https://devnet.logianalytics.com/hc/en-us/articles/4415504761879-ReportFilterField
updated_at: 2021-12-10T03:09:20Z
---

# ReportFilterField

# ReportFilterField

| Field | NULL | Description | Note |
| --- | --- | --- | --- |
| **connectionName**  string |  | The name of the connection |  |
| **querySourceCategoryName**  string |  | The name of the category of the data source |  |
| **sourceFieldName**  string |  | The name of the data source field |  |
| **sourceFieldVisible**  boolean |  | Is the data source field selected to be visible in Data Model |  |
| **sourceFieldFilterable**  boolean |  | Is the data source field selected to be filterable in Data Model |  |
| **sourceDataObjectName**  string |  | The name of the data source |  |
| **sourceDataObjectFullName**  string |  | The fully-qualified name of the data source |  |
| **dataType**  string |  | The data type of the data source field |  |
| **isParameter**  boolean |  | Is the filter field a stored procedure parameter |  |
| **isCalculated**  boolean |  | Is this a calculated field |  |
| **calculatedTree**  string |  | The calculated tree |  |
| **compareFieldCalculatedTree**  string |  | The compare field calculated tree used for filter field comparison |  |
| **compareField**  string (GUID) | Y | The id of the compare field - used for filter field comparison |  |
| **selected**  boolean |  | Is the filter field selected |  |
| **dataFormat**  object |  | A [DataFormat](https://devnet.logianalytics.com/hc/en-us/articles/4415504710423-DataFormat) object |  |
| **reportId**  string (GUID) | Y | The id of the report |  |
| **useMappedFieldAlias**  boolean |  | Internal use: whether filter uses mapped field alias, if yes, it will not be re-calculated to generate expression. |  |
| **uniqueId**  string (GUID) |  | The unique id for [Front-end](https://devnet.logianalytics.com/hc/en-us/articles/4415492696343-Glossary#term-front-end) to show specific error messages |  |
| **comparisonValue**  string |  | The comparison value |  |
| **inTimePeriodType**  string |  | The type of custom in time period |  |
| **valueInTimePeriod**  string |  | The value of custom in time period |  |
| **hasModifiedCalculatedTree**  boolean |  | Whether this instance has modified calculated tree |  |
| **isHiddenFilter**  boolean |  | Whether this instance is hidden filter |  |
| **isInheritableFilter**  boolean |  | Whether this filter is inherited from its master report |  |
| **operatorName**  string |  | The name of the operator |  |
| **filterLookupType**  int  New in version 2.15.0. |  | Determine the type of lookup setting:  - 0: No filter lookup   - 1: Filter lookup key-value   - 2: User defined user lookup |  |
| **useLookup**  boolean  New in version 2.15.0. |  | Whether use lookup key-value setting or not |  |
| **hasFilterLookup**  boolean  Obsolete from version 2.15.0 |  | Whether this field has filter lookup setting or not |  |
| **isOveridingInheritedFilter**  boolean  New in version 2.15.1. |  | Whether the master filter value overrides the sub filter value |  |

Inherited fields:

## FilterField

| Field | NULL | Description | Note |
| --- | --- | --- | --- |
| **filterId**  string (GUID) |  | The id of the filter |  |
| **reportFieldAlias**  string |  | The alias of the field |  |
| **reportPartTitle**  string |  | The report part title |  |
| **querySourceFieldId**  string (GUID) |  | The id of the query source field |  |
| **querySourceType**  string |  | Either “Table”, “View”, “Stored Procedure” or “Function” |  |
| **querySourceId**  string (GUID) | Y | The id of the query source |  |
| **relationshipId**  string (GUID) | Y | The id of the relationship if this field is in a relationship |  |
| **alias**  string |  | The alias of the field |  |
| **position**  integer |  | The position in the list of filters |  |
| **visible**  boolean |  | Is the filter field visible |  |
| **required**  boolean |  | Is the filter field required |  |
| **cascading**  boolean |  | Whether common filter field will be cascaded |  |
| **operatorId**  string (GUID) | Y | The id of the operator |  |
| **operatorSetting**  string |  | The operator setting |  |
| **value**  string |  | The value for the filter field and the selected operator |  |
| **dataFormatId**  string (GUID) | Y | The id of the display format for the filter field |  |
| **sortType**  string |  | Either “Unsorted”, “Ascending” or “Descending” |  |
| **fontFamily**  string |  | The font family |  |
| **fontSize**  integer |  | The font size |  |
| **textColor**  string |  | The text color |  |
| **backgroundColor**  string |  | The background color |  |
| **fontBold**  boolean |  | Is the text in bold |  |
| **fontItalic**  boolean |  | Is the text in italic |  |
| **fontUnderline**  boolean |  | Is the text underlined |  |
| **querySourceUniqueName**  string |  | A unique name for query source |  |
| **querySourceFieldName**  string |  | The name of query source field |  |
| **comparisonFieldUniqueName**  string |  | The unique name for comparison field |  |
| **isNegative**  boolean |  | Whether this filter field is indeterminate |  |

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

**ReportFilterField Sample**:

```
{"connectionName":"Northwind","querySourceCategoryName":"dbo","sourceFieldName":"ShipCountry","sourceFieldVisible":true,"sourceFieldFilterable":true,"sourceDataObjectName":"Orders","dataType":"Text","filterId":"00000000-0000-0000-0000-000000000000","querySourceFieldId":"d0f88020-8d3f-4f80-a1ac-0c187f87dfd3","querySourceType":"Table","querySourceId":"8fda0166-5f38-4ca1-ae20-9b6cab288f9d","relationshipId":null,"alias":"ShipCountry","position":1,"visible":false,"required":false,"cascading":true,"operatorId":"737307d1-1e5f-407f-889f-1b3c9a66dd6f","operatorSetting":null,"value":"'US'","sortType":"Unsorted","fontFamily":null,"fontSize":0,"textColor":null,"backgroundColor":null,"fontBold":false,"fontItalic":false,"fontUnderline":false,"id":"00000000-0000-0000-0000-000000000000","status":0,"modified":null,"dateTimeNow":"2016-06-13T07:23:25.9138114Z","isParameter":false,"sourceDataObjectFullName":"Northwind.dbo.Orders","selected":false}
```
