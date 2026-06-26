---
title: "ReportQuerySource"
id: 4415492871575
section: "System Reference"
category: "Izenda"
url: https://devnet.logianalytics.com/hc/en-us/articles/4415492871575-ReportQuerySource
updated_at: 2021-12-10T03:09:34Z
---

# ReportQuerySource

# ReportQuerySource

| Field | NULL | Description | Note |
| --- | --- | --- | --- |
| **id**  string (GUID) |  | The id of the query source |  |
| **name**  string |  | The name of the query source |  |
| **originalName**  string |  | The orignal name of the query source |  |
| **type**  string |  | Either “Table”, “View”, “Function” or “Stored Procedure” |  |
| **selected**  boolean |  | Is the query source selected |  |
| **visible**  boolean |  | Is the query source visible |  |
| **querySourceCategoryName**  string |  | The name of the category of the query source if available |  |
| **connectionName**  string |  | The name of the connection of the query source |  |
| **isAlias**  boolean |  | Is the query source an alias |  |
| **isDynamic**  boolean |  | Is the query source a dynamic stored procedure |  |
| **fields**  array of objects |  | An array of [QuerySourceField](https://devnet.logianalytics.com/hc/en-us/articles/4415504743703-QuerySourceField) objects |  |

**Sample**:

```
{"id":"d9728d5f-b6f6-462b-b988-8180bc733972","name":"HumanResources.Employee","type":"Table","selected":false,"visible":true,"querySourceCategoryName":null,"connectionName":null,"isAlias":false,"fields":[{"id":"bd207050-e2a4-4128-9b5a-89409bee0377","name":"Gender","alias":"","dataType":"nchar","izendaDataType":"Text","visible":true,"filterable":true,"extendedProperties":null,"isParameter":false,"allowDistinct":false}]}
```
