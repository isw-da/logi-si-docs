---
title: " Maintain Custom Metrics"
id: 34932836147341
section: "Manipulate Data In The Composer 25 Data Store"
product: "Logi Composer v25"
url: https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932836147341--Maintain-Custom-Metrics
updated_at: 2026-05-26T22:06:59Z
---

#  Maintain Custom Metrics

# Maintain Custom Metrics

*Custom metrics*, formerly called *calculations*, serve as additional metrics to use with your visuals to help you analyze your data. When you define a [data source configuration](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932941009037-Manage-Data-Sources), you can create custom metrics for it. After custom metrics are defined, they are listed with the other metrics in your visuals and dashboards that use the data source and can be used just as any other metric.

You can use custom metrics to aggregate data in different ways, whether from an entire data source or from a selected subset and, as needed, applying arithmetic or trigonometric operators to them. Because a custom metric represents aggregated data, it must be created using an [aggregate function](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932900526221-Supported-Aggregation-Functions). Data can be aggregated on a [column-wide scope](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932868505741-Column-Aggregation-Functions), a [table scope](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932868847245-Table-Aggregation-Functions), or a [window scope](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932858318989-Window-Aggregation-Functions). For more information, see [Supported Aggregation Functions](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932900526221-Supported-Aggregation-Functions).

Scope of data refers to the domain of data included in a custom metric - whether a whole column from the data source, or just part of the column. Composer always excludes data from a custom metric if it is excluded from the visual by a filter even if that data would otherwise be included in the scope of the custom metric. You can further control what data is included by choosing metric functions that match the scope you want.

You can also use row-level functions and constant values to build your formula for a custom metric. In this way, you can create custom metrics of percentages, differences, averages, and the like. For more information about row-level functions, see [Supported Row-Level Functions](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932902575629-Supported-Row-Level-Functions).

Custom metrics can be filtered. Filters are created using the [SQL-like expressions](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932861652621-Supported-SQL-Like-Expressions) WHERE and TRANSFORM and may also use [date and time filter aggregate functions](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932900526221-Supported-Aggregation-Functions). For more information about the use of filters in custom metrics, see [Apply Filters to Custom Metrics](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932814261773-Apply-Filters-to-Custom-Metrics).

For information on creating and deleting custom metrics, see the following links:

* [Custom Metrics Editor](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932820475405-Custom-Metrics-Editor)
* [Create and Modify Custom Metrics](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932813034765-Create-and-Modify-Custom-Metrics)
* [Supported Aggregation Functions](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932900526221-Supported-Aggregation-Functions)
* [Supported Row-Level Functions](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932902575629-Supported-Row-Level-Functions)
* [Apply Filters to Custom Metrics](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932814261773-Apply-Filters-to-Custom-Metrics)
* [Delete Custom Metrics](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932819677837-Delete-Custom-Metrics)
* [Custom Metric Examples](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932848105101-Custom-Metric-Examples)
