---
title: " Screenshot Service Configuration"
id: 43701121246989
section: "Install, Upgrade, and Remove Composer 26"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701121246989--Screenshot-Service-Configuration
updated_at: 2026-05-29T14:08:53Z
---

#  Screenshot Service Configuration

# Screenshot Service Configuration

The [Screenshot Service](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701073104013-Set-Up-the-Screenshot-Microservice) component is an optional component for , disabled by default. Enable if you are going to [schedule Dashboard Reports](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43700998266509-About-Scheduled-Dashboard-Reports).

To enable, add the following configuration to your `values.yaml`:

screenshotService:
enabled: true

**Note:** 
Find more information about Composer and Kubernetes here: [Running Composer in Kubernetes](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701110924173-Running-Composer-in-Kubernetes).
