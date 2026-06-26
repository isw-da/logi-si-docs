---
title: "Diagnose Problems"
id: 4405859335575
section: "Manage Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405859335575-Diagnose-Problems
updated_at: 2021-09-21T01:28:24Z
---

# Diagnose Problems

# Diagnose Problems

Composer provides a "one-click" diagnostics bundle for the Composer platform as part of the [Composer Service Monitor](https://devnet.logianalytics.com/hc/en-us/articles/4405859475735-Composer-Service-Monitor).

The diagnostics bundle is primarily useful as an easy way to send Composer the information needed to help you debug a problem. The bundle is a zip file containing all the current log files from all Composer's microservices. If distributed tracing is enabled and properly configured, the diagnostics bundle may also contain a JSON trace file with the trace ID you specify.

An example of the uncompressed contents of the diagnostic bundle might look like this:

![](https://devnet.logianalytics.com/hc/article_attachments/4406743806231/diagnostic-bundle_502x87.png)

### Prerequisites

Before you can download the diagnostics bundle, the following conditions must be met:

* Composer and its microservices must be version 3.5 or later.
* All microservices must have service discovery enabled.
* The Composer Service Monitor must be manually installed, configured and started. See [*Install and Configure the Composer Service Monitor*](https://devnet.logianalytics.com/hc/en-us/articles/4405859474711-Install-and-Configure-the-Composer-Service-Monitor).

If you want the diagnostics bundle to include tracing information when a trace ID is specified, the following additional conditions must be met:

* The Composer tracing microservice must be is manually installed, configured and started. See [*Install the Composer Tracing Microservice*](https://devnet.logianalytics.com/hc/en-us/articles/4405851043991-Install-the-Composer-Tracing-Microservice).
* The tracing microservice must have service discovery enabled.

After the Service Monitor is installed, you can download the diagnostics bundle. See [*Download the Diagnostics Bundle*](https://devnet.logianalytics.com/hc/en-us/articles/4405851038615-Download-the-Diagnostics-Bundle).
