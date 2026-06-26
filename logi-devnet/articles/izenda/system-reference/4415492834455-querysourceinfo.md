---
title: "QuerySourceInfo"
id: 4415492834455
section: "System Reference"
category: "Izenda"
url: https://devnet.logianalytics.com/hc/en-us/articles/4415492834455-QuerySourceInfo
updated_at: 2021-12-10T03:09:07Z
---

# QuerySourceInfo

# QuerySourceInfo

| Field | NULL | Description | Note |
| --- | --- | --- | --- |
| **id**  string (GUID) |  | The id of the query source |  |
| **name**  string |  | The query source name |  |
| **alias**  string |  | The alias of the query source |  |
| **category**  string |  | The category name |  |
| **serverTypeId**  string (GUID) |  | The id of the type of database server |  |
| **connectionStringId**  string (GUID) |  | The id of the connection |  |
| **connectionString**  string |  | The connection string |  |
| **connectionName**  string |  | The name of the connection containing the query source |  |
| **querySourceCategoryName**  string |  | The name of the [query source category](https://devnet.logianalytics.com/hc/en-us/articles/4415492696343-Glossary#term-query-source-category) containing the query source |  |

**Sample**:

```
{"id":"77882ea1-6d82-45c2-b762-6c8612682b91","name":"Categories","alias":null,"category":"dbo","serverTypeId":"00000000-0000-0000-0000-000000000000","connectionStringId":"00000000-0000-0000-0000-000000000000","connectionString":null}
```
