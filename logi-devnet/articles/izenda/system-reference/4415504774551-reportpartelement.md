---
title: "ReportPartElement"
id: 4415504774551
section: "System Reference"
category: "Izenda"
url: https://devnet.logianalytics.com/hc/en-us/articles/4415504774551-ReportPartElement
updated_at: 2021-12-10T03:09:29Z
---

# ReportPartElement

# ReportPartElement

| Field | NULL | Description |
| --- | --- | --- |
| **name**  string |  | The name of the selected data source field |
| **properties**  object |  | The properties for the selected data source field   A [ReportPartElementProperties](https://devnet.logianalytics.com/hc/en-us/articles/4415512042263-ReportPartElementProperties) object |
| **position**  integer |  | The position in the list of selected items, starting from 0 |
| **field**  object |  | The data of the selected data source field |
| **fieldId**  string (GUID) |  | The id of the field |
| **fieldName**  string |  | The name of the field |
| **fieldNameAlias**  string |  | The alias of the field |
| **dataFieldType**  string |  | The Izenda data type |
| **querySourceId**  string (GUID) |  | The id of the data source |
| **querySourceType**  string |  | The type of the data source (Table, View or Stored Procedure) or null if it is an alias |
| **sourceAlias**  string |  | The alias of the data source |
| **relationshipId**  string (GUID) |  | The id of the alias data source, null if data source is not an alias |
| **visible**  boolean |  | Is the field visible |
| **calculatedTree**  object |  | Place-holder |
| **schemaName**  string |  | The name of the schema of the query source |
| **querySourceName**  string |  | The name of the query source |
| **databaseName**  string |  | The name of the connection |
| **isCalculated**  boolean |  | Is this a calculated field |
| **hasAggregatedFunction**  boolean |  | In case of calculated field, does it use an aggregated function |
