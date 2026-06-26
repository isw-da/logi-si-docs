---
title: "OpenSearch  Composite Aggregation"
id: 43701044429709
section: "Connect to Data in Composer 26"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701044429709-OpenSearch-Composite-Aggregation
updated_at: 2026-05-29T14:07:49Z
---

# OpenSearch  Composite Aggregation

# OpenSearch Composite Aggregation

Composite aggregations are implemented by OpenSearch connectors. This support optimizes aggregations of OpenSearch data, except for queries with:

* histograms
* time groups with WEEK granularity
* multiple groups when group fields belong to different nested contexts.

An OpenSearch configuration property `elasticsearch.query.composite-agg.max-fetch-size` in the OpenSearch configuration file (`edc-elasticsearch-7.0.properties`) can be used to specify the maximum number of buckets to return for each query within a composite aggregation. Valid values must be greater than zero; the default value is 10000. This property corresponds to the OpenSearch setting `search.max_buckets`, that also has a default value of 10000. If you elect to increase the value of the `elasticsearch.query.composite-agg.max-fetch-size property`, be sure to correspondingly increase the value of the OpenSearch `search.max_buckets` setting.

**Important:** If you are connecting to OpenSearch versions earlier than 2.x, use the [Elasticsearch 7 connector](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701025911309-Manage-the-Elasticsearch-Connector).
