---
title: "ReportFilterValidationParameter"
id: 4415504764951
section: "System Reference"
category: "Izenda"
url: https://devnet.logianalytics.com/hc/en-us/articles/4415504764951-ReportFilterValidationParameter
updated_at: 2021-12-10T03:09:22Z
---

# ReportFilterValidationParameter

# ReportFilterValidationParameter

| Field | NULL | Description | Note |
| --- | --- | --- | --- |
| **reportId**  string (GUID) |  | The id of the report |  |
| **masterReportId**  string (GUID) | Y | The id of the master report |  |
| **reportWrapper** object | Y | A special object that is simplified in representation [ReportDefinition](https://devnet.logianalytics.com/hc/en-us/articles/4415492852759-ReportDefinition) object (used in the Report Designer 2.0) |  |
| **inheritMasterReportFilter** boolean |  | A flag that determines whether to inherit filters from master report |  |

**Sample**:

```
{
						"reportId": "90c5ee59-b816-4034-b927-e8f16b1c2759",
						"masterReportId": "ec7efb62-8a54-4803-bce6-5a2b10e6e3bd",
						"reportWrapper": null,
						"inheritMasterReportFilter": true,
						}
						
```
