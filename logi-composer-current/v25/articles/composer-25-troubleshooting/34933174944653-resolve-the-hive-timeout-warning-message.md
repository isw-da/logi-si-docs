---
title: "Resolve the Hive Timeout Warning Message"
id: 34933174944653
section: "Composer 25 Troubleshooting"
product: "Logi Composer v25"
url: https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933174944653-Resolve-the-Hive-Timeout-Warning-Message
updated_at: 2026-05-26T22:08:29Z
---

# Resolve the Hive Timeout Warning Message

# Resolve the Hive Timeout Warning Message

## Troubleshooting

**Issue description:** A timeout warning message is displayed when you try to open a dashboard based on a Hive data source. This is possibly being caused by the configuration of the Hive server.

**Workaround:** If you are encountering timeout errors, you can first try to create or modify the settings in the Hive configuration file `edc-hive.properties`. See [Configure Composer](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932701121421-Configure-Composer).

* Increase the timeout value that causes this exception to 2 minutes:

  datasource.time-limits.max-wait-time-sec=120
* If the Hive server has at least 64 GB storage and 16 cores, modify the values for the following parameters:

  datasource.connection-limits.max-idle=5  
  datasource.connection-limits.max-total=5
