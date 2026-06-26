---
title: "ConnectionVerificationResult"
id: 4415492774167
section: "System Reference"
category: "Izenda"
url: https://devnet.logianalytics.com/hc/en-us/articles/4415492774167-ConnectionVerificationResult
updated_at: 2021-12-10T03:08:26Z
---

# ConnectionVerificationResult

# ConnectionVerificationResult

| Field | NULL | Description | Note |
| --- | --- | --- | --- |
| **serverNotValid**  boolean |  | Is the server not valid |  |
| **databaseNotValid**  boolean |  | Is the database not valid |  |
| **differentDatabase**  boolean |  | Does the connection string point to a different database |  |
| **loginFail**  boolean |  | Did the login succeed |  |
| **hasValidLicense**  boolean |  | Has the database already had a valid license |  |

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

**Sample**:

```
{"serverNotValid":false,"databaseNotValid":false,"loginFail":false,"hasValidLicense":false,"success":true,"messages":[]}
```
