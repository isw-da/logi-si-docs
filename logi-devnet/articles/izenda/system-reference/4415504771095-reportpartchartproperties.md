---
title: "ReportPartChartProperties"
id: 4415504771095
section: "System Reference"
category: "Izenda"
url: https://devnet.logianalytics.com/hc/en-us/articles/4415504771095-ReportPartChartProperties
updated_at: 2021-12-10T03:09:27Z
---

# ReportPartChartProperties

# ReportPartChartProperties

| Field | NULL | Description |
| --- | --- | --- |
| **chartType**  string |  | The chart type   |  |  |  | | --- | --- | --- | | * Line * Column * Bar * Area * Pie | * Funnel * Donut * Combination * TreeMap * HeatMap | * Bubble * Scatter * Waterfall * Sparkline | |
| **commonOptions**  object |  | The options that are common for all chart types |
| **izHoverLabels**  boolean |  | Whether to show labels on hover |
| **izLegend.visibility**  boolean |  | Is the legend visible |
| **izLegend.horizontalAlign**  string |  | The alignment for horizontal axis, either izRight, izLeft or izCenter |
| **izLegend.verticalAlign**  string |  | The alignment for vertical axis, either izTop, izBottom or izMiddle |
| **izLegend.borderWidth**  integer |  | The border width for the legend |
| **izChartStyle**  object |  | To be updated |
| **izendaHiddenAllAxis**  boolean |  | Whether to hide all axis |
| **optionByType**  object |  | The options that are specific for each chart type |
| **izTotalLabel**  string |  | To be updated |
| **izUseSeparator**  boolean |  | Whether to use separators |
| **izInverted**  boolean |  | Whether to invert X-axis and Y-axis |
| **izSpline**  boolean |  | Whether to use spline |
| **izValueLabel**  boolean |  | Whether to show labels for values |
| **legendSettings**  boolean |  | Whether to use settings for legends |
| **view**  object |  |  |
| **dataRefreshInterval**  object |  | An object with the following fields |
| **enable**  boolean |  | Is this feature turned on |
| **updateInteval**  integer |  | The refresh interval |
| **isAll**  boolean |  | View all data (or x latest records) |
| **latestRecord**  integer |  | How many latest records to retrieve |
| **commonXYAxis**  object |  |  |
| **printing**  object |  | An object with the following fields |
| **izPageBreak** **AfterSeparator**  boolean |  | Whether to insert page break after separator |
