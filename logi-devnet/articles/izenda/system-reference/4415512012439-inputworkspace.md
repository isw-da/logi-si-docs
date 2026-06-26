---
title: "InputWorkspace"
id: 4415512012439
section: "System Reference"
category: "Izenda"
url: https://devnet.logianalytics.com/hc/en-us/articles/4415512012439-InputWorkspace
updated_at: 2021-12-10T03:08:56Z
---

# InputWorkspace

# InputWorkspace

| Field | NULL | Description | Note |
| --- | --- | --- | --- |
| **sourceTenantId**  string |  | The user-defined id of the source tenant |  |
| **reportIds**  array of strings |  | The list of report ids |  |
| **reportIdsLineNumber**  array of objects |  | An array of [CopiedItem](https://devnet.logianalytics.com/hc/en-us/articles/4415511983639-CopiedItem) objects |  |
| **templateIds**  array of strings |  | The list of template ids |  |
| **templateIdsLineNumber**  array of objects |  | An array of [CopiedItem](https://devnet.logianalytics.com/hc/en-us/articles/4415511983639-CopiedItem) objects |  |
| **dashboardIds**  array of strings |  | The list of dashboard ids |  |
| **dashboardIdsLineNumber**  array of objects |  | An array of [CopiedItem](https://devnet.logianalytics.com/hc/en-us/articles/4415511983639-CopiedItem) objects |  |
| **destinationTenants**  array of objects |  | An array of [DestinationTenant](https://devnet.logianalytics.com/hc/en-us/articles/4415504719255-DestinationTenant) objects |  |
| **dataInSource**  object |  | A [DataInSource](https://devnet.logianalytics.com/hc/en-us/articles/4415511994263-DataInSource) object |  |
| **sourceLineNumber**  integer |  | The line number for source tag |  |
| **destinationLineNumber**  integer |  | The line number for destination tag |  |
| **sourceTenantLineNumber**  integer |  | The line number for source tenant tag |  |
| **usingFields**  array of strings |  | An array of using fields  New in version 2.6.21. |  |

**Sample**:

```
{"sourceTenantId":"78e5699a-6a67-471f-8374-529a80777754","reportIds":["4b6d592e-ad29-408d-a3f2-845776d555db"]}
```
