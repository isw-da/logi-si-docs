---
title: "Configuration Property Files"
id: 4405850888599
section: "Manage Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405850888599-Configuration-Property-Files
updated_at: 2021-09-21T01:26:48Z
---

# Configuration Property Files

# Configuration Property Files

Composer uses the configuration files in the following table to ensure successful deployment in your operating environment. You can edit many of the properties and options in these files. You can edit them in `/etc/zoomdata` as described in [*Edit a Composer Configuration File*](https://devnet.logianalytics.com/hc/en-us/articles/4405850887703-Edit-a-Composer-Configuration-File).

![](https://devnet.logianalytics.com/hc/article_attachments/4406747382295/noteicon.jpg)Composer discourages changing properties in the `/opt/zoomdata/conf` directory. Instead we recommend that you copy the files you want to change to the `/etc/zoomdata` directory and change them there. This will ensure that your changes are not overwritten when Composer is next upgraded. In addition, you can quickly determine what changes you've made to a properties file using `diff`. For example:

```
diff /opt/zoomdata/conf/edc-<connector-name>.properties /etc/zoomdata/<edc-<connector-name>.properties
```

or

```
diff /opt/zoomdata/conf/zoomdata.properties /etc/zoomdata/zoomdata.properties
```

| File | Defines.... |
| --- | --- |
| `admin-server.jvm` | JVM options related to the Composer Service Monitor. |
| `admin-server.properties` | Configuration properties related to the Composer Service Monitor. |
| `config-server.jvm` | JVM options related to the Composer configuration microservice. |
| `config-server.properties` | Configuration properties related to the Composer configuration microservice. |
| `consul.json` | Settings related to the Composer Service Discovery microservice. For a description of these settings, see <https://www.consul.io/docs/agent/options>. |
| `data-writer-postgresql.jvm` | JVM options related to the Data Writer microservice's Postgres relational database. |
| `data-writer-postgresql.properties` | Configuration properties related to the Data Writer microservice's Postgres relational database. |
| `edc-<connector>.jvm` | JVM options related to the specific Composer connector microservice. For example, `edc-impala.jvm` contains JVM options for the Composer Cloudera Impala connector microservice. See [*Connector Properties and Property Files*](https://devnet.logianalytics.com/hc/en-us/articles/4405850892439-Connector-Properties-and-Property-Files). |
| `edc-<connector>.properties` | Configuration properties related to the specific Composer connector microservice. For example, `edc-impala.properties` contains configuration properties for the Composer Cloudera Impala connector microservice. See [*Connector Properties and Property Files*](https://devnet.logianalytics.com/hc/en-us/articles/4405850892439-Connector-Properties-and-Property-Files). |
| `query-engine.jvm` | JVM options related to the Composer query engine. See [*Manage the Composer Query Engine*](https://devnet.logianalytics.com/hc/en-us/articles/4405859161751-Manage-the-Composer-Query-Engine). |
| `query-engine.properties` | Configuration properties related to the Composer query engine. See [*Query Engine Properties*](https://devnet.logianalytics.com/hc/en-us/articles/4405859160727-Query-Engine-Properties). |
| `screenshot-service.jvm` | JVM options related to Composer Screenshot microservice processing. |
| `screenshot-service.properties` | Configuration properties related to Composer Screenshot microservice processing. See [*screenshot-service.properties Properties*](https://devnet.logianalytics.com/hc/en-us/articles/4405850904471-screenshot-service-properties-Properties). |
| `tracing-server.jvm` | JVM options related to Composer's tracing microservice. |
| `tracing-server.properties` | configuration parameters related to Composer's tracing microservice. |
| `zoomdata.jvm` | JVM options (e.g. memory configuration) and Java system properties (e.g. timezone, temp directory, etc.) related to Composer. See [*zoomdata.jvm Options*](https://devnet.logianalytics.com/hc/en-us/articles/4405850906263-zoomdata-jvm-Options). |
| `zoomdata.properties` | Configuration properties related to Composer. See [*zoomdata.properties Properties*](https://devnet.logianalytics.com/hc/en-us/articles/4405850907159-zoomdata-properties-Properties). |
