---
title: "Scaling Composer Microservices"
id: 34933050010381
section: "Manage Composer 25"
product: "Logi Composer v25"
url: https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933050010381-Scaling-Composer-Microservices
updated_at: 2026-05-26T22:07:42Z
---

# Scaling Composer Microservices

# Scaling Composer Microservices

Composer microservices allow you to scale your Composer installation, giving you expanded performance gains. As you roll out your microservices changes, you'll need to:

* [Estimate User and Microservice Loads](#Estimate "Estimate User and Microservice Loads details")
* [Add or Remove Nodes in a High Availability Environment](#Add "Add or Remove Nodes in a High Availability Environment details")
* [Configure Throughput for Microservices](#Configur "Configure Throughput for Microservices
   details")
* [Load Monitor Microservices](#Load "Load Monitor Microservices details")
* [Scale  Microservices Up](#Scale "Scale  Microservices Up details")
* [Scale Microservices Down](#Scale2 "Scale Microservices Down
   details")

All microservices, except composer web, support horizontal scaling. Composer web supports vertical scaling only.

## Estimate User and Microservice Loads

The load used by each microservice depends on the type of interactions your users have while using Composer. Some actions load only the composer web component, while others may load multiple components.

Some examples of actions that load microservices are included in the table below.

| Action | Microservices Loaded |
| --- | --- |
| Open the home page | composer web |
| Open a dashboard | composer web, connector, query engine |
| Open the visual Gallery | composer web |
| Create a source | composer web, connector, query engine |
| Create an uploaded source | composer web, connector, data writer, query engine |
| Upload new data via API | composer web, data writer |
| Execute scheduled dashboard report | composer web, connector, screenshot service, query engine |
| Live mode | composer web, connector, query engine |

**Note:** 
Horizontal scaling up of a microservice doesn't provide doubled performance gains due to sharing of PostreSQL resources and overlapping of microservices.

Start your scale planning based on an approximate number of services and expected number of users. See [Server Size Guidelines](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933032055437-Server-Size-Guidelines) for more information on services and user estimation.

## Add or Remove Nodes in a High Availability Environment

To scale a microservice up or down, you may need to [Add Nodes to an Existing High Availability Installation](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933016586765-Add-Nodes-to-an-Existing-High-Availability-Installation) or [Remove Nodes from a High Availability Environment](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932982260877-Remove-Nodes-from-a-High-Availability-Environment). Before you add or remove nodes, you should understand the actual load on your microservices to make the decision of scaling up or down. See [Composer System Metrics](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933022064781-Composer-System-Metrics).

## Configure Throughput for Microservices

All microservices have a configuration property, `server.jetty.max-threads`, you can use to limit throughput. Once configured, you can more accurately monitor the load on each microservice.

Set your estimated concurrent users for each service at +20%, based on your calculations made using [Server Size Guidelines](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933032055437-Server-Size-Guidelines). To manage configuration properties of `server.jetty.max-threads`, see [Configure and Start the Configuration Microservice](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933169035789-Configure-and-Start-the-Configuration-Microservice).

For example, if you have three instances of the query engine microservice and you expect 150 concurrent users, each instance is expected to handle 50 concurrent users. To accommodate this demand, set `server.jetty.max-threads` to (`60 = 150 / 3 & 120%`) for each instance of query engine.

**Note:** Composer v7.1 and earlier use the property `jetty.threadPool.maxThreads` to limit throughput for the composer web and query engine microservices.

## Load Monitor Microservices

With throughput defined for your microservices, you can measure their use to decide what services to scale up or scale down.

Composer microservices exposes several different metrics to help you understand the current load on each service. The main outputs to monitor include:

* `jetty_threads_busy` shows a current count of concurrent users.
* `jetty_threads_config_max` shows the maximum allowed concurrent users. This should match the value you set in `server.jetty.max-threads`.

These show a moment in time, which can vary depending on use spikes that may not actually require scaling up or down. Smooth out the data by looking at a specific length of time, such as five minutes, and monitor the average load across all instances of the same microservice.

Average over five minutes:

avg by instance\_type (jetty\_threads\_busy) over 5m / avg by instance\_type (jetty\_threads\_config\_max)

In Prometheus:

sum by (job)(sum\_over\_time(jetty\_threads\_busy[5m]))
/ sum by (job)(count\_over\_time(jetty\_threads\_busy[5m]))
/ avg by (job) (jetty\_threads\_config\_max)

## Scale  Microservices Up

The recommended load threshold for all microservices is 90%. After setting up your thresholds, monitor them manually, or use a metric monitoring tool such as [Prometheus](https://prometheus.io/docs/prometheus/latest/configuration/alerting_rules/) to define alerts at that threshold.

sum by (job)(sum\_over\_time(jetty\_threads\_busy[5m]))
/ sum by (job)(count\_over\_time(jetty\_threads\_busy[5m]))
/ avg by (job) (jetty\_threads\_config\_max)
> 90

For more information on scaling up your environment, see [Add Nodes to an Existing High Availability Installation](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933016586765-Add-Nodes-to-an-Existing-High-Availability-Installation).

**Note:** 
Composer-Web does not support horizontal scaling, only vertical scaling. Increase machine resources to accommodate your needs. Configure `server.jetty.max-threads` or `jetty.threadPool.maxThreads` for Composer v7.1 and earlier after increasing machine resources.

## Scale Microservices Down

When monitoring microservices for scaling up, you define and set alerts around defined load thresholds for types of services.

In contrast, when you monitor services to scale them down, monitor free resources, the amount of free threads dedicated to the system. The recommended threshold is dedicate two times the resources of a single instance `(2 * resources)`.

Average over five minutes:

sum by instance\_type (jetty\_threads\_config\_max) - avg by instance\_type (jetty\_threads\_busy) over 5m

In Prometheus:

(sum by (job) (jetty\_threads\_config\_max) - (sum by (job)(sum\_over\_time(jetty\_threads\_busy[5m])) / sum by (job)(count\_over\_time(jetty\_threads\_busy[5m])))) / avg by (job) (jetty\_threads\_config\_max) > 2
