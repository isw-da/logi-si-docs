---
title: "QuerySourceSchema"
id: 4415492835479
section: "System Reference"
category: "Izenda"
url: https://devnet.logianalytics.com/hc/en-us/articles/4415492835479-QuerySourceSchema
updated_at: 2021-12-10T03:09:08Z
---

# QuerySourceSchema

# QuerySourceSchema

| Field | NULL | Description | Note |
| --- | --- | --- | --- |
| **id**  string (GUID) |  | The id of the query source schema |  |
| **name**  string |  | The name |  |
| **type**  string |  | Either “Table”, “View”, “Stored Procedure” or “Function” |  |
| **color**  string |  | The color for display |  |
| **connectionId**  string (GUID) |  | The id of the connection containing the query source |  |
| **modified**  datetime |  | The modify datetime |  |
| **fields**  array of objects |  | An array of child [QuerySourceFieldSchema](https://devnet.logianalytics.com/hc/en-us/articles/4415512021143-QuerySourceFieldSchema) objects |  |
