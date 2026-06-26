---
title: "SecuritySetting"
id: 12528283127191
section: "System Reference"
category: "Izenda"
url: https://devnet.logianalytics.com/hc/en-us/articles/12528283127191-SecuritySetting
updated_at: 2023-02-19T08:37:37Z
---

# SecuritySetting

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

# SecuritySetting

| Field | NULL | Description | Note |
| --- | --- | --- | --- |
| **allowShowTenant**  boolean |  | Is Show Tenant Field disabled. |  |
| **dataSecurityRuleSets**  array of objects  New in version 3.11.0. |  | An array of [DataSecurityRuleSet](https://devnet.logianalytics.com/hc/en-us/articles/12528297021591-DataSecurityRuleSet) objects. |  |
| **modified**  datetime | Y | The modification date time. |  |
| **setAdditiveFieldAutoFilterableDefaultValue**  boolean |  | The default value for Additive Fields Auto Filterable (`false`). |  |
| **setAdditiveFieldAutoFilterableValue**  boolean |  | Additive Fields Auto Filterable - if checked then additive fields when physical data model changes will be set as Filterable automatically. |  |
| **setAdditiveFieldAutoVisibleDefaultValue**  boolean |  | The default value for Additive Fields Auto Visible (`false`). |  |
| **setAdditiveFieldAutoVisibleValue**  boolean |  | Additive Fields Auto Visible - if checked then additive fields when physical data model changes will be set as Visible automatically. |  |
| **showTenantFieldDefaultValue**  boolean |  | The default value for Show Tenant Field (`true`). |  |
| **showTenantFieldValue**  boolean |  | Show Tenant Field - when false, this hides the fields identified in the TenantField property from being selected or viewed by users. Any filters based on the tenant fields will still affect the results. |  |
| **tenantId**  string (GUID) | Y | The id of the tenant   (null if the setting belongs to system). |  |
| **tenantFields**  array of objects |  | An array of [TenantField](https://devnet.logianalytics.com/hc/en-us/articles/12528283272343-TenantField) objects. |  |
| **tenantFieldDefaultValue**  string |  | The default value for tenantFieldValue. |  |
| **tenantFieldValue**  string |  | Names of tenant fields, separated by semi-colon.    Example: `TenantID;UserID` |  |

**Sample**:

```
{"tenantFieldValue":"TenantID;UserID","tenantFieldDefaultValue":"","showTenantFieldValue":true,"showTenantFieldDefaultValue":true,"setAdditiveFieldAutoVisibleValue":false,"setAdditiveFieldAutoVisibleDefaultValue":false,"setAdditiveFieldAutoFilterableValue":false,"setAdditiveFieldAutoFilterableDefaultValue":false,"tenantId":null,"tenantFields":[{"name":"TenantID","isSystem":true},{"name":"UserID","isSystem":true}],"allowShowTenant":true,"dataSecurityRuleSets":[],"modified":"2017-02-15T06:31:15"}
```
