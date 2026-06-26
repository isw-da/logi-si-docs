---
title: "Live Mode and Historical Playback"
id: 4402552905879
section: "Use Dashboards and Visuals in Composer v5"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4402552905879-Live-Mode-and-Historical-Playback
updated_at: 2021-09-15T02:22:39Z
---

# Live Mode and Historical Playback

# Live Mode and Historical Playback

Live mode and historical playback (also known as Data DVR) allow you to get the most from data stores that support playback. The only difference between live mode and historical playback is the time range that is selected.

* Live mode refreshes field data on your visuals for date-time fields that are indexed as playable. In live mode, your data plays forever without an end date.
* Historical playback (Data DVR) shows the historical record of field data for date-time fields that are indexed as playable. Playback can show up to the last moment before the current period in your data.

Live mode and historical playback require:

* A date-time field in your data store (data base) that is either indexed or partitioned.

  If indexed, the index should be non-clustered.

  If your data store does not support indexing or partitioning, then live mode and historical playback are not available for that data. For most data stores, indexing is the default.
* The time zone used by the date-time field in the Composer data source should align with the time zone used by the date-time field in your data store. The data source time zone can be set using the **Time Zone** attribute on the [Fields tab](https://devnet.logianalytics.com/hc/en-us/articles/4402537783063-Fields-Tab) of the data source definition.
* The data source should have live mode enabled. Use the **Live Mode** switch on the Visuals tab of the data source configuration. See [*Configuring Time Bar Defaults*](https://devnet.logianalytics.com/hc/en-us/articles/4402537788055-Configuring-Time-Bar-Defaults).
* The data store should be capable of receiving new or updated data, that is, data that is not static like flat files.

Playback mode (Data DVR) is available if the date-time field in your data source has the **playable** property set to **True** and the granularity of the field is not greater than **day**. When is the **playable** property in the data source set to true?

1. If the date-time field in the data store is indexed or partitioned. For Impala data stores, this option can also be enabled if the selected date field has a connection to the partitioned date field.
2. If the data store is Spark (for example, Spark SQL)
3. In Amazon Redshift, data sources for the first sort key.

See also [*Configuring Time Bar Defaults*](https://devnet.logianalytics.com/hc/en-us/articles/4402537788055-Configuring-Time-Bar-Defaults).

Live mode and historical playback are supported for even time intervals. See [*Even Time Intervals*](https://devnet.logianalytics.com/hc/en-us/articles/4402537753623-Even-Time-Intervals). Live mode an historical playback are not supported for fused data sources. See [*Data Fusion Limitations*](https://devnet.logianalytics.com/hc/en-us/articles/4402537803799-Data-Fusion-Limitations).
