---
title: "RelationshipOrder"
id: 12528297710103
section: "System Reference"
category: "Izenda"
url: https://devnet.logianalytics.com/hc/en-us/articles/12528297710103-RelationshipOrder
updated_at: 2023-02-19T08:37:00Z
---

# RelationshipOrder

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

# RelationshipOrder

| Field | NULL | Description | Note |
| --- | --- | --- | --- |
| **alias**  string |  | The alias |  |
| **joinQuerySourceId**  string (GUID) | Y | The id of the query source containing the relationship |  |
| **selectedForeignAlias**  string |  | The foreign alias of the selected relationship |  |
| **relationshipPosition**  integer |  | The ordinal position of this relationship inside a list of relationships |  |
| **convertedKeyJoinIds**  an array of string(GUID)  New in version 2.11.0. |  | The relationship ids that converted to key join |  |
| **hasBeenModified**  boolean  New in version 2.11.0. |  | Whether the relationship has been modified or not |  |
