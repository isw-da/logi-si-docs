---
title: "Fuse Data Sources"
id: 43701072155405
section: "Connect to Data in Composer 26"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701072155405-Fuse-Data-Sources
updated_at: 2026-05-29T14:10:44Z
---

# Fuse Data Sources

# Fuse Data Sources

Data fusion is the concept of tying together data from two or more connections or flat files into a single source for exploration and analysis. After Composer joins the data, you can visualize the combined results in visuals and dashboards. Composer supports data fusion between all data connections it supports.

Fused data can generate more meaningful insights than what might be available in the data from a single data store. For example, suppose a data warehouse stores ticketing sales and events data in the following different data stores:

* Information about buyers and sellers stored in SAP IQ
* Events data stored in Elasticsearch
* Ticket sales stored in Cloudera Impala

You can create a Fusion source to fuse the data in these data stores together. After you create [a connection](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43700992503437-Add-Data-Store-Connections) to each data store, create [data entities](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701080568205-Source-Creation-Tab#Data) for each during [source creation](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701072201741-Create-a-Fusion-Source), you can join the data to use the combined data for more in-depth and complete analysis and exploration.

The following diagram depicts the basic concept of Composer data fusion.

![a diagram of multiple data sources brought together into a fused data source to create visualizations](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46242468408589 "a diagram of multiple data sources brought together into a fused data source to create visualizations")

Data fusion is available through Composer’s familiar and intuitive user interface. Step-by-step instructions are provided in [Create a Fusion Source](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701072201741-Create-a-Fusion-Source).

Fused data sets are stored as a Fusion source (![Data Fusion icon](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46242529959181)). Access Fusion data sources in the same way as other Composer data sources. Visualize the fused data in standard or custom charts.

For more information, see:

* [Data Fusion Limitations](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701134173965-Data-Fusion-Limitations)
* [Data Fusion Processing](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701104623373-Data-Fusion-Processing)
* [Data Fusion Join Rules](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701119743885-Data-Fusion-Join-Rules)
* [Filter Fused Data](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701134152333-Filter-Fused-Data)
* [Data Fusion Table Structures](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701072222221-Data-Fusion-Table-Structures)
* [Data Fusion Use Cases](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701104692237-Data-Fusion-Use-Cases)
* [Create a Fusion Source](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701072201741-Create-a-Fusion-Source)
* [Optimize Joins](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701134208269-Optimize-Joins)
