---
title: "Apply Group Filters"
id: 34932955067661
section: "Use Dashboards and Visuals in Composer 25"
product: "Logi Composer v25"
url: https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932955067661-Apply-Group-Filters
updated_at: 2026-05-26T22:07:19Z
---

# Apply Group Filters

# Apply Group Filters

You can use group filters to filter the aggregated result set of a visual or filter snippet. Group filters are filters based on metrics and custom metrics, rather than fields (row-level filters).

You can create custom metrics or derived fields to use as a group filter on the fly. See [Access the Derived Field Editor from the Filters Sidebar](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932881853581-Access-the-Derived-Field-Editor-from-the-Filters-Sidebar) and [Access the Custom Metrics Editor from the Filters Sidebar](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932813600525-Access-the-Custom-Metrics-Editor-from-the-Filters-Sidebar) for information on how to access the Derived Field Editor or the Custom Metrics Editor from the Filters sidebar.

Group filters are applied in the same way row-level filters are applied. Using group filters, you can filter on saved custom metrics that are not applied to your visual or filter snippet. Metrics and custom metrics can be limited at the data source level. If the Filters sidebar does not display all fields, refresh the field at the data source to display all elements within the data. For steps, see [Display All Unique Elements for a Selected Filter Panel Attribute](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933180187917-Display-All-Unique-Elements-for-a-Selected-Filter-Panel-Attribute).

The following visual styles do not support group filters:

* [Arc gauges](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933196538125-Arc-Gauges)
* [KPI charts](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933237388941-KPI-Charts)
* [Histograms](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933212496141-Bars-Histograms)
* [Marker maps](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933230696461-Maps#Marker "Marker maps")
* [Tables of raw data](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933270449037-Tables)

Global dashboard filters do not include group filters that may be applied to the visuals or filter snippets in the dashboard, even if all items on the dashboard use the same data source. You also cannot apply a group filter to your dashboard; only row-level filters (and keyset filters) can be applied globally to a dashboard.

**Note:** 
When working with multiple filter types, row-level filters are applied first to a visual, keyset filters are applied next, and group filters are applied last on the aggregated result set.

Read the following topics for more information:

* [Apply a Group Filter from a Metric](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932986213773-Apply-a-Group-Filter-from-a-Metric)
* [Apply a Group Filter from a Custom Metric](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932969662477-Apply-a-Group-Filter-from-a-Custom-Metric)
