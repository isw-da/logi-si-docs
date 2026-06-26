---
title: "OpenSearch Last Value Processing"
id: 37515123456909
section: "Connect to Data in Composer 25"
product: "Logi Composer v25"
url: https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/37515123456909-OpenSearch-Last-Value-Processing
updated_at: 2026-05-26T22:05:56Z
---

# OpenSearch Last Value Processing

# OpenSearch Last Value Processing

There are situations in which the OpenSearch connector cannot compute the Last Value metric correctly.

1. When the original value *is* available for a metric field, an error appears in either of the following situations:

   * Both metric and group fields are nested and related.
   * Both metric and time fields are nested and related.

   **Note:** 
   The OpenSearch connector still may not always choose the maximum value among several values for the Last Value of a time field. This should happen only in the following cases:

   * When the metric field is nested and neither the group or time field is located in the same hierarchy (group and time fields are either at the root level or belong to another hierarchy)
   * When the Last Value is an array.
2. When the original value *is not* available for a metric field (the result is fetched from doc values or stored fields), an error appears when the metric field is nested and the time field is not located on the same or lower level in the hierarchy.

   **Note:** 
   The OpenSearch connector still may not always choose the maximum value among several values for the Last Value of a time field. This should happen only when the Last Value is an array.

**Important:** If you are connecting to OpenSearch versions earlier than 2.x, use the [Elasticsearch 7 connector](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932728155405-Manage-the-Elasticsearch-Connector).
