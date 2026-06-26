---
title: "ReportPartGridProperties"
id: 4415492863895
section: "System Reference"
category: "Izenda"
url: https://devnet.logianalytics.com/hc/en-us/articles/4415492863895-ReportPartGridProperties
updated_at: 2021-12-10T03:09:32Z
---

# ReportPartGridProperties

# ReportPartGridProperties

| Field | NULL | Description |
| --- | --- | --- |
| **generalInfo**  object |  | An object with the following fields |
| **gridStyle**  string |  | Either “Vertical”, “Horizontal”, “Pivot” or “Drill Down” |
| **separatorStyle**  string |  | Either “Comma”, “Comma With Label”, “Line”, “Line With Label”, “Multi Level” or “Multi Level With Label” |
| **table**  object |  | An object with the following fields |
| **border**  object |  | An object with the following fields |
| **top**  object |  | An object with 3 fields: dashStyle, color and thickness   Example: {“dashStyle”:”dotted”,”color”:”#000”,”thickness”:1} |
| **right**  object |  | An object with 3 fields: dashStyle, color and thickness   Example: {“dashStyle”:”dotted”,”color”:”#000”,”thickness”:1} |
| **bottom**  object |  | An object with 3 fields: dashStyle, color and thickness   Example: {“dashStyle”:”dotted”,”color”:”#000”,”thickness”:1} |
| **midVer**  object |  | An object with 3 fields: dashStyle, color and thickness   Example: {“dashStyle”:”dotted”,”color”:”#000”,”thickness”:1} |
| **left**  object |  | An object with 3 fields: dashStyle, color and thickness   Example: {“dashStyle”:”dotted”,”color”:”#000”,”thickness”:1} |
| **midHor** |  | An object with 3 fields: dashStyle, color and thickness   Example: {“dashStyle”:”dotted”,”color”:”#000”,”thickness”:1} |
| **backgroundColor**  string |  | The background color value |
| **columns**  object |  | An object with the following fields |
| **width**  object |  | An object with the following fields |
| **value**  integer |  | The width |
| **alterBackgroundColor**  boolean |  | Use Alternating Background Color or not |
| **rows**  object |  | An object with the following fields |
| **alterBackgroundColor**  boolean |  | Use Alternating Background Color or not |
| **headers**  object |  | An object with the following fields |
| **font**  object |  | An object with the following fields |
| **family**  string |  | The font family |
| **size**  integer |  | The font size |
| **bold**  boolean |  | Is the text in bold |
| **italic**  boolean |  | Is the text italic |
| **underline**  boolean |  | Is the text underlined |
| **backgroundColor**  string |  | The background color |
| **alignment**  string |  | The text alignment |
| **wordWrap**  boolean |  | Turns on word wrap or not |
| **removeHeaderForExport**  boolean |  | Remove header when exporting or not |
| **grouping**  object |  | An object with the following fields |
| **useSeparator**  boolean |  | Turns on Separator or not |
| **view**  object |  | An object with the following fields |
| **dataRefreshInterval**  object |  | An object with the following fields |
| **enable**  boolean |  | Is this feature turned on |
| **updateInteval**  integer |  | The refresh interval |
| **isAll**  boolean |  | View all data (or x latest records) |
| **latestRecord**  integer |  | How many latest records to retrieve |
| **usePagination**  boolean |  | Whether to use pagination |
| **pivotColumns** **PerExportedPage**  integer |  | An object with the following fields |
| **pageSize**  integer |  | The page size |
| **printing**  object |  | An object with the following fields |
| **usePageBreak** **AfterSeparator**  boolean |  | Whether to insert page break after separator |
