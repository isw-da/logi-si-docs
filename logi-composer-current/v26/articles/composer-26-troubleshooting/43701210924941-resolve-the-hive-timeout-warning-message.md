---
title: "Resolve the Hive Timeout Warning Message"
id: 43701210924941
section: "Composer 26 Troubleshooting"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701210924941-Resolve-the-Hive-Timeout-Warning-Message
updated_at: 2026-05-29T14:09:36Z
---

# Resolve the Hive Timeout Warning Message

# Resolve the Hive Timeout Warning Message

## Troubleshooting

**Issue description:** A timeout warning message is displayed when you try to open a dashboard based on a Hive data source. This is possibly being caused by the configuration of the Hive server.

**Workaround:** If you are encountering timeout errors, you can first try to create or modify the settings in the Hive configuration file `edc-hive.properties`. See [Configure Composer](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43700989620365-Configure-Composer).

* Increase the timeout value that causes this exception to 2 minutes:

  datasource.time-limits.max-wait-time-sec=120
* If the Hive server has at least 64 GB storage and 16 cores, modify the values for the following parameters:

  datasource.connection-limits.max-idle=5  
  datasource.connection-limits.max-total=5
