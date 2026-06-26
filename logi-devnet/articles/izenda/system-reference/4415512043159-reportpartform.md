---
title: "ReportPartForm"
id: 4415512043159
section: "System Reference"
category: "Izenda"
url: https://devnet.logianalytics.com/hc/en-us/articles/4415512043159-ReportPartForm
updated_at: 2021-12-10T03:09:30Z
---

# ReportPartForm

# ReportPartForm

| Field | NULL | Description |
| --- | --- | --- |
| **type**  integer |  | The type of the report part (1 = Form) |
| **title**  object |  | To be updated |
| **description**  object |  | To be updated |
| **properties**  object |  | A [ReportPartFormProperties](https://devnet.logianalytics.com/hc/en-us/articles/4415504775831-ReportPartFormProperties) object |
| **columns**  object |  | Data for Columns box   A [ReportPartContainer](https://devnet.logianalytics.com/hc/en-us/articles/4415512040215-ReportPartContainer) object containing “columns” in **name** and the list of selected data source fields ([ReportPartElement](https://devnet.logianalytics.com/hc/en-us/articles/4415504774551-ReportPartElement) objects) in **elements** |
| **separators**  object |  | Data for Separators box   A [ReportPartContainer](https://devnet.logianalytics.com/hc/en-us/articles/4415512040215-ReportPartContainer) object containing “separators” in **name** and the list of selected data source fields ([ReportPartElement](https://devnet.logianalytics.com/hc/en-us/articles/4415504774551-ReportPartElement) objects) in **elements** |
| **reportPartFormRepeater**  object |  | To be updated |
| **reportPartFormEmbeddedReport**  object |  | To be updated |
| **reportPartFormSmartTag**  object |  | To be updated |
| **reportPartFormField**  object |  | To be updated |
| **formState**  object |  | To be updated |
| **htmlContent**  string |  | The HTML code built up for display, optionally edited by user |
| **selectedFieldElement**  object |  | To be updated |
| **activeTabKey**  string |  | To be updated |
| **isSelectedCell**  boolean |  | Whether |
| **isActiveForEdit**  string |  | Whether |
