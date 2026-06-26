---
title: "Scaling Configuration"
id: 43701106082701
section: "Install, Upgrade, and Remove Composer 26"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701106082701-Scaling-Configuration
updated_at: 2026-05-29T14:08:53Z
---

# Scaling Configuration

# Scaling Configuration

When deployed in Kubernetes, Logi Composer supports both vertical (adding resources) and horizontal (adding pods) scaling.

This topic covers:

* [Horizontal Autoscaling](#Horizont)
* [Manual Scaling](#Manual)

  + [Manual Horizontal Scaling](#Manual2)
  + [Manual Vertical Scaling](#Manual3)

## Horizontal Autoscaling

By default, the Helm chart comes with horizontal autoscaling disabled. Follow this guide to learn more about [Horizontal Pod Autoscaling](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701121297421-Horizontal-Pod-Autoscaling) and how to enable it.

## Manual Scaling

If you decide not to enable autoscaling you can still scale the resources/pods manually.

### Manual Horizontal Scaling

To set the number of replicas for a Composer service such as `zoomdataWeb` do the following:

1. Add the desired number of replicas to the `values.yaml`:

   zoomdataWeb:
   replicaCount: 2 *# default is 1*
2. Install a [new helm chart release](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701110873869-Helm-Chart-for-Composer#Customiz) or [upgrade](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701110873869-Helm-Chart-for-Composer#Upgrade) an existing one.

   **Important:** 
   Don’t use `kubectl` to change the number of replicas for Logi Composer pods. These changes will be overwritten on the next usage of Helm.

### Manual Vertical Scaling

Configure each [pod’s resource](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/) manually in the corresponding block of the `values.yaml` file, but it's always recommended to prefer horizontal over vertical scaling. Improper change of the resources may lead to application failure on startup or instability during the operation.

Since Logi Composer consists of a number of Java-based microservices, apart from generic pod [resource types](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/) (i.e. CPU and memory), Logi Composer services also expose properties for configuring application JVM memory: `heapSizeMin` and `heapSizeMax`. For example, here are the resource-related defaults for the `zoomdataWeb`service:

zoomdataWeb:
*# Initial JVM heap size*
heapSizeMin: "4G"
*# Maximum JVM heap size*
heapSizeMax: "4G"
resources:
limits:
memory: "6Gi"
requests:
cpu: "3.5"
memory: "6Gi"

If you decide to customize these properties, please follow these general recommendations:

1. Memory request and limit should be the same.
2. Memory request should be at least 25% bigger than JVM's maximum heap size to account for non-heap memory consumed by Java applications.
3. CPU limit is empty.

**Note:** 
Find more information about Composer and Kubernetes here: [Running Composer in Kubernetes](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701110924173-Running-Composer-in-Kubernetes).
