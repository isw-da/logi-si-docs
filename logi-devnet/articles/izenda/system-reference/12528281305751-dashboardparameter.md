---
title: "DashboardParameter"
id: 12528281305751
section: "System Reference"
category: "Izenda"
url: https://devnet.logianalytics.com/hc/en-us/articles/12528281305751-DashboardParameter
updated_at: 2023-02-19T08:36:19Z
---

# DashboardParameter

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

# DashboardParameter

| Field | NULL | Description | Note |
| --- | --- | --- | --- |
| **dashboard**  object |  | A [DashboardDefinition](https://devnet.logianalytics.com/hc/en-us/articles/12528296811159-DashboardDefinition) object |  |
| **dashboardId**  string (GUID) | Y | The id of the dashboard |  |
| **section**  integer |  | The dashboard section  * 0 = All * 1 = Dashboard * 2 = Access * 3 = Subscription |  |
| **action**  integer | Y | Specify the action from client site  * null, undefined, 1 = view report * 2 = cancel change on report |  |
| **page**  string(GUID) | Y | Id of the current web page |  |

**Sample**:

```
{"dashboardId":"a496ad94-fe92-48d5-a285-e45be738921f"}
```
