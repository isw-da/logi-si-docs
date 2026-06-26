---
title: "Ingress Configuration"
id: 34933067333773
section: "Install, Upgrade, and Remove Composer 25"
product: "Logi Composer v25"
url: https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933067333773-Ingress-Configuration
updated_at: 2026-05-26T22:07:39Z
---

# Ingress Configuration

# Ingress Configuration

By default, the chart creates an [Ingress](https://kubernetes.io/docs/concepts/services-networking/ingress/) resource with the name `default-ingress`. Also, it relies on the [ingress-nginx](https://github.com/kubernetes/ingress-nginx) sub-chart to install an [Ingress Controller](https://kubernetes.io/docs/concepts/services-networking/ingress-controllers/) with the default name `nginx`. This might not work with your existing Ingress Controller. To resolve this issue, override the config for the ComposerIngress in your `values.yaml`:

ingress:
enabled: true
installController: false
className: <your-ingress-controller-name>
ingressName: default-ingress

This config disables installation of the `nginx` Ingress Controller and points Composer’s Ingress to your controller. If such a config is still not versatile enough for your needs, disable both the Ingress and Ingress Controller and create your own Ingress.

**Note:** 
Find more information about Composer and Kubernetes here: [Running Composer in Kubernetes](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933085585677-Running-Composer-in-Kubernetes).
