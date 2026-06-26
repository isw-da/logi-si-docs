---
title: "Derived Field Editor"
id: 43701095677581
section: "Manipulate Data In The Composer 26 Data Store"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701095677581-Derived-Field-Editor
updated_at: 2026-05-29T14:11:07Z
---

# Derived Field Editor

# Derived Field Editor

Composer provides a Derived Field Editor to help you create and test derived fields for a data source.

To define derived fields for a data source, you must have:

* Read permission for the data source and the Edit Calculations privilege, or
* Write permission for the data source.

The Derived Field Editor:

![Build, edit, and test a derived field here](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46242638806669 "Derived Field work area")

The numbered regions are:

1. Derived Field Label: Mandatory, fewer than 255 characters long.
2. Editing space: Build your expression in this space. Syntax highlighting improves the readability of your expression.
3. Expression Builder: This tool includes Row Level Functions and Fields to help you build your derived field.
4. Preview space: Shows a preview of the results of your expression.
5. Calculation Help: Provides more detailed information about the types of expressions Composer supports.

Create a derived field by defining a formula composed of metrics and attributes that include row level functions. You can also include existing derived fields in your new derived field formula. Composer automatically assigns data types to your derived fields.

Derived Field Editor Features:

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
* Row Level Functions and Fields sections always appear in the Expression Builder.
* Autocomplete functionality is included: Type two letters and a list of possible auto-completions appears.

  1. Function completions provide the type of function, the name of the function, the description of the function, and an example of how the function is used, including parameters.
  2. Field completions are available by typing either the field ID or the field label. The field ID appears in square brackets next to the field label when the two are different. Field completions provide the type of the field, the field label and ID, expressions for derived fields, and information about whether the field is hidden (as applicable).
  3. Metric completions provide the metric label and the expression that will be inserted into the editor when the metric is selected.
* Syntax and validation errors are shown in the Preview area.
* When you're creating or editing an expression, select **Cancel** to return your expression to the initial state.
* Composer disables the **Save** button, preventing you from saving a derived field unless it has a successfully run expression.
* When you close the editor with unsaved changes, Composer displays a confirmation message.

  + Select **Cancel** to continue editing or changing the text of the label for your derived field.
  + Select **Discard** to discard your changes. If you are editing an existing item, your last saved version remains in Composer.
  + If you select **Discard** while creating a new expression, Composer returns you to the source work area.

Access the Derived Field Editor in the following ways:

* [Access the Derived Field Editor from a Data Source](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701067056269-Access-the-Derived-Field-Editor-from-a-Data-Source)
* [Access the Derived Field Editor from the Metric Selection Dialog](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701067026573-Access-the-Derived-Field-Editor-from-the-Metric-Selection-Dialog)
* [Access the Derived Field Editor from the Group Selection Dialog](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701083392781-Access-the-Derived-Field-Editor-from-the-Group-Selection-Dialog)
* [Access the Derived Field Editor from the Color Sidebar](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701066890253-Access-the-Derived-Field-Editor-from-the-Color-Sidebar)
* [Access the Derived Field Editor from the Filters Sidebar](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701066934285-Access-the-Derived-Field-Editor-from-the-Filters-Sidebar)
