---
title: "Connector Graceful Shutdown"
id: 43701055604621
section: "Connect to Data in Composer 26"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701055604621-Connector-Graceful-Shutdown
updated_at: 2026-05-29T14:07:33Z
---

# Connector Graceful Shutdown

# Connector Graceful Shutdown

Composer supports the graceful shutdown of connectors. When a connector is shut down, it gracefully completes queries that are in-flight and notifies clients that it is terminating.

Three connector properties in each [connector property file](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43700992050061-Connector-Properties-and-Property-Files) support graceful shutdown:

* `connector.graceful.shutdown.enabled` indicates whether or not graceful shutdown processing should occur. Valid values are `true` (perform graceful shutdown processing) or `false` (do not perform graceful shutdown processing). The default is `true`.
* `connector.graceful.shutdown.event.propagation.timeout-sec` specifies how long (in seconds) the connector will wait to allow clients to receive the information that it is out of service. The default is 35 seconds.
* `connector.graceful.shutdown.force.kill.timeout-sec` specifies the maximum number of seconds that the connector will wait for the number of its active tasks to reach zero. The default is 30 seconds. When this time has elapsed, the connector will stop.
