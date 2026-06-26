---
title: "Configure Composer Logs"
id: 43701053914637
section: "Manage Composer 26"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701053914637-Configure-Composer-Logs
updated_at: 2026-05-29T14:07:18Z
---

# Configure Composer Logs

# Configure Composer Logs

The microservices used in Composer write logs to their [corresponding service's log files](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701143687181-Composer-Log-Files-Reference) by default. You can configure Composer to write these logs to the console only, or to write logs both to the console and the service's log files. Structured logging is also supported. See [Structured Logging](#Structur).

Every [service config file](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43700991919117-Configuration-Property-Files) includes two properties you can use to define where the logs are written:

* `log.console.level` - edit to define the types of logs to write to the console
* `log.file.level` - edit to define the types of logs to write to the files

## Log Properties in Config Files

If you install using the bootstrap script, logging to files is enabled by default. You can reroute the logging to the console as needed to customize your installation.

**Note:** 
If the value of log properties is set to `OFF`, Composer access logs are not written. For all other cases (`ALL`, `ERROR`, `WARN`, `DEBUG`, and `INFO`) access logs are written to the selected destination: file, console or both.

* Bootstrap installation: The `*.jvm` file specifies `log.console.level=OFF` and `log.file.level=ALL` to support compatibility with earlier versions of Composer.

### Values for log.file.level and log.console.level

The following table lists possible values for `log.file.level` and `log.console.level`.

| Value | Description |
| --- | --- |
| `ALL` | All available log information. |
| `ERROR` | Application error messages that may affect processes. |
| `WARN` | Unexpected application issues that may not affect processes. |
| `INFO` | Expected activities. |
| `DEBUG` | Triggers capture of `WARN`, `INFO`, and `ERROR`information. |
| `OFF` | Disables logging. |

## Enable Logging for a Service to the Console

Enable logging to the console and append the desired corresponding value of the properties to the appropriate service configuration file.

* Use `log.console.level=ALL` to route duplicates of all logs to the console.
* Use `log.console.level=ERROR` to route only duplicates of errors to the console.
* Alternatively, use `log.console.level=ALL` and `log.console.level=ERROR` to have all logs in files and errors duplicated to the console.

Adjust the values to meet your needs, then restart the service after you've edited the config.

**Note:** Composer services have two config files, `*properties` and `*.jvm`. If you add log configuration properties to both files, the priority of `*.jvm` is higher than `*. properties`.

## Consul Logging

By default, Consul writes logs to the console, but you can duplicate logs to files if needed.

Configure Consul Logs to Duplicate to Files:

1. Edit the Consul config file, `consul.json`. For Linux installations, this is located in `/opt/zoomdata/conf/consul.json.`
2. Add the following properties:

   "log\_file": "/opt/zoomdata/logs/zoomdata-consul.log",
   "log\_rotate\_bytes": 104857600,
   "log\_rotate\_max\_files" : 5

   Adjust the path to your log file and other log configuration properties as needed for your environment. In Linux environments, the log is located in `/opt/zoomdata/logs`, and in `<install-path>/logs` for Windows environments. See [Consul documentation](https://www.consul.io/docs/v1.11.x/agent/options#log_file) for more information.

## Structured Logging

Composer supports structured logging. You can enable for installations done via bootstrap, and is enabled by default for Kubernetes environments.

### Components Support for Structured Logging

* zoomdata-web
* query engine
* admin server
* screenshot service
* data writer
* data connectors

### Enable Structured Logging

In bootstrap environments, set the property `log.structured.enabled` to `true` in the config files of your microservices to output logs in JSON format to the `STDOUT` destination. Logs output to the `FILE` logs destination are sent in plain text. See [Configuration Property Files](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43700991919117-Configuration-Property-Files).

In Kubernetes environments, structured logging is enabled by default. To disable, use one of the following approaches:

* Set the environment variable `LOG_STRUCTURED_ENABLED` to `false` to disable logging for specific services.
* Set `structuredLogsEnabled` in `values.yaml` to `false` to disable logging for all services.
* For Consul, change the `log_json` value to `false` in the `consul.server.extraConfig` section of `values.yaml`.
