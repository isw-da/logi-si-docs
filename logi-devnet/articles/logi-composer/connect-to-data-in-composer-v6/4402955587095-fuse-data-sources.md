---
title: "Fuse Data Sources"
id: 4402955587095
section: "Connect to Data in Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4402955587095-Fuse-Data-Sources
updated_at: 2021-08-07T17:31:06Z
---

# Fuse Data Sources

# Fuse Data Sources

Data fusion is the concept of tying together two or more data sources as a single data source for exploration and analysis. After the Composer server joins together data from various data sources, you can visualize the combined results in visuals and dashboards. Composer supports data fusion between all data stores it supports.

Fused data can generate more meaningful insights than what might be available in the data from a single data source. For example, suppose a data warehouse stores ticketing sales and events data in the following different data stores:

* Information about buyers and sellers stored in SAP IQ
* Events data stored in Elasticsearch
* Ticket sales stored in Cloudera Impala

You can fuse the data in these data stores together into a single Fusion data source. This combined data can be used for more in-depth and complete analysis and exploration.

The following diagram depicts the basic concept of Composer data fusion.

![](https://devnet.logianalytics.com/hc/article_attachments/4404959530007/fusion-scheme_282x354.png)

Data fusion is available through Composer’s familiar and intuitive user interface. Connections to data fusion data sources can be established using Composer's standard connection interface. Step-by-step instructions are provided in [*Create a Fusion Data Source*](https://devnet.logianalytics.com/hc/en-us/articles/4402955589015-Create-a-Fusion-Data-Source).

Fused data sets are stored as a Fusion data source (![Data Fusion icon](https://devnet.logianalytics.com/hc/article_attachments/4404959530391/fusion_24x23.png)). The Fusion data sources can be accessed and interacted with in the same manner as any other standard data source. You can visualize the fused data in standard or custom charts. Text fields can be joined in fused data sources.

For more information, see the following sections:

* [*Data Fusion Limitations*](https://devnet.logianalytics.com/hc/en-us/articles/4402955585815-Data-Fusion-Limitations)
* [*Data Fusion Processing*](https://devnet.logianalytics.com/hc/en-us/articles/4402955587735-Data-Fusion-Processing)
* [*Data Fusion Join Rules*](https://devnet.logianalytics.com/hc/en-us/articles/4402955588375-Data-Fusion-Join-Rules)
* [*Filter Fused Data*](https://devnet.logianalytics.com/hc/en-us/articles/4402955585175-Filter-Fused-Data)
* [*Data Fusion Table Structures*](https://devnet.logianalytics.com/hc/en-us/articles/4402955589783-Data-Fusion-Table-Structures)
* [*Data Fusion Use Cases*](https://devnet.logianalytics.com/hc/en-us/articles/4402955590423-Data-Fusion-Use-Cases)
* [*Create a Fusion Data Source*](https://devnet.logianalytics.com/hc/en-us/articles/4402955589015-Create-a-Fusion-Data-Source)
* [*Optimize Joins*](https://devnet.logianalytics.com/hc/en-us/articles/4402955586455-Optimize-Joins)
