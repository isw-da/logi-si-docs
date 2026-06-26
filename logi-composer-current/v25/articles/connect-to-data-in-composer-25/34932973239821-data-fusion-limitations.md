---
title: "Data Fusion Limitations"
id: 34932973239821
section: "Connect to Data in Composer 25"
product: "Logi Composer v25"
url: https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932973239821-Data-Fusion-Limitations
updated_at: 2026-05-26T22:07:23Z
---

# Data Fusion Limitations

# Data Fusion Limitations

Fusion data sources have the following limitations:

* Fused data can be used in [tables (raw data)](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933270449037-Tables). Composer recommends that you initially use a subset of fields from Fusion data sources on tables to limit the load on Composer's query engine and improve its performance. You can change the subset in data source configurations and add additional fields, later, as needed while working on a dashboard.
* Text Search and Facet filtering are not supported for fused data, even if one or all the data sources defining the fused source support it.
* The [COUNT](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932868505741-Column-Aggregation-Functions), [COUNTD](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932868505741-Column-Aggregation-Functions), [TableCOUNT](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932868847245-Table-Aggregation-Functions), [TableCOUNTD](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932868847245-Table-Aggregation-Functions), [WindowCOUNT](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932858318989-Window-Aggregation-Functions), and [WindowCOUNTD](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932858318989-Window-Aggregation-Functions)[aggregate functions](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932900526221-Supported-Aggregation-Functions) are supported for Fusion data sources. However, they normally ignore null values for the specified field. Consequently, the result of these aggregate functions may not be the same as the actual number of records in the data. Use the wildcard character (\*) for `<field>` to include null values for the field in the count.
* [Live mode and historical playback](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933163012621-Live-Mode-and-Historical-Playback) are now supported for fused data.
* [Data Sharpening](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932821554701-Use-Data-Sharpening) is not supported for Fusion data sources.
* Two levels of top-of-the-top [multi-group](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932786052109-Visual-Type-Configuration-Properties#Multi-Group) fusion are supported. If you have [custom charts](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932772142477-Manage-Custom-Charts) that require more than two levels, you cannot use fused data sources.

  **Note:** 
  Multi-group fusion provides multiple levels of grouping under a single header. A multi-group variable is a stringified array of grouped queries. Each of the listed groups is described in the same manner as a group in the [Query Configuration Object](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933134876173-Query-Configuration-Object).
