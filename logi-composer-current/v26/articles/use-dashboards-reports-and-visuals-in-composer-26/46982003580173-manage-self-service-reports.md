---
title: "Manage Self Service Reports"
id: 46982003580173
section: "Use Dashboards, Reports  and Visuals in Composer 26"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/46982003580173-Manage-Self-Service-Reports
updated_at: 2026-08-26T07:08:58Z
---

# Manage Self Service Reports

# Manage Self Service Reports

**Note:** To use self service reports, you will need to enable it in your environment. See [Server-Level Variables](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701053868173-Server-Level-Variables#scheduled-report).

After you have successfully connected to your data stores and configured your data sources, you can immediately start using your data to generate self service reports.
Quickly build, edit, and filter reports. Group your data and apply conditional formatting to highlight specific information. Add header and footer information to provide context to the information you're presenting in each report.

A self service report is an easy to create from a data source. Create as many self service reports as you need to share with users add to an SFTP location ([if enabled in your environment](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701053868173-Server-Level-Variables#scheduled-report)), distribute as a PDF, or [share as a scheduled repor](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701093791245-Schedule-a-Self-Service-Report-or-Dashboard-Report)t.

## Performance, Memory Management, and Scheduling

Self Service Reports are designed to provide flexible and efficient report generation while maintaining optimal system performance. Report complexity directly impacts memory consumption: advanced features and extensive data transformations require additional computational resources.

To ensure the best reporting experience, we recommend careful data selection, mindful use of complex conditional formatting, and awareness of potential memory constraints during large-scale report generation. Layout, paper size and orientation for export, as well as conditional formatting and grouping can affect performance. More complex reports may require additional processing time and resources, so design the reports accordingly. For more information, see [Report Type Performance](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/47077282029965-Self-Service-Report-Microservice#Report).

To ensure optimal performance and reliability when scheduling Self-Service Reports, keep in mind that this system is designed to handle multiple concurrent schedules efficiently. However, we recommend you space out schedules to avoid overlaps and potential conflicts. For more information, see [Report Type Performance](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/47077282029965-Self-Service-Report-Microservice#Report).

Additionally, there is a limit on the size of emails that can be sent, determined by your SMTP provider that includes both the message body and any attachments. Exceeding this may result in delivery failures due to those restrictions.

Before you begin, make sure that the data sources you want to use have been added and you have privileges to access the sources and create reports.

Before you begin, make sure that the data sources you want to use have been added and you have privileges to access the sources and create reports.

For more information, see:

* [Self Service Report Microservice](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/47077282029965-Self-Service-Report-Microservice)
* [Use the Self Service Reports Library](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/46982003574285-Use-the-Self-Service-Reports-Library)
* [Create Self Service Reports](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/46982018753165-Create-Self-Service-Reports)
* [Format Self Service Reports](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/46981992392077-Format-Self-Service-Reports)
* [Edit and Delete a Self Service Report](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/46982032879373-Edit-and-Delete-a-Self-Service-Report)
* [Schedule a Self Service Report or Dashboard Report](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701093791245-Schedule-a-Self-Service-Report-or-Dashboard-Report)
* [Scheduled Self Service Reports and Dashboard Report Prerequisites](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701047328013-Scheduled-Self-Service-Reports-and-Dashboard-Report-Prerequisites)
* [Use the Report Icon Bars](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/46981992411661-Use-the-Report-Icon-Bars)

**Note:** 
You can bypass the visualization cache and query the underlying data source by selecting the Refresh icon in the [reports icon bar](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/46981992411661-Use-the-Report-Icon-Bars).
