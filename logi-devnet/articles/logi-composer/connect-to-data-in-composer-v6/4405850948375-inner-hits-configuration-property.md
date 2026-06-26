---
title: "Inner Hits Configuration Property"
id: 4405850948375
section: "Connect to Data in Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405850948375-Inner-Hits-Configuration-Property
updated_at: 2021-09-21T01:27:24Z
---

# Inner Hits Configuration Property

# Inner Hits Configuration Property

Use the Composer Elasticsearch 6 & 7 `elasticsearch.inner-hits.size property` to specify the maximum number of hits to return per `inner_hits` query (used for raw data requests involving nested fields). The default value is 100.

If you specify a value that is too small, the number of values returned for a nested field in a document with a large number of sub-documents may be limited. If you specify a value that is too large, excessive memory may be consumed.
