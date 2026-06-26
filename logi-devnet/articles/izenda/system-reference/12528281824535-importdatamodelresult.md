---
title: "ImportDataModelResult"
id: 12528281824535
section: "System Reference"
category: "Izenda"
url: https://devnet.logianalytics.com/hc/en-us/articles/12528281824535-ImportDataModelResult
updated_at: 2023-02-23T16:12:52Z
---

# ImportDataModelResult

# ImportDataModelResult

| Field | NULL | Description | Note |
| --- | --- | --- | --- |
| **success** boolean |  | * true if the import was successful * false if not |  |
| **messages** array of objects | Y | An array of [ModelError](https://devnet.logianalytics.com/hc/en-us/articles/12528297464471-ModelError) objects |  |
| **inconsistentDataSources** object | Y | A dynamic object to list inconsistent data sources |  |

**Sample**:

```
{"success":true,"messages":null,"inconsistentDataSources":null}
```
