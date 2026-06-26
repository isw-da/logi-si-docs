---
title: "ReportPartGaugeProperties"
id: 12528282773271
section: "System Reference"
category: "Izenda"
url: https://devnet.logianalytics.com/hc/en-us/articles/12528282773271-ReportPartGaugeProperties
updated_at: 2023-02-19T08:37:22Z
---

# ReportPartGaugeProperties

[Skip To Main Content](#)

Account

Settings

---

Logout

* placeholder

Account

Settings

---

Logout

Filter: 

* All Files

Submit Search

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
