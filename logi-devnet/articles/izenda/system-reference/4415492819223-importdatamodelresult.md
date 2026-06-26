---
title: "ImportDataModelResult"
id: 4415492819223
section: "System Reference"
category: "Izenda"
url: https://devnet.logianalytics.com/hc/en-us/articles/4415492819223-ImportDataModelResult
updated_at: 2021-12-10T03:08:55Z
---

# ImportDataModelResult

# ImportDataModelResult

| Field | NULL | Description | Note |
| --- | --- | --- | --- |
| **success**  boolean |  | * true if the import was successful * false if not |  |
| **messages**  array of objects | Y | An array of [ModelError](https://devnet.logianalytics.com/hc/en-us/articles/4415504736279-ModelError) objects |  |
| **inconsistentDataSources**  object | Y | A dynamic object to list inconsistent data sources |  |

**Sample**:

```
{"success":true,"messages":null,"inconsistentDataSources":null}
```
