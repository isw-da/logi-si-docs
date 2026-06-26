---
title: "Diagnose Problems"
id: 43701117349389
section: "Manage Composer 26"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701117349389-Diagnose-Problems
updated_at: 2026-05-29T14:10:55Z
---

# Diagnose Problems

# Diagnose Problems

Composer provides a "one-click" diagnostics bundle for the Composer platform as part of the [Composer Service Monitor](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701149014925-Composer-Service-Monitor).

The diagnostics bundle is primarily useful as an easy way to send Composer the information needed to help you debug a problem. The bundle is a zip file containing all the current log files from all Composer's microservices. If distributed tracing is enabled and properly configured, the diagnostics bundle may also contain a JSON trace file with the trace ID you specify.

An example of the uncompressed contents of the diagnostic bundle might look like this:

![](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46242554924685)

### Prerequisites

Before you can download the diagnostics bundle, the following conditions must be met:

* Composer and its microservices must be version 3.5 or later.
* All microservices must have service discovery enabled.
* The Composer Service Monitor must be manually installed, configured and started. See [Install and Configure the Composer Service Monitor](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701162883597-Install-and-Configure-the-Composer-Service-Monitor).

After the Service Monitor is installed, you can download the diagnostics bundle. See [Download the Diagnostics Bundle](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701069730317-Download-the-Diagnostics-Bundle).
