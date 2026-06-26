---
title: "Ingress Configuration"
id: 43701121221389
section: "Install, Upgrade, and Remove Composer 26"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701121221389-Ingress-Configuration
updated_at: 2026-05-29T14:08:53Z
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
Find more information about Composer and Kubernetes here: [Running Composer in Kubernetes](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701110924173-Running-Composer-in-Kubernetes).
