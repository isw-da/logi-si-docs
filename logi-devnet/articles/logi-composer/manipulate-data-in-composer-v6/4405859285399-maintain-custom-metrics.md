---
title: "Maintain Custom Metrics"
id: 4405859285399
section: "Manipulate Data in Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405859285399-Maintain-Custom-Metrics
updated_at: 2021-09-21T01:27:58Z
---

# Maintain Custom Metrics

# Maintain Custom Metrics

*Custom metrics*, formerly called *calculations*, serve as additional metrics to use with your visuals to help you analyze your data. When you define a [data source configuration](https://devnet.logianalytics.com/hc/en-us/articles/4405851027479-Manage-Data-Source-Configurations), you can create custom metrics for it. After custom metrics are defined, they are listed with the other metrics in your visuals and dashboards that use the data source and can be used just as any other metric.

You can use custom metrics to aggregate data in different ways, whether from an entire data source or from a selected subset and, as needed, applying arithmetic operators to them. Because a custom metric represents aggregated data, it must be created using an [aggregate function](https://devnet.logianalytics.com/hc/en-us/articles/4405859304727-Supported-Aggregation-Functions). Data can be aggregated on a [column-wide scope](https://devnet.logianalytics.com/hc/en-us/articles/4405859301911-Column-Aggregation-Functions), a [table scope](https://devnet.logianalytics.com/hc/en-us/articles/4405859303319-Table-Aggregation-Functions), or a [window scope](https://devnet.logianalytics.com/hc/en-us/articles/4405851016343-Window-Aggregation-Functions). For more information, see [*Supported Aggregation Functions*](https://devnet.logianalytics.com/hc/en-us/articles/4405859304727-Supported-Aggregation-Functions).

*Scope of data* refers to the domain of data included in a custom metric - whether a whole column from the data source, or just part of the column. Composer always excludes data from a custom metric if it is excluded from the visual by a filter even if that data would otherwise be included in the scope of the custom metric. You can further control what data is included by choosing metric functions that match the scope you want.

You can also use row-level functions and constant values to build your formula for a custom metric. In this way, you can create custom metrics of percentages, differences, averages, and the like. For more information about row-level functions, see [*Supported Row-Level Functions*](https://devnet.logianalytics.com/hc/en-us/articles/4405851021079-Supported-Row-Level-Functions).

Custom metrics can be filtered. Filters are created using the [SQL-like expressions](https://devnet.logianalytics.com/hc/en-us/articles/4405859312535-Supported-SQL-Like-Expressions) WHERE and TRANSFORM and may also use [date and time filter aggregate functions](https://devnet.logianalytics.com/hc/en-us/articles/4405859304727-Supported-Aggregation-Functions). For more information about the use of filters in custom metrics, see [*Apply Filters to Custom Metrics*](https://devnet.logianalytics.com/hc/en-us/articles/4405851003543-Apply-Filters-to-Custom-Metrics).

For information on creating and deleting custom metrics, see the following links:

* [*Custom Metrics Editor*](https://devnet.logianalytics.com/hc/en-us/articles/4405859284119-Custom-Metrics-Editor)
* [*Create and Modify Custom Metrics*](https://devnet.logianalytics.com/hc/en-us/articles/4405850997911-Create-and-Modify-Custom-Metrics)
* [*Duplicate Custom Metrics*](https://devnet.logianalytics.com/hc/en-us/articles/4405850996887-Duplicate-Custom-Metrics)
* [*Supported Aggregation Functions*](https://devnet.logianalytics.com/hc/en-us/articles/4405859304727-Supported-Aggregation-Functions)
* [*Supported Row-Level Functions*](https://devnet.logianalytics.com/hc/en-us/articles/4405851021079-Supported-Row-Level-Functions)
* [*Apply Filters to Custom Metrics*](https://devnet.logianalytics.com/hc/en-us/articles/4405851003543-Apply-Filters-to-Custom-Metrics)
* [*Delete Custom Metrics*](https://devnet.logianalytics.com/hc/en-us/articles/4405850998935-Delete-Custom-Metrics)
* [*Custom Metric Examples*](https://devnet.logianalytics.com/hc/en-us/articles/4405851002647-Custom-Metric-Examples)
