---
title: "Data Writer Configuration"
id: 34933024004237
section: "Install, Upgrade, and Remove Composer 25"
product: "Logi Composer v25"
url: https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933024004237-Data-Writer-Configuration
updated_at: 2026-05-26T22:07:31Z
---

# Data Writer Configuration

# Data Writer Configuration

The [Data Writer](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933071011725-Data-Writer-Microservice) component is an optional component that is enabled by default. It’s required by the following Composerfeatures:

1. [Uploading flat files](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932721668365-Manage-File-Uploads) (e.g. CSV, JSON) for further analysis.
2. Landing streaming data via [Upload API](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932721668365-Manage-File-Uploads#Working).
3. Performing multipass and multisource filtering of your data with the help of [Keysets](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933047406605-Use-Keysets).
4. Tracking end users' access to data via [User Auditing](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933076803085-User-Auditing).

If none of these features are required, add the following configuration to your `values.yaml` to disable it:

dataWriter:
enabled: false

Then install a [new helm chart release](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933053804557-Helm-Chart-for-Composer#Customiz) or [upgrade](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933053804557-Helm-Chart-for-Composer#Upgrade) an existing one.

**Note:** 
Find more information about Composer and Kubernetes here: [Running Composer in Kubernetes](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933085585677-Running-Composer-in-Kubernetes).
