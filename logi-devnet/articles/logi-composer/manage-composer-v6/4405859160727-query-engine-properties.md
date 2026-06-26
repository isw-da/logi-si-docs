---
title: "Query Engine Properties"
id: 4405859160727
section: "Manage Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405859160727-Query-Engine-Properties
updated_at: 2021-09-21T01:26:57Z
---

# Query Engine Properties

# Query Engine Properties

Most of the query engine components can be edited in the `query-engine.properties` file. You can manage the query engine using the following properties.
For information on editing configuration files, see [*Edit a Composer Configuration File*](https://devnet.logianalytics.com/hc/en-us/articles/4405850887703-Edit-a-Composer-Configuration-File).

| Property | Default Value | Description |
| --- | --- | --- |
| Service Discovery | | |
| discovery.enabled | true | Whether Consul is used for microservice discovery |
| discovery.registry.host | localhost | Service Discovery microservice host |
| discovery.registry.port | 8500 | Service Discovery microservice port |
| Service Logging | | |
| logging.level.com.zoomdata | INFO | Sets the log level for log messages in the query engine microservice log file. The following options are available for this property: TRACE, DEBUG, INFO, WARN, and ERROR. |
| logging.unified.host | 127.0.0.1 | Sets the host IP address for [Fluentd server](https://www.fluentd.org/) message logging. For more information, see [*Set Up Unified Logging Using Fluentd*](https://devnet.logianalytics.com/hc/en-us/articles/4405859397655-Set-Up-Unified-Logging-Using-Fluentd). |
| logging.unified.label | Query Engine | Fluentd |
| logging.unified.level | OFF | Sets the log level for messages logged to the [Fluentd server](https://www.fluentd.org/). The following options are available for this property: TRACE, DEBUG, INFO, WARN, ERROR, and OFF. If set to OFF, Fluentd unified logging is disabled. For more information, see [*Set Up Unified Logging Using Fluentd*](https://devnet.logianalytics.com/hc/en-us/articles/4405859397655-Set-Up-Unified-Logging-Using-Fluentd). |
| logging.unified.port | 24224 | Sets the port for [Fluentd server](https://www.fluentd.org/) message logging. For more information, see [*Set Up Unified Logging Using Fluentd*](https://devnet.logianalytics.com/hc/en-us/articles/4405859397655-Set-Up-Unified-Logging-Using-Fluentd). |
| logging.unified.tag | query-engine | Sets the microservice tag name for messages logged to the [Fluentd server](https://www.fluentd.org/). This is important because the tag identifies the microservice to which the log messages apply. Valid values are `query-engine`, `job-scheduler`, `zoomdata-server`, `stream-writer`, `upload-service`, and `edc-<connector-name>` (where `<connector-name>` is one of the names listed in [*Connector Properties and Property Files*](https://devnet.logianalytics.com/hc/en-us/articles/4405850892439-Connector-Properties-and-Property-Files)). For more information, see [*Set Up Unified Logging Using Fluentd*](https://devnet.logianalytics.com/hc/en-us/articles/4405859397655-Set-Up-Unified-Logging-Using-Fluentd). |
| qe.access.log.file.size | 10 | Access log file size (in MB) |
| qe.error.log.file.size | 5 | Error log file size (in MB) |
| qe.log.file.size | 20 | General log file size (in MB) |
| qe.websocket.log.file.size | 10 | Websocket log file size (in MB) |
| syslog.host | 127.0.0.1 | Sets the host IP address for [Syslog server](https://www.networkmanagementsoftware.com/what-is-syslog/) message logging. |
| syslog.log.level | OFF | Sets the syslog log level for messages logged to the [Syslog server](https://www.networkmanagementsoftware.com/what-is-syslog/). The following options are available for this property: TRACE, DEBUG, INFO, WARN, ERROR. and OFF. |
| syslog. port | 1514 | Sets the port for [Syslog server](https://www.networkmanagementsoftware.com/what-is-syslog/) message logging. |
| trace.requests | false | Enables detailed tracing of HTTP request |
| tracing.sampler.probability | 1 | The distributed tracing request rate percentage. Valid values are between 0 to 1.0, where 0 disables tracing and 1.0 indicates tracing 100% of requests. |
| General Microservice Configuration for Jetty Web Server | | |
| jetty.threadPool.maxThreads | 200 | Number of threads to serve the HTTP & WebSocket clients |
| qe.server.ws.idle.timeout | 86400000 | Idle time (in milliseconds) that allows the WebSocket to be still valid |
| qe.server.ws.input.buffer.size | 16384 | Buffer size (in bytes) for the WebSocket message |
| qe.server.ws.max.message.size | 1048576 | Max size (in bytes) of a message that could be sent over the query engine WebSocket |
| server.port | 5580 | REST/WebSocket microservice port |
| server.ssl.enabled | false | Defines whether the REST/WS API should use SSL |
| server.ssl.key-store |  | Path to the file with the keystore |
| server.ssl.key-store.password |  | Password for the keystore |
| Graceful Shutdown |  |  |
| application.graceful.shutdown.enabled | true | Indicates whether or not graceful shutdown processing should occur. Valid values are `true` (perform graceful shutdown processing) or `false` (do not perform graceful shutdown processing). |
| application.graceful.shutdown.event-propagation-timeout-sec | 5 | Specifies how long (in seconds) a query engine instance will wait to allow clients to receive the information that it is out of service. |
| application.graceful.shutdown.force-kill-timeout-sec | 30 | The maximum number of seconds that a query engine instance will wait for the number of its active tasks to reach zero. When this time has elapsed, all remaining active WebSockets serving in-flight queries are closed and then the query engine instance will stop. |
| Topology Configuration |  |  |
| calculations.detect.array.fields | true | Enables and disables the query engine validation of multivalue fields in a derived field. By disabling (set the value to `false`) this functionality, any custom metrics that you may have created in earlier versions of Composer that are aggregations of multivalue fields will produce valid values. |
| calculations.rle.now.function | false | Enables and disables `NOW(0` functionality in derived fields. `NOW()` can be used to obtain the current date and time for a derive field. By default, this functionality is disabled (`false`). |
| qe.max.allowed.time.groups | 10000 | The maximum amount of time in which groups can be generated by the **Include Blanks** function. For information on even time intervals, see [*Even Time Intervals*](https://devnet.logianalytics.com/hc/en-us/articles/4405850992919-Even-Time-Intervals). |
| qe.max.rows.during.execution | 5000000 | The maximum number of rows that can be processed during a single query. The value specified must be at least slightly greater than the value for the `qe.zengine.edc.rows.limit` property. If you increase the value of `qe.zengine.edc.rows.limit`, consider increasing the value of this property.  When a query exceeds the limit set by this property, a `Resource limit is reached during query execution` message appears. |
| qe.zengine.edc.rows.limit | 1000000 | The maximum number of records that can be fused from a single data source. |
| zoomdata.validation.histogram.max.size | 1000 | Histogram max bucket count |
| Query Engine Metadata Store Configuration | | |
| spring.qe.datasource.jdbcUrl | `jdbc:postgresql://<IP_address> :<port>/zoomdata-qe` | The URL of the `zoomdata-qe` database in the PostgreSQL metadata store. For example: `spring.qe.datasource.jdbcUrl=jdbc:postgresql://localhost:5432/zoomdata-qe` |
| spring.qe.datasource.username | --- | The user name for the `zoomdata-qe` database in the PostgreSQL metadata store. |
| spring.qe.datasource.password | --- | The password associated with the user name for the `zoomdata-qe` database in the PostgreSQL metadata store. |
