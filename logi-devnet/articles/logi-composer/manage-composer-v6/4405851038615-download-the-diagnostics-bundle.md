---
title: "Download the Diagnostics Bundle"
id: 4405851038615
section: "Manage Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405851038615-Download-the-Diagnostics-Bundle
updated_at: 2021-09-21T01:28:24Z
---

# Download the Diagnostics Bundle

# Download the Diagnostics Bundle

After the Composer Service Monitor microservice is installed and running, you can use it to download a diagnostic bundle. If you want to include trace details in the diagnostics bundle, be sure to collect tracing information as described in [*Trace Composer Problems*](https://devnet.logianalytics.com/hc/en-us/articles/4405859338263-Trace-Composer-Problems).

To download a diagnostics bundle:

1. Using a web browser, navigate to the Service Monitor. Its default port is 8050. For example, if running locally, the Composer instance would be **http://localhost:8080**, so the Service Monitor URL would be **http://localhost:8050**. If your Composer instance is at port 10.2.3.24, the Service Monitor URL would be **http://10.2.3.24:8050**.

   A login screen will appear.
2. Log into the Service Monitor using the Service Monitor user name and password you defined when the Service Monitor was installed. See [*Install and Configure the Composer Service Monitor*](https://devnet.logianalytics.com/hc/en-us/articles/4405859474711-Install-and-Configure-the-Composer-Service-Monitor).
3. Select **Downloads** on the main menu bar.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4406743806487/service-monitor-menu-download_768x28.png)

   A screen appears that you can use to download the diagnostics bundle:

   ![](https://devnet.logianalytics.com/hc/article_attachments/4406743806743/diagnostic-download_576x97.png)
4. Optionally enter a trace ID in the Trace ID box.

   If the Composer tracing server is not running, the Trace ID box will be disabled, with a relevant error message. When this happens, the diagnostic bundle contains only log files.
5. Select **Download Diagnostic Bundle**.

   If you did not specify a trace ID, the zip file that is produced contains only log files for all configured Composer microservices. If you specify a valid trace ID (from a log statement or found using the Composer tracing microservice), the trace JSON file will also be included as part of the bundle. (See [*View a Trace*](https://devnet.logianalytics.com/hc/en-us/articles/4405851042199-View-a-Trace) for tips on identifying a trace ID.)

   If you specify an invalid trace ID, a relevant error message displays.

   In some cases, a previously valid trace ID may be reported as not found. The Composer tracing microservice does not keep traces forever, and in some cases retention may be as low as a few hours (depending on volume and configuration). Traces are best retrieved as soon as an error is encountered. See [*Persist Traces*](https://devnet.logianalytics.com/hc/en-us/articles/4405851040407-Persist-Traces).

   ![](https://devnet.logianalytics.com/hc/article_attachments/4406747382295/noteicon.jpg) Attempting to retrieve an older trace and receiving "not found" is an expected behavior unless the same trace ID can be retrieved using the Composer tracing microservice UI.

   For more information about the Composer tracing microservices, see [*Trace Composer Problems*](https://devnet.logianalytics.com/hc/en-us/articles/4405859338263-Trace-Composer-Problems).
