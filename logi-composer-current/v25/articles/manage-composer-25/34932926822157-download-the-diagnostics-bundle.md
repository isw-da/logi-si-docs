---
title: "Download the Diagnostics Bundle"
id: 34932926822157
section: "Manage Composer 25"
product: "Logi Composer v25"
url: https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932926822157-Download-the-Diagnostics-Bundle
updated_at: 2026-05-26T22:09:38Z
---

# Download the Diagnostics Bundle

# Download the Diagnostics Bundle

After the Composer Service Monitor microservice is installed and running, you can use it to download a diagnostic bundle. If you want to include trace details in the diagnostics bundle, be sure to collect tracing information as described in [Distributed Tracing for Composer](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932919325197-Distributed-Tracing-for-Composer).

**Download a diagnostics bundle**

1. Using a web browser, navigate to the Service Monitor. Its default port is 8050. For example, if running locally, the Composer instance would be **http://localhost:8080**, so the Service Monitor URL would be **http://localhost:8050**. If your Composer instance is at port 10.2.3.24, the Service Monitor URL would be **http://10.2.3.24:8050**.

   A login screen will appear.
2. Log into the Service Monitor using the Service Monitor user name and password you defined when the Service Monitor was installed. See [Install and Configure the Composer Service Monitor](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933159112589-Install-and-Configure-the-Composer-Service-Monitor).
3. Select **Downloads** on the main menu bar.

   ![](https://logi-composer-v25.insightsoftware.com/hc/article_attachments/46167258762893)

   A screen appears that you can use to download the diagnostics bundle:

   ![](https://logi-composer-v25.insightsoftware.com/hc/article_attachments/46167252399757)
4. Optionally enter a trace ID in the Trace ID box.

   If the tracing service is not configured, the Trace ID box will be disabled, with a relevant error message. When this happens, the diagnostic bundle contains only log files.
5. Select **Download Diagnostic Bundle**.

   If you did not specify a trace ID, the zip file that is produced contains only log files for all configured Composer microservices. If you specify a valid trace ID, the trace JSON file will also be included as part of the bundle.

   If you specify an invalid trace ID, a relevant error message displays.

   In some cases, a previously valid trace ID may be reported as not found. Traces are best retrieved as soon as an error is encountered.

   For more information about distributed tracing microservices, see [Distributed Tracing for Composer](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932919325197-Distributed-Tracing-for-Composer).
