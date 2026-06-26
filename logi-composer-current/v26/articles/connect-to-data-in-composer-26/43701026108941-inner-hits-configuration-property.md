---
title: "Inner Hits Configuration Property"
id: 43701026108941
section: "Connect to Data in Composer 26"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701026108941-Inner-Hits-Configuration-Property
updated_at: 2026-05-29T14:07:45Z
---

# Inner Hits Configuration Property

# Inner Hits Configuration Property

Use the Composer Elasticsearch `elasticsearch.inner-hits.size property` to specify the maximum number of hits to return per `inner_hits` query (used for raw data requests involving nested fields). The default value is 100.

If you specify a value that is too small, the number of values returned for a nested field in a document with a large number of sub-documents may be limited. If you specify a value that is too large, excessive memory may be consumed.

**Note:** 
To learn more about this property, see [inner hits.](https://www.elastic.co/guide/en/elasticsearch/reference/8.2/inner-hits.html)
