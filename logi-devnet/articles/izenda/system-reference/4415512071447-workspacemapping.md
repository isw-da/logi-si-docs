---
title: "WorkspaceMapping"
id: 4415512071447
section: "System Reference"
category: "Izenda"
url: https://devnet.logianalytics.com/hc/en-us/articles/4415512071447-WorkspaceMapping
updated_at: 2021-12-10T03:10:05Z
---

# WorkspaceMapping

# WorkspaceMapping

| Field | NULL | Description | Note |
| --- | --- | --- | --- |
| **workspaceId**  string (GUID) | Y | The id of the workspace tenant |  |
| **type**  integer |  | The type of the database in Source   * 1 = Schema * 2 = Database |  |
| **fromServer**  string |  | The from server |  |
| **toServer**  string |  | The to server |  |
| **fromDatabaseName**  string |  | The name of the database in Source |  |
| **toDatabaseName**  string |  | The name of the database in Destination |  |
| **fromObject**  string |  | The name of the object in Source |  |
| **toObject**  string |  | The name of the object in Destination |  |
| **fromDatabaseUser**  string  New in version 3.10.0. |  | The source (encrypted) database username |  |
| **toDatabaseUser**  string  New in version 3.10.0. |  | The destination (encrypted) database username |  |
| **isGlobal**  boolean |  | Is this a global mapping |  |

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
