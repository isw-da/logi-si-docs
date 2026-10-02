> ## Documentation Index
> Fetch the complete documentation index at: https://insightsoftware.mintlify.site/llms.txt
> Use this file to discover all available pages before exploring further.

# About Microservices

You can manage microservices in CentOS environments or in supported Ubuntu environments. You can also manage the microservices using the Logi Composer CLI.

See the following sections:

* [Enable Microservices](#enable-microservices)
* [Start Microservices](#start-microservices)
* [Restart Microservices](#restart-microservices)
* [Stop Microservices](#stop-microservices)
* [Disable Microservices](#disable-microservices)
* [Microservice Startup Order](#microservice-startup-order)

<h2 id="enable-microservices">
  Enable Microservices
</h2>

You can also enable microservices using the CLI. See [Manage Self-Service Analytics Microservices Using the Command Line Utility](#manage-self-service-analytics-microservices-using-the-command).

To enable all microservices, enter the following command:

```bash theme={null}
sudo systemctl enable $(systemctl list-unit-files | grep zoomdata | grep edc | awk '{print $1}')
```

To enable a specific microservice, enter the following command:

```bash theme={null}
sudo systemctl enable <service>
```

Replace `<service>` with the name of the microservice. See [Self-Service Analytics Microservice Name Reference](/simba-embedded-analytics/docs/self-service-analytics/26.3/get-started/arch-microservice#self-service-analytics-microservice-name-reference).

<h2 id="start-microservices">
  Start Microservices
</h2>

The list of microservices can be found in [Self-Service Analytics Microservice Name Reference](/simba-embedded-analytics/docs/self-service-analytics/26.3/get-started/arch-microservice#self-service-analytics-microservice-name-reference). The order in which microservices should be started is described in [Microservice Startup Order](#microservice-startup-order).

You can also start microservices using the CLI. See [Manage Self-Service Analytics Microservices Using the Command Line Utility](#manage-self-service-analytics-microservices-using-the-command).

To start all microservices, enter the following command:

```bash theme={null}
sudo systemctl start $(systemctl list-unit-files | grep zoomdata | grep edc | awk '{print $1}')
```

To start a specific microservice, enter the following command:

```bash theme={null}
sudo systemctl start <service>
```

Replace `<service>` with the name of the microservice. See [Self-Service Analytics Microservice Name Reference](/simba-embedded-analytics/docs/self-service-analytics/26.3/get-started/arch-microservice#self-service-analytics-microservice-name-reference).

<h2 id="restart-microservices">
  Restart Microservices
</h2>

You can also restart microservices using the CLI. See [Manage Self-Service Analytics Microservices Using the Command Line Utility](#manage-self-service-analytics-microservices-using-the-command).

**To restart all microservices, enter the following command:**

```bash theme={null}
sudo systemctl restart $(systemctl list-unit-files | grep zoomdata | grep edc | awk '{print $1}')
```

**To restart a specific microservice, enter the following command:**

```bash theme={null}
sudo systemctl restart <service>
```

Replace `<service>` with the name of the microservice. See [Self-Service Analytics Microservice Name Reference](/simba-embedded-analytics/docs/self-service-analytics/26.3/get-started/arch-microservice#self-service-analytics-microservice-name-reference).

<h2 id="stop-microservices">
  Stop Microservices
</h2>

You can also stop microservices using the CLI. See [Manage Self-Service Analytics Microservices Using the Command Line Utility](#manage-self-service-analytics-microservices-using-the-command).

To stop all microservices, enter the following command:

```bash theme={null}
sudo systemctl stop $(systemctl list-unit-files | grep zoomdata | awk '{print $1}')
```

To stop a specific microservice, enter the following command:

```bash theme={null}
sudo systemctl stop <service>
```

Replace `<service>` with the name of the microservice. See [Self-Service Analytics Microservice Name Reference](/simba-embedded-analytics/docs/self-service-analytics/26.3/get-started/arch-microservice#self-service-analytics-microservice-name-reference).

<h2 id="disable-microservices">
  Disable Microservices
</h2>

You can also disable microservices using the CLI. See [Manage Self-Service Analytics Microservices Using the Command Line Utility](#manage-self-service-analytics-microservices-using-the-command).

To disable all microservices, enter the following command:

```bash theme={null}
sudo systemctl disable $(systemctl list-unit-files | grep zoomdata | awk '{print $1}')
```

To disable a specific microservice, enter the following command:

```bash theme={null}
sudo systemctl disable <service>
```

Replace `<service>` with the name of the microservice. See [Self-Service Analytics Microservice Name Reference](/simba-embedded-analytics/docs/self-service-analytics/26.3/get-started/arch-microservice#self-service-analytics-microservice-name-reference).

<h2 id="microservice-startup-order">
  Microservice Startup Order
</h2>

The only microservices that must be started first are the Postgres and Service Discovery microservices. The other microservices are more tolerant and can be started in any order.

insightsoftware recommends starting microservices in the following order. You can start microservices using CentOS or Ubuntu commands or using the CLI. See [Start Microservices](#start-microservices) and [Manage Self-Service Analytics Microservices Using the Command Line Utility](#manage-self-service-analytics-microservices-using-the-command). A full list of Self-Service Analytics microservices can be found in [Self-Service Analytics Microservice Name Reference](/simba-embedded-analytics/docs/self-service-analytics/26.3/get-started/arch-microservice#self-service-analytics-microservice-name-reference).

1. The Postgres microservice (`postgresql-<version>`) used for metadata storage (where `<version>` is the version of Postgres you have installed.

2. The Service Discovery microservice (`zoomdata-consul`) used for microservice discovery.

3. The connector microservices (in the format `zoomdata-edc-<connector_name>`) used to connect to different data stores. The following CentOS example starts all available connector microservices, rather than starting them individually:

   ```bash theme={null}
   sudo systemctl start $(systemctl list-unit-files | grep zoomdata-edc | awk ‘{print $1}‘)
   ```

4. The query engine microservice (`zoomdata-query-engine`) used for query engine processing.

5. The `zoomdata-data-writer-postgresql` microservice.

6. The following optional microservices, if they are installed.

   * `zoomdata-admin-server`
   * `zoomdata-screenshot-service`

7. The main Self-Service Analytics microservice (`zoomdata`).

<h2 id="scaling-self-service-analytics-microservices">
  Scaling Self-Service Analytics Microservices
</h2>

Self-Service Analytics microservices allow you to scale your Self-Service Analytics installation, giving you expanded performance gains. As you roll out your microservices changes, you will need to:

* [Estimate User and Microservice Loads](#estimate-user-and-microservice-loads)
* [Add or Remove Nodes in a High Availability Environment](#add-or-remove-nodes-in-a-high-availability-environment)
* [Configure Throughput for Microservices](#configure-throughput-for-microservices)
* [Load Monitor Microservices](#load-monitor-microservices)
* [Scale Microservices Up](#scale-microservices-up)
* [Scale Microservices Down](#scale-microservices-down)

All microservices, except composer web, support horizontal scaling. Composer web supports vertical scaling only.

<h3 id="estimate-user-and-microservice-loads">
  Estimate User and Microservice Loads
</h3>

The load used by each microservice depends on the type of interactions your users have while using Self-Service Analytics. Some actions load only the composer web component, while others may load multiple components.

Some examples of actions that load microservices are included in the table below.

| Action | Microservices Loaded |
| - | - |
| Open the home page | composer web |
| Open a dashboard | composer web, connector, query engine |
| Open the visual Gallery | composer web |
| Create a source | composer web, connector, query engine |
| Create an uploaded source | composer web, connector, data writer, query engine |
| Upload new data via API | composer web, data writer |
| Execute scheduled dashboard report | composer web, connector, screenshot service, query engine |
| Live mode | composer web, connector, query engine |

<Note>
  Horizontal scaling up of a microservice does not provide doubled performance gains due to sharing of PostreSQL resources and overlapping of microservices.
</Note>

Start your scale planning based on an approximate number of services and expected number of users. See [Server Size Guidelines](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/install/installation-prerequisites#server-size-guidelines) for more information on services and user estimation.

<h3 id="add-or-remove-nodes-in-a-high-availability-environment">
  Add or Remove Nodes in a High Availability Environment
</h3>

To scale a microservice up or down, you may need to [Add Nodes to an Existing High Availability Installation](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/install/distenv-ov#add-nodes-to-an-existing-high-availability-installation) or [Remove Nodes from a High Availability Environment](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/install/distenv-ov#remove-nodes-from-a-high-availability-environment). Before you add or remove nodes, you should understand the actual load on your microservices to make the decision of scaling up or down. See [Self-Service Analytics System Metrics](#self-service-analytics-system-metrics).

<h3 id="configure-throughput-for-microservices">
  Configure Throughput for Microservices
</h3>

All microservices have a configuration property, `server.jetty.max-threads`, you can use to limit throughput. Once configured, you can more accurately monitor the load on each microservice.

Set your estimated concurrent users for each service at +20%, based on your calculations made using [Server Size Guidelines](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/install/installation-prerequisites#server-size-guidelines). To manage configuration properties of `server.jetty.max-threads`, see [Configure and Start the Configuration Microservice](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/monitor/service-monitor-overview#configure-and-start-the-configuration-microservice).

For example, if you have three instances of the query engine microservice and you expect 150 concurrent users, each instance is expected to handle 50 concurrent users. To accommodate this demand, set `server.jetty.max-threads` to (`60 = 150 / 3 & 120%`) for each instance of query engine.

<h3 id="load-monitor-microservices">
  Load Monitor Microservices
</h3>

With throughput defined for your microservices, you can measure their use to decide what services to scale up or scale down.

Self-Service Analytics microservices exposes several different metrics to help you understand the current load on each service. The main outputs to monitor include:

* `jetty_threads_busy` shows a current count of concurrent users.
* `jetty_threads_config_max` shows the maximum allowed concurrent users. This should match the value you set in `server.jetty.max-threads`.

These show a moment in time, which can vary depending on use spikes that may not actually require scaling up or down. Smooth out the data by looking at a specific length of time, such as five minutes, and monitor the average load across all instances of the same microservice.

Average over five minutes:

```
avg by instance_type (jetty_threads_busy) over 5m / avg by instance_type (jetty_threads_config_max)
```

In Prometheus:

```
sum by (job)(sum_over_time(jetty_threads_busy[5m]))
/ sum by (job)(count_over_time(jetty_threads_busy[5m]))
/ avg by (job) (jetty_threads_config_max)
```

<h3 id="scale-microservices-up">
  Scale Microservices Up
</h3>

The recommended load threshold for all microservices is 90%. After setting up your thresholds, monitor them manually, or use a metric monitoring tool such as [Prometheus](https://prometheus.io/docs/prometheus/latest/configuration/alerting_rules/) to define alerts at that threshold.

```
sum by (job)(sum_over_time(jetty_threads_busy[5m]))
/ sum by (job)(count_over_time(jetty_threads_busy[5m]))
/ avg by (job) (jetty_threads_config_max)
> 90
```

For more information on scaling up your environment, see [Add Nodes to an Existing High Availability Installation](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/install/distenv-ov#add-nodes-to-an-existing-high-availability-installation).

<h3 id="scale-microservices-down">
  Scale Microservices Down
</h3>

When monitoring microservices for scaling up, you define and set alerts around defined load thresholds for types of services.

In contrast, when you monitor services to scale them down, monitor free resources, the amount of free threads dedicated to the system. The recommended threshold is dedicate two times the resources of a single instance `(2 * resources)`.

Average over five minutes:

```
sum by instance_type (jetty_threads_config_max) - avg by instance_type (jetty_threads_busy) over 5m
```

In Prometheus:

```
(sum by (job) (jetty_threads_config_max) - (sum by (job)(sum_over_time(jetty_threads_busy[5m])) / sum by (job)(count_over_time(jetty_threads_busy[5m])))) / avg by (job) (jetty_threads_config_max)
```

<h2 id="self-service-analytics-system-metrics">
  Self-Service Analytics System Metrics
</h2>

Self-Service Analytics exposes metrics for discovering and monitoring Self-Service Analytics microservices. Discover system metrics using one of several available tools.

### Discovering Metrics

Connect to the composer-webservice actuator endpoints at: `http://[host_ip]:[port]/composer/actuator`.

Available endpoints include:

```yaml theme={null}
"prometheus": {
	"href": "http://127.0.0.1:8080/composer/actuator/prometheus",
	"templated": false
},
	"metrics-requiredMetricName": (
		"href": "http://127.0.0.1:8080/composer/actuator/metrics/{requiredMetricName)",
		"templated": true
	},
	"metrics":{
		"href": "http://127.0.0.:8080/composer/actuator/metrics",
		"templated": false
	},
```

Connect to all other microservices actuator endpoints at: `http://[host_ip]:[port]/actuator`.

Available endpoints include:

```json theme={null}
{
	"_links": {
		"self": {
			"http://127.0.0.1:8105/actuator",
			"templated": false
		},
		"metrics-sorted": (
			"href": "http://127.0.0.1:8105/actuator/metrics-sorted",
			"templated": false
		},
		"health-path": (
			"href": "http://127.0.0.1:8105/actuator/health/{*path}",
			"templated": true
		},
```

For a list of all metrics exposed by Composer, connect to: `http://[host_ip]:[port]/actuator/metrics`.

<h3 id="monitoring-microservices-prometheus">
  Monitoring Microservices: Prometheus
</h3>

Self-Service Analytics metrics data is formatted so you can access that data through a [Prometheus](https://github.com/prometheus) server. Navigate to the Prometheus composer-web actuator endpoint to see your data: `http://[host_ip]:[port]/composer/actuator/prometheus`.

Example Prometheus actuator response:

```
# HELP jvm_classes_unloaded_classes_total The total number of classes unloaded since the Java virtual machine has started execution
# TYPE jvm_classes_unloaded_classes_total counter jvm_classes_unloaded_classes_total{service_instance="Zoomdata:ip-127-0-0-0.ec2.internal:8080",} 63.0
# HELP process_files_max_files The maximum file descriptor count
# TYPE process_files_max_files gauge process_files_max_files_{service_instance="Zoomdata:ip-127-0-0-0:ec2.internal:8080",} 10240.0
# HELP jvm_gc_memory_allocated_bytes_total Incremented for an increase in the size of the young generation memory pool after one GC to be
# TYPE jvm_gc_memory_allocated_bytes_total counter jvm_gc_memory_allocated_bytes_total{service_instance="Zoomdata:ip-127-0-0-0.ec2.internal:8080",} 4.1484812288E10
# HELP websocket_sessions_active
# TYPE websocket_sessions_active gauge websocket_sessions_active{service_instance="Zoomdata:ip-127-0-0-0.ec2.internal.8080",} 2.0
# HELP zoomdata_sessions_count_last_minute
# TYPE zoomdata_sessions_count_last_minute gauge zoomdata_sessions_count_last_minute{service_instance=Zoomdata:ip-127-0-0-0.ec2.internal:8080",} 0.0
```

#### Configure Prometheus

Install Prometheus. See [https://prometheus.io/docs/prometheus/latest/getting\_started/](https://prometheus.io/docs/prometheus/latest/getting_started/) for more information.

Build your `prometheus.yml` as shown in the example here to connect to the composer-webservice. Replace `[username]`, `[password]` , `[host_ip]` and `[port]` with your appropriate values.

```yaml theme={null}
scrape_configs:
	- job_name: 'composer-web'
		metrics_path: 'composer/actuator/prometheus'
		scrape_interval: 5s
		basic_auth:
			username: [username]
			password: [password]
		static_configs:
		- targets: ['[host_ip]:[port]']

	- job_name: 'query-engine'
		metrics_path: 'actuator/prometheus'
		scrape_interval: 5s
		static_configs:
		- targets: ['[host_ip]:[port]']
```

<h3 id="monitoring-microservices-statsd-and-graphite">
  Monitoring Microservices: Statsd and Graphite
</h3>

You can also collect Self-Service Analytics metrics using the network daemon [statsd](https://github.com/statsd/statsd). This network daemon runs on the Node.js platform to listen for statistics sent over UDP or TCP and sends aggregate information to one or more backend services. Unlike Prometheus, statsd does not collect metric data from specific endpoints.

Use in conjunction with [Graphite](https://graphite.readthedocs.io/en/stable/overview.html) to store numeric time-series data and render data graphs on demand.

#### Setup and Configure Statsd and Graphite

Install [statsd](https://github.com/statsd/statsd#installation-and-configuration) and [Graphite](https://graphite.readthedocs.io/en/stable/install.html) to connect to and access system metrics.

Example of a Graphite dashboard with metrics collected by statsd:

<img src="https://mintcdn.com/insightsoftware/2cXq_sDOxrDVXUcv/simba-embedded-analytics/docs/self-service-analytics/26.3/images/config/21602-graphite-dashboard-example.png?fit=max&auto=format&n=2cXq_sDOxrDVXUcv&q=85&s=0187bae9a86b59f81d4e33fd8a86804f" alt="" width="1208" height="966" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/config/21602-graphite-dashboard-example.png" />

<h2 id="manage-self-service-analytics-microservices-using-the-command">
  Manage Self-Service Analytics Microservices Using the Command Line Utility
</h2>

You can use the `zdmanage` CLI command to manage the various microservices that are deployed in the Self-Service Analytics environment. This command line utility is automatically installed when installing your software using the automated installation script. This utility script wraps underlying UNIX commands to help you perform common management operations such as stopping and starting microservices.

### Prerequisites

To use the command line utility tool, you need root access.

### Using the Command Line Utility Tool

The `zdmanage` command line utility is located in the following directory:

```
/opt/zoomdata/bin/zdmanage
```

The `zdmanage` CLI command syntax is as follows:

```
zdmanage services <command> <service_name>
```

The following commands (`<command>`) are supported:

<table>
  <thead>
    <tr>
      <th>Command</th>
      <th>Action</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>`list`</td>
      <td>Displays all the microservices installed in your deployment.</td>
    </tr>

    <tr>
      <td>`status`</td>
      <td>Provides a status of all microservices in your Self-Service Analytics environment.</td>
    </tr>

    <tr>
      <td>`start`</td>

      <td>
        Starts microservices.

        <br />

        The order in which microservices should be restarted is described in [Microservice Startup Order](#microservice-startup-order).
      </td>
    </tr>

    <tr>
      <td>`stop`</td>
      <td>Stops microservices.</td>
    </tr>

    <tr>
      <td>`restart`</td>
      <td>Restarts microservices.</td>
    </tr>

    <tr>
      <td>`enable`</td>
      <td>Enables microservices automatically when the OS starts up.</td>
    </tr>

    <tr>
      <td>`disable`</td>
      <td>Shuts down microservices automatically when the OS starts up.</td>
    </tr>

    <tr>
      <td>`configure`</td>
      <td>Opens the specified Self-Service Analytics property file.</td>
    </tr>
  </tbody>
</table>

For `<service_name>`, specify the microservice name or `all` (to apply the command to all Self-Service Analytics microservices). For a complete list of microservices, see [Self-Service Analytics Microservice Name Reference](/simba-embedded-analytics/docs/self-service-analytics/26.3/get-started/arch-microservice#self-service-analytics-microservice-name-reference).

### Common Commands

Show all Self-Service Analytics microservices installed:

```bash theme={null}
sudo /opt/zoomdata/bin/zdmanage services list
```

Provide a status of all installed microservices:

```bash theme={null}
sudo /opt/zoomdata/bin/zdmanage services status all
```

Show the status of the web microservice:

```bash theme={null}
sudo /opt/zoomdata/bin/zdmanage services status zoomdata
```

Stop a specific microservice:

```bash theme={null}
sudo /opt/zoomdata/bin/zdmanage services stop [zoomdata-service_name]
```

<h2 id="manage-the-self-service-analytics-query-engine">
  Manage the Self-Service Analytics Query Engine
</h2>

The query engine is a stand-alone microservice within your Self-Service Analytics environment that processes visual queries. If you install or upgrade Self-Service Analytics [using the supplied installation script](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/install/install-ov#installation-steps), the query engine microservice is started automatically. If you install or upgrade Self-Service Analytics [manually](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/install/install-ov#install-self-service-analytics-manually), you must manually enable and start the query engine microservice.

### Configure the Query Engine

In your environment, the query engine is called `zoomdata-query-engine`. To configure and manage the microservices that the query engine executes and runs, you need to make changes to the `query-engine.properties` file. It contains properties that are specific to how the query engine operates within your environment.

The query engine also has a `query-engine.env` file and a `query-engine.jvm` file. You can edit these files to configure the following:

* To define the environment variables that are visible for the microservice, edit the `query-engine.env` file.
* To configure the JVM options that are used to start up Self-Service Analytics microservices, edit the `query-engine.jvm` file.

The default memory configurations give the query engine is 4 GB of heap memory. During microservice startup, the query engine consumes at least 4 GB of memory (plus some off heap memory). You can alter this using the following parameters in the query-engine.jvm file, i.e. by increasing to 6Gb.

```
-Xms6g
-Xmx6g
```

For information on editing configuration files, see [Edit a Configuration File](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/configure/config-mgmt-ov#edit-a-configuration-file). For information about query engine properties, see [Query Engine Properties](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/configure/properties-reference#query-engine-properties).
