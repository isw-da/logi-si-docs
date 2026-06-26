---
title: "Applying Group Filters"
id: 4402537800599
section: "Use Dashboards and Visuals in Composer v5"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4402537800599-Applying-Group-Filters
updated_at: 2021-09-15T02:21:40Z
---

# Applying Group Filters

# Applying Group Filters

You can use group filters to filter the aggregated result set of a visual. Group filters are filters based on metrics and custom metrics, rather than fields (row-level filters).

You can create custom metrics or derived fields to use as a group filter on the fly. See [*Accessing the Derived Field Editor from the Filters Sidebar*](https://devnet.logianalytics.com/hc/en-us/articles/4402537770263-Accessing-the-Derived-Field-Editor-from-the-Filters-Sidebar) and [*Accessing the Custom Metrics Editor from the Filters Sidebar*](https://devnet.logianalytics.com/hc/en-us/articles/4402537758743-Accessing-the-Custom-Metrics-Editor-from-the-Filters-Sidebar) for information on how to access the Derived Field Editor or the Custom Metrics Editor from the Filters sidebar.

Group filters are applied in the same way row-level filters are applied. Using group filters, you can filter on saved custom metrics that are not applied to your visual. Remember that metrics and custom metrics can be limited at the data source level. If the Filters sidebar does not display all fields, refresh the field at the data source to display all elements within the data. For steps, see [*Displaying All Unique Elements for a Selected Filter Panel Attribute*](https://devnet.logianalytics.com/hc/en-us/articles/4402552910615-Displaying-All-Unique-Elements-for-a-Selected-Filter-Panel-Attribute).

The following visual styles do not support group filters:

* Arc gauges
* KPI charts
* Histograms
* Marker maps
* Raw Data Tables

Global dashboard filters do not include group filters that may be applied to the visuals in the dashboard, even if all the visuals on the dashboard use the same data source. You also cannot apply a group filter to your dashboard; only row-level filters (and keyset filters) can be applied globally to a dashboard.

![](https://devnet.logianalytics.com/hc/article_attachments/4406753437463/noteicon.jpg) When working with multiple filter types, row-level filters are applied first to a visual, keyset filters are applied next, and group filters are applied last on the aggregated result set.

Read the following topics for more information:

* [*Applying a Group Filter from a Metric*](https://devnet.logianalytics.com/hc/en-us/articles/4402537799959-Applying-a-Group-Filter-from-a-Metric)
* [*Applying a Group Filter from a Custom Metric*](https://devnet.logianalytics.com/hc/en-us/articles/4402537799319-Applying-a-Group-Filter-from-a-Custom-Metric)
