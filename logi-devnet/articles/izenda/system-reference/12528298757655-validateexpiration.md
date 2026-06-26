---
title: "ValidateExpiration"
id: 12528298757655
section: "System Reference"
category: "Izenda"
url: https://devnet.logianalytics.com/hc/en-us/articles/12528298757655-ValidateExpiration
updated_at: 2023-02-19T08:37:53Z
---

# ValidateExpiration

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

# ValidateExpiration

| Field | Null | Description | Note |
| --- | --- | --- | --- |
| **tenantId**  string (GUID) | Y | The id of the tenant if available |  |

Inherited fields:

## Expiration

| Field | NULL | Description | Note |
| --- | --- | --- | --- |
| **isExpired**  boolean |  | Is the item expired |  |
| **notifyDuringDay**  integer | Y | The number of days to notify in advance, before the item is expired |  |

**Sample**:

```
{"tenantId":null,"isExpired":false,"notifyDuringDay":null}
```
