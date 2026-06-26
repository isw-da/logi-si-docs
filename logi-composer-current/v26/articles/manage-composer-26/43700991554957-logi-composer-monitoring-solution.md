---
title: "Logi Composer Monitoring Solution"
id: 43700991554957
section: "Manage Composer 26"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43700991554957-Logi-Composer-Monitoring-Solution
updated_at: 2026-05-29T14:11:38Z
---

# Logi Composer Monitoring Solution

# Logi Composer Monitoring Solution

Composer system metrics are published by all Composer microservices. While these measurements provide some visibility of the operating state of the services, the metric data becomes more useful once it can be stored and viewed. In order to provide Composer deployments with observability into the health and performance of the running system, you can use a monitoring solution. This topic describes an example monitoring solution that we make available for download with each release of Composer.

## Monitoring Solution Components

The monitoring solution consists of several components that are built up as layers.

* Generic operating and Composer specific metrics form the fixed foundation layer and are published in various formats.
* Subsequent layers provide storage and visualization capabilities to support further analysis.

**Note:** 
Subsequent components added to the metrics foundation can be implemented as provided in the monitoring solution package, or you can substitute them with preferred components that were already deployed.

![Microsystem and Metrics solution diagram.](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46242772563213 "Composer Monitoring")

The example solution is built using the following industry-standard, open-source tools:

1. Prometheus service collects and stores metrics in a time series database.
2. Grafana supports further analysis by providing visualization of stored metrics on pre-built application-specific dashboards.

We provide these components in a tarball containing docker-compose files. We include the configuration files required for monitoring Composer services, along with ready to use dashboards.

## Downloading and Installing the Solution Package

1. Contact your ComposerCustomer Support representative to download the Solution Package: [Customer Support.](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701072313613-Contact-Technical-Support)
2. When you get the tarball, extract the tarball to the directory you create.

   mkdir composer-monitoring
   tar -xvf composer-monitoring-X.Y.Z.tar.gz -C composer-monitoring
3. Open the READ.me file and follow the directions included.
