---
title: "DataSecurityRule"
id: 12528281493015
section: "System Reference"
category: "Izenda"
url: https://devnet.logianalytics.com/hc/en-us/articles/12528281493015-DataSecurityRule
updated_at: 2023-02-19T08:36:27Z
---

# DataSecurityRule

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

# DataSecurityRule

| Field | NULL | Description | Note |
| --- | --- | --- | --- |
| **accessMode**  integer |  | The access mode of this object  * 1 = Block * 2 = Allow |  |
| **accessibleValues**  array of string values |  | The list of values to block or allow.  There are also some preset values   * {all} - all values * {tenantId} - the current Tenant ID * {tenantName} - the current Tenant Name * {roleName} - any role name of the current user * {userName} - the current User ID |  |
| **accessors**  array of objects |  | An array of [DataSecurityAccessor](https://devnet.logianalytics.com/hc/en-us/articles/12528281479703-DataSecurityAccessor) objects. |  |
| **id**  string (GUID) |  | The ID of the data security rule. |  |
| **position**  integer |  | The position in the list of data security rules. |  |
| **state**  integer |  | The state of this object   * 0 = None * 1 = Insert * 2 = Delete * 3 = Update |  |
| **userGroup**  integer |  | The selected user group of this object   * 1 = Everyone * 2 = Role * 3 = User |  |
