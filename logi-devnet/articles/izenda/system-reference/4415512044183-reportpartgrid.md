---
title: "ReportPartGrid"
id: 4415512044183
section: "System Reference"
category: "Izenda"
url: https://devnet.logianalytics.com/hc/en-us/articles/4415512044183-ReportPartGrid
updated_at: 2021-12-10T03:09:32Z
---

# ReportPartGrid

# ReportPartGrid

| Field | NULL | Description |
| --- | --- | --- |
| **type**  integer |  | The type of the report part (3 = Grid) |
| **title**  object |  | To be updated |
| **description**  object |  | To be updated |
| **properties**  object |  | A [ReportPartGridProperties](https://devnet.logianalytics.com/hc/en-us/articles/4415492863895-ReportPartGridProperties) object |
| **settings**  object |  | A dynamic object to keep the settings in Report Part Configuration, can be user-defined. |
| **columns**  object |  | Data for the Columns box   A [ReportPartContainer](https://devnet.logianalytics.com/hc/en-us/articles/4415512040215-ReportPartContainer) object containing “columns” in **name** and the list of selected data source fields in **elements** |
| **values**  object |  | To be updated |
| **rows**  object |  | To be updated |
| **separators**  object |  | Data for the Separators box   A [ReportPartContainer](https://devnet.logianalytics.com/hc/en-us/articles/4415512040215-ReportPartContainer) object containing “separators” in **name** and the list of selected data source fields in **elements** |
