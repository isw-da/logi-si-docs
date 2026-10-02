> ## Documentation Index
> Fetch the complete documentation index at: https://insightsoftware.mintlify.site/llms.txt
> Use this file to discover all available pages before exploring further.

# Distributed Tracing for Self-Service Analytics

All microservices support distributed tracing using the [OpenTelemetry](https://opentelemetry.io/) (OTel) specifications. Integrate with OTel javaagent or any other OTel compliant agent. Install a tracing server of your choice, an OTel collector, and configure the microservices to trace Self-Service Analytics front end and back end requests.

Tracing collects information about requests. Use it to associate logs of the other microservices with the collected information.

* [Install a Tracing Server](#install-a-tracing-server)
* [Install and Configure OTel Collector](#install-and-configure-otel-collector)
* [Configure the Collector](#configure-the-collector)
* [Configure Self-Service Analytics Microservice Tracing](#configure-self-service-analytics-microservice-tracing)

<h3 id="install-a-tracing-server">
  Install a Tracing Server
</h3>

Self-Service Analytics integrates with any tracing server that supports [OpenTelemetry](https://opentelemetry.io/) (OTel) specifications and its export protocols (otlp, zipkin, jaeger).

After you have installed a tracing server, install the otel collector.

<h3 id="install-and-configure-otel-collector">
  Install and Configure OTel Collector
</h3>

Install an OTel collector to act as a proxy between Self-Service Analytics microservices and your tracing server, both to simplify configuration and improve security by passing information through the proxy. See [https://opentelemetry.io/docs/collector/](https://opentelemetry.io/docs/collector/) and [https://opentelemetry.io/docs/collector/getting-started/](https://opentelemetry.io/docs/collector/getting-started/).

After installation, configure your collector or collectors to export tracing information to the tracing server.

<img src="https://mintcdn.com/insightsoftware/2cXq_sDOxrDVXUcv/simba-embedded-analytics/docs/self-service-analytics/26.3/images/config/otel-dt-collector-diagram-23-1.png?fit=max&auto=format&n=2cXq_sDOxrDVXUcv&q=85&s=2cf9294b3016a61cbde67d77c2c2592d" alt="diagram of otel collector in use in a Composer environment" width="1282" height="897" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/config/otel-dt-collector-diagram-23-1.png" />

<h3 id="configure-the-collector">
  Configure the Collector
</h3>

Provide the appropriate configuration information for your collector. The configuration information consists of three main sections, receivers, processors, and exporters. See [https://opentelemetry.io/docs/collector/configuration/](https://opentelemetry.io/docs/collector/configuration/).

```yaml theme={null}
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
```

* **Receivers**: Configure available protocols and endpoints for the receiver to receive tracing information from Self-Service Analytics's microservices. insightsoftware recommends you use the OTlp protocol.
* **Processor**: Enable additional processing of tracing information. In this example, batch processing is enabled to optimize network communication.
* **Exporters**: Configure export information. Provide a destination URL and other connection parameters to communicate with the tracing server. insightsoftware recommends you use the OTlp protocol.

After you have installed and configured the OTel collector, install and configure a java agent and Self-Service Analytics's microservices.

<h3 id="configure-self-service-analytics-microservice-tracing">
  Configure Self-Service Analytics Microservice Tracing
</h3>

You must install and configure the OTel java agent to trace Self-Service Analytics microservices. Optionally, next configure the Self-Service Analytics front end for tracing. After these steps are complete and you have restarted the microservices, you can extract the traceID in a REST request or from a web socket outbound message.

* [Install the Java Agent](#install-the-java-agent)
* [Configure the Collector](#configure-the-collector)
* [Configure the Self-Service Analytics Front End](#configure-the-self-service-analytics-front-end)
* [Extract the traceID](#extract-the-traceid)

<Warning>
  insightsoftware recommends you use the OTel java agent.
</Warning>

<h4 id="install-the-java-agent">
  Install the Java Agent
</h4>

1. Download the java agent to the server running the Self-Service Analytics microservice. [https://github.com/open-telemetry/opentelemetry-java-instrumentation/releases/latest/download/opentelemetry-javaagent.jar](https://github.com/open-telemetry/opentelemetry-java-instrumentation/releases/latest/download/opentelemetry-javaagent.jar)

2. Define the path to the java agent for Self-Service Analytics. Select the option that works best for your environment.

   1. Specify the path in `SERVICE_NAME.jvm` (such as `zoomdata.jvm` or `edc-postgresql.jvm`) in the `/opt/zoomdata/conf/` folder, such as `-javaagent:/path/to/java/agent/opentelemetry-javaagent.jar`. See [Self-Service Analytics Microservice Name Reference](/simba-embedded-analytics/docs/self-service-analytics/26.3/get-started/arch-microservice#self-service-analytics-microservice-name-reference).
   2. Define an environment variable, `_JAVA_OPTS`, that contains the path, such as `_JAVA_OPTIONS="-javaagent:/path/to/java/agent/opentelemetry-javaagent.jar"`.

<Note>
  Some application performance monitoring tools provide their own java agents that are built on top of the OpenTelemetry java agent, or is compliant with the OTLP protocol. Use at your own discretion; the behavior may be different from the OTel java agent.
</Note>

#### Configure the Java Agent

After you have installed the java agent, specify backend configuration properties for the agent using required and optional configuration properties. Include in the SERVICE\_NAME.jvm or use environment variables. See [https://opentelemetry.io/docs/instrumentation/java/automatic/agent-config/](https://opentelemetry.io/docs/instrumentation/java/automatic/agent-config/) and [https://opentelemetry.io/docs/reference/specification/sdk-environment-variables/](https://opentelemetry.io/docs/reference/specification/sdk-environment-variables/).

<h5 id="configure-the-java-agent-required-configuration-properties">
  Required Configuration Properties
</h5>

<table>
  <thead>
    <tr>
      <th>Property</th>
      <th>Recommended Value</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>OTEL\_TRACES\_EXPORTER</td>
      <td>otlp</td>
      <td>Defines the protocol to use to export tracing information.</td>
    </tr>

    <tr>
      <td>OTEL\_METRICS\_EXPORTER</td>
      <td>none</td>
      <td>Disable metrics export using opentelemetry.</td>
    </tr>

    <tr>
      <td>OTEL\_LOGS\_EXPORTER</td>
      <td>none</td>
      <td>Disable logs export using opentelemetry.</td>
    </tr>

    <tr>
      <td>OTEL\_EXPORTER\_OTLP\_TRACES\_ENDPOINT</td>
      <td>http\://OTEL\_COLLECTOR\_HOST:4317</td>
      <td>Defines the URL for the otel collector or tracing server.</td>
    </tr>

    <tr>
      <td>OTEL\_SERVICE\_NAME</td>

      <td>
        * zoomdata
        * query-engine
        * edc-postgresql
        * edc-mssql
        * screenshot-service
        * data-writer
      </td>

      <td>Define the names of the services.</td>
    </tr>

    <tr>
      <td>OTEL\_INSTRUMENTATION\_SPRING\_BOOT\_ACTUATOR\_AUTOCONFIGURE\_ENABLED</td>
      <td>false</td>
      <td>Required, for now, to enable tracing. This may be updated after future otel releases.</td>
    </tr>
  </tbody>
</table>

<h4 id="configure-the-self-service-analytics-front-end">
  Configure the Self-Service Analytics Front End
</h4>

After you have provided back end configuration properties for tracking, provide any needed variables for the Self-Service Analytics front end as well.

Enable tracing and provide environment variables by specifying the fe.env configuration property for the zoomdata-web microservice using the following format: `fe.env=ENV_VARIABLE1=value1;ENV_VARIABLE2=value2;ENV_VARIABLE3=value3`.

The default value of `OTEL_SDK_DISABLED` is `false` in the OpenTelemetry SDK. When used in your environment, installation changes this value to `true` for front end support. To enable tracing, specify `OTEL_SDK_DISABLED=false` in the environment variable.

<h5 id="configure-the-self-service-analytics-front-end-required">
  Required Configuration Properties
</h5>

<table>
  <thead>
    <tr>
      <th>Property</th>
      <th>Recommended Value</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>OTEL\_TRACES\_EXPORTER</td>
      <td>otlp</td>
      <td>Defines the protocol to use to export tracing information.</td>
    </tr>

    <tr>
      <td>OTEL\_METRICS\_EXPORTER</td>
      <td>none</td>
      <td>Disable metrics export using opentelemetry.</td>
    </tr>

    <tr>
      <td>OTEL\_LOGS\_EXPORTER</td>
      <td>none</td>
      <td>Disable logs export using opentelemetry.</td>
    </tr>

    <tr>
      <td>OTEL\_EXPORTER\_OTLP\_TRACES\_ENDPOINT</td>
      <td>http\://OTEL\_COLLECTOR\_HOST:4317</td>
      <td>Defines the URL for the otel collector or tracing server.</td>
    </tr>

    <tr>
      <td>OTEL\_SERVICE\_NAME</td>

      <td>
        * zoomdata
        * query-engine
        * edc-postgresql
        * edc-mssql
        * screenshot-service
        * data-writer
      </td>

      <td>Define the names of the services.</td>
    </tr>

    <tr>
      <td>OTEL\_INSTRUMENTATION\_SPRING\_BOOT\_ACTUATOR\_AUTOCONFIGURE\_ENABLED</td>
      <td>false</td>
      <td>Required, for now, to enable tracing. This may be updated after future otel releases.</td>
    </tr>
  </tbody>
</table>

OpenTelemetry is executed in the user's browser and all tracing information is sent to the collector from the browser. The `OTEL_EXPORTER_OTLP_TRACES_ENDPOINT` must be reachable by the browser to execute tracing collection. Depending on your environment, you may need to configure [cors](https://github.com/open-telemetry/opentelemetry-collector/blob/main/config/confighttp/README.md).

After you have installed and configured the java agent, restart all microservices.

<h4 id="extract-the-traceid">
  Extract the traceID
</h4>

When tracing is configured and enabled, you can extract the `traceID` in a REST request or from a web socket outbound message. `traceID` is embedded in the `traceparent` property. The structure is `traceparent` is `{version}-{traceId}-{spanId}-{sampleDecision}`.
