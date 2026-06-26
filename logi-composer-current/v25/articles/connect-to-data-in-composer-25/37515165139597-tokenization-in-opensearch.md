---
title: "Tokenization in OpenSearch "
id: 37515165139597
section: "Connect to Data in Composer 25"
product: "Logi Composer v25"
url: https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/37515165139597-Tokenization-in-OpenSearch
updated_at: 2026-05-26T22:05:58Z
---

# Tokenization in OpenSearch 

# Tokenization in OpenSearch

Keep in mind that OpenSearch, by default, tokenizes or analyzes fields that are of type `text`. As a result, strings consisting of two or more words may become separate fields when connected to Composer (for example, city names like
*Las Vegas*). To disable this process and ensure that a string field is not analyzed, specify its type as `keyword`:

City: {
type: "keyword"
}

To learn more about tokenization in Elasticsearch, see [Get Trained Models API.](https://www.elastic.co/guide/en/elasticsearch/reference/8.2/get-trained-models.html#ml-get-trained-models-query-params)

**Important:** If you are connecting to OpenSearch versions earlier than 2.x, use the [Elasticsearch 7 connector](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932728155405-Manage-the-Elasticsearch-Connector).
