---
title: "Build a Simple Grid"
id: 4415504585495
section: "Developer Guide"
category: "Izenda"
url: https://devnet.logianalytics.com/hc/en-us/articles/4415504585495-Build-a-Simple-Grid
updated_at: 2021-12-10T15:40:07Z
---

# Build a Simple Grid

# Build a Simple Grid

Steps:

1. Follow [Build a Generic Report](https://devnet.logianalytics.com/hc/en-us/articles/4415492651031-Build-a-Generic-Report) until the step to add report parts.
2. Prepare an empty [ReportPartGrid](https://devnet.logianalytics.com/hc/en-us/articles/4415512044183-ReportPartGrid) object with default properties.
3. For each selected data source fields, populate a [ReportPartElement](https://devnet.logianalytics.com/hc/en-us/articles/4415504774551-ReportPartElement) object with default properties.
4. Add the [ReportPartElement](https://devnet.logianalytics.com/hc/en-us/articles/4415504774551-ReportPartElement) objects into `columns.elements` in [ReportPartGrid](https://devnet.logianalytics.com/hc/en-us/articles/4415512044183-ReportPartGrid) object.
5. Update the properties of the grid in `properties` field per user selection (See [ReportPartGridProperties](https://devnet.logianalytics.com/hc/en-us/articles/4415492863895-ReportPartGridProperties)).
6. Back to the steps in [Build a Generic Report](https://devnet.logianalytics.com/hc/en-us/articles/4415492651031-Build-a-Generic-Report).

## Prepare an empty ReportPartGrid object

Empty ReportPartGrid object

* The highlighted `columns.elements` is where the selected data source fields will be added
* The highlighted `properties` contains the default properties

|  |  |
| --- | --- |
| ```   1 										2 										3 										4 										5 										6 										7 										8 										9 										10 										11 										12 										13 										14 										15 										16 										17 										18 										19 										20 										21 										22 										23 										24 										25 										26 										27 										28 										29 										30 										31 										32 										33 										34 										35 										36 										37 										38 										39 										40 										41 										42 										43 										44 										45 										46 										47 										48 										49 										50 										51 										52 										53 										54 										55 										56 										57 										58 										59 										60 										61 										62 										63 										64 										65 										66 										67 										68 										69 										70 										71 										72 										73 										74 										75 										76 										77 										78 										79 										80 										81 										82 										83 										84 										85 										86 										87 										88 										89 										90 										91 										92 										93 										94 										95 										96 										97 										98 										99 										100 										101 										102 										103 										104 										105 										106 										107 										108 										109 										110 										111 										112 										113 									114 ``` | ``` {"type":3,"columns":{"elements":[],"name":"columns"},"rows":{"elements":[],"name":"rows"},"values":{"elements":[],"name":"values"},"separators":{"elements":[],"name":"separators"},"properties":{"generalInfo":{"gridStyle":"Vertical","separatorStyle":"Comma"},"table":{"border":{"top":{},"right":{},"bottom":{},"midVer":{},"left":{},"midHor":{}},"backgroundColor":"#fff"},"columns":{"width":{"value":150},"alterBackgroundColor":false},"rows":{"alterBackgroundColor":false},"headers":{"font":{"family":"Roboto","size":14,"bold":true,"italic":false,"underline":false,"backgroundColor":"#E4E4E4"},"alignment":"left","wordWrap":false,"removeHeaderForExport":false},"grouping":{"useSeparator":true},"view":{"dataRefreshInterval":{"enable":false,"updateInterval":0,"isAll":true,"latestRecord":0},"usePagination":true,"pivotColumnsPerExportedPage":"","pageSize":10},"printing":{"usePageBreakAfterSeparator":false}},"settings":{},"title":{"text":"","properties":{},"settings":{"font":{"family":"","size":14,"bold":true,"italic":false,"underline":false,"color":"","highlightColor":""},"alignment":{"alignment":""}},"elements":[]},"description":{"text":"","properties":{},"settings":{"font":{"family":"","size":14,"bold":false,"italic":false,"underline":false,"color":"","highlightColor":""},"alignment":{"alignment":""}},"elements":[]}} ``` |

## Populate selected data sources fields

1. Get the list of available data sources fields from [POST report/availableQuerySourceFields](https://devnet.logianalytics.com/hc/en-us/articles/4415511952919-Report-Designer-Data-Sources-APIs#POST_report/availableQuerySourceFields) with this payload:

   ```
   {"reportKey":{"key":"<the id of the report>"}}
   ```

   The response is an array containing exactly one ReportDataSourceCategory object, with `querySource` field containing an array of selected data sources ([ReportQuerySource](https://devnet.logianalytics.com/hc/en-us/articles/4415492871575-ReportQuerySource) objects), with `fields` field containing an array of available data source fields. For example:

   ```
   [{"id":null,"name":"Selected Data Source","querySource":[{"id":"af773c7b-878e-461b-9345-27ee6592db1a","name":"Orders","originalName":"Orders","type":"Table","selected":true,"visible":true,"querySourceCategoryName":"dbo","connectionName":"test","isAlias":false,"isDynamic":false,"fields":[{"name":"CustomerID","remaining items":"have been omitted"},{"name":"OrderID","remaining items":"have been omitted"}]}]}]
   ```
2. For each selected data source field ([QuerySourceField](https://devnet.logianalytics.com/hc/en-us/articles/4415504743703-QuerySourceField) object), build a corresponding [ReportPartElement](https://devnet.logianalytics.com/hc/en-us/articles/4415504774551-ReportPartElement) object

   ```
   {"name":"<User-defined Field Name Alias of the selected QuerySourceField>","position":"<position in the list of selected fields>","field":{"fieldId":"<id of the selected QuerySourceField>","fieldName":"<name of the selected QuerySourceField>","fieldNameAlias":"User-defined Field Name Alias of the selected QuerySourceField","dataFieldType":"<Izenda data type of the selected QuerySourceField>","querySourceId":"<id of the parent QuerySource>","querySourceType":"<Table, View or Stored Procedure>","sourceAlias":"","relationshipId":null,"visible":true,"calculatedTree":null,"schemaName":"<name of the schema>","querySourceName":"<name of the parent QuerySource>","databaseName":"<name of the connection>","isCalculated":false,"hasAggregatedFunction":false},"properties":{}}
   ```

   | [`SampleQuerySourceField`](_downloads/9c3fee26c9afa1f6cd0d1515eeb3a9c0/QuerySourceField_OrderID.json) | [`SampleReportPartElement`](_downloads/a1a8300cb38019deceaf218c429c5fde/ReportPartElement_OrderID.json) |
   | --- | --- |
   | ``` {"name":"OrderID", ``` | ``` {"name":"OrderID", ``` |
   |  | ``` "position":1, ``` |
   | ``` "id":"b648344c-526e-4984-bfc3-7be462b800fe", ``` | ``` "fieldId":"b648344c-526e-4984-bfc3-7be462b800fe", ``` |
   | ``` "name":"OrderID", ``` | ``` "fieldName":"OrderID", ``` |
   | User entered “OID” | ``` "fieldNameAlias":"OID", ``` |
   | ``` "izendaDataType":"Numeric", ``` | ``` "dataFieldType":"Numeric", ``` |
   | ``` "querySourceId":"af773c7b-878e-461b-9345-27ee6592db1a", ``` | ``` "querySourceId":"af773c7b-878e-461b-9345-27ee6592db1a", ``` |
   | ``` "type":0, ``` | ``` "querySourceType":"Table", ``` |
   | Alias of the parent QuerySource | ``` "sourceAlias":"Orders", ``` |
   | Name of the schema | ``` "schemaName":"dbo", ``` |
   | Name of the parent QuerySource | ``` "querySourceName":"Orders", ``` |
   | Name of the database | ``` "databaseName":"test", ``` |
   | ``` "visible":true, ``` | ``` "visible":true, ``` |
   |  | ``` "relationshipId":null,"calculatedTree":null,"isCalculated":false,"hasAggregatedFunction":false}, ``` |

   See [Sample Properties for a ReportPartElement](https://devnet.logianalytics.com/hc/en-us/articles/4415492658583-Sample-Properties-for-a-ReportPartElement) for more samples.
3. Populate a default [ReportPartElementProperties](https://devnet.logianalytics.com/hc/en-us/articles/4415512042263-ReportPartElementProperties) for `properties` field in each [ReportPartElement](https://devnet.logianalytics.com/hc/en-us/articles/4415504774551-ReportPartElement) object

   Default ReportPartElementProperties object

   ```
   {"fieldItemVisible":true,"dataFormattings":{"function":"","functionInfo":{},"format":{},"font":{"family":"Roboto","size":14,"bold":false,"italic":false,"underline":false,"color":"","backgroundColor":""},"width":{"value":null},"alignment":"alignLeft","sort":"ASC","color":{"textColor":{"rangePercent":null,"rangeValue":null,"value":null},"cellColor":{"rangePercent":null,"rangeValue":null,"value":null}},"alternativeText":{"rangePercent":null,"rangeValue":null,"value":null},"customURL":{"url":"","option":"LINK_NEW_WINDOW"},"embeddedJavascript":{"script":""},"subTotal":{"label":"","function":"","expression":"","dataType":"","format":{},"previewResult":""},"grandTotal":{"label":"","function":"","expression":"","dataType":"","format":{},"previewResult":""}},"headerFormating":{"font":{"family":null,"size":null,"bold":null,"italic":null,"underline":null,"color":null,"backgroundColor":null},"alignment":null,"wordWrap":null,"columnGroup":""},"drillDown":{"subReport":{"selectedReport":null,"style":null,"reportPartUsed":null,"reportFilter":true,"mappingFields":[],"selectedIconValue":{"icon":null,"value":null},"viewSettingByLink":null}},"otherProps":{}}
   ```
4. Add the [ReportPartElement](https://devnet.logianalytics.com/hc/en-us/articles/4415504774551-ReportPartElement) objects into `columns.elements` in [ReportPartGrid](https://devnet.logianalytics.com/hc/en-us/articles/4415512044183-ReportPartGrid) object.

   Sample full ReportPartGrid object

   ```
   {"type":3,"columns":{"elements":[{"name":"OrderID","position":1,"field":{"fieldId":"b648344c-526e-4984-bfc3-7be462b800fe","fieldName":"OrderID","fieldNameAlias":"OID","dataFieldType":"Numeric","querySourceId":"af773c7b-878e-461b-9345-27ee6592db1a","querySourceType":"Table","sourceAlias":"Orders","schemaName":"dbo","querySourceName":"Orders","databaseName":"test","visible":true,"relationshipId":null,"calculatedTree":null,"isCalculated":false,"hasAggregatedFunction":false},"properties":{"fieldItemVisible":true,"dataFormattings":{"function":"","functionInfo":{},"format":{},"font":{"family":"Roboto","size":14,"bold":false,"italic":false,"underline":false,"color":"","backgroundColor":""},"width":{"value":null},"alignment":"alignLeft","sort":"ASC","color":{"textColor":{"rangePercent":null,"rangeValue":null,"value":null},"cellColor":{"rangePercent":null,"rangeValue":null,"value":null}},"alternativeText":{"rangePercent":null,"rangeValue":null,"value":null},"customURL":{"url":"","option":"LINK_NEW_WINDOW"},"embeddedJavascript":{"script":""},"subTotal":{"label":"","function":"","expression":"","dataType":"","format":{},"previewResult":""},"grandTotal":{"label":"","function":"","expression":"","dataType":"","format":{},"previewResult":""}},"headerFormating":{"font":{"family":null,"size":null,"bold":null,"italic":null,"underline":null,"color":null,"backgroundColor":null},"alignment":null,"wordWrap":null,"columnGroup":""},"drillDown":{"subReport":{"selectedReport":null,"style":null,"reportPartUsed":null,"reportFilter":true,"mappingFields":[],"selectedIconValue":{"icon":null,"value":null},"viewSettingByLink":null}},"otherProps":{}},"isDeleted":false,"isSelected":false,"offset":{}}],"name":"columns"},"rows":{"elements":[],"name":"rows"},"values":{"elements":[],"name":"values"},"separators":{"elements":[],"name":"separators"},"properties":{"generalInfo":{"gridStyle":"Vertical","separatorStyle":"Comma"},"table":{"border":{"top":{},"right":{},"bottom":{},"midVer":{},"left":{},"midHor":{}},"backgroundColor":"#fff"},"columns":{"width":{"value":150},"alterBackgroundColor":false},"rows":{"alterBackgroundColor":false},"headers":{"font":{"family":"Roboto","size":14,"bold":true,"italic":false,"underline":false,"backgroundColor":"#E4E4E4"},"alignment":"left","wordWrap":false,"removeHeaderForExport":false},"grouping":{"useSeparator":true},"view":{"dataRefreshInterval":{"enable":false,"updateInterval":0,"isAll":true,"latestRecord":0},"usePagination":true,"pivotColumnsPerExportedPage":"","pageSize":10},"printing":{"usePageBreakAfterSeparator":false}},"settings":{},"title":{"text":"","properties":{},"settings":{"font":{"family":"","size":14,"bold":true,"italic":false,"underline":false,"color":"","highlightColor":""},"alignment":{"alignment":""}},"elements":[]},"description":{"text":"","properties":{},"settings":{"font":{"family":"","size":14,"bold":false,"italic":false,"underline":false,"color":"","highlightColor":""},"alignment":{"alignment":""}},"elements":[]}}
   ```

## Update the properties of each field per user selection

Please see [ReportPartElementProperties](https://devnet.logianalytics.com/hc/en-us/articles/4415512042263-ReportPartElementProperties) for the purpose of each field.

See [Sample Properties for a ReportPartElement](https://devnet.logianalytics.com/hc/en-us/articles/4415492658583-Sample-Properties-for-a-ReportPartElement) for more samples.

## Update the properties of the grid in “properties” field per user selection

Please see [ReportPartGridProperties](https://devnet.logianalytics.com/hc/en-us/articles/4415492863895-ReportPartGridProperties) for the purpose of each field.

## Back to the step in Build a Generic Report
