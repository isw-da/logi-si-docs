---
title: "ReportSavingResult"
id: 12528282949143
section: "System Reference"
category: "Izenda"
url: https://devnet.logianalytics.com/hc/en-us/articles/12528282949143-ReportSavingResult
updated_at: 2023-02-23T16:44:23Z
---

# ReportSavingResult

# ReportSavingResult

| Field | NULL | Description | Note |
| --- | --- | --- | --- |
| **reportKey** object |  | A [ReportKey](https://devnet.logianalytics.com/hc/en-us/articles/12528282642071-ReportKey) object |  |
| **report** object |  | A [ReportDefinition](https://devnet.logianalytics.com/hc/en-us/articles/12528297929111-ReportDefinition) object |  |

Inherited fields:

## OperationResult

| Field | NULL | Description | Note |
| --- | --- | --- | --- |
| **success** boolean |  | Is the operation successful |  |
| **messages** array of objects |  | An array of [ModelError](https://devnet.logianalytics.com/hc/en-us/articles/12528297464471-ModelError) objects |  |
| **data** object |  | A dynamic object to store additional data |  |

**Sample**:

```
{"success":true,"data":"4e2d54c8-20e7-437f-a5ce-43e963c763a2"}
```

**Sample**:

```
{"reportKey":{"key":null,"tenantId":null},"report":null}
```
