---
title: "Tokenization in Elasticsearch"
id: 4402955485719
section: "Connect to Data in Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4402955485719-Tokenization-in-Elasticsearch
updated_at: 2021-08-07T17:29:59Z
---

# Tokenization in Elasticsearch

# Tokenization in Elasticsearch

Keep in mind that Elasticsearch, by default, tokenizes or analyzes fields that are of type `text`. As a result, strings consisting of two or more words may become separate fields when connected to Composer (for example, city names like
*Las Vegas*). To disable this process and ensure that a string field is not analyzed, specify its type as `keyword`:

```
City: {  
    type: "keyword"  
    }
```
