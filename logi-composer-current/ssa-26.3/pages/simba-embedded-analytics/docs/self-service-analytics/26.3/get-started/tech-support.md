> ## Documentation Index
> Fetch the complete documentation index at: https://insightsoftware.mintlify.site/llms.txt
> Use this file to discover all available pages before exploring further.

# Contact Technical Support

To open a support ticket, navigate to: [https://central.insightsoftware.com](https://central.insightsoftware.com).

## Diagnose Problems

Self-Service Analytics provides a "one-click" diagnostics bundle for the Self-Service Analytics platform as part of the [Self-Service Analytics Service Monitor](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/monitor/service-monitor-overview).

The diagnostics bundle is primarily useful as an easy way to send insightsoftware the information needed to help you debug a problem. The bundle is a zip file containing all the current log files from all Self-Service Analytics's microservices. If distributed tracing is enabled and properly configured, the diagnostics bundle may also contain a JSON trace file with the trace ID you specify.

An example of the uncompressed contents of the diagnostic bundle might look like this:

<img src="https://mintcdn.com/insightsoftware/GTXU--ZlYc3DodOR/simba-embedded-analytics/docs/self-service-analytics/26.3/images/diagnostics/diagnostic-bundle.png?fit=max&auto=format&n=GTXU--ZlYc3DodOR&q=85&s=1f02b550e6d48f125122c781dbe9d900" alt="" width="1518" height="266" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/diagnostics/diagnostic-bundle.png" />

#### Prerequisites

Before you can download the diagnostics bundle, the following conditions must be met:

* Self-Service Analytics and its microservices must be version 3.5 or later.
* All microservices must have service discovery enabled.
* The Self-Service Analytics Service Monitor must be manually installed, configured and started. See [Install and Configure the Self-Service Analytics Service Monitor](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/monitor/service-monitor-overview#install-and-configure-the-self-service-analytics-service-monitor).

After the Service Monitor is installed, you can download the diagnostics bundle. See [Download the Diagnostics Bundle](#download-the-diagnostics-bundle).

<h2 id="download-the-diagnostics-bundle">
  Download the Diagnostics Bundle
</h2>

After the Service Monitor microservice is installed and running, you can use it to download a diagnostic bundle. If you want to include trace details in the diagnostics bundle, be sure to collect tracing information as described in [Distributed Tracing for Self-Service Analytics](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/monitor/distributed-tracing-using).

**Download a diagnostics bundle**

1. Using a web browser, navigate to the Service Monitor. Its default port is 8050. For example, if running locally, the Self-Service Analytics instance would be **[http://localhost:8080](http://localhost:8080)**, so the Service Monitor URL would be **[http://localhost:8050](http://localhost:8050)**. If your instance is at port 10.2.3.24, the Service Monitor URL would be **[http://10.2.3.24:8050](http://10.2.3.24:8050)**.

   A login screen will appear.

2. Log into the Service Monitor using the Service Monitor user name and password you defined when the Service Monitor was installed. See [Install and Configure the Self-Service Analytics Service Monitor](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/monitor/service-monitor-overview#install-and-configure-the-self-service-analytics-service-monitor).

3. Select **Downloads** on the main menu bar.

   <img src="https://mintcdn.com/insightsoftware/GTXU--ZlYc3DodOR/simba-embedded-analytics/docs/self-service-analytics/26.3/images/diagnostics/service-monitor-menu-download.png?fit=max&auto=format&n=GTXU--ZlYc3DodOR&q=85&s=c4337019773f3b816b91ec08045e4e6d" alt="" width="1899" height="68" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/diagnostics/service-monitor-menu-download.png" />

   A screen appears that you can use to download the diagnostics bundle:

   <img src="https://mintcdn.com/insightsoftware/GTXU--ZlYc3DodOR/simba-embedded-analytics/docs/self-service-analytics/26.3/images/diagnostics/diagnostic-download.png?fit=max&auto=format&n=GTXU--ZlYc3DodOR&q=85&s=66858489c65be702654b49f71718ee78" alt="" width="1824" height="306" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/diagnostics/diagnostic-download.png" />

4. Optionally enter a trace ID in the Trace ID box.

   If the tracing service is not configured, the Trace ID box will be disabled, with a relevant error message. When this happens, the diagnostic bundle contains only log files.

5. Select **Download Diagnostic Bundle**.

   If you did not specify a trace ID, the zip file that is produced contains only log files for all configured Self-Service Analytics microservices. If you specify a valid trace ID, the trace JSON file will also be included as part of the bundle.

   If you specify an invalid trace ID, a relevant error message displays.

   In some cases, a previously valid trace ID may be reported as not found. Traces are best retrieved as soon as an error is encountered.

   For more information about distributed tracing microservices, see [Distributed Tracing for Self-Service Analytics](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/monitor/distributed-tracing-using).
