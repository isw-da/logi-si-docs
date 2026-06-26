---
title: "OpenSearch  Composite Aggregation"
id: 37515147766797
section: "Connect to Data in Composer 25"
product: "Logi Composer v25"
url: https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/37515147766797-OpenSearch-Composite-Aggregation
updated_at: 2026-05-26T22:05:59Z
---

# OpenSearch  Composite Aggregation

# OpenSearch Composite Aggregation

Composite aggregations are implemented by OpenSearch connectors. This support optimizes aggregations of OpenSearch data, except for queries with:

* histograms
* time groups with WEEK granularity
* multiple groups when group fields belong to different nested contexts.

An OpenSearch configuration property `elasticsearch.query.composite-agg.max-fetch-size` in the OpenSearch configuration file (`edc-elasticsearch-7.0.properties`) can be used to specify the maximum number of buckets to return for each query within a composite aggregation. Valid values must be greater than zero; the default value is 10000. This property corresponds to the OpenSearch setting `search.max_buckets`, that also has a default value of 10000. If you elect to increase the value of the `elasticsearch.query.composite-agg.max-fetch-size property`, be sure to correspondingly increase the value of the OpenSearch `search.max_buckets` setting.

**Important:** If you are connecting to OpenSearch versions earlier than 2.x, use the [Elasticsearch 7 connector](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932728155405-Manage-the-Elasticsearch-Connector).
