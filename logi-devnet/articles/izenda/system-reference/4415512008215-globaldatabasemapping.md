---
title: "GlobalDatabaseMapping"
id: 4415512008215
section: "System Reference"
category: "Izenda"
url: https://devnet.logianalytics.com/hc/en-us/articles/4415512008215-GlobalDatabaseMapping
updated_at: 2021-12-10T03:08:53Z
---

# GlobalDatabaseMapping

# GlobalDatabaseMapping

| Field | NULL | Description | Note |
| --- | --- | --- | --- |
| **type**  integer |  | * 1 = Schema * 2 = Database |  |
| **fromServer**  string |  | The source server |  |
| **toServer**  string |  | The destination server |  |
| **fromDatabaseName**  string |  | The source database name |  |
| **toDatabaseName**  string |  | The destination database name |  |
| **fromObject**  string |  | The source schema (N/A in case of type 2 Database) |  |
| **toObject**  string |  | The destination |  |
| **fromDatabaseUser**  string  New in version 3.10.0. |  | The source (encrypted) database username |  |
| **toDatabaseUser**  string  New in version 3.10.0. |  | The destination (encrypted) database username |  |
| **selectAllTenants**  boolean |  | Is option All Tenants selected |  |
| **tenants**  array of strings |  | An array of tenant ids |  |
| **errorType**  integer |  | * 0 = None * 1 = Required * 2 = Duplicate * 3 = MultipleMapping |  |

Inherited fields:

## Entity

| Field | NULL | Description | Note |
| --- | --- | --- | --- |
| **id**  string (GUID) |  | The id of this object   Example: `572bd576-8c92-4901-ab2a-b16e38144813` | Allow null incase insert a new entity |
| **state**  integer |  | The entity state of this object   * 0 = None * 1 = Insert * 2 = Delete * 3 = Update |  |
| **deleted**  boolean |  | Is this object deleted |  |
| **inserted**  boolean |  | Is this object inserted |  |
| **version**  string | Y | The version |  |
| **created**  datetime in ISO 8601 format | Y | The created datetime |  |
| **createdBy**  string |  | The creator |  |
| **modified**  datetime in ISO 8601 format | Y | The modification datetime |  |
| **modifiedBy**  string |  | The user who last modified this object |  |
