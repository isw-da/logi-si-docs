---
title: "Use Materialized Views (Experimental)"
id: 34933088978573
section: "Connect to Data in Composer 25"
product: "Logi Composer v25"
url: https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933088978573-Use-Materialized-Views-Experimental
updated_at: 2026-05-26T22:07:43Z
---

# Use Materialized Views (Experimental)

# Use Materialized Views (Experimental)

**Note:** 
Materialized view functionality is disabled by default. To enable, [contact technical support](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932980712461-Contact-Technical-Support) for assistance.
The [Materialized Views API](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932682254861-Materialized-Views-API-Experimental) is deprecated and will be removed in a future release.

Materialized views allow you to use pre-aggregated query results to speed up query processing in certain scenarios, especially when processing a query with heavily aggregated data. This boosts your visual rendering time.

**Important:** 
This is an experimental feature.

Materialized views only work if the metrics and groups in the materialized view definitions match those used by your visuals. For example, no benefit from using materialized views will occur if you define a materialized view for the Planned Sales metric in a data source, but none of the visuals in your environment use the Planned Sales metric. Consequently, it is a good idea to understand what data in your data source is used (or will be used) in visuals before you define a materialized view.

**Note:** 
A Count metric is required in all materialized view definitions.

Support for materialized views is performed using the REST API endpoint `/api/materialized-views`, described in [Materialized Views API (Experimental)](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932682254861-Materialized-Views-API-Experimental). You can also specify materialized view settings for a data source configuration using the UI. See the following topics:

* [List Materialized View Definitions](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933057267725-List-Materialized-View-Definitions)
* [Add a Materialized View Definition](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933077179789-Add-a-Materialized-View-Definition)
* [Edit a Materialized View Definition](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933077573773-Edit-a-Materialized-View-Definition)
* [Delete a Materialized View Definition](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933056898701-Delete-a-Materialized-View-Definition)
* [Enable and Disable Materialized View Definitions](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933077830669-Enable-and-Disable-Materialized-View-Definitions)
