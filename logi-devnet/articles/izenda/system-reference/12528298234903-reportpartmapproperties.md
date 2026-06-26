---
title: "ReportPartMapProperties"
id: 12528298234903
section: "System Reference"
category: "Izenda"
url: https://devnet.logianalytics.com/hc/en-us/articles/12528298234903-ReportPartMapProperties
updated_at: 2023-02-19T08:37:24Z
---

# ReportPartMapProperties

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

# ReportPartMapProperties

| Field | NULL | Description |
| --- | --- | --- |
| **chartType**  string | No | The map type: either SolidGauge, LinearGauge or SimpleGauge |
| **reportPartState**  object |  |  |
| **drilldownInfo**  array of objects |  | The drill down information |
| **activeSerie**  object | Y | To be updated |
| **pointOptionsList**  array of objects | **No** | Selected data source fields in Point Options boxes   Cannot be empty |
| **label**  string |  | Name of the data source field |
| **value**  string |  | Name of the data source field |
| **field**  object |  | The data of the selected data source field   An exact copy of content of **field** in [ReportPartElement](https://devnet.logianalytics.com/hc/en-us/articles/12528298149527-ReportPartElement) |
| **pointType**  string |  | Type of the point, either “country”, “state”, “county”, “city”, “postalCode”, “latitude” or “longtitude” |
| **pointTypeName**  string |  | Same value as **pointType** |
| **activePointOption**  object | **No** | The active point in the above **pointOptionsList**  Cannot be empty |
| **continentInfo**  object |  | To be updated |
| **countryInfo**  object |  | To be updated |
| **stateInfo**  object |  | To be updated |
| **commonOptions**  object |  | The options that are common for all map types |
| **izLegend.visibility**  boolean |  | Is the legend visible |
| **izLegend.horizontalAlign**  string |  | The alignment for horizontal axis, either izRight, izLeft or izCenter |
| **izLegend.verticalAlign**  string |  | The alignment for vertical axis, either izTop, izBottom or izMiddle |
| **izLegend.borderWidth**  integer |  | The border width for the legend |
| **izChartStyle**  object |  | To be updated |
| **izendaHiddenAllAxis**  boolean |  | Whether to hide all axis |
| **optionByType**  object |  | The options that are specific for each map type |
| **izValueLabel**  boolean |  | Whether to show value labels |
| **izShowTooltip**  boolean |  | Whether to show tooltips |
| **izMapLabel**  boolean |  | Whether to show labels for map |
| **izMapNavigation.enabled**  boolean |  | Whether map navigation is enabled |
| **legendSettings**  boolean |  | Whether legend settings are set |
| **view**  object |  |  |
| **showLabels**  boolean |  | Whether to show labels |
| **dataRefreshInterval**  object |  | An object with the following fields |
| **enable**  boolean |  | Is this feature turned on |
| **updateInteval**  integer |  | The refresh interval |
| **isAll**  boolean |  | View all data (or x latest records) |
| **latestRecord**  integer |  | How many latest records to retrieve |
