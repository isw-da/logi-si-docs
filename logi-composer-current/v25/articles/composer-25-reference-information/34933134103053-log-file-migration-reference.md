---
title: "Log File Migration Reference"
id: 34933134103053
section: "Composer 25 Reference Information"
product: "Logi Composer v25"
url: https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933134103053-Log-File-Migration-Reference
updated_at: 2026-05-26T22:07:54Z
---

# Log File Migration Reference

# Log File Migration Reference

With the introduction of unified log properties and unified logback configurations, a number of log files have new names. When you upgrade your Composer environment from an earlier version, you may need to rename properties overwritten by external configurations.

## Zoomdata-web

| Current Name | Deprecated Name |
| --- | --- |
| `log.file.size` | `zoomdata.log.file.size` |
| `log.file.count` | `zoomdata.log.rolling.maxIndex` |
| `log.error.file.size` | `zoomdata.error.log.file.size` |
| `access.log.file.size` | `zoomdata.access.log.file.size` |
| `license.log.file.size` | `zoomdata.license.log.file.size` |
| `activity.log.file.count` | `zoomdata.activity.log.file.max.index` |
| `activity.log.file.size` | `zoomdata.activity.log.file.size` |
| `activity.logs.dir` | `zoomdata.activity.logs.dir` |
| `websocket.log.file.size` | `zoomdata.websocket.log.file.size` |
| `websocket.log.file.count` | `zoomdata.websocket.log.rolling.maxIndex` |

## Query Engine

| Current Name | Deprecated Name |
| --- | --- |
| `log.file.size` | `qe.log.file.size` |
| `log.file.count` | `qe.log.rolling.maxIndex` |
| `log.error.file.size` | `qe.error.log.file.size` |
| `websocket.log.file.count` | `qe.websocket.log.rolling.maxIndex` |
| `websocket.log.level` | `qe.websocket.log.level` |
| `websocket.log.file.size` | `qe.websocket.log.file.size` |
| `access.log.file.size` | `qe.access.log.file.size` |

## EDC

| Current Name | Deprecated Name |
| --- | --- |
| `logs.file-name` | `log.file.base.name` |

## Admin Service, Config Server, Data Writer, and Screenshot Service

| Current Name | Deprecated Name |
| --- | --- |
| `log.file.count` | `log.rolling.maxIndex` |
| `log.error.file.size` | `error.log.file.size` |
| `log.error.file.count` | `error.log.rolling.maxIndex` |
