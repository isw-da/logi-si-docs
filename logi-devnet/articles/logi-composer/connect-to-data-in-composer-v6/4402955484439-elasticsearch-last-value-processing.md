---
title: "Elasticsearch Last Value Processing"
id: 4402955484439
section: "Connect to Data in Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4402955484439-Elasticsearch-Last-Value-Processing
updated_at: 2021-08-07T17:30:02Z
---

# Elasticsearch Last Value Processing

# Elasticsearch Last Value Processing

There are situations in which the Elasticsearch connector cannot compute the Last Value metric correctly.

1. When the original value *is* available for a metric field, an error appears in either of the following situations:

   * Both metric and group fields are nested and related.
   * Both metric and time fields are nested and related.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404959473559/noteicon.jpg) The Elasticsearch connector still may not always choose the maximum value among several values for the Last Value of a time field. This should happen only in the following cases:

   * When the metric field is nested and neither the group or time field is located in the same hierarchy (group and time fields are either at the root level or belong to another hierarchy)
   * When the Last Value is an array.
2. When the original value *is not* available for a metric field (the result is fetched from doc values or stored fields), an error appears when the metric field is nested and the time field is not located on the same or lower level in the hierarchy.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404959473559/noteicon.jpg) The Elasticsearch connector still may not always choose the maximum value among several values for the Last Value of a time field. This should happen only when the Last Value is an array.
