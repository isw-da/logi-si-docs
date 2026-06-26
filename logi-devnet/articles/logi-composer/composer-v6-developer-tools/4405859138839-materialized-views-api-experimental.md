---
title: "Materialized Views API (Experimental)"
id: 4405859138839
section: "Composer v6 Developer Tools"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405859138839-Materialized-Views-API-Experimental
updated_at: 2021-09-21T01:26:44Z
---

# Materialized Views API (Experimental)

# Materialized Views API (Experimental)

Materialized views allow you to use pre-aggregated query results, stored in some external storage, to speed up query processing in certain scenarios, especially when processing a query with heavily aggregated data.

![](https://devnet.logianalytics.com/hc/article_attachments/4406743778327/criticalicon_23x23.gif) Pre-aggregated data is not managed by Composer, so it should be maintained manually and kept up to date by the owner of the data.

![](https://devnet.logianalytics.com/hc/article_attachments/4406743739159/criticalicon.gif) This is an experimental feature.

![](https://devnet.logianalytics.com/hc/article_attachments/4406747382295/noteicon.jpg) The Volume metric is required in all materialized view definitions.

API support for materialized views is performed using the REST API endpoint `/api/materialized-views`, as described below.

| Endpoint | Method | Description |
| --- | --- | --- |
| `/api/materialized-views` | GET | Returns a list of all materialized view mappings. Optionally, include the `sourceId={<data-source-id>}` parameter to obtain a list of materialized views for a specific data source. |
| `/api/materialized-views` | POST | Creates a new materialized view mapping. |
| `/api/materialized-views/<source-ID>` | PUT | Updates a specific materialized view mapping. |
| `/api/materialized-views/<source-ID>` | PATCH | Patches (partially updates) a specific materialized view mapping. |
| `/api/materialized-views/<source-ID>` | DELETE | Deletes a specific materialized view mapping. |
| `/api/sources/<source-ID>/fields/meta` | GET | Returns information about all the fields and metrics in a data source. |

API documentation is provided with your Composer installation at this link: `https://<composer-URL>/composer/swagger-ui.html`.

Here is a sample of the general object structure for materialized views:

```
{  
  "name": "string",
  "description": "string",
  "enabled": true,
  "definition": { ... },
  "storageSettings": {
    "targetStorage": { ... },
    "fieldMappings": [ ... ]
  }
}
```

Each object is described in the following table.

| Object | Specifies |
| --- | --- |
| `name` | The name of the materialized view definition. |
| `description` | The description of the materialized view definition. |
| `enabled` | Whether or not the definition is enabled. A value of `true` indicates that it is enabled; `false` indicates that it is not. |
| `definition` | The query that this materialized view should match. |
| `storageSettings` | Where the data for the query results are stored. |
| `targetStorage` | The connection and the specific table or collection of data |
| `fieldMappings` | The mapping between the fields used in the definition and the columns or fields in the data identified by the `targetStorage` object.  Every field returned by the `definition` query should be mapped in `fieldMappings`.  You can skip fields in the target table if they are not used in the query results (for example, redundant metrics). |
