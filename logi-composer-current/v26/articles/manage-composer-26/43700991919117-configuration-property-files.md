---
title: "Configuration Property Files"
id: 43700991919117
section: "Manage Composer 26"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43700991919117-Configuration-Property-Files
updated_at: 2026-05-29T14:07:19Z
---

# Configuration Property Files

# Configuration Property Files

Composer uses the configuration files in the following table to ensure successful deployment in your operating environment. You can edit many of the properties and options in these files. You can edit them in `/etc/zoomdata` as described in [Edit a Configuration File](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701053803917-Edit-a-Configuration-File).

**Note:** insightsoftware discourages changing properties in the `/opt/zoomdata/conf` directory (Linux) or `<install-path>/conf` (Windows). Copy the files you want to change to the `/etc/zoomdata` directory (Linux) or `<install-path>/conf-modify` (Windows) and change them there. This will ensure that your changes are not overwritten when Composer is next upgraded.

Quickly determine what changes you've made to a properties file using `diff` in Linux. For example:

diff /opt/zoomdata/conf/edc-<connector-name>.properties /etc/zoomdata/<edc-<connector-name>.properties

or

diff /opt/zoomdata/conf/zoomdata.properties /etc/zoomdata/zoomdata.properties

For Windows environments, use your preferred diff utility to compare the differences between your original and updated property files.

| File | Defines.... |
| --- | --- |
| `admin-server.jvm` | JVM options related to the Service Monitor. |
| `admin-server.properties` | Configuration properties related to the Service Monitor. |
| `config-server.jvm` | JVM options related to the configuration microservice. |
| `config-server.properties` | Configuration properties related to the configuration microservice. |
| `consul.json` | Settings related to the Service Discovery microservice. For a description of these settings, see <https://www.consul.io/docs/agent/options>. |
| `data-writer-postgresql.jvm` | JVM options related to the Data Writer microservice's Postgres relational database. |
| `data-writer-postgresql.properties` | Configuration properties related to the Data Writer microservice's Postgres relational database. |
| `edc-<connector>.jvm` | JVM options related to the specific connector microservice. For example, `edc-impala.jvm` contains JVM options for the Composer Cloudera Impala connector microservice. See [Connector Properties and Property Files](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43700992050061-Connector-Properties-and-Property-Files). |
| `edc-<connector>.properties` | Configuration properties related to the specific connector microservice. For example, `edc-impala.properties` contains configuration properties for the Cloudera Impala connector microservice. See [Connector Properties and Property Files](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43700992050061-Connector-Properties-and-Property-Files). |
| `query-engine.jvm` | JVM options related to the Composer query engine. See [Manage the Composer Query Engine](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701037846797-Manage-the-Composer-Query-Engine). |
| `query-engine.properties` | Configuration properties related to the query engine. See [Query Engine Properties](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701041000973-Query-Engine-Properties). |
| `screenshot-service.jvm` | JVM options related to Composer Screenshot microservice processing. |
| `screenshot-service.properties` | Configuration properties related to Screenshot microservice processing. See [screenshot-service.properties Properties](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701054295053-screenshot-service-properties-Properties). |
| `zoomdata.jvm` | JVM options (e.g. memory configuration) and Java system properties (e.g. timezone, temp directory, etc.) related to Composer. See [zoomdata.jvm Options](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43700990181901-zoomdata-jvm-Options). |
| `zoomdata.properties` | Configuration properties related to Composer. See [zoomdata.properties Properties](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701054421133-zoomdata-properties-Properties). |
