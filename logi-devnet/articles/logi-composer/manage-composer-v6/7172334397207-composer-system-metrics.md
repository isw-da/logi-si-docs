---
title: "Composer System Metrics"
id: 7172334397207
section: "Manage Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/7172334397207-Composer-System-Metrics
updated_at: 2022-07-01T18:49:28Z
---

# Composer System Metrics

# Composer System Metrics

Composer exposes metrics for discovering and monitoring Composer microservices. Discover system metrics using one of several available tools.

## Discovering Metrics

Connect to the composer-webservice actuator endpoints at: `http://[host_ip]:[port]/composer/actuator`.

Available endpoints include:

```
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

```
{
	"_links": {
		"self": { 
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

## Monitoring Microservices: Prometheus

Composer metrics data is formatted so you can access that data through a [Prometheus](https://github.com/prometheus "Prometheus information") server. Navigate to the Prometheus composer-web actuator endpoint to see your data: `http://[host_ip]:[port]/composer/actuator/prometheus`.

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

### Configure Prometheus

Install Prometheus. See [https://prometheus.io/docs/prometheus/latest/getting\_started/](https://prometheus.io/docs/prometheus/latest/getting_started/ "Prometheus documentation link") for more information.

Build your `prometheus.yml` as shown in the example here to connect to the composer-webservice. Replace `[username]`, `[password]` , `[host_ip]` and `[port]` with your appropriate values.

```
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

## Monitoring Microservices: Statsd and Graphite

You can also collect Composer metrics using the network daemon [statsd](https://github.com/statsd/statsd "statsd information"). This network daemon runs on the Node.js platform to listen for statistics sent over UDP or TCP and sends aggregate information to one or more backend services. Unlike Prometheus, statsd does not collect metric data from specific endpoints.

Use in conjunction with [Graphite](https://graphite.readthedocs.io/en/stable/overview.html "Graphie information") to store numeric time-series data and render data graphs on demand.

### Setup and Configure Statsd and Graphite

Install [statsd](https://github.com/statsd/statsd#installation-and-configuration) and [Graphite](https://graphite.readthedocs.io/en/stable/install.html) to connect to and access system metrics.

Example of a Graphite dashboard with metrics collected by statsd:

![](https://devnet.logianalytics.com/hc/article_attachments/6726420288663/21602-graphite-dashboard-example.png)
