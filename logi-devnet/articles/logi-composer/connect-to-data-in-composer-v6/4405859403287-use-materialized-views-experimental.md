---
title: "Use Materialized Views (Experimental)"
id: 4405859403287
section: "Connect to Data in Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405859403287-Use-Materialized-Views-Experimental
updated_at: 2021-09-21T01:29:06Z
---

# Use Materialized Views (Experimental)

# Use Materialized Views (Experimental)

Materialized views allow you to use pre-aggregated query results to speed up query processing in certain scenarios, especially when processing a query with heavily aggregated data. This boosts your visual rendering time.

![](https://devnet.logianalytics.com/hc/article_attachments/4406743739159/criticalicon.gif) This is an experimental feature.

Materialized views only work if the metrics and groups in the materialized view definitions match those used by your visuals. For example, no benefit from using materialized views will occur if you define a materialized view for the Planned Sales metric in a data source, but none of the visuals in your environment use the Planned Sales metric. Consequently, it is a good idea to understand what data in your data source is used (or will be used) in visuals before you define a materialized view.

![](https://devnet.logianalytics.com/hc/article_attachments/4406747382295/noteicon.jpg) A Volume metric is required in all materialized view definitions. The supplied Volume metric can be renamed.

Support for materialized views is performed using the REST API endpoint `/api/materialized-views`, described in [*Materialized Views API (Experimental)*](https://devnet.logianalytics.com/hc/en-us/articles/4405859138839-Materialized-Views-API-Experimental-). You can also specify materialized view settings for a data source configuration using the UI. See the following topics:

* [*List Materialized View Definitions*](https://devnet.logianalytics.com/hc/en-us/articles/4405851113751-List-Materialized-View-Definitions)
* [*Add a Materialized View Definition*](https://devnet.logianalytics.com/hc/en-us/articles/4405859398807-Add-a-Materialized-View-Definition)
* [*Edit a Materialized View Definition*](https://devnet.logianalytics.com/hc/en-us/articles/4405859399959-Edit-a-Materialized-View-Definition)
* [*Delete a Materialized View Definition*](https://devnet.logianalytics.com/hc/en-us/articles/4405851112855-Delete-a-Materialized-View-Definition)
* [*Enable and Disable Materialized View Definitions*](https://devnet.logianalytics.com/hc/en-us/articles/4405859401367-Enable-and-Disable-Materialized-View-Definitions)
