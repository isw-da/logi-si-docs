---
title: "ReportPartGaugeProperties"
id: 4415504777879
section: "System Reference"
category: "Izenda"
url: https://devnet.logianalytics.com/hc/en-us/articles/4415504777879-ReportPartGaugeProperties
updated_at: 2021-12-10T03:09:31Z
---

# ReportPartGaugeProperties

# ReportPartGaugeProperties

| Field | NULL | Description |
| --- | --- | --- |
| **chartType**  string |  | The gauge type: either SolidGauge, LinearGauge or SimpleGauge |
| **optionByType**  object |  | The options that are specific for each chart type |
| **izUseSeparator**  boolean |  | Whether to use separators |
| **izUsePagination**  boolean |  | Whether to use pagination |
| **izItemPerRow**  integer |  | The number of gauges per row, default 3 |
| **view**  object |  |  |
| **showLabels**  boolean |  | Whether to show labels |
| **dataRefreshInterval**  object |  | An object with the following fields |
| **enable**  boolean |  | Is this feature turned on |
| **updateInteval**  integer |  | The refresh interval |
| **isAll**  boolean |  | View all data (or x latest records) |
| **latestRecord**  integer |  | How many latest records to retrieve |
| **printing**  object |  | An object with the following fields |
| **izPageBreak** **AfterSeparator**  boolean |  | Whether to insert page break after separator |
