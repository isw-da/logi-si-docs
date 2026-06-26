---
title: "Custom Metrics Editor"
id: 4405859284119
section: "Manipulate Data in Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405859284119-Custom-Metrics-Editor
updated_at: 2021-09-21T01:30:40Z
---

# Custom Metrics Editor

# Custom Metrics Editor

  

Composer provides a Custom Metrics Editor to help you create and test custom metrics for a data source. To define custom metrics for a data source, you must have access to the data source.

The Custom Metrics Editor is depicted below.

![](https://devnet.logianalytics.com/hc/article_attachments/4406743856407/custom-metrics-editor_576x318.png)

The numbered regions are:

1. Custom metric name
2. Functions, Row-Level Functions, and Attributes & Metrics list
3. Editing space
4. Preview space

Custom metrics are created by defining a formula composed of metrics and attributes with row-level functions and aggregation functions applied to them. You can also include existing custom metrics in your new custom metric's formula.

Note the following things about the Custom Metrics Editor:

* Syntax highlighting is used to improve the readability of expressions and provide visual clues about the items being used and their validity.

  The following parts of an expression are highlighted in different colors or with different text treatments: function names, both row level and aggregate; fields and metrics; keywords such as CASE and IN; example parameters; date period constants such as `year`; values such as numbers and `true` or `false`; strings; arithmetic operators such as `+`.

  References to fields that do not exist in the data source or are otherwise not usable in an expression are interpreted as values and show up in black, alerting you to possible typos or other issues.
* The Function Library, Row Level Function, and Attributes & Metrics sections always appear in the left-hand panel.
* Attributes and metrics in the left-hand panel include tooltips that provide information on the field ID in square brackets when it is different from the field label.
* Autocomplete functionality is supported in the editor. After typing two letters, a list of possible auto-completions appears.

  1. Function completions provide the type of function, the name of the function, the description of the function, and an example of how the function is used, including parameters.
  2. Field completions are available by typing either the field ID or the field label. The field ID appears in square brackets next to the field label when the two are different. Field completions provide the type of the field, the field label and ID.
  3. Metric completions provide the metric label and the expression that will be inserted into the editor when the metric is selected.
* In addition to the alert notifying you of syntax errors in an expression, an indicator appears in the gutter area. When you hover over the indicator, information about the syntax error, including line and column numbers, appears.

You can access the Custom Metrics Editor in the following ways:

* [*Access the Custom Metrics Editor from a Data Source Configuration*](https://devnet.logianalytics.com/hc/en-us/articles/4405851001751-Access-the-Custom-Metrics-Editor-from-a-Data-Source-Configuration)
* [*Access the Custom Metrics Editor from the Metric Selection Dialog*](https://devnet.logianalytics.com/hc/en-us/articles/4405859282967-Access-the-Custom-Metrics-Editor-from-the-Metric-Selection-Dialog)
* [*Access the Custom Metrics Editor from the Group Selection Dialog*](https://devnet.logianalytics.com/hc/en-us/articles/4405859281943-Access-the-Custom-Metrics-Editor-from-the-Group-Selection-Dialog)
* [*Access the Custom Metrics Editor from the Color Sidebar*](https://devnet.logianalytics.com/hc/en-us/articles/4405850999831-Access-the-Custom-Metrics-Editor-from-the-Color-Sidebar)
* [*Access the Custom Metrics Editor from the Filters Sidebar*](https://devnet.logianalytics.com/hc/en-us/articles/4405851000727-Access-the-Custom-Metrics-Editor-from-the-Filters-Sidebar)
