---
title: "ValidateExpiration"
id: 4415512070039
section: "System Reference"
category: "Izenda"
url: https://devnet.logianalytics.com/hc/en-us/articles/4415512070039-ValidateExpiration
updated_at: 2021-12-10T03:09:59Z
---

# ValidateExpiration

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
