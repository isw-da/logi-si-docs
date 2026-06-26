---
title: "ReportValidation"
id: 12528298376215
section: "System Reference"
category: "Izenda"
url: https://devnet.logianalytics.com/hc/en-us/articles/12528298376215-ReportValidation
updated_at: 2023-02-23T16:44:32Z
---

# ReportValidation

# ReportValidation

| Field | NULL | Description | Note |
| --- | --- | --- | --- |
| **reportName** string |  | The name of the report |  |
| **categoryName** string |  | The name of the category  Used in [POST report/validateExistingReport](https://devnet.logianalytics.com/hc/en-us/articles/12528279020567-Report-Designer-Details-APIs#post-report-validateexistingreport) |  |
| **subCategoryName** string |  | The name of the sub-category  Used in [POST report/validateExistingReport](https://devnet.logianalytics.com/hc/en-us/articles/12528279020567-Report-Designer-Details-APIs#post-report-validateexistingreport) |  |
| **tenantId** string (GUID) | Y | The id of the tenant if available |  |
| **columnFullReference** array of strings |  | An array of column names to be validated  Used in [POST report/validateExistingField](https://devnet.logianalytics.com/hc/en-us/articles/12528279020567-Report-Designer-Details-APIs#post-report-validateexistingfield) |  |
