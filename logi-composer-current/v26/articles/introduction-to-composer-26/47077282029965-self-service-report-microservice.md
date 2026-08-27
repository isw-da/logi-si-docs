---
title: "Self Service Report Microservice"
id: 47077282029965
section: "Introduction to Composer 26"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/47077282029965-Self-Service-Report-Microservice
updated_at: 2026-08-26T07:10:51Z
---

# Self Service Report Microservice

# Self Service Report Microservice

The self service report microservice included in your environment, when [enabled](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701053868173-Server-Level-Variables#self-srv-rpt-ssa), supports a number of self service analytics capabilities. To support these features, keep some performance details in mind.

* [Self Service Reports](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/46982003580173-Manage-Self-Service-Reports): Users with appropriate permissions can create, edit, and send self service reports. If enabled, users can schedule and send reports to other users, or add them to a designated SFTP location.

  * Generate, export, and schedule delivery of PDF reports in a variety of page size and orientation formats.
  * Generate, export, and schedule delivery of reports in Excel (XLSX) format. These reports can include and support formatting and [conditional formatting](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701183616525-Configure-Conditional-Formatting).
* Scheduled Reports: Limit each scheduled report to fewer than 10 users, and plan time gaps between consecutive runs.
* Table visuals: Users with appropriate permissions can export table visuals in [Excel (XLSX) format](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/47469265422605-Export-Visual-Data-in-Excel-XLSX-Format). These visuals can include and support formatting and [conditional formatting](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701183616525-Configure-Conditional-Formatting).

## Environment Configuration

Before you [enable](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701053868173-Server-Level-Variables#self-srv-rpt-ssa) the self service report microservice in production, work with your infrastructure team to provision appropriate resources. The microservice requires [dedicated memory allocation](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701040681613-Configure-Memory-Settings) and can scale with additional pods to accommodate concurrent user load and report complexity.

The name of this service, when installing from bootstrap, is `report-service`.

## Performance Considerations

Report generation and export performance varies significantly based on report complexity and export format. The following guidelines are provided to help you plan your deployment and use.

Performance expectations noted here are based on internal testing we performed across three report service pods. Your results may vary based on [resource allocation](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701040681613-Configure-Memory-Settings) and concurrent user load.

In general, test your typical use report configurations thoroughly before deploying at scale.

### Report Type Performance

These guidelines are based on the report service running across three pods, with a memory request of 6 Gi and limit of 9 Gi, on one CPU core. Structure your environment to accommodate your reporting needs.

* Simple grouped reports are the best performers across both PDF and Excel (XLSX) formats.
* Simple reports perform well in PDF format; response times increase substantially with more complex datasets. XLSX is more resilient than PDF for simple reports.
* Keep your header and footer image sized between 200kb and 500kb for optimal rendering performance.
* The maximum generated report file size is 50 MB. Validate with test runs before you put large conditionally-formatted reports into production.
* Structured reports are the most resource-intensive type. Excel (XLSX) exports for structured reports average a few minutes and are not recommended for high-throughput or user-facing scenarios.

### Conditional Formatting

[Conditional formatting](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701183616525-Configure-Conditional-Formatting) increases report generation time significantly. A report with conditional formatting can take from twice as long to significantly longer than an equivalent report without it. Conditional formatting in complex reports exported to PDF format place a higher load on your environment, resulting in a percentage of error rates.

### File Size and Media

Keep in mind when designing your reports the limitations we built in to optimize performance, and guidelines users should follow for designing and formatting their reports.

* Generated report file size is capped at 50 MB.
* Keep header and footer images in the 200 KB–500 KB range.

### Landscape Orientation Considerations

* Reports generated in landscape orientation accommodate more columns per page. This requires additional write operations and memory allocation when compared to portrait, and can result in measurable performance impact.
* Due to the increased demands of landscape oriented reports, test landscape configurations in your environment before you deploy them to production.
* Landscape orientation combined with conditional formatting brings the highest load. Explore alternative configurations or expand the resources available to the self service report microservice.

## Scheduling and Distribution

When you enable scheduled reports for your users, keep these operational limits in mind.

* Scheduled reports should be limited to a maximum of 10 recipients per report. Leave adequate time gaps between consecutive scheduled runs.
* Stagger report schedules to avoid concentration of export operations during the same time window.
