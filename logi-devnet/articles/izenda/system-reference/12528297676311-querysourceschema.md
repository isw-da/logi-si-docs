---
title: "QuerySourceSchema"
id: 12528297676311
section: "System Reference"
category: "Izenda"
url: https://devnet.logianalytics.com/hc/en-us/articles/12528297676311-QuerySourceSchema
updated_at: 2023-02-23T16:14:56Z
---

# QuerySourceSchema

# QuerySourceSchema

| Field | NULL | Description | Note |
| --- | --- | --- | --- |
| **id** string (GUID) |  | The id of the query source schema |  |
| **name** string |  | The name |  |
| **type** string |  | Either “Table”, “View”, “Stored Procedure” or “Function” |  |
| **color** string |  | The color for display |  |
| **connectionId** string (GUID) |  | The id of the connection containing the query source |  |
| **modified** datetime |  | The modify datetime |  |
| **fields** array of objects |  | An array of child [QuerySourceFieldSchema](https://devnet.logianalytics.com/hc/en-us/articles/12528282171287-QuerySourceFieldSchema) objects |  |
