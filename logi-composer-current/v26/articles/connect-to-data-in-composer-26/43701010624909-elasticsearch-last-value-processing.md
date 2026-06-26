---
title: "Elasticsearch Last Value Processing"
id: 43701010624909
section: "Connect to Data in Composer 26"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701010624909-Elasticsearch-Last-Value-Processing
updated_at: 2026-05-29T14:07:43Z
---

# Elasticsearch Last Value Processing

# Elasticsearch Last Value Processing

There are situations in which the Elasticsearch connector cannot compute the Last Value metric correctly.

1. When the original value *is* available for a metric field, an error appears in either of the following situations:

   * Both metric and group fields are nested and related.
   * Both metric and time fields are nested and related.

   **Note:** 
   The Elasticsearch connector still may not always choose the maximum value among several values for the Last Value of a time field. This should happen only in the following cases:

   * When the metric field is nested and neither the group or time field is located in the same hierarchy (group and time fields are either at the root level or belong to another hierarchy)
   * When the Last Value is an array.
2. When the original value *is not* available for a metric field (the result is fetched from doc values or stored fields), an error appears when the metric field is nested and the time field is not located on the same or lower level in the hierarchy.

   **Note:** 
   The Elasticsearch connector still may not always choose the maximum value among several values for the Last Value of a time field. This should happen only when the Last Value is an array.
