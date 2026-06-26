---
title: "SystemCacheSetting"
id: 12528283227031
section: "System Reference"
category: "Izenda"
url: https://devnet.logianalytics.com/hc/en-us/articles/12528283227031-SystemCacheSetting
updated_at: 2023-02-19T08:37:42Z
---

# SystemCacheSetting

[Skip To Main Content](#)

Account

Settings

---

Logout

* placeholder

Account

Settings

---

Logout

Filter: 

* All Files

Submit Search

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
