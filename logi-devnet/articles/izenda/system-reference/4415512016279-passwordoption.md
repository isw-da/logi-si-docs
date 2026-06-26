---
title: "PasswordOption"
id: 4415512016279
section: "System Reference"
category: "Izenda"
url: https://devnet.logianalytics.com/hc/en-us/articles/4415512016279-PasswordOption
updated_at: 2021-12-10T03:09:02Z
---

# PasswordOption

# PasswordOption

| Field | Null | Description | Note |
| --- | --- | --- | --- |
| **passwordLink**  string |  | The [password link](https://devnet.logianalytics.com/hc/en-us/articles/4415492696343-Glossary#term-password-link). |  |
| **user**  object |  | A [UserDetail](https://devnet.logianalytics.com/hc/en-us/articles/4415512065431-UserDetail) object |  |
| **sendEmail**  boolean |  | Send password link via email or not |  |
| **clearSecurityQuestion**  boolean |  | Clear all security questions or not |  |
| **emailAddresses**  array of strings |  | The list of email addresses to send password link |  |

Inherited fields:

## Expiration

| Field | NULL | Description | Note |
| --- | --- | --- | --- |
| **isExpired**  boolean |  | Is the item expired |  |
| **notifyDuringDay**  integer | Y | The number of days to notify in advance, before the item is expired |  |

**Sample**:

```
{"passwordLink":"http://127.0.0.1:8888/account/activation?verification=H8K....RU%3D","user":{"userName":"jdoe","id":"6c447061-8f1d-4ff4-803c-b6b15695b8c3"},"sendEmail":false,"clearSercurityQuestion":false,"emailAddresses":["jdoe@acme.com"]}
```
