---
title: "ReportDataSourceCategory"
id: 4415504754839
section: "System Reference"
category: "Izenda"
url: https://devnet.logianalytics.com/hc/en-us/articles/4415504754839-ReportDataSourceCategory
updated_at: 2021-12-10T03:09:16Z
---

# ReportDataSourceCategory

# ReportDataSourceCategory

| Field | NULL | Description | Note |
| --- | --- | --- | --- |
| **id**  string (GUID) | Y | The id of the object |  |
| **name**  string |  | The name of the [data source category](https://devnet.logianalytics.com/hc/en-us/articles/4415492696343-Glossary#term-data-source-category) |  |
| **querySource**  array of objects |  | An array of [ReportQuerySource](https://devnet.logianalytics.com/hc/en-us/articles/4415492871575-ReportQuerySource) objects |  |

**Sample**:

```
{"id":"f28d7175-4cef-478e-b914-ae075c3c33b8","name":"Data Source Category 1","querySource":[{"id":"ffd40590-aa27-4a14-8ebf-f32a0567bc08","name":"Department","type":"Table","selected":false,"visible":true,"querySourceCategoryName":"HumanResources","connectionName":"AdventureWorks2008R2","isAlias":false,"fields":[{"id":"5da4090d-9b31-433c-b9bb-e9e82fcc92a8","name":"DepartmentID","alias":null,"dataType":"smallint","unitDataType":"Number","visible":true,"filterable":true,"extendedProperties":"{\"PrimaryKey\":true}","isParameter":false,"allowDistinct":false},{"id":"2636eeb4-cb65-48f4-9da6-2bfe5cd0659a","name":"Name","alias":null,"dataType":"nvarchar","unitDataType":"Text","visible":true,"filterable":true,"extendedProperties":"","isParameter":false,"allowDistinct":false}]}]}
```
