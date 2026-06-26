---
title: "Distinct Counts and Percentiles in Elasticsearch"
id: 4405850942487
section: "Connect to Data in Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405850942487-Distinct-Counts-and-Percentiles-in-Elasticsearch
updated_at: 2021-09-21T01:27:23Z
---

# Distinct Counts and Percentiles in Elasticsearch

# Distinct Counts and Percentiles in Elasticsearch

Distinct count and percentiles metrics return approximate values in Elasticsearch. The precision of the result returned by distinct count metric depends on the precision threshold setting (default value is 1000).

You can change the value of the precision threshold by setting the
`elasticsearch.query.cardinality.precision.threshold`
property in the
`zoomdata.properties`
file.

See Elasticsearch's documentation on the following for more information:

* For Elasticsearch version 6, see the following for
  [percentiles](https://www.elastic.co/guide/en/elasticsearch/reference/6.1/search-aggregations-metrics-percentile-aggregation.html)
  and
  [distinct count](https://www.elastic.co/guide/en/elasticsearch/guide/master/cardinality.html).
* For Elasticsearch version 7, see the following for [percentiles](https://www.elastic.co/guide/en/elasticsearch/reference/current/search-aggregations-metrics-percentile-aggregation.html) and [distinct count](https://www.elastic.co/guide/en/elasticsearch/reference/current/search-aggregations-metrics-cardinality-aggregation.html).

The table below lists all available properties that you can modify to work with Elasticsearch.

| Property | Default | Use | Notes |
| --- | --- | --- | --- |
| elasticsearch.query.cardinality.precision.threshold | 1000 | control the level of accuracy of the distinct counts | The maximum supported value is 40000. However, Composer does not recommend to set such value as it may result in performance issues and the data source itself may return errors. For more info, refer to the [Precision Control](https://www.elastic.co/guide/en/elasticsearch/reference/2.0/search-aggregations-metrics-cardinality-aggregation.html#_precision_control) section by Elasticsearch. |
| elasticsearch.query.limit.nongrouped | 10000 | set the limit for the number of non-grouped records (per shard) to execute on. |  |
| elasticsearch.query.limit.grouped | 10000 | set the limit for the number of grouped records (per shard) to execute on. |  |

If you need to change the default settings, you can add the corresponding properties (listed above) to the
`zoomdata.properties`
file and assign the required values. For more details about working with the
`zoomdata.properties`
file, refer to the topic [Managing Configurations in Composer](https://devnet.logianalytics.com/hc/en-us/articles/4405859144343-Configure-Composer)
.
