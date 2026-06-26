---
title: "DataSecurityRuleSet"
id: 12528297021591
section: "System Reference"
category: "Izenda"
url: https://devnet.logianalytics.com/hc/en-us/articles/12528297021591-DataSecurityRuleSet
updated_at: 2023-02-19T08:36:28Z
---

# DataSecurityRuleSet

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

# DataSecurityRuleSet

| Field | NULL | Description | Note |
| --- | --- | --- | --- |
| **description**  string |  | The description of the data security rule set. |  |
| **fields**  array of objects |  | An array of [DataSecurityField](https://devnet.logianalytics.com/hc/en-us/articles/12528296982295-DataSecurityField) objects. |  |
| **id**  string (GUID) |  | The ID of the data security rule set. |  |
| **name**  string |  | The name of the data security rule set. |  |
| **position**  integer |  | The position in the list of data security rule sets. |  |
| **rules**  array of objects |  | An array of [DataSecurityRule](https://devnet.logianalytics.com/hc/en-us/articles/12528281493015-DataSecurityRule) objects. |  |
| **state**  integer |  | The state of this object   * 0 = None * 1 = Insert * 2 = Delete * 3 = Update |  |
| **tenantId**  string (GUID) |  | The ID of the tenant (null if the setting belongs to System). |  |
