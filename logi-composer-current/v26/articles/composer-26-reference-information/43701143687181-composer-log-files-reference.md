---
title: "Composer Log Files Reference"
id: 43701143687181
section: "Composer 26 Reference Information"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701143687181-Composer-Log-Files-Reference
updated_at: 2026-05-29T14:09:15Z
---

# Composer Log Files Reference

# Composer Log Files Reference

Composer uses the following log files. You can configure Composer to write these logs to the console in addition to or instead of the service files. See [Configure Composer Logs](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701053914637-Configure-Composer-Logs).

| Log File | Contains |
| --- | --- |
| `edc-<connector>.log` | Specific data connector service log file. |
| `edc-<connector>-errors.log` | Specific data connector service log file, filtered to ERROR level log messages. |
| `query-engine.log` | Operational information about the query engine microservice. |
| `query-engine-access.log` | Standard web server access log for the query engine microservice. |
| `query-engine-activity.log` | Audit-related information for the query engine microservice. |
| `Security_service.log` | Information related to [enabling or disabling a security service](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701209060237-Enable-or-Disable-a-Security-Service) in the supervisor UI. |
| `stream-writer.log` | Upload service information. |
| `zoomdata.log` | A wide variety of errors and information. This is the best place to start with troubleshooting. |
| `zoomdata-access.log` | Standard web server access log for the Composer microservice. |
| `zoomdata-consul-{unixTimestamp}.log` | Information on service discovery and registration. |
| `zoomdata-errors.log` | Composer log information with a log level of `ERROR`. |
| `zoomdata-installer.<date/time>.log` | Information related to the installation. Installation errors typically appear here. |
| `zoomdata-upgrade.log` | Information related to upgrades. Errors with an upgrade will typically show up here. |
| `zoomdata-websocket.log` | Information sent and received over a WebSocket from the browser. |
