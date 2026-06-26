---
title: "Apply Group Filters"
id: 4405851068567
section: "Use Dashboards and Visuals in Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405851068567-Apply-Group-Filters
updated_at: 2021-09-21T01:28:38Z
---

# Apply Group Filters

# Apply Group Filters

You can use group filters to filter the aggregated result set of a visual. Group filters are filters based on metrics and custom metrics, rather than fields (row-level filters).

You can create custom metrics or derived fields to use as a group filter on the fly. See [*Access the Derived Field Editor from the Filters Sidebar*](https://devnet.logianalytics.com/hc/en-us/articles/4405859296663-Access-the-Derived-Field-Editor-from-the-Filters-Sidebar) and [*Access the Custom Metrics Editor from the Filters Sidebar*](https://devnet.logianalytics.com/hc/en-us/articles/4405851000727-Access-the-Custom-Metrics-Editor-from-the-Filters-Sidebar) for information on how to access the Derived Field Editor or the Custom Metrics Editor from the Filters sidebar.

Group filters are applied in the same way row-level filters are applied. Using group filters, you can filter on saved custom metrics that are not applied to your visual. Remember that metrics and custom metrics can be limited at the data source level. If the Filters sidebar does not display all fields, refresh the field at the data source to display all elements within the data. For steps, see [*Display All Unique Elements for a Selected Filter Panel Attribute*](https://devnet.logianalytics.com/hc/en-us/articles/4405851199895-Display-All-Unique-Elements-for-a-Selected-Filter-Panel-Attribute).

The following visual styles do not support group filters:

* [Arc gauges](https://devnet.logianalytics.com/hc/en-us/articles/4405851211287-Arc-Gauges)
* [KPI charts](https://devnet.logianalytics.com/hc/en-us/articles/4405859522327-KPI-Charts)
* [Histograms](https://devnet.logianalytics.com/hc/en-us/articles/4405859514775-Bars-Histograms)
* [Marker maps](https://devnet.logianalytics.com/hc/en-us/articles/4405851224727-Marker-Maps)
* [Tables of raw data](https://devnet.logianalytics.com/hc/en-us/articles/4405851243799-Tables)

Global dashboard filters do not include group filters that may be applied to the visuals in the dashboard, even if all the visuals on the dashboard use the same data source. You also cannot apply a group filter to your dashboard; only row-level filters (and keyset filters) can be applied globally to a dashboard.

![](https://devnet.logianalytics.com/hc/article_attachments/4406747382295/noteicon.jpg) When working with multiple filter types, row-level filters are applied first to a visual, keyset filters are applied next, and group filters are applied last on the aggregated result set.

Read the following topics for more information:

* [*Apply a Group Filter from a Metric*](https://devnet.logianalytics.com/hc/en-us/articles/4405859351703-Apply-a-Group-Filter-from-a-Metric)
* [*Apply a Group Filter from a Custom Metric*](https://devnet.logianalytics.com/hc/en-us/articles/4405851067415-Apply-a-Group-Filter-from-a-Custom-Metric)
