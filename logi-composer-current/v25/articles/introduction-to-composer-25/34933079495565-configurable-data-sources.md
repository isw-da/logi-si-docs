---
title: "Configurable Data Sources"
id: 34933079495565
section: "Introduction to Composer 25"
product: "Logi Composer v25"
url: https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933079495565-Configurable-Data-Sources
updated_at: 2026-05-26T22:07:41Z
---

# Configurable Data Sources

# Configurable Data Sources

Data queries in Composer use data source configurations to identify the data needed and the data store from which it should be obtained. A Composer data source configuration defines the following settings:

| Setting | Description |
| --- | --- |
| connection definition | The connection string that should be used to connect to your data store. |
| data store table, index, or data to use | The table, index, or other data in your data store that should be collected when the data source is used in a Composer query. |
| data customizations | Any customizations you want made to the data collected from the data store. This can include customizations to the field names, types, partition settings, distinct count activation for the data, filter display customizations, and other configurations such as the time pattern or granularity used for time fields or the aggregation used for numeric fields. |
| derived fields and custom metrics | Any derived fields or custom metrics you want calculated from the data collected from the data store. |
| refresh schedule | The schedule by which the data collected from the data store is refreshed. Derived field and custom metric data is also refreshed on this schedule, after the data store data is updated. |
| time bar settings | The default time bar settings that should be used for visuals and dashboards created using the data source. |

For more information about creating and managing data source configurations, see [Manage Data Sources](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932941009037-Manage-Data-Sources).

In addition to standard data source configurations, Composer provides methods of analyzing data from multiple sources at the same time, including the ability to fuse data sources. See [Multisource Analysis](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933104442765-Multisource-Analysis).
