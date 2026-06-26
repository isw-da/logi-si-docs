---
title: "DataCacheSetting"
id: 12528296898711
section: "System Reference"
category: "Izenda"
url: https://devnet.logianalytics.com/hc/en-us/articles/12528296898711-DataCacheSetting
updated_at: 2023-02-19T08:36:23Z
---

# DataCacheSetting

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

# DataCacheSetting

| Field | NULL | Description | Note |
| --- | --- | --- | --- |
| **isEnableDataCache**  boolean |  | Whether data cache is enable or not |  |
| **timeToLive**  integer |  | Define the lifespan in second for data caches |  |
| **evictionInterval**  integer |  | Define the inteval to clear expired data caches |  |
| **refreshInterval**  integer |  | Define the interval to load new data for data caches |  |
| **refreshDuration**  integer |  | Limit the time to run refresh data cache job |  |
| **defaultIsEnableDataCache**  boolean | Y | Default value of `isEnableDataCache` |  |
| **defaultEvictionInterval**  integer | Y | Default value of `EvictionInterval` |  |
| **defaultTimeToLive**  integer | Y | Default value of `timeToLive` |  |
| **defaultRefreshInterval**  integer | Y | Default value of `refreshInterval` |  |
| **defaultRefreshDuration**  integer | Y | Default value of `refreshDuration` |  |

**Sample**:

```
{"isEnableDataCache":true,"timeToLive":600,"evictionInterval":600,"refreshInterval":200,"refreshDuration":100,"defaultIsEnableDataCache":true,"defaultEvictionInterval":600,"defaultTimeToLive":600,"defaultRefreshInterval":200,"defaultRefreshDuration":100}
```
