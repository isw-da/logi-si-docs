---
title: "Horizontal Pod Autoscaling"
id: 34933048607885
section: "Install, Upgrade, and Remove Composer 25"
product: "Logi Composer v25"
url: https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933048607885-Horizontal-Pod-Autoscaling
updated_at: 2026-05-26T22:07:37Z
---

# Horizontal Pod Autoscaling

# Horizontal Pod Autoscaling

Enable the Horizontal Pod Autoscaler in your environment with a new or existing instance of Prometheus and Prometheus Adapter and our custom metrics for Kubernetes to adjust the number of replicas used, scaling up or down depending on the workload.

This topic covers:

* [Overview - About HPA](#Overview)
* [Composer's HPA Metrics](#'s)
* [HPA Configuration](#HPA)

  + [Enable HPA](#Enable)
  + [Global and Per-Service HPA Configuration](#Global)
  + [Additional Properties](#Addition)
* [Caveats of the Default Config](#Caveats)
* [Cluster-wide Prometheus and Prometheus Adapter](#Cluster-)

## Overview - About HPA

The [Horizontal Pod Autoscaler](https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/) (HPA) is a Kubernetes feature that dynamically adjusts the number of replicas (pods) in a deployment or replica set based on the observed metrics. It helps maintain optimal resource utilization and ensures that the application can handle varying levels of workload efficiently. HPA continuously monitors the specified metrics and automatically scales the number of pods up or down to meet the desired performance targets.

The Composer HPA implementation works by utilizing [custom metrics](https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/#scaling-on-custom-metrics) provided by [Prometheus Adapter](https://github.com/kubernetes-sigs/prometheus-adapter) and [Prometheus](https://prometheus.io/). Prometheus collects application metrics from each pod. Prometheus Adapter makes these metrics available to the Horizontal Pod Autoscaler, which uses them to make scaling decisions.

## Composer's HPA Metrics

Three custom metrics are utilized in Composer environments:

* `cpuAverageUtilization` - CPU average utilization measures the average CPU utilization of the application over a specific period. It provides insights into how much CPU capacity the application requires to handle its workload. The default value is 80%.
* `memoryAverageUtilization` - JVM heap average utilization monitors the average utilization of Java Virtual Machine (JVM) heap memory. It measures the proportion of heap memory consumed by the application over a defined interval. HPA utilizes this metric to scale the application based on memory consumption, preventing memory-related issues and optimizing resource allocation. The default value is 90%.
* `threadsQueueAverageSize` - The number of threads in the queue to the application reflects the number of HTTP requests waiting in the application's processing queue. This metric provides visibility into the application's ability to handle incoming requests promptly. HPA automatically adjusts the number of replicas to ensure sufficient processing capacity and minimize request queuing. The default value is 400 requests in the queue.

These metrics work in conjunction to ensure optimal performance and resource utilization.

## HPA Configuration

HPA is disabled by default. Once you've enabled it, it’s preconfigured with reasonable defaults.

### Enable HPA

Before you enable HPA, see [Caveats of the Default Config](#Caveats).

1. Add the following to your `values.yaml`:

   hpa:
   enabled: true
2. Install a [new helm chart release](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933053804557-Helm-Chart-for-Composer#Customiz) or [upgrade](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933053804557-Helm-Chart-for-Composer#Upgrade) an existing one.

   **Note:** 
   When you enable HPA, 8GB of additional storage for Prometheus is required if you install it using the Helm chart.

### Global and Per-Service HPA Configuration

All Composer HPA configuration properties can be specified on the global and per-service levels. The service-level configuration has higher priority and overrides the global one.

For example, here are the steps to change the number of replicas on the global level:

1. Set the value of the minimum and/or maximum number of replicas in your`values.yaml`:

   hpa:
   minReplicas: 2 *# default is 1*
   maxReplicas: 4 *# default is 3*
2. Install a [new helm chart release](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933053804557-Helm-Chart-for-Composer#Customiz) or [upgrade](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933053804557-Helm-Chart-for-Composer#Upgrade) an existing one.

   This configuration will be applied to all Composer services.

**Note:** 
The default number of maximum replicas is 3. A higher value requires a corresponding license.

HPA can also be configured on the per-service level, for example:

hpa:
enabled: true
zoomdataWeb:
hpa:
maxReplicas: 5
dataWriter:
hpa:
enabled: false

In the above example, HPA is enabled for all services except for the Data Writer. The maximum number of replicas for Zoomdata Web is increased to 5 and defaults to 3 for all other services.

### Additional Properties

The full list of configuration properties can be found in the chart values under the hpa object:

helm show values composer/composer

While enabling HPA and customizing the minimum and maximum replicas is a common practice, it's important to exercise caution when modifying other properties. Many properties are preconfigured for optimal performance. Modifying these properties without a clear understanding of their implications may lead to unexpected issues or degraded performance.

## Caveats of the Default Config

By default, when you enable HPA for Composer, Composer’s helm chart will try and install an instance of Prometheus and Prometheus Adapter into the namespace of Composer’s deployment. This is not a best practice, but rather a convenient getting-started setup for those who are new to Kubernetes and who have no other things running in their clusters.

The limitation is that only one service can implement [Kubernetes Custom Metrics API](https://github.com/kubernetes/design-proposals-archive/blob/main/instrumentation/custom-metrics-api.md). In our case it’s Prometheus Adapter. By installing Prometheus Adapter from our helm chart it will come pre-configured with Composer-specific rules and it’ll be difficult to re-use it in other Kubernetes applications. Also, you won’t be able to install another instance of the Composer application or another Prometheus Adapter into the same cluster. The recommended approach is to have a [cluster-wide Prometheus and Prometheus Adapter](https://insightsoftware.atlassian.net/wiki/spaces/CDOC/pages/edit-v2/15974040097#Cluster-wide-Prometheus-and-Prometheus-Adapter) that can serve all the HPAs in the cluster.

## Cluster-wide Prometheus and Prometheus Adapter

Installing an instance of Prometheus and Prometheus Adapter as part of the Composer’s deployment is not a best practice. For a production deployment, we recommend that you deploy a cluster-wide instance of Prometheus and Prometheus Adapter and refer to them from different Composer deployments.

**Note:** 
If you already have Prometheus and the Prometheus Adapter installed and configured you’ll only need to add Composer rules to your Prometheus Adapter configuration (step 3) and disable Prometheus and Prometheus Adapter installation in Composer’s helm chart (steps 4 and 5).

Installing and configuring Prometheus and Prometheus Adapter:

1. Create a `monitoring` namespace in your Kubernetes cluster:

   kubectl create namespace monitoring
2. Install [Prometheus](https://artifacthub.io/packages/helm/prometheus-community/prometheus) into the `monitoring` namespace. We don’t require any special configurations for Prometheus, all our pods will be automatically discovered and scraped by Prometheus with the default configuration:

   helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
   helm repo update
   helm install prometheus prometheus-community/prometheus -n monitoring
3. Install the [Prometheus Adapter](https://artifacthub.io/packages/helm/prometheus-community/prometheus-adapter) into the `monitoring` namespace. The Prometheus Adapter requires two pieces of configuration:

* The URL and port of the Prometheus server. If they are installed in the same namespace (for Composer, the `monitoring`namespace), it’ll be simply `http://prometheus-server:80`.
* The rules for converting Composerapplication metrics coming from Prometheus to custom Kubernetes metrics required by the HPA configuration. Copy the following snippet into a file called `prometheus-adapter.yml`:

  prometheus-adapter:
  prometheus:
  url: http://prometheus-server
  port: 80
  rules:
  custom:
  - seriesQuery: '{\_\_name\_\_=~"jvm\_memory\_(used|max)\_bytes",area="heap"}'
  resources:
  overrides:
  namespace: { resource: "namespace" }
  pod: { resource: "pod" }
  name:
  matches: '^jvm\_memory\_(used|max)\_bytes$'
  as: "jvm\_heap\_usage\_percent"
  metricsQuery: 'round(sum(jvm\_memory\_used\_bytes{area="heap", <<.LabelMatchers>>}) by (<<.GroupBy>>) \* 100 / sum(jvm\_memory\_max\_bytes{area="heap", <<.LabelMatchers>>}) by ((<<.GroupBy>>))'
  - seriesQuery: 'system\_cpu\_usage'
  resources:
  overrides:
  namespace: { resource: "namespace" }
  pod: { resource: "pod" }
  name:
  matches: 'system\_cpu\_usage'
  as: 'cpu\_usage\_percent'
  metricsQuery: 'round(sum(<<.Series>>{<<.LabelMatchers>>}) by (<<.GroupBy>>) \* 100)'
  - seriesQuery: 'jetty\_threads\_jobs'
  resources:
  overrides:
  namespace: { resource: "namespace" }
  pod: { resource: "pod" }
  name:
  matches: 'jetty\_threads\_jobs'
  as: 'jetty\_threads\_jobs'
  metricsQuery: 'sum(<<.Series>>{<<.LabelMatchers>>}) by (<<.GroupBy>>)'

  Run the following commands to install the Prometheus Adapter into the `monitoring` namespace:

  helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
  helm repo update
  helm install prometheus-adapter prometheus-community/prometheus-adapter -f prometheus-adapter.yml -n monitoring

4. Update the Composer helm chart configuration file `values.yaml`:

   # Make sure HPA is enabled
   hpa:
   enabled: true
   # Disable installation of Prometheus
   prometheus:
   enabled: false
   # Disable installation of Prometheus Adapter
   prometheus-adapter:
   enabled: false
5. Install a [new helm chart release](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933053804557-Helm-Chart-for-Composer#Customiz) or [upgrade](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933053804557-Helm-Chart-for-Composer#Upgrade) an existing one.

**Note:** 
Find more information about Composer and Kubernetes here: [Running Composer in Kubernetes](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933085585677-Running-Composer-in-Kubernetes).
