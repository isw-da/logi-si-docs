---
title: "LicenseStatusResult"
id: 4415504735127
section: "System Reference"
category: "Izenda"
url: https://devnet.logianalytics.com/hc/en-us/articles/4415504735127-LicenseStatusResult
updated_at: 2021-12-10T03:08:58Z
---

# LicenseStatusResult

# LicenseStatusResult

| Field | NULL | Description | Note |
| --- | --- | --- | --- |
| **licenseStatus**  object |  | A [LicenseStatus](https://devnet.logianalytics.com/hc/en-us/articles/4415504734231-LicenseStatus) object |  |

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
{"licenseStatus":{"disabled":false,"meetExprireWarningPeriod":false,"numberOfDayToExpire":88,"numberOfDayToValid":0,"exceedLostConnectionAllowPeriod":false,"isAdminUser":false,"trialLicense":false},"success":true,"messages":null}
```
