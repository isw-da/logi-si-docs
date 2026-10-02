> ## Documentation Index
> Fetch the complete documentation index at: https://insightsoftware.mintlify.site/llms.txt
> Use this file to discover all available pages before exploring further.

# Set Up Unified Logging Using Fluentd

In Self-Service Analytics, you can use Fluentd as a logging layer to which you can direct the logs for various components of Self-Service Analytics. This allows you to customize the log output to meet the needs of your environment.

Self-Service Analytics leverages Fluentd’s unified logging layer to collect logs via a central API. Fluentd can be configured to aggregate logs to various data sources or outputs. For example, if you are directing all log files from your `zoomdata-websocket.log` and `zoomdata-errors.log` to a Fluentd server, you can add one of Fluentd’s plug-ins to write the log files to Elasticsearch to analyze web client errors for your environment.

Unified logging does not replace Self-Service Analytics's default logging architecture. It only augments that experience with an option for those wanting additional logging control.

By default, unified logging is disabled and needs to be enabled for each microservice you want captured in Fluentd.

If written to a data store compatible with Self-Service Analytics’s connectors, Self-Service Analytics can then be used to analyze and visualize your logs. The selected data store must be supported by Self-Service Analytics's connectors if you plan to view the log files in Self-Service Analytics dashboards. A list of supported data stores is provided in [Data Connector Reference](/simba-embedded-analytics/docs/self-service-analytics/26.3/reference/data-connector-reference). The selected data store should be available and configured in conjunction with Fluentd to receive logs.

At a high level, the steps to set up Fluentd are as follows:

1. Set up a database to store the Fluentd log files. Typically, customers store log files in a log capture service such as Elasticsearch or in a database server such as PostgreSQL.
2. Configure Fluentd logging for your Self-Service Analytics installation. See [Configure Unified Logging Using Fluentd](#configure-unified-logging-using-fluentd). This includes configuring the Fluentd `td-agent.conf` file to identify the Self-Service Analytics [microservice](/simba-embedded-analytics/docs/self-service-analytics/26.3/get-started/arch-microservice#self-service-analytics-microservice-name-reference) log data you want logged.
3. Enable unified logging and configure the host and port information for your Fluentd server for each [microservice](/simba-embedded-analytics/docs/self-service-analytics/26.3/get-started/arch-microservice#self-service-analytics-microservice-name-reference) log file from which you are extracting data for Fluentd logging. See [Enable Unified Logging in Self-Service Analytics Using Fluentd](#enable-unified-logging-in-self-service-analytics-using-fluentd).

<h2 id="enable-unified-logging-in-self-service-analytics-using-fluentd">
  Enable Unified Logging in Self-Service Analytics Using Fluentd
</h2>

Identify the Self-Service Analytics microservices for which you want activity logged to Fluentd. A complete list of the Self-Service Analytics microservices is given in [Self-Service Analytics Microservice Name Reference](/simba-embedded-analytics/docs/self-service-analytics/26.3/get-started/arch-microservice#self-service-analytics-microservice-name-reference), but not all microservices support unified logging. You can enable unified logging for these microservices:

* Web microservices (`zoomdata.properties`)
* Query engine (`query-engine.properties`)
* Data source connectors (see [Connector Properties and Property Files](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/configure/properties-reference#connector-properties-and-property-files) for a list of property files)
* Data Writer framework (`data-writer-postgresql.properties`)

**Enable unified logging using Fluentd for a Self-Service Analytics** **microservice**

1. On your Self-Service Analytics server, edit the `.properties` file for the microservice. For example, `etc/zoomdata/query-engine.properties`.

2. Define the following parameters in the `.properties` file:

   <table>
     <thead>
       <tr>
         <th>Property Syntax</th>
         <th>Description</th>
       </tr>
     </thead>

     <tbody>
       <tr>
         <td>`logging.unified.level = <log-level>`</td>
         <td>Specify one of the following log levels for `<log-level>`: ERROR, WARN, INFO, DEBUG, TRACE, or OFF. If set to OFF, Fluentd unified logging is disabled.</td>
       </tr>

       <tr>
         <td>`logging.unified.tag = <service-tag>`</td>

         <td>
           Specify the unique tag for the Self-Service Analytics microservice, used in grouping logs. This tag must be unique throughout Self-Service Analytics.

           <br />

           Supply the Self-Service Analytics microservice name for `<service-tag>`. For example, `logging.unified.tag = query-engine`. This is important because the tag identifies which microservice the log message applies to.

           <br />

           Valid values are `query-engine`, `zoomdata-server`, `data-writer-postgresql`, and `edc-<connector-name>` (where `<connector-name>` is one of the names listed in [Connector Properties and Property Files](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/configure/properties-reference#connector-properties-and-property-files)).
         </td>
       </tr>

       <tr>
         <td>`logging.unified.label = <service-label>`</td>
         <td>Specify a more verbose label for the Self-Service Analytics microservice.</td>
       </tr>

       <tr>
         <td>`logging.unified.host = <yourFluentdServerIPaddress>`</td>
         <td>Specify the IP address of the Fluentd logging server.</td>
       </tr>

       <tr>
         <td>`logging.unified.port = <yourFluentdServerPort>`</td>
         <td>Specify the port of the Fluentd logging server.</td>
       </tr>
     </tbody>
   </table>

3. Save your changes and exit the `.properties` file.

4. Restart the Self-Service Analytics server.

On the Fluentd server, you can then direct your logs to a data source of your choice. For information and steps, see Fluentd's documentation on [Output](https://docs.fluentd.org/output).

<h2 id="configure-unified-logging-using-fluentd">
  Configure Unified Logging Using Fluentd
</h2>

For information and steps on installing Fluentd, refer to [Fluentd's installation documentation](https://docs.fluentd.org/installation). If Fluentd is not installed on the same server as the Self-Service Analytics, you will need to obtain the host and port numbers for the Fluentd server.

This section provides describes how to configure Fluentd to log Self-Service Analytics log data.

Configure Fluentd for logging Self-Service Analytics log data

1. Run the following command on the server where Self-Service Analytics is installed to install `td-agent` on that server.

   ```bash theme={null}
   curl -L https://toolbelt.treasuredata.com/sh/install-redhat-td-agent3.sh
   ```

2. Browse to the `/etc` folder on the Self-Service Analytics server to verify that `td-agent` is installed in the `/etc/td-agent` folder.

3. Install the Fluentd plugin for the data store you are using to store your Fluentd logs. Refer to your [Fluentd documentation](https://www.fluentd.org/plugins/all) for more information.

   For example, if you are using an Elasticsearch database to store Fluentd logs. run the following command to install the Fluentd Elasticsearch plugin on the Self-Service Analytics server.

   ```bash theme={null}
   sudo td-agent-gem install fluent-plugin-elasticsearch
   ```

4. Modify the `td-agent.conf` file in the `/etc/td-agent` folder using the following template.

   The following is an example of `td-agent.conf` using an Elasticsearch database for Fluentd logs.

   ```xml theme={null}
   <source>
      @type forward
      port <fluentd_port>
      bind 0.0.0.0
   </source>
   <match *.**>
      @type copy
      <store>
         @type elasticsearch
         host <elasticsearch_host>
         port <elasticsearch_port>
         user <elasticsearch-user>
         password <elasticsearch-password>
         logstash_format true
         logstash_prefix composer-unified-log
         logstash_dateformat %Y%m%d
         include_tag_key true
         index_name composer-unified-log
         type_name composer-unified-log
         tag_key @log_name
         flush_interval 1s
      </store>
      <store>
         @type stdout
      </store>
   </match>
   ```

5. Restart `td-agent`.

   ```bash theme={null}
   systemctl restart td-agent
   ```

6. Complete the steps described in [Enable Unified Logging in Self-Service Analytics Using Fluentd](#enable-unified-logging-in-self-service-analytics-using-fluentd) to enable Fluentd logging by Self-Service Analytics.

<h2 id="configure-self-service-analytics-logs">
  Configure Self-Service Analytics Logs
</h2>

The microservices used in Self-Service Analytics write logs to their [corresponding service's log files](#self-service-analytics-log-files-reference) by default. You can configure Self-Service Analytics to write these logs to the console only, or to write logs both to the console and the service's log files. Structured logging is also supported. See [Structured Logging](#structured-logging).

Every [service config file](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/configure/config-mgmt-ov#configuration-property-files) includes two properties you can use to define where the logs are written:

* `log.console.level` - edit to define the types of logs to write to the console
* `log.file.level` - edit to define the types of logs to write to the files

### Log Properties in Config Files

If you install using the bootstrap script, logging to files is enabled by default. You can reroute the logging to the console as needed to customize your installation.

<Note>
  If the value of log properties is set to `OFF`, Self-Service Analytics access logs are not written. For all other cases (`ALL`, `ERROR`, `WARN`, `DEBUG`, and `INFO`) access logs are written to the selected destination: file, console or both.
</Note>

* Bootstrap installation: The `*.jvm` file specifies `log.console.level=OFF` and `log.file.level=ALL` to support compatibility with earlier versions of Self-Service Analytics.

<h4 id="values-for-log-file-level-and-log-console-level">
  Values for log.file.level and log.console.level
</h4>

The following table lists possible values for `log.file.level` and `log.console.level`.

| Value | Description |
| - | - |
| `ALL` | All available log information. |
| `ERROR` | Application error messages that may affect processes. |
| `WARN` | Unexpected application issues that may not affect processes. |
| `INFO` | Expected activities. |
| `DEBUG` | Triggers capture of `WARN`, `INFO`, and `ERROR`information. |
| `OFF` | Disables logging. |

### Enable Logging for a Service to the Console

Enable logging to the console and append the desired corresponding value of the properties to the appropriate service configuration file.

* Use `log.console.level=ALL` to route duplicates of all logs to the console.
* Use `log.console.level=ERROR` to route only duplicates of errors to the console.
* Alternatively, use `log.console.level=ALL` and `log.console.level=ERROR` to have all logs in files and errors duplicated to the console.

Adjust the values to meet your needs, then restart the service after you have edited the config.

<Note>
  Self-Service Analytics services have two config files, `*properties` and `*.jvm`. If you add log configuration properties to both files, the priority of `*.jvm` is higher than `*. properties`.
</Note>

### Consul Logging

By default, Consul writes logs to the console, but you can duplicate logs to files if needed.

Configure Consul Logs to Duplicate to Files:

1. Edit the Consul config file, `consul.json`. For Linux installations, this is located in `/opt/zoomdata/conf/consul.json.`

2. Add the following properties:

   ```yaml theme={null}
   "log_file": "/opt/zoomdata/logs/zoomdata-consul.log",
   "log_rotate_bytes": 104857600,
   "log_rotate_max_files" : 5
   ```

   Adjust the path to your log file and other log configuration properties as needed for your environment. In Linux environments, the log is located in `/opt/zoomdata/logs`, and in `<install-path>/logs` for Windows environments. See [Consul documentation](https://www.consul.io/docs/v1.11.x/agent/options#log_file) for more information.

<h3 id="structured-logging">
  Structured Logging
</h3>

Self-Service Analytics supports structured logging. You can enable for installations done via bootstrap, and is enabled by default for Kubernetes environments.

#### Components Support for Structured Logging

* zoomdata-web
* query engine
* admin server
* screenshot service
* data writer
* data connectors
* self service reports

#### Enable Structured Logging

In bootstrap environments, set the property `log.structured.enabled` to `true` in the config files of your microservices to output logs in JSON format to the `STDOUT` destination. Logs output to the `FILE` logs destination are sent in plain text. See [Configuration Property Files](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/configure/config-mgmt-ov#configuration-property-files).

In Kubernetes environments, structured logging is enabled by default. To disable, use one of the following approaches:

* Set the environment variable `LOG_STRUCTURED_ENABLED` to `false` to disable logging for specific services.
* Set `structuredLogsEnabled` in `values.yaml` to `false` to disable logging for all services.
* For Consul, change the `log_json` value to `false` in the `consul.server.extraConfig` section of `values.yaml`.

<h2 id="self-service-analytics-log-files-reference">
  Self-Service Analytics Log Files Reference
</h2>

Self-Service Analytics uses the following log files. You can configure Self-Service Analytics to write these logs to the console in addition to or instead of the service files. See [Configure Self-Service Analytics Logs](#configure-self-service-analytics-logs).

| Log File | Contains |
| - | - |
| `edc-<connector>.log` | Specific data connector service log file. |
| `edc-<connector>-errors.log` | Specific data connector service log file, filtered to ERROR level log messages. |
| `query-engine.log` | Operational information about the query engine microservice. |
| `query-engine-access.log` | Standard web server access log for the query engine microservice. |
| `query-engine-activity.log` | Audit-related information for the query engine microservice. |
| `Security_service.log` | Information related to [enabling or disabling a security service](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/security/changing-encryption-mode#enable-or-disable-a-security-service). |
| `stream-writer.log` | Upload service information. |
| `zoomdata.log` | A wide variety of errors and information. This is the best place to start with troubleshooting. |
| `zoomdata-access.log` | Standard web server access log for the Self-Service Analytics microservice. |
| `zoomdata-consul-{unixTimestamp}.log` | Information on service discovery and registration. |
| `zoomdata-errors.log` | Self-Service Analytics log information with a log level of `ERROR`. |
| `zoomdata-installer.<date/time>.log` | Information related to the installation. Installation errors typically appear here. |
| `zoomdata-upgrade.log` | Information related to upgrades. Errors with an upgrade will typically show up here. |
| `zoomdata-websocket.log` | Information sent and received over a WebSocket from the browser. |

## Log Unification

Self-Service Analytics has unified logback configuration throughout Self-Service Analytics microservices. You can configure Self-Service Analytics to write these logs to the console in addition to or instead of the service files. See [Configure Self-Service Analytics Logs](#configure-self-service-analytics-logs) and [Self-Service Analytics Log Files Reference](#self-service-analytics-log-files-reference).

### Log Configuration Properties

Adjust these properties to set up logging for your environment.

<table>
  <thead>
    <tr>
      <th>Name</th>
      <th>Default Value</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>install.dir</td>
      <td>`.`</td>
      <td>Use to evaluate the value of `logs.dir`.</td>
    </tr>

    <tr>
      <td>logs.dir</td>
      <td>`${install.dir}/logs`</td>
      <td>The location of the log file and error log file.</td>
    </tr>

    <tr>
      <td>spring.application.name</td>
      <td>`zoomdata-service`</td>
      <td>Use to evaluate the default values of `logs.file-name`.</td>
    </tr>

    <tr>
      <td>logs.file-name</td>
      <td>`${spring.application.name}`</td>
      <td>Name of log file. Log file suffix: `.log`. Error log file suffix: `error.log`.</td>
    </tr>

    <tr>
      <td>log.console.level</td>
      <td>`ALL`</td>
      <td>The maximum level of logs to print to `stdout`. See [Log File Values](#log-file-values).</td>
    </tr>

    <tr>
      <td>log.file.level</td>
      <td>`ALL`</td>
      <td>The maximum level of logs to print to the log file. See [Log File Values](#log-file-values).</td>
    </tr>

    <tr>
      <td>log.password.regex</td>
      <td>`(?i)PASSWORD=[a-zA-Z0-9!@#\$%\^\*\&amp;]*`</td>
      <td>Regular expression used to detect passwords in log output. Replaces with `PASSWORD=****`.</td>
    </tr>

    <tr>
      <td>log.url-password.regex</td>
      <td>`(?&lt;=://)[^:]+:[^@]+@`</td>
      <td>Regular expression used to detect and remove credential in URLs and remove the credentials.</td>
    </tr>

    <tr>
      <td>log.sanitization.enabled</td>
      <td>`true`</td>

      <td>
        The default, `true`, is specified in `logging.properties`.

        <br />

        Toggles sanitization of log message via `org.apache.commons.text.StringEscapeUtils.escapeJava`.
      </td>
    </tr>

    <tr>
      <td>log.file.size</td>
      <td>`20`</td>
      <td>The maximum size of the log file in MB. When that size is reached, the file is renamed using this pattern: `{log.file-name}.log.%i`.</td>
    </tr>

    <tr>
      <td>log.file.count</td>
      <td>`5`</td>
      <td>Maximum number of log files.</td>
    </tr>

    <tr>
      <td>log.error.file.size</td>
      <td>`5`</td>
      <td>The maximum size of the error log file in MB. When that size is reached, the file is renamed using this pattern: `{log.file-name}-error.log.%i`.</td>
    </tr>

    <tr>
      <td>log.error.file.count</td>
      <td>`5`</td>
      <td>Maximum number of error log files.</td>
    </tr>

    <tr>
      <td>syslog.log.level</td>
      <td>`OFF`</td>
      <td>Syslog log level. See [Log File Values](#log-file-values).</td>
    </tr>

    <tr>
      <td>syslog.host</td>
      <td>`127.0.0.1`</td>
      <td>Syslog host name.</td>
    </tr>

    <tr>
      <td>syslog.port</td>
      <td>`514`</td>
      <td>Syslog port number.</td>
    </tr>

    <tr>
      <td>syslog.suffix</td>
      <td>`${spring.application.name}`</td>
      <td>Syslog suffix. Used to distinguish applications.</td>
    </tr>

    <tr>
      <td>trace.requests</td>
      <td>`false`</td>
      <td>Adds the MDC value of `requestId` to log output. Propagate value using `X-REQUEST-ID` http header.</td>
    </tr>
  </tbody>
</table>

<h4 id="log-file-values">
  Log File Values
</h4>

| Value | Description |
| - | - |
| `OFF` | Disables logging. |
| `FATAL` | Only error messages (the same as `ERROR` for logback). |
| `ERROR` | Application error messages that may affect processes. |
| `WARN` | Unexpected application issues that may not affect processes. |
| `INFO` | Expected activities. |
| `DEBUG` | Triggers capture of `WARN`, `INFO`, and `ERROR`information. |
| `TRACE` | Capture of `DEBUG` level of information, and low importance informational messages. |
| `ALL` | All available log information (the same as `TRACE` for logback). |

### Other Configuration Properties

Both Zoomdata-Web and Query Engine have properties you can adjust to suit your needs as well.

<h4 id="other-configuration-properties-zoomdata-web">
  Zoomdata-Web
</h4>

| Name | Default Value | Description |
| - | - | - |
| activity.log.file.count | `1` | Maximum number of activity log files . |
| activity.log.file.size | `10` | The maximum size of the activity log file in MB. When that size is reached, the file is renamed using this pattern: `{log.file-name}-activity.log.%i`. |
| activity.logs.dir | n/a | The location of the activity log file. If no location is specified, `{logs.dir}` is used. |
| websocket.log.file.size | `10` | The maximum size of the websocket log file in MB. When that size is reached, the file is renamed using this pattern: `{log.file-name}-websocket.log.%i`. |
| websocket.log.file.count | `5` | Maximum number of websocket log files. |
| websocket.log.level | `OFF` | Overall maximum log level of websocket logs. |
| websocket.file.level | `OFF` | Maximum log level of websocket logs in the file. |
| websocket.console.level | `OFF` | Maximum log level of websocket logs in the console. |
| access.log.file.size | `10` | The maximum size of the access log file in MB. When that size is reached, the file is renamed using this pattern: `{log.file-name}-access.log.%i`. |
| license.log.file.size | `10` | The maximum size of the license log file in MB. When that size is reached, the file is renamed using this pattern: `{log.file-name}-sessions.log.%i`. |

<h4 id="other-configuration-properties-query-engine">
  Query Engine
</h4>

| Name | Default Value | Description |
| - | - | - |
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

### Set Logging Levels

Every logging level can be changed using a [standard spring boot approach](https://docs.spring.io/spring-boot/docs/current/reference/htmlsingle/#features.logging.log-levels). Specify the corresponding property, as shown below.

<Note>
  The logback.zoomdata property, previously used to control the log level of some loggers, has been removed. Use a standard spring boot approach to specify appropriate properties.
</Note>

```properties theme={null}
# Enable debug logs for 'com.zoomdata' logger and it's children
logging.level.com.zoomdata=DEBUG
# Set log level to error for root logger (parent of all loggers) and it's children
logging.level.root=ERROR
```

#### Default Log File Names

Self-Service Analytics's microservices each have a series of default log files where you can find captured events.

| Name | Microservice | Description |
| - | - | - |
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
| `query-engine-slow-expression-parsing.log` | Query Engine | |
| `query-engine-slow-requests.log` | Query Engine | |
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

## Log File Migration Reference

With the introduction of unified log properties and unified logback configurations, a number of log files have new names. When you upgrade your Self-Service Analytics environment from an earlier version, you may need to rename properties overwritten by external configurations.

<h3 id="log-file-migration-reference-zoomdata-web">
  Zoomdata-web
</h3>

| Current Name | Deprecated Name |
| - | - |
| `log.file.size` | `zoomdata.log.file.size` |
| `log.file.count` | `zoomdata.log.rolling.maxIndex` |
| `log.error.file.size` | `zoomdata.error.log.file.size` |
| `access.log.file.size` | `zoomdata.access.log.file.size` |
| `license.log.file.size` | `zoomdata.license.log.file.size` |
| `activity.log.file.count` | `zoomdata.activity.log.file.max.index` |
| `activity.log.file.size` | `zoomdata.activity.log.file.size` |
| `activity.logs.dir` | `zoomdata.activity.logs.dir` |
| `websocket.log.file.size` | `zoomdata.websocket.log.file.size` |
| `websocket.log.file.count` | `zoomdata.websocket.log.rolling.maxIndex` |

<h3 id="log-file-migration-reference-query-engine">
  Query Engine
</h3>

| Current Name | Deprecated Name |
| - | - |
| `log.file.size` | `qe.log.file.size` |
| `log.file.count` | `qe.log.rolling.maxIndex` |
| `log.error.file.size` | `qe.error.log.file.size` |
| `websocket.log.file.count` | `qe.websocket.log.rolling.maxIndex` |
| `websocket.log.level` | `qe.websocket.log.level` |
| `websocket.log.file.size` | `qe.websocket.log.file.size` |
| `access.log.file.size` | `qe.access.log.file.size` |

### EDC

| Current Name | Deprecated Name |
| - | - |
| `logs.file-name` | `log.file.base.name` |

<h3 id="admin-service-config-server-data-writer-and-screenshot-service">
  Admin Service, Config Server, Data Writer, and Screenshot Service
</h3>

| Current Name | Deprecated Name |
| - | - |
| `log.file.count` | `log.rolling.maxIndex` |
| `log.error.file.size` | `error.log.file.size` |
| `log.error.file.count` | `error.log.rolling.maxIndex` |
