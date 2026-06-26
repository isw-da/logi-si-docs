---
title: "Elasticsearch Source Document Storage Configurations"
id: 34932736907661
section: "Connect to Data in Composer 25"
product: "Logi Composer v25"
url: https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932736907661-Elasticsearch-Source-Document-Storage-Configurations
updated_at: 2026-05-26T22:06:37Z
---

# Elasticsearch Source Document Storage Configurations

# Elasticsearch Source Document Storage Configurations

Elasticsearch data stores generally store the original JSON source documents passed when Elasticsearch performs its document indexing in the `_source` field in the index. However, some organizations disable the `_source` field to save storage and thus do not store the original JSON source documents.

Composer Elasticsearch 7 and 8 connectors support Elasticsearch data stores with any of the following source document configurations:

* Source documents disabled. For example:

  ...
  "mappings": {  
   "\_source": {  
   "enabled": false
  },
  }
  ...
* Source documents enabled, but with some source exclusions. For example:

  ...
  "mappings": {
  "\_source": {
  "enabled": true,
  "includes": [
  "order\_\*"
  ],
  "excludes": [
  "order\_items.\*"
  ]
  }
  },
  ...
* Source documents enabled, with no exclusions.

  ...
  "mappings": {  
   "\_source": {  
   "enabled": true
  }
  },
  ...

The data sources created from connections to Elasticsearch data stores with any of these configurations function almost identically.

## Known Issue Summary

The following known issues exist when the `_source` field is disabled or when it is enabled with exclusions:

* **Raw data presentation will vary, depending on the source from which the raw field data is fetched.** In particular, fused data sources may be affected where Elasticsearch indices with different mappings are joined (for example, when such indices are joined by an IP field and one of them allows Composer to fetch the data from the original documents but another requires Composer to fetch the data from doc values). See [Raw Data Differences](#Raw) .
* **The last value metric may be computed incorrectly for nested fields.** Last value metrics are computed incorrectly when a time field is higher in the nested hierarchy or when a time field does not belong to the same hierarchy as the metric field.
* **Raw data is not available for some nested fields in multi-index Elasticsearch data sources.** When a nested field exists in some indices but is absent in other indices, the field's raw data is not available. It is represented as having a NULL value in all documents when it is included in a table.
* **Some nested fields are not searchable in multi-index data sources.** When a nested field exists in some indices but is absent in other indices, it cannot be used in text search queries. Such fields will not be used for text searches.

## Raw Data Differences

The following Composer functions are impacted by the source document storage configuration of your Elasticsearch data stores:

* The data source collection preview on the Indices tab of the data source configuration
* Tables
* Text search results
* Last value metric computations.

Composer fetches the raw value of a field (including its last value metric result) in the following order:

1. If the field is stored, the stored value is fetched.
2. If the field is available in the original stored document, the value in the original stored document is fetched.
3. If doc values are available for the field and the field is not a text field, the doc value is fetched. For more information, see [Text Field Raw Data Considerations](#Text).

Results vary based on the source from which the value was fetched, as described in the following table:

| Value Fetched From | Differences from the original stored document |
| --- | --- |
| The stored value | * NULL values in arrays are excluded. * Arrays may be sorted, completely or partially. * Numeric values may be approximated. * IPv6 addresses are normalized. |
| The doc value | * NULL values in arrays are excluded. * Arrays may be sorted, completely or partially. * Duplicates in `string (keyword)` arrays are excluded, completely or partially. * Numeric values may be approximated. * IPv6 addresses are normalized. |

### Text Field Raw Data Considerations

Doc values are enabled by default for all fields, except for text fields. Consequently, by default, even if the original document is not stored or some fields are excluded from it, raw data is available for all fields, except for text fields.

An alternative structure called field data can be used for text fields. However, field data contains a set of terms for a text field, not its original value.

For this reason, raw data for a text field is not available if the text field is not stored in the index and cannot be fetched from the original document.

For example, the following mapping specifies that original documents should not be stored and declares two fields: `name` of type `keyword` and `description` of type `text`:

{
"mappings": {
"\_source": {
"enabled": false
},
"properties": {
"name": {
"type": "keyword"
},
"description": {
"type": "text"
}
}
}
}

Raw data for the text field `description` is not available in the index. To make raw data available for this field, declare it stored, as shown below:

{
"mappings": {
"\_source": {
"enabled": false
},
"properties": {
"name": {
"type": "keyword"
},
"description": {
"type": "text",
"store": true
}
}
}
}
