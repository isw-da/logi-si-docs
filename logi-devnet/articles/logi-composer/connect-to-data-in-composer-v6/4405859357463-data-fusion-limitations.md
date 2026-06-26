---
title: "Data Fusion Limitations"
id: 4405859357463
section: "Connect to Data in Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405859357463-Data-Fusion-Limitations
updated_at: 2021-09-21T01:28:41Z
---

# Data Fusion Limitations

# Data Fusion Limitations

Fusion data sources have the following limitations:

* Fused data can be used in [tables (raw data)](https://devnet.logianalytics.com/hc/en-us/articles/4405851243799-Tables). Composer recommends that you initially use a subset of fields from Fusion data sources on tables to limit the load on Composer's query engine and improve its performance. You can change the subset in data source configurations and add additional fields, later, as needed while working on a dashboard.
* Faceted searches are not supported for fused data, even if one or all the data sources defining the fused source support it.
* There is no support for security filters or column-level security for Fusion data sources. Row-level security is inherited from the parent sources.
* The [COUNT](https://devnet.logianalytics.com/hc/en-us/articles/4405859301911-Column-Aggregation-Functions), [COUNTD](https://devnet.logianalytics.com/hc/en-us/articles/4405859301911-Column-Aggregation-Functions), [TableCOUNT](https://devnet.logianalytics.com/hc/en-us/articles/4405859303319-Table-Aggregation-Functions), [TableCOUNTD](https://devnet.logianalytics.com/hc/en-us/articles/4405859303319-Table-Aggregation-Functions), [WindowCOUNT](https://devnet.logianalytics.com/hc/en-us/articles/4405851016343-Window-Aggregation-Functions), and [WindowCOUNTD](https://devnet.logianalytics.com/hc/en-us/articles/4405851016343-Window-Aggregation-Functions)[aggregate functions](https://devnet.logianalytics.com/hc/en-us/articles/4405859304727-Supported-Aggregation-Functions) are supported for Fusion data sources. However, they normally ignore null values for the specified field. Consequently, the result of these aggregate functions may not be the same as the actual number of records in the data. Use the wild card character (\*) for `<field>` to include null values for the field in the count.
* [Live mode and historical playback](https://devnet.logianalytics.com/hc/en-us/articles/4405851191447-Live-Mode-and-Historical-Playback) are not supported for fused data.
* [Data Sharpening](https://devnet.logianalytics.com/hc/en-us/articles/4405851008023-Use-Data-Sharpening) is not supported for Fusion data sources.
* Two levels of top-of-the-top [multi-group](https://devnet.logianalytics.com/hc/en-us/articles/4405851154199-Visualization-Variable-Descriptions#Multi-Group) fusion are supported. If you have [custom charts](https://devnet.logianalytics.com/hc/en-us/articles/4405859248279-Manage-Custom-Charts) that require more than two levels, you cannot use fused data sources.
* To import (using the OVERWRITE strategy) a dashboard that uses a Fusion data source with custom metrics or derived fields, users with the necessary write permissions and the **Can Manage Connections**[privilege](https://devnet.logianalytics.com/hc/en-us/articles/4405859114647-Group-Privilege-Reference) must also have read permissions for the Fusion data source and its parent sources.
