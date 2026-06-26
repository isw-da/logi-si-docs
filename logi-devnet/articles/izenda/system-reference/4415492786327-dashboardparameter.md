---
title: "DashboardParameter"
id: 4415492786327
section: "System Reference"
category: "Izenda"
url: https://devnet.logianalytics.com/hc/en-us/articles/4415492786327-DashboardParameter
updated_at: 2021-12-10T03:08:31Z
---

# DashboardParameter

# DashboardParameter

| Field | NULL | Description | Note |
| --- | --- | --- | --- |
| **dashboard**  object |  | A [DashboardDefinition](https://devnet.logianalytics.com/hc/en-us/articles/4415492783767-DashboardDefinition) object |  |
| **dashboardId**  string (GUID) | Y | The id of the dashboard |  |
| **section**  integer |  | The dashboard section  * 0 = All * 1 = Dashboard * 2 = Access * 3 = Subscription |  |
| **action**  integer | Y | Specify the action from client site  * null, undefined, 1 = view report * 2 = cancel change on report |  |
| **page**  string(GUID) | Y | Id of the current web page |  |

**Sample**:

```
{"dashboardId":"a496ad94-fe92-48d5-a285-e45be738921f"}
```
