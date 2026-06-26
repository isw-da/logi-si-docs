---
title: "Dashboard Designer: Interactive Filters (pre-v2019.2)"
id: 5281588173975
section: "Dashboards"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281588173975-Dashboard-Designer-Interactive-Filters-pre-v2019-2
updated_at: 2022-05-03T22:08:21Z
---

# Dashboard Designer: Interactive Filters (pre-v2019.2)

# Dashboard Designer: Interactive Filters (*pre-v2019.2*)

> ![red exclamation point](https://devnet.logianalytics.com/hc/article_attachments/5432173635607/criticalicon.gif "Important")
>
> This topic applies to *pre-v2019.2* of the application. For current Dashboard documentation, see [Dashboard Designer (v2019.2+)](https://devnet.logianalytics.com/hc/en-us/articles/5281580652951-Dashboard-Designer-v2019-2-).

Interactive filters are filters that appear as tiles directly on the **Dashboard** itself. Filter tiles have several different styles to choose between, and can resize and scale just like any other tile. Filters can apply to as many or as few reports as needed.

## Type

You can choose between four styles of filters and two orientations:

* *Single Choice* A drop down menu with all possible filter values. Users can choose one value.
* *Multiple Choice* A check list with all possible filter values. Users can choose multiple values.
* *Single Slider* – Users can choose one value by sliding a point along a scale.
* *Range Slider* – Users can choose multiple values between two points on a scale.

You may also select whether the filter values are oriented horizontally or vertically.

## Reports

Select which reports the filter applies to. Only reports that include the filter data field are valid.

## Data

Select which data field the filter applies to. The filter is automatically populated with values from the data field. You can select which value or values are selected by default when the Dashboard is executed. Select *Prompt for value* to prompt users to enter a value when running the Dashboard.

## Text and Format

Choose how the filter value labels are styled and formatted.

## Exports (*v2018.2+*)

Interactive filter tiles will not display in exported **Dashboards**, which are exported in the form of **Chained Reports**. Though the tiles themselves will not display, the default values set for the filters will apply to their corresponding reports and visualizations in the exported file. See [Exporting Dashboards (pre-v2019.2)](https://devnet.logianalytics.com/hc/en-us/articles/5281610715287-Exporting-Dashboards-pre-v2019-2-)

[![Concept Link Icon](https://devnet.logianalytics.com/hc/article_attachments/5432159914263/transparent.gif)See Also](javascript:void(0);)
