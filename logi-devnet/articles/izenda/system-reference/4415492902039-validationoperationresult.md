---
title: "ValidationOperationResult"
id: 4415492902039
section: "System Reference"
category: "Izenda"
url: https://devnet.logianalytics.com/hc/en-us/articles/4415492902039-ValidationOperationResult
updated_at: 2021-12-10T03:10:01Z
---

# ValidationOperationResult

# ValidationOperationResult

| Field | NULL | Description | Note |
| --- | --- | --- | --- |
| **result**  object |  | An object with   - a string field **izendaDataType** containing the suggested data type   - a boolean field **isRunningField** whether expression in request payload contains running field   - a boolean field **isCompositeField** whether the calculated field is a composite field and will not be able to filter |  |

Inherited fields:

## OperationResult

| Field | NULL | Description | Note |
| --- | --- | --- | --- |
| **success**  boolean |  | Is the operation successful |  |
| **messages**  array of objects |  | An array of [ModelError](https://devnet.logianalytics.com/hc/en-us/articles/4415504736279-ModelError) objects |  |
| **data**  object |  | A dynamic object to store additional data |  |

**Sample**:

```
{"success":true,"data":"4e2d54c8-20e7-437f-a5ce-43e963c763a2"}
```

**ValidationOperationResult Sample**:

```
{"result":{"izendaDataType":"Numeric","isRunningField":false,"isCompositeField":false},"success":true,"messages":[],"data":null}
```
