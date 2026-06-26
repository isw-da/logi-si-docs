---
title: "ReportPartGauge"
id: 4415504776855
section: "System Reference"
category: "Izenda"
url: https://devnet.logianalytics.com/hc/en-us/articles/4415504776855-ReportPartGauge
updated_at: 2021-12-10T03:09:30Z
---

# ReportPartGauge

# ReportPartGauge

| Field | NULL | Description |
| --- | --- | --- |
| **type**  integer |  | The type of the report part (2 = Gauge) |
| **title**  object |  | To be updated |
| **description**  object |  | To be updated |
| **properties**  object |  | A [ReportPartGaugeProperties](https://devnet.logianalytics.com/hc/en-us/articles/4415504777879-ReportPartGaugeProperties) object |
| **labels**  object |  | Data for the Labels box   A [ReportPartContainer](https://devnet.logianalytics.com/hc/en-us/articles/4415512040215-ReportPartContainer) object containing “labels” in **name** and the list of selected data source fields in **elements** |
| **values**  object |  | Data for the Values box   A [ReportPartContainer](https://devnet.logianalytics.com/hc/en-us/articles/4415512040215-ReportPartContainer) object containing “values” in **name** and the list of selected data source fields in **elements** |
| **separators**  object |  | Data for the Separators box   A [ReportPartContainer](https://devnet.logianalytics.com/hc/en-us/articles/4415512040215-ReportPartContainer) object containing “separators” in **name** and the list of selected data source fields in **elements** |
