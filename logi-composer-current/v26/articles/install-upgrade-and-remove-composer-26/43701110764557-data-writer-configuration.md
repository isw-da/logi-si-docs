---
title: "Data Writer Configuration"
id: 43701110764557
section: "Install, Upgrade, and Remove Composer 26"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701110764557-Data-Writer-Configuration
updated_at: 2026-05-29T14:08:52Z
---

# Data Writer Configuration

# Data Writer Configuration

The [Data Writer](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701106979981-Data-Writer-Microservice) component is an optional component that is enabled by default. It’s required by the following Composerfeatures:

1. [Uploading flat files](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701044052621-Manage-File-Uploads) (e.g. CSV, JSON) for further analysis.
2. Landing streaming data via [Upload API](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701044052621-Manage-File-Uploads#Working).
3. Performing multipass and multisource filtering of your data with the help of [Keysets](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701105959565-Use-Keysets).
4. Tracking end users' access to data via [User Auditing](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701124523021-User-Auditing).

If none of these features are required, add the following configuration to your `values.yaml` to disable it:

dataWriter:
enabled: false

Then install a [new helm chart release](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701110873869-Helm-Chart-for-Composer#Customiz) or [upgrade](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701110873869-Helm-Chart-for-Composer#Upgrade) an existing one.

**Note:** 
Find more information about Composer and Kubernetes here: [Running Composer in Kubernetes](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701110924173-Running-Composer-in-Kubernetes).
