---
title: "Tokenization in Elasticsearch"
id: 43701010734605
section: "Connect to Data in Composer 26"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701010734605-Tokenization-in-Elasticsearch
updated_at: 2026-05-29T14:07:44Z
---

# Tokenization in Elasticsearch

# Tokenization in Elasticsearch

Keep in mind that Elasticsearch, by default, tokenizes or analyzes fields that are of type `text`. As a result, strings consisting of two or more words may become separate fields when connected to Composer (for example, city names like
*Las Vegas*). To disable this process and ensure that a string field is not analyzed, specify its type as `keyword`:

City: {
type: "keyword"
}

To learn more about tokenization in Elasticsearch, see [Get Trained Models API.](https://www.elastic.co/guide/en/elasticsearch/reference/8.2/get-trained-models.html#ml-get-trained-models-query-params)
