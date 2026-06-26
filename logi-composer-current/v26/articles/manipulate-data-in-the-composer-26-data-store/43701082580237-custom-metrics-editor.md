---
title: "Custom Metrics Editor"
id: 43701082580237
section: "Manipulate Data In The Composer 26 Data Store"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701082580237-Custom-Metrics-Editor
updated_at: 2026-05-29T14:11:11Z
---

# Custom Metrics Editor

# Custom Metrics Editor

Composer provides a Custom Metrics Editor to help you create and test custom metrics for a data source.

To define custom metrics for a data source, you must have:

* Read permission for the data source and the **Edit Calculation** privilege, or
* Write permission for the data source.

The Custom Metrics Editor is shown below. For every source added, the custom metric **Volume**, using a `Count(*)` expression is created.

![Use this work area to build, test, and preview custom metrics](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46242635486221 "Custom Metrics Editor work area")

The numbered regions are:

1. Custom Metric Label: Mandatory, fewer than 255 characters long.
2. Editing space: Build your expression in this space. Syntax highlighting improves the readability of your expression.
3. Expression Builder work area: Includes a Function Library, Row Level Functions, and Fields to help you build your custom metric.
4. Preview space: Shows a preview of the results of your expression.
5. Calculation Help: Provides more detailed information about the types of metrics Composer supports.

Create a custom metric by defining a formula composed of metrics and attributes that include row level functions and aggregation functions. You can include existing custom metrics in your new custom metric formula, and control the visibility of each metric.

Custom Metrics Editor Features:

* Syntax highlighting improves the readability of your expressions to provide visual clues about the items being used and their validity.

  Parts of an expression are highlighted in different colors or with different text treatments:

  + function names, both row level and aggregate
  + fields and metrics
  + keywords such as CASE and IN
  + example parameters
  + date period constants such as `year`
  + values such as numbers and `true` or `false`
  + strings
  + arithmetic operators such as `+`

  References to fields that do not exist in the data source or are otherwise not usable in an expression are interpreted as values. These are shown in black, alerting you to possible typos or other issues.
* Limit the number of records shown in **Preview** by adjusting the **Rows per Page**.
* The Function Library, Row Level Functions and Fields sections always appear in the Expression Builder.
* Autocomplete functionality is included: Type two letters and a list of possible auto-completions appears.

  1. Function completions provide the type of function, the name of the function, the description of the function, and an example of how the function is used, including parameters.
  2. Field completions are available by typing either the field ID or the field label. The field ID appears in square brackets next to the field label when the two are different. Field completions provide the type of the field, the field label and ID.
  3. Metric completions provide the metric label and the expression that will be inserted into the editor when the metric is selected.
* Syntax and validation errors are shown in the Preview area.
* When you're creating or editing an expression, select **Cancel** to return your expression to the initial state.
* Composer disables the **Save** button, preventing you from saving a custom metric unless it has a successfully run expression.
* When you close the editor with unsaved changes, Composer displays a confirmation message.

  + Select **Cancel** to continue editing or changing the text of the label for your custom metric.
  + Select **Discard** to discard your changes. If you are editing an existing item, your last saved version remains in Composer.
  + If you select **Discard** while creating a new expression, Composer returns you to the source work area.

Access the Custom Metrics Editor in the following ways:

* [Access the Custom Metrics Editor from a Data Source Configuration](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701077822605-Access-the-Custom-Metrics-Editor-from-a-Data-Source-Configuration)
* [Access the Custom Metrics Editor from the Metric Selection Dialog](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701030041613-Access-the-Custom-Metrics-Editor-from-the-Metric-Selection-Dialog)
* [Access the Custom Metrics Editor from the Group Selection Dialog](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701048112525-Access-the-Custom-Metrics-Editor-from-the-Group-Selection-Dialog)
* [Access the Custom Metrics Editor from the Color Sidebar](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701015283341-Access-the-Custom-Metrics-Editor-from-the-Color-Sidebar)
* [Access the Custom Metrics Editor from the Filters Sidebar](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701015326349-Access-the-Custom-Metrics-Editor-from-the-Filters-Sidebar)
