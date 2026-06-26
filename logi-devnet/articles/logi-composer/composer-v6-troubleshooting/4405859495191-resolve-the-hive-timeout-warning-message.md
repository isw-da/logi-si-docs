---
title: "Resolve the Hive Timeout Warning Message"
id: 4405859495191
section: "Composer v6 Troubleshooting"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405859495191-Resolve-the-Hive-Timeout-Warning-Message
updated_at: 2021-09-21T01:29:50Z
---

# Resolve the Hive Timeout Warning Message

# Resolve the Hive Timeout Warning Message

## Troubleshooting

**Issue description:** A timeout warning message is displayed when you try to open a dashboard based on a Hive data source. This is possibly being caused by the configuration of the Hive server.

**Workaround:** If you are encountering timeout errors, you can first try to create or modify the settings in the Hive configuration file `edc-hive.properties`. See [*Configure Composer*](https://devnet.logianalytics.com/hc/en-us/articles/4405859144343-Configure-Composer).

* Increase the timeout value that causes this exception to 2 minutes:

  ```
  datasource.time-limits.max-wait-time-sec=120
  ```
* If the Hive server has at least 64 GB storage and 16 cores, modify the values for the following parameters:

  ```
  datasource.connection-limits.max-idle=5  
  datasource.connection-limits.max-total=5
  ```
