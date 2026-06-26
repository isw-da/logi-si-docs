---
title: "Derived Field Editor"
id: 4405851014551
section: "Manipulate Data in Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405851014551-Derived-Field-Editor
updated_at: 2021-09-21T01:28:06Z
---

# Derived Field Editor

# Derived Field Editor

  

Composer provides a Derived Field Editor to help you create and test derived fields for a data source. To define derived fields for a data source, you must have access to the data source.

The Derived Field Editor is depicted below.

![](https://devnet.logianalytics.com/hc/article_attachments/4406747432727/derived-field-editor_480x265.png)

The numbered regions are:

1. Derived field name
2. The type of derived field (attribute, time or number)
3. Row-Level Functions and the Attributes & Metrics list
4. Editing space
5. Preview space

Derived fields are created by defining a formula composed of metrics and attributes with row-level functions applied to them. You can also include existing derived fields in your new derived field's formula.

Note the following things about the Derived Field Editor:

* Syntax highlighting is used to improve the readability of expressions and provide visual clues about the items being used and their validity.

  The following parts of an expression are highlighted in different colors or with different text treatments: function names, both row level and aggregate; fields and metrics; keywords such as CASE and IN; example parameters; date period constants such as `year`; values such as numbers and `true` or `false`; strings; arithmetic operators such as `+`.

  References to fields that do not exist in the data source or are otherwise not usable in an expression are interpreted as values and show up in black, alerting you to possible typos or other issues.
* Hidden fields are listed in the left-hand panel editor when it is [accessed via the Fields tab of the data source configuration wizard](https://devnet.logianalytics.com/hc/en-us/articles/4405851013655-Access-the-Derived-Field-Editor-from-a-Data-Source-Configuration). (When the editor is accessed in other ways, hidden fields are not listed). Hidden fields appear italicized in the list to differentiate them from visible fields.
* The Row Level Function and Attributes & Metrics sections always appear in the left-hand panel.
* Attributes and metrics in the left-hand panel include tooltips that provide information on the field ID in square brackets when it is different from the field label. These tooltips provide the hidden status of the field, when applicable.
* Autocomplete functionality is supported in the editor. After typing two letters, a list of possible auto-completions appears.

  1. Function completions provide the type of function, the name of the function, the description of the function, and an example of how the function is used, including parameters.
  2. Field completions are available by typing either the field ID or the field label. The field ID appears in square brackets next to the field label when the two are different. Field completions provide the type of the field, the field label and ID, expressions for derived fields, and information about whether the field is hidden (as applicable).
  3. Metric completions provide the metric label and the expression that will be inserted into the editor when the metric is selected.
* In addition to the alert notifying you of syntax errors in an expression, an indicator appears in the gutter area. When you hover over the indicator, information about the syntax error, including line and column numbers, appears.

You can access the Derived Field Editor in the following ways:

* [*Access the Derived Field Editor from a Data Source Configuration*](https://devnet.logianalytics.com/hc/en-us/articles/4405851013655-Access-the-Derived-Field-Editor-from-a-Data-Source-Configuration)
* [*Access the Derived Field Editor from the Metric Selection Dialog*](https://devnet.logianalytics.com/hc/en-us/articles/4405859298071-Access-the-Derived-Field-Editor-from-the-Metric-Selection-Dialog)
* [*Access the Derived Field Editor from the Group Selection Dialog*](https://devnet.logianalytics.com/hc/en-us/articles/4405851012631-Access-the-Derived-Field-Editor-from-the-Group-Selection-Dialog)
* [*Access the Derived Field Editor from the Color Sidebar*](https://devnet.logianalytics.com/hc/en-us/articles/4405859295383-Access-the-Derived-Field-Editor-from-the-Color-Sidebar)
* [*Access the Derived Field Editor from the Filters Sidebar*](https://devnet.logianalytics.com/hc/en-us/articles/4405859296663-Access-the-Derived-Field-Editor-from-the-Filters-Sidebar)
