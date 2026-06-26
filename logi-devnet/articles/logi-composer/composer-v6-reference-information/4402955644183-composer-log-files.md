---
title: "Composer Log Files"
id: 4402955644183
section: "Composer v6 Reference Information"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4402955644183-Composer-Log-Files
updated_at: 2021-08-07T17:31:38Z
---

# Composer Log Files

# Composer Log Files

Composer uses the following log files.

| Log File | Contains |
| --- | --- |
| `edc-<connector>.log` | Specific data connector service log file. |
| `edc-<connector>-errors.log` | Specific data connector service log file, filtered to ERROR level log messages. |
| `query-engine.log` | Operational information about the query engine microservice. |
| `query-engine-access.log` | Standard web server access log for the query engine microservice. |
| `query-engine-activity.log` | Audit-related information for the query engine microservice. |
| `Remember_me.log` | Information related to the "Keep me logged in" functionality available on the [UI login screen](https://devnet.logianalytics.com/hc/en-us/articles/4402955424535-Log-Into-the-Composer-UI). |
| `Security_service.log` | Information related to [enabling or disabling a security service](https://devnet.logianalytics.com/hc/en-us/articles/4402955670423-Enable-or-Disable-a-Security-Service) in the supervisor UI. |
| `stream-writer.log` | Upload service information. |
| `zoomdata.log` | A wide variety of errors and information. This is the best place to start with troubleshooting. |
| `zoomdata-access.log` | Standard web server access log for the Composer microservice. |
| `zoomdata-activity.log` | Audit-related information for the Composer microservice. |
| `zoomdata-consul.out.log` | Information on service discovery and registration. |
| `zoomdata-errors.log` | Composer log information with a log level of `ERROR`. |
| `zoomdata-installer.<date/time>.log` | Information related to the installation. Installation errors typically appear here. |
| `zoomdata-upgrade.log` | Information related to upgrades. Errors with an upgrade will typically show up here. |
| `zoomdata-websocket.log` | Information sent and received over a WebSocket from the browser. |
