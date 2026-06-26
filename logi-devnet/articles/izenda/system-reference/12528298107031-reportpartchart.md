---
title: "ReportPartChart"
id: 12528298107031
section: "System Reference"
category: "Izenda"
url: https://devnet.logianalytics.com/hc/en-us/articles/12528298107031-ReportPartChart
updated_at: 2023-02-23T16:54:18Z
---

# ReportPartChart

# ReportPartChart

| Field | NULL | Description |
| --- | --- | --- |
| **type** integer |  | The type of the report part (0 = Chart) |
| **title** object |  | The title object |
| **description** object |  | The description object |
| **properties** object |  | A [ReportPartChartProperties](https://devnet.logianalytics.com/hc/en-us/articles/12528298115223-ReportPartChartProperties) object |
| **settings** object |  | A dynamic object to keep the settings in Report Part Configuration, can be user-defined. |
| **labels** object |  | Data for the Labels box  A [ReportPartContainer](https://devnet.logianalytics.com/hc/en-us/articles/12528298126359-ReportPartContainer) object containing “labels” in **name** and the list of selected data source fields in **elements** |
| **values** object |  | Data for the Values box  A [ReportPartContainer](https://devnet.logianalytics.com/hc/en-us/articles/12528298126359-ReportPartContainer) object containing “values” in **name** and the list of selected data source fields in **elements** |
| **valuesLabels** object |  | Data for the Values Labels box  A [ReportPartContainer](https://devnet.logianalytics.com/hc/en-us/articles/12528298126359-ReportPartContainer) object containing “valuesLabels” in **name** and the list of selected data source fields in **elements** |
| **separators** object |  | Data for the Separators box  A [ReportPartContainer](https://devnet.logianalytics.com/hc/en-us/articles/12528298126359-ReportPartContainer) object containing “separators” in **name** and the list of selected data source fields in **elements** |
| **bubbleSize** object |  | Data for the Bubble Size box  A [ReportPartContainer](https://devnet.logianalytics.com/hc/en-us/articles/12528298126359-ReportPartContainer) object containing “bubbleSize” in **name** and the list of selected data source fields in **elements** |
