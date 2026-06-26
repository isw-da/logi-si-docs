---
title: "Inner Hits Configuration Property"
id: 34932736557197
section: "Connect to Data in Composer 25"
product: "Logi Composer v25"
url: https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932736557197-Inner-Hits-Configuration-Property
updated_at: 2026-05-26T22:06:36Z
---

# Inner Hits Configuration Property

# Inner Hits Configuration Property

Use the Composer Elasticsearch `elasticsearch.inner-hits.size property` to specify the maximum number of hits to return per `inner_hits` query (used for raw data requests involving nested fields). The default value is 100.

If you specify a value that is too small, the number of values returned for a nested field in a document with a large number of sub-documents may be limited. If you specify a value that is too large, excessive memory may be consumed.

**Note:** 
To learn more about this property, see [inner hits.](https://www.elastic.co/guide/en/elasticsearch/reference/8.2/inner-hits.html)
