---
title: "Composer Log Unification"
id: 34933142118541
section: "Composer 25 Reference Information"
product: "Logi Composer v25"
url: https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933142118541-Composer-Log-Unification
updated_at: 2026-05-26T22:08:00Z
---

# Composer Log Unification

# Composer Log Unification

Composer has unified logback configuration throughout Composer microservices. You can configure Composer to write these logs to the console in addition to or instead of the service files. See [Configure Composer Logs](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932701466765-Configure-Composer-Logs) and [Composer Log Files Reference](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933097277069-Composer-Log-Files-Reference).

## Log Configuration Properties

Adjust these properties to set up logging for your environment.

| Name | Default Value | Description |
| --- | --- | --- |
| install.dir | `.` | Use to evaluate the value of `logs.dir`. |
| logs.dir | `${install.dir}/logs` | The location of the log file and error log file. |
| spring.application.name | `zoomdata-service` | Use to evaluate the default values of `logs.file-name`. |
| logs.file-name | `${spring.application.name}` | Name of log file. Log file suffix: `.log`. Error log file suffix: `error.log`. |
| log.console.level | `ALL` | The maximum level of logs to print to `stdout`. See [Log File Values](#LogFileVal). |
| log.file.level | `ALL` | The maximum level of logs to print to the log file. See [Log File Values](#LogFileVal). |
| log.password.regex | `(?i)PASSWORD=[a-zA-Z0-9!@#\$%\^\*\&amp;]*` | Regular expression used to detect passwords in log output. Replaces with `PASSWORD=****`. |
| log.url-password.regex | `(?&lt;=://)[^:]+:[^@]+@` | Regular expression used to detect and remove credential in URLs and remove the credentials. |
| log.sanitization.enabled | `true` | The default, `true`, is specified in `logging.properties`.  Toggles sanitization of log message via `org.apache.commons.text.StringEscapeUtils.escapeJava`. |
| log.file.size | `20` | The maximum size of the log file in MB. When that size is reached, the file is renamed using this pattern: `{log.file-name}.log.%i`. |
| log.file.count | `5` | Maximum number of log files. |
| log.error.file.size | `5` | The maximum size of the error log file in MB. When that size is reached, the file is renamed using this pattern: `{log.file-name}-error.log.%i`. |
| log.error.file.count | `5` | Maximum number of error log files. |
| syslog.log.level | `OFF` | Syslog log level. See [Log File Values](#LogFileVal). |
| syslog.host | `127.0.0.1` | Syslog host name. |
| syslog.port | `514` | Syslog port number. |
| syslog.suffix | `${spring.application.name}` | Syslog suffix. Used to distinguish applications. |
| trace.requests | `false` | Adds the MDC value of `requestId` to log output. Propagate value using `X-REQUEST-ID` http header. |

### Log File Values

| Value | Description |
| --- | --- |
| `OFF` | Disables logging. |
| `FATAL` | Only error messages (the same as `ERROR` for logback). |
| `ERROR` | Application error messages that may affect processes. |
| `WARN` | Unexpected application issues that may not affect processes. |
| `INFO` | Expected activities. |
| `DEBUG` | Triggers capture of `WARN`, `INFO`, and `ERROR`information. |
| `TRACE` | Capture of `DEBUG` level of information, and low importance informational messages. |
| `ALL` | All available log information (the same as `TRACE` for logback). |

## Other Configuration Properties

Both Zoomdata-Web and Query Engine have properties you can adjust to suit your needs as well.

### Zoomdata-Web

| Name | Default Value | Description |
| --- | --- | --- |
| activity.log.file.count | `1` | Maximum number of activity log files . |
| activity.log.file.size | `10` | The maximum size of the activity log file in MB. When that size is reached, the file is renamed using this pattern: `{log.file-name}-activty.log.%i`. |
| activity.logs.dir | n/a | The location of the activity log file. If no location is specified, `{logs.dir}` is used. |
| websocket.log.file.size | `10` | The maximum size of the websocket log file in MB. When that size is reached, the file is renamed using this pattern: `{log.file-name}-websocket.log.%i`. |
| websocket.log.file.count | `5` | Maximum number of websocket log files. |
| websocket.log.level | `OFF` | Overall maximum log level of websocket logs. |
| websocket.file.level | `OFF` | Maximum log level of websocket logs in the file. |
| websocket.console.level | `OFF` | Maximum log level of websocket logs in the console. |
| access.log.file.size | `10` | The maximum size of the access log file in MB. When that size is reached, the file is renamed using this pattern: `{log.file-name}-access.log.%i`. |
| license.log.file.size | `10` | The maximum size of the license log file in MB. When that size is reached, the file is renamed using this pattern: `{log.file-name}-sessions.log.%i`. |

### Query Engine

| Name | Default Value | Description |
| --- | --- | --- |
| websocket.log.level | `OFF` | Overall maximum log level of websocket logs. |
| websocket.file.level | `OFF` | Maximum log level of websocket logs in the file. |
| websocket.console.level | `OFF` | Maximum log level of websocket logs in the console. |
| websocket.log.file.size | `10` | The maximum size of the websocket log file in MB. When that size is reached, the file is renamed using this pattern: `{log.file-name}-websocket.log.%i`. |
| websocket.log.file.count | `1` | Maximum number of websocket log files. |
| access.log.file.size | `10` | The maximum size of the access log file in MB. When that size is reached, the file is renamed using this pattern: `{log.file-name}-access.log.%i`. |
| slow-request.file.level | `INFO` | Maximum log level of slow request logs in the file. |
| slow-request.console.level | `OFF` | Maximum log level of slow request logs in the console. |
| slow-request.log.file.size | `10` | The maximum size of the slow requests log file in MB. When that size is reached, the file is renamed using this pattern: `{log.file-name}-slow-requests.log.%i` . |
| slow-request.log.file.count | `5` | Maximum number of slow requests log files. |
| slow-expression-parsing.file.level | `INFO` | Maximum log level of slow expression parsing logs in the file. |
| slow-expression-parsing.console.level | `OFF` | Maximum log level of slow expression parsing logs in the console. |
| slow-expression-parsing.log.file.size | `10` | The maximum size of the slow expression parsing log file in MB. When that size is reached, the file is renamed using this pattern: `{log.file-name}-slow-expression-parsing.log.%i` |
| slow-expression-parsing.log.file.count | `5` | Maximum number of slow expression parsing log files. |

## Set Logging Levels

Every logging level can be changed using a [standard spring boot approach](https://docs.spring.io/spring-boot/docs/current/reference/htmlsingle/#features.logging.log-levels). Specify the corresponding property, as shown below.

**Note:** 
The logback.zoomdata property, previously used to control the log level of some loggers, has been removed. Use a standard spring boot approach to specify appropriate properties.

# Enable debug logs for 'com.zoomdata' logger and it's children
logging.level.com.zoomdata=DEBUG
# Set log level to error for root logger (parent of all loggers) and it's children
logging.level.root=ERROR

### Default Log File Names

Composer's microservices each have a series of default log files where you can find captured events.

| Name | Microservice | Description |
| --- | --- | --- |
| `zoomdata.log` | Zoomdata-web | Common logs. |
| `zoomdata-errors.log` | Zoomdata-web | Only server error logs. |
| `zoomdata-access.log` | Zoomdata-web | Access logs. |
| `zoomdata-activity.log` | Zoomdata-web | Activity audit logs. |
| `zoomdata-websocket.log` | Zoomdata-web | Websocket logs. |
| `zoomdata-sessions.log` | Zoomdata-web | Licensing related logs. |
| `query-engine.log` | Query Engine | Common logs. |
| `query-engine-errors.log` | Query Engine | Only server error logs. |
| `query-engine-access.log` | Query Engine | Access logs. |
| `query-engine-websocket.log` | Query Engine | Websocket logs. |
| `query-engine-slow-expression-parsing.log` | Query Engine |  |
| `query-engine-slow-requests.log` | Query Engine |  |
| `admin-server.log` | Admin Service | Common logs. |
| `admin-server-errors.log` | Admin Service | Only server error logs. |
| `config-server.log` | Config Server | Common logs. |
| `config-server-errors.log` | Config Server | Only server error logs. |
| `stream-writer-postgresql.log` | Data-Writer | Postgresql: Common logs. |
| `stream-writer-postgresql-errors.log` | Data-Writer | Postgresql: Only server error logs. |
| `stream-writer-mssql.log` | Data-Writer | MSSQL: Common logs. |
| `stream-writer-mssql-errors.log` | Data-Writer | MSSQL: Only server error logs. |
| `screenshot-service.log` | Screenshot Service | Common logs. |
| `screenshot-service-errors.log` | Screenshot Service | Only server error logs. |
| `${connector.name}.log` | EDC | Common logs. |
| `${connector.name}-errors.log` | EDC | Only server error logs. |
