---
title: "ReportPartElementProperties"
id: 4415512042263
section: "System Reference"
category: "Izenda"
url: https://devnet.logianalytics.com/hc/en-us/articles/4415512042263-ReportPartElementProperties
updated_at: 2021-12-10T03:09:29Z
---

# ReportPartElementProperties

# ReportPartElementProperties

| Field | NULL | Description |
| --- | --- | --- |
| **fieldItemVisible**  boolean |  | Is the field visible |
| **dataFormattings**  object |  | The properties of the data source field, in Data Formatting group |
| **function**  string (GUID) |  | The id of the Izenda function |
| **functionInfo**  object |  | The properties for the function |
| **id**  string (GUID) |  | The id of the Izenda function |
| **name**  string |  | The name of the Izenda function |
| **expression**  string |  | The expression |
| **dataType**  string |  | The data type |
| **formatDataType**  string |  | The output data type |
| **syntax**  string |  | The syntax displayed to user |
| **expressionSyntax**  string |  | The syntax of the function/operator |
| **isOperator**  boolean |  | Is this an operator (or a function) |
| **userDefined**  boolean |  | Is this a user-defined function |
| **extendedProperties**  object |  | A dynamic object to store the extended properties |
| **format**  object |  |  |
| **createNewHiddenPercenOfGroupField**  string |  | Whether to create a new hidden “PercentOfGroup” field |
| **font**  string |  | The font properties |
| **family**  string |  | The font family, e.g. “Roboto” |
| **size**  integer |  | The font size |
| **bold**  boolean |  | Whether text is in bold |
| **italic**  boolean |  | Whether text is in italic |
| **underline**  boolean |  | Whether text is underlined |
| **color**  string |  | The text color |
| **backgroundColor**  string |  | The background color |
| **width**  string (GUID) |  | The width properties |
| **alignment**  string |  | The text alignment for the data source field, either “alignLeft”, “alignCenter” or “alignRight” |
| **sort**  string |  | The sorting option, either “ASC” or “DESC” |
| **color**  object |  | The color properties for the data source field |
| **textColor**  object |  | The text color properties |
| **rangePercent**  string |  | The range percent color option if available |
| **rangeValue**  string |  | The range value color option if available |
| **value**  string |  | The color value if available |
| **cellColor**  object |  | The cell color properties |
| **rangePercent**  string |  | The range percent color option if available |
| **rangeValue**  string |  | The range value color option if available |
| **value**  string |  | The color value if available |
| **alternativeText**  object |  | The alternative text property for the data source field |
| **rangePercent**  string |  | The range percent color option if available |
| **rangeValue**  string |  | The range value color option if available |
| **value**  string |  | The color value if available |
| **customURL**  object |  | The custom url property for the data source field |
| **url**  string |  | The url |
| **option**  string |  | Either “LINK\_NEW\_WINDOW”, “LINK\_NEW\_TAB” or “LINK\_CURRENT\_WINDOW” |
| **embeddedJavascript**  string |  | The Embedded Javascript property for the data source field |
| **script**  string |  | The script |
| **subTotal**  string |  | The Sub Total property for the data source field |
| **label**  string |  | The Subtotal label |
| **function**  string |  | The Subtotal function |
| **expression**  string |  | The Subtotal expression if available |
| **dataType**  string |  | The target data type |
| **format**  object |  | Format options |
| **previewResult**  string |  | The cached preview result |
| **levels**  string |  | The level of subtotal   For Form report part only  New in version 2.12.0. |
| **grandTotal**  string |  | The Grand Total property for the data source field |
| **label**  string |  | The Subtotal label |
| **function**  string |  | The Grandtotal function |
| **expression**  string |  | The Grandtotal expression if available |
| **dataType**  string |  | The target data type |
| **format**  object |  | Format options |
| **previewResult**  string |  | The cached preview result |
| **headerFormating**  object |  | The formatting of the header |
| **font**  object |  | The font properties of the header |
| **family**  string |  | The font family, e.g. “Roboto” |
| **size**  integer |  | The font size |
| **bold**  boolean |  | Whether text is in bold |
| **italic**  boolean |  | Whether text is in italic |
| **underline**  boolean |  | Whether text is underlined |
| **color**  string |  | The text color |
| **backgroundColor**  string |  | The background color |
| **alignment**  string |  | The header alignment |
| **wordWrap**  object |  | The header word wrap setting |
| **columnGroup**  string |  | The column group setting |
| **drillDown**  object |  | The drill down properties |
| **otherProps**  object |  | Other properties   A dynamic object |
| **metric**  object | Y | Properties for Gauge metrics |
| **scale**  object |  | The scale settings |
| **from**  integer |  | The minimum value of the scale |
| **to**  integer |  | The maximum value of the scale |
| **unitLabel**  string |  | The display unit label beneath the gauge |
| **thresholds**  object |  |  |
| **setting**  string |  | “static” or “dynamic” |
| **levels**  array of objects |  | An array of objects with the following fields |
| **name**  string |  | Either “low”, “target” or “high” |
| **color**  string |  | The color for the threshold level |
| **operator**  string |  | Either “less than”, “between” or “greater than” |
| **value**  integer |  | The value for “greater than” operator, or the minimum value for “between than” operator |
| **valueUpper**  integer |  | The value for “less than” operator, or the maximum value for “between than” operator |
| **element**  object |  | The element value for “greater than” operator, or the minimum element value for “between than” operator |
| **elementUpper**  object |  | The element value for “less than” operator, or the maximum element value for “between than” operator |
