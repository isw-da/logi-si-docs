---
title: "Composer System Metrics"
id: 34933022064781
section: "Manage Composer 25"
product: "Logi Composer v25"
url: https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933022064781-Composer-System-Metrics
updated_at: 2026-05-26T22:09:30Z
---

# Composer System Metrics

# ComposerSystem Metrics

Composer exposes metrics for discovering and monitoring Composer microservices. Discover system metrics using one of several available tools.

## Discovering Metrics

Connect to the composer-webservice actuator endpoints at: `http://[host_ip]:[port]/composer/actuator`.

Available endpoints include:

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

Connect to all other microservices actuator endpoints at: `http://[host_ip]:[port]/actuator`.

Available endpoints include:

{
"\_links": {
"self": {
"http://127.0.0.1:8105/actuator",
"templated": false
},
"metrics-sorted": (
"href": "http://127.0.0.1:8105/actuator/metrics-sorted",
"templated": false
},
"health-path": (
"href": "http://127.0.0.1:8105/actuator/health/{\*path}",
"templated": true
},

For a list of all metrics exposed by Composer, connect to: `http://[host_ip]:[port]/actuator/metrics`.

## Monitoring Microservices: Prometheus

Composer metrics data is formatted so you can access that data through a [Prometheus](https://github.com/prometheus "Prometheus information") server. Navigate to the Prometheus composer-web actuator endpoint to see your data: `http://[host_ip]:[port]/composer/actuator/prometheus`.

Example Prometheus actuator response:

# HELP jvm\_classes\_unloaded\_classes\_total The total number of classes unloaded since the Java virtual machine has started execution
# TYPE jvm\_classes\_unloaded\_classes\_total counter jvm\_classes\_unloaded\_classes\_total{service\_instance="Zoomdata:ip-127-0-0-0.ec2.internal:8080",} 63.0
# HELP process\_files\_max\_files The maximum file descriptor count
# TYPE process\_files\_max\_files gauge process\_files\_max\_files\_{service\_instance="Zoomdata:ip-127-0-0-0:ec2.internal:8080",} 10240.0
# HELP jvm\_gc\_memory\_allocated\_bytes\_total Incremented for an increase in the size of the young generation memory pool after one GC to be
# TYPE jvm\_gc\_memory\_allocated\_bytes\_total counter jvm\_gc\_memory\_allocated\_bytes\_total{service\_instance="Zoomdata:ip-127-0-0-0.ec2.internal:8080",} 4.1484812288E10
# HELP websocket\_sessions\_active
# TYPE websocket\_sessions\_active gauge websocket\_sessions\_active{service\_instance="Zoomdata:ip-127-0-0-0.ec2.internal.8080",} 2.0
# HELP zoomdata\_sessions\_count\_last\_minute
# TYPE zoomdata\_sessions\_count\_last\_minute gauge zoomdata\_sessions\_count\_last\_minute{service\_instance=Zoomdata:ip-127-0-0-0.ec2.internal:8080",} 0.0

### Configure Prometheus

Install Prometheus. See [https://prometheus.io/docs/prometheus/latest/getting\_started/](https://prometheus.io/docs/prometheus/latest/getting_started/ "Prometheus documentation link") for more information.

Build your `prometheus.yml` as shown in the example here to connect to the composer-webservice. Replace `[username]`, `[password]` , `[host_ip]` and `[port]` with your appropriate values.

scrape\_configs:
- job\_name: 'composer-web'
metrics\_path: 'composer/actuator/prometheus'
scrape\_interval: 5s
basic\_auth:
username: [username]
password: [password]
static\_configs:
- targets: ['[host\_ip]:[port]']
- job\_name: 'query-engine'
metrics\_path: 'actuator/prometheus'
scrape\_interval: 5s
static\_configs:
- targets: ['[host\_ip]:[port]']

## Monitoring Microservices: Statsd and Graphite

You can also collect Composer metrics using the network daemon [statsd](https://github.com/statsd/statsd "statsd information"). This network daemon runs on the Node.js platform to listen for statistics sent over UDP or TCP and sends aggregate information to one or more backend services. Unlike Prometheus, statsd does not collect metric data from specific endpoints.

Use in conjunction with [Graphite](https://graphite.readthedocs.io/en/stable/overview.html "Graphie information") to store numeric time-series data and render data graphs on demand.

### Setup and Configure Statsd and Graphite

Install [statsd](https://github.com/statsd/statsd#installation-and-configuration) and [Graphite](https://graphite.readthedocs.io/en/stable/install.html) to connect to and access system metrics.

Example of a Graphite dashboard with metrics collected by statsd:

![](https://logi-composer-v25.insightsoftware.com/hc/article_attachments/46167130236685)
