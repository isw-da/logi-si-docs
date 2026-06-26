---
title: "SystemCacheSetting"
id: 4415492888983
section: "System Reference"
category: "Izenda"
url: https://devnet.logianalytics.com/hc/en-us/articles/4415492888983-SystemCacheSetting
updated_at: 2021-12-10T03:09:50Z
---

# SystemCacheSetting

# SystemCacheSetting

| Field | NULL | Description | Note |
| --- | --- | --- | --- |
| **timeToLive**  integer |  | Define the lifespan in second for system caches |  |
| **evictionInterval**  integer |  | Define the inteval to clear expired system caches |  |
| **defaultEvictionInterval**  integer | Y | Default value of `EvictionInterval` |  |
| **defaultTimeToLive**  integer | Y | Default value of `timeToLive` |  |

**Sample**:

```
{"timeToLive":60,"evictionInterval":3600,"defaultEvictionInterval":3600,"defaultTimeToLive":60}
```
