---
title: "SharingRoleUserParameter"
id: 4415492886295
section: "System Reference"
category: "Izenda"
url: https://devnet.logianalytics.com/hc/en-us/articles/4415492886295-SharingRoleUserParameter
updated_at: 2021-12-10T03:09:46Z
---

# SharingRoleUserParameter

# SharingRoleUserParameter

| Field | NULL | Description | Note |
| --- | --- | --- | --- |
| **tenantId**  string (GUID) | Y | The tenant id |  |
| **reportId**  string (GUID) | Y | The report id |  |
| **dashboardId**  string (GUID) | Y | The dashboard id |  |
| **isGlobal**  boolean |  | Whether to set roles for global reports |  |

**Sample**:

```
{"reportId":"63d50ed1-5323-47a1-bc11-3a03a070ec34","tenantId":null}
```
