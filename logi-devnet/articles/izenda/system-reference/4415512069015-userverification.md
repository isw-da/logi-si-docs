---
title: "UserVerification"
id: 4415512069015
section: "System Reference"
category: "Izenda"
url: https://devnet.logianalytics.com/hc/en-us/articles/4415512069015-UserVerification
updated_at: 2021-12-10T03:09:59Z
---

# UserVerification

# UserVerification

| Field | Null | Description | Note |
| --- | --- | --- | --- |
| **id**  string (GUID) |  | The id of user |  |
| **firstName**  string |  | The first name |  |
| **lastName**  string |  | The last name |  |
| **emailAddress**  string |  | The email |  |
| **userName**  string |  | The user name |  |
| **verification**  string |  | The encoded info of user from [password link](https://devnet.logianalytics.com/hc/en-us/articles/4415492696343-Glossary#term-password-link) |  |
| **issueDate**  datetime |  | The time when token was generated |  |
| **tenantId**  string (GUID) | Y | The id of the tenant if available |  |
| **tenantDisplayId**  string |  | The user-entered id of the tenant |  |
| **tenantName**  string |  | The name of the tenant |  |

**Sample**:

```
{"tenantDisplayID":null,"userName":"jdoe","firstName":"John","lastName":"Doe","emailAddress":"jdoe@acme.com","verification":"H8K....RU="}
```
