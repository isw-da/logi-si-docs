---
title: " Screenshot Service Configuration"
id: 34933040091149
section: "Install, Upgrade, and Remove Composer 25"
product: "Logi Composer v25"
url: https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933040091149--Screenshot-Service-Configuration
updated_at: 2026-05-26T22:07:35Z
---

#  Screenshot Service Configuration

# Screenshot Service Configuration

The [Screenshot Service](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933044663181-Set-Up-the-Screenshot-Microservice) component is an optional component for , disabled by default. Enable if you are going to [schedule Dashboard Reports](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932793437325-About-Scheduled-Dashboard-Reports).

To enable, add the following configuration to your `values.yaml`:

screenshotService:
enabled: true

**Note:** 
Find more information about Composer and Kubernetes here: [Running Composer in Kubernetes](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933085585677-Running-Composer-in-Kubernetes).
