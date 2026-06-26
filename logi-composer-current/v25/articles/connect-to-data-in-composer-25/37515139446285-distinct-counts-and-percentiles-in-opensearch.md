---
title: "Distinct Counts and Percentiles in OpenSearch "
id: 37515139446285
section: "Connect to Data in Composer 25"
product: "Logi Composer v25"
url: https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/37515139446285-Distinct-Counts-and-Percentiles-in-OpenSearch
updated_at: 2026-05-26T22:05:57Z
---

# Distinct Counts and Percentiles in OpenSearch 

# Distinct Counts and Percentiles in OpenSearch

Distinct count and percentiles metrics return approximate values in OpenSearch. The precision of the result returned by distinct count metric depends on the precision threshold setting (default value is 1000).

You can change the value of the precision threshold by setting the `elasticsearch.query.cardinality.precision.threshold` property in the `zoomdata.properties` file.

See OpenSearch 's documentation on the following for more information:

* For OpenSearch, see the following for [percentiles](https://docs.opensearch.org/docs/2.19/search.html?q=percentiles "percentiles") and [distinct count](https://docs.opensearch.org/docs/2.19/search.html?q=distinct%20count "distinct count").

The table below lists all available properties that you can modify to work with OpenSearch.

| Property | Default | Use | Notes |
| --- | --- | --- | --- |
| elasticsearch.query.cardinality.precision.threshold | 1000 | control the level of accuracy of the distinct counts | The maximum supported value is 40000. However, Composer does not recommend to set such value as it may result in performance issues and the data source itself may return errors. |
| elasticsearch.query.limit.nongrouped | 10000 | set the limit for the number of non-grouped records (per shard) to execute on. |  |
| elasticsearch.query.limit.grouped | 10000 | set the limit for the number of grouped records (per shard) to execute on. |  |

If you need to change the default settings, add the corresponding properties (listed above) to the `zoomdata.properties` file and assign the required values. For more details, see [Managing Configurations](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932701121421-Configure-Composer).

**Important:** If you are connecting to OpenSearch versions earlier than 2.x, use the [Elasticsearch 7 connector](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932728155405-Manage-the-Elasticsearch-Connector).
