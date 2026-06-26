---
title: "AdvancedSetting"
id: 12528296609431
section: "System Reference"
category: "Izenda"
url: https://devnet.logianalytics.com/hc/en-us/articles/12528296609431-AdvancedSetting
updated_at: 2023-02-19T08:36:09Z
---

# AdvancedSetting

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

# AdvancedSetting

| Field | NULL | Description | Note |
| --- | --- | --- | --- |
| **id**  string (GUID) |  | The id |  |
| **name**  string |  | The name of the setting |  |
| **value**  string |  | The value of the setting |  |
| **defaultValue**  string |  | The default value of the setting |  |
| **type**  string |  | Either Performance, Security, Others, or null (e.g. Default Header Image) |  |
| **tenantId**  string (GUID) | Y | The id of the tenant if available |  |
| **deleted**  boolean |  | Is this deleted |  |
| **modified**  datetime | Y | The date of modification |  |

**Sample**:

```
{"id":"c8ecf9fd-196d-44a3-90ec-97f393ebfc0c","name":"DefaultImageUrl","value":"http://localhost/img/default.png","defaultValue":null,"type":null,"tenantId":null,"deleted":false,"modified":"2017-04-12T16:55:11.4900000+07:00"}
```
