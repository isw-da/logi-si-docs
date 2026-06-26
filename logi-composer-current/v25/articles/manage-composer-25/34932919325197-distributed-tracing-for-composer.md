---
title: "Distributed Tracing for Composer"
id: 34932919325197
section: "Manage Composer 25"
product: "Logi Composer v25"
url: https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932919325197-Distributed-Tracing-for-Composer
updated_at: 2026-05-26T22:09:36Z
---

# Distributed Tracing for Composer

# Distributed Tracing for Composer

All Composer microservices support distributed tracing using the [OpenTelemetry](https://opentelemetry.io/) (OTel) specifications. Integrate with OTel javaagent or any other OTel compliant agent. Install a tracing server of your choice, an OTel collector, and configure the microservices to trace Composer front end and back end requests.

Tracing collects information about requests. Use it to associate logs of the other microservices with the collected information.

* [Install a Tracing Server](#Install)
* [Install and Configure OTel Collector](#Install2)
* [Configure the Collector](#Configur)
* [Configure Composer Microservice Tracing](#Configur3)

## Install a Tracing Server

Composer integrates with any tracing server that supports [OpenTelemetry](https://opentelemetry.io/) (OTel) specifications and its export protocols (otlp, zipkin, jeager).

After you have installed a tracing server, install the otel collector.

## Install and Configure OTel Collector

Install an OTel collector to act as a proxy between Composer microservices and your tracing server, both to simplify configuration and improve security by passing information through the proxy. See <https://opentelemetry.io/docs/collector/> and <https://opentelemetry.io/docs/collector/getting-started/>.

After installation, configure your collector or collectors to export tracing information to the tracing server.

![diagram of otel  collector in use in a Composer environment](https://logi-composer-v25.insightsoftware.com/hc/article_attachments/46167251885069 "diagram of otel  collector in use in a Composer environment")

## Configure the Collector

Provide the appropriate configuration information for your collector. The configuration information consists of three main sections, receivers, processors, and exporters. See <https://opentelemetry.io/docs/collector/configuration/>.

receivers:
otlp:
protocols:
grpc:
processors:
batch:
exporters:
otlp:
endpoint: zoomdata-tempo:4317
tls:
insecure: true
service:
pipelines:
traces:
receivers: [otlp]
processors: [batch]
exporters: [otlp]

* **Receivers**: Configure available protocols and endpoints for the receiver to receive tracing information from Composer's microservices. insightsoftware recommends you use the OTlp protocol.
* **Processor**: Enable additional processing of tracing information. In this example, batch processing is enabled to optimize network communication.
* **Exporters**: Configure export information. Provide a destination URL and other connection parameters to communicate with the tracing server. insightsoftware recommends you use the OTlp protocol.

After you have installed and configured the OTel collector, install and configure a java agent and Composer's microservices.

## Configure Composer Microservice Tracing

You must install and configure the OTel java agent to trace Composer microservices. Optionally, next configure the Composer front end for tracing. After these steps are complete and you've restarted the microservices, you can extract the traceID in a REST request or from a web socket outbound message.

* [Install the Java Agent](#Install4)
* [Configure the Collector](#Configur)
* [Configure the Composer Front End](#Configur2)
* [Extract the traceID](#Extract)

**Important:** insightsoftware recommends you use the OTel java agent.

### Install the Java Agent

1. Download the java agent to the server running the Composer microservice. <https://github.com/open-telemetry/opentelemetry-java-instrumentation/releases/latest/download/opentelemetry-javaagent.jar>
2. Define the path to the java agent for Composer. Select the option that works best for your environment.

   1. Specify the path in `SERVICE_NAME.jvm` (such as `zoomdata.jvm` or `edc-postgresql.jvm`) in the `/opt/zoomdata/conf/` folder, such as `-javaagent:/path/to/java/agent/opentelemetry-javaagent.jar`. See [Composer  Microservice Name Reference](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933143202829-Composer-Microservice-Name-Reference).
   2. Define an environment variable, `_JAVA_OPTS`, that contains the path, such as `_JAVA_OPTIONS="-javaagent:/path/to/java/agent/opentelemetry-javaagent.jar"`.

**Note:** 
Some application performance monitoring tools provide their own java agents that are built on top of the OpenTelemetry java agent, or is compliant with the OTLP protocol. Use at your own discretion; the behavor may be different from the OTel java agent.

### Configure the Java Agent

After you've installed the java agent, specify backend configuration properties for the agent using required and optional configuration properties. Include in the SERVICE\_NAME.jvm or use environment variables. See <https://opentelemetry.io/docs/instrumentation/java/automatic/agent-config/> and <https://opentelemetry.io/docs/reference/specification/sdk-environment-variables/>.

#### Required Configuration Properties

| Property | Recommended Value | Description |
| --- | --- | --- |
| OTEL\_TRACES\_EXPORTER | otlp | Defines the protocol to use to export tracing information. |
| OTEL\_METRICS\_EXPORTER | none | Disable metrics export using opentelemetry. |
| OTEL\_LOGS\_EXPORTER | none | Disable logs export using opentelemetry. |
| OTEL\_EXPORTER\_OTLP\_TRACES\_ENDPOINT | http://OTEL\_COLLECTOR\_HOST:4317 | Defines the URL for the otel collector or tracing server. |
| OTEL\_SERVICE\_NAME | * zoomdata * query-engine * edc-postgresql * edc-mssql * screenshot-service * data-writer | Define the names of the services. |
| OTEL\_INSTRUMENTATION\_SPRING\_BOOT\_ACTUATOR\_AUTOCONFIGURE\_ENABLED | false | Required, for now, to enable tracing. This may be updated after future otel releases. |

### Configure the Composer Front End

After you've provided back end configuration properties for tracking, provide any needed variables for the Composer front end as well.

Enable tracing and provide environment variables by specifying the fe.env configuration property for the zoomdata-web microservice using the following format: `fe.env=ENV_VARIABLE1=value1;ENV_VARIABLE2=value2;ENV_VARIABLE3=value3`.

The default value of `OTEL_SDK_DISABLED` is `false` in the OpenTelemetry SDK. When used in your Composer environment, installation changes this value to `true` for front end support. To enable tracing, specify `OTEL_SDK_DISABLED=false` in the environment variable.

#### Required Configuration Properties

| Property | Recommended Value | Description |
| --- | --- | --- |
| OTEL\_TRACES\_EXPORTER | otlp | Defines the protocol to use to export tracing information. |
| OTEL\_METRICS\_EXPORTER | none | Disable metrics export using opentelemetry. |
| OTEL\_LOGS\_EXPORTER | none | Disable logs export using opentelemetry. |
| OTEL\_EXPORTER\_OTLP\_TRACES\_ENDPOINT | http://OTEL\_COLLECTOR\_HOST:4317 | Defines the URL for the otel collector or tracing server. |
| OTEL\_SERVICE\_NAME | * zoomdata * query-engine * edc-postgresql * edc-mssql * screenshot-service * data-writer | Define the names of the services. |
| OTEL\_INSTRUMENTATION\_SPRING\_BOOT\_ACTUATOR\_AUTOCONFIGURE\_ENABLED | false | Required, for now, to enable tracing. This may be updated after future otel releases. |

OpenTelemetry is executed in the user's browser and all tracing information is sent to the collector from the browser. The `OTEL_EXPORTER_OTLP_TRACES_ENDPOINT` must be reachable by the browser to execute tracing collection. Depending on your environment, you may need to configure [cors](https://github.com/open-telemetry/opentelemetry-collector/blob/main/config/confighttp/README.md).

After you have installed and configured the java agent, restart all microservices.

### Extract the traceID

When tracing is configured and enabled, you can extract the `traceID` in a REST request or from a web socket outbound message. `traceID` is embedded in the `traceparent` property. The structure is `traceparent` is `{version}-{traceId}-{spanId}-{sampleDecision}`.
