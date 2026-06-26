---
title: "Elasticsearch 7 Composite Aggregation"
id: 43700994753549
section: "Connect to Data in Composer 26"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43700994753549-Elasticsearch-7-Composite-Aggregation
updated_at: 2026-05-29T14:07:37Z
---

# Elasticsearch 7 Composite Aggregation

# Elasticsearch 7 Composite Aggregation

Composite aggregations are implemented by Elasticsearch 7 connectors. This support optimizes aggregations of Elasticsearch 7 data, except for queries with:

* histograms
* time groups with WEEK granularity
* multiple groups when group fields belong to different nested contexts.

An Elasticsearch 7 configuration property `elasticsearch.query.composite-agg.max-fetch-size` in the Elasticsearch 7 configuration file (`edc-elasticsearch-7.0.properties`) can be used to specify the maximum number of buckets to return for each query within a composite aggregation. Valid values must be greater than zero; the default value is 10000. This property corresponds to the Elasticsearch setting `search.max_buckets`, that also has a default value of 10000. If you elect to increase the value of the `elasticsearch.query.composite-agg.max-fetch-size property`, be sure to correspondingly increase the value of the Elasticsearch `search.max_buckets` setting.
