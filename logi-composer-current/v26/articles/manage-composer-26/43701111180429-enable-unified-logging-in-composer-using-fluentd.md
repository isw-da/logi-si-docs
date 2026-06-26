---
title: "Enable Unified Logging in Composer  Using Fluentd"
id: 43701111180429
section: "Manage Composer 26"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701111180429-Enable-Unified-Logging-in-Composer-Using-Fluentd
updated_at: 2026-05-29T14:08:56Z
---

# Enable Unified Logging in Composer  Using Fluentd

# Enable Unified Logging in Composer Using Fluentd

Identify the Composer microservices for which you want activity logged to Fluentd. A complete list of the Composer microservices is given in [Composer  Microservice Name Reference](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701144824589-Composer-Microservice-Name-Reference), but not all microservices support unified logging. You can enable unified logging for these microservices:

* Web microservices (`zoomdata.properties`)
* Query engine (`query-engine.properties`)
* Data source connectors (see [Connector Properties and Property Files](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43700992050061-Connector-Properties-and-Property-Files) for a list of property files)
* Data Writer framework (`data-writer-postgresql.properties`)

**Enable unified logging using Fluentd for a** Composer **microservice**

1. On your Composer server, edit the `.properties` file for the microservice. For example, `etc/zoomdata/query-engine.properties`.
2. Define the following parameters in the `.properties` file:

   | Property Syntax | Description |
   | --- | --- |
   | `logging.unified.level = <log-level>` | Specify one of the following log levels for `<log-level>`: ERROR, WARN, INFO, DEBUG, TRACE, or OFF. If set to OFF, Fluentd unified logging is disabled. |
   | `logging.unified.tag = <service-tag>` | Specify the unique tag for the Composer microservice, used in grouping logs. This tag must be unique throughout Composer.  Supply the Composer microservice name for `<service-tag>`. For example, `logging.unified.tag = query-engine`. This is important because the tag identifies which microservice the log message applies to.  Valid values are `query-engine`, `zoomdata-server`, `data-writer-postgresql`, and `edc-<connector-name>` (where `<connector-name>` is one of the names listed in [Connector Properties and Property Files](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43700992050061-Connector-Properties-and-Property-Files)). |
   | `logging.unified.label = <service-label>` | Specify a more verbose label for the Composer microservice. |
   | `logging.unified.host = <yourFluentdServerIPaddress>` | Specify the IP address of the Fluentd logging server. |
   | `logging.unified.port = <yourFluentdServerPort>` | Specify the port of the Fluentd logging server. |
3. Save your changes and exit the `.properties` file.
4. Restart the Composer server.

On the Fluentd server, you can then direct your logs to a data source of your choice. For information and steps, see Fluentd's documentation on [Output](https://docs.fluentd.org/output).
