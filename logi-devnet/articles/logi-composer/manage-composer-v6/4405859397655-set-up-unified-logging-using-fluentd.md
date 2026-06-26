---
title: "Set Up Unified Logging Using Fluentd"
id: 4405859397655
section: "Manage Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405859397655-Set-Up-Unified-Logging-Using-Fluentd
updated_at: 2021-09-21T01:29:02Z
---

# Set Up Unified Logging Using Fluentd

# Set Up Unified Logging Using Fluentd

In Composer, you can use Fluentd as a logging layer to which you can direct the logs for various components of Composer. This allows you to customize the log output to meet the needs of your environment.

Composer leverages Fluentd’s unified logging layer to collect logs via a central API. Fluentd can be configured to aggregate logs to various data sources or outputs. For example, if you are directing all log files from your `zoomdata-websocket.log` and `zoomdata-errors.log` to a Fluentd server, you can add one of Fluentd’s plug-ins to write the log files to Elasticsearch to analyze web client errors for your environment.

Unified logging does not replace Composer's default logging architecture. It only augments that experience with an option for those wanting additional logging control.

By default, unified logging is disabled and needs to be enabled for each microservice you want captured in Fluentd.

If written to a data store compatible with Composer’s connectors, Composer can then be used to analyze and visualize your logs. The selected data store must be supported by Composer's connectors if you plan to view the log files in Composer dashboards. A list of supported data stores is provided in [*Composer Data Connector Reference*](https://devnet.logianalytics.com/hc/en-us/articles/4405859436055-Composer-Data-Connector-Reference). The selected data store should be available and configured in conjunction with Fluentd to receive logs.

At a high level, the steps to set up Fluentd are as follows:

1. Set up a database to store the Fluentd log files. Typically, customers store log files in a log capture service such as Elasticsearch or in a database server such as PostgreSQL.
2. Configure Fluentd logging for your Composer installation. See [*Configure Unified Logging Using Fluentd*](https://devnet.logianalytics.com/hc/en-us/articles/4405851110935-Configure-Unified-Logging-Using-Fluentd). This includes configuring the Fluentd `td-agent.conf` file to identify the Composer [microservice](https://devnet.logianalytics.com/hc/en-us/articles/4405851149591-Composer-Microservice-Name-Reference) log data you want logged.
3. Enable unified logging and configure the host and port information for your Fluentd server for each [microservice](https://devnet.logianalytics.com/hc/en-us/articles/4405851149591-Composer-Microservice-Name-Reference) log file from which you are extracting data for Fluentd logging. See [*Enable Unified Logging in Composer v6 Using Fluentd*](https://devnet.logianalytics.com/hc/en-us/articles/4405859396631-Enable-Unified-Logging-in-Composer-v6-Using-Fluentd).
