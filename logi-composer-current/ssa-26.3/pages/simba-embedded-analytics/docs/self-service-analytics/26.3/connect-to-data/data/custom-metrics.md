> ## Documentation Index
> Fetch the complete documentation index at: https://insightsoftware.mintlify.site/llms.txt
> Use this file to discover all available pages before exploring further.

# Maintain Custom Metrics

*Custom metrics* serve as additional metrics to use with your visuals to help you analyze your data. When you define a [data source configuration](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/data-source-config-overview), you can create custom metrics for it. After custom metrics are defined, they are listed with the other metrics in your visuals and dashboards that use the data source and can be used just as any other metric. Access is defined by the [**Edit Calculations** privilege](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/aaa-ov#group-privilege-reference).

You can use custom metrics to aggregate data in different ways, whether from an entire data source or from a selected subset and, as needed, applying arithmetic or trigonometric operators to them. Because a custom metric represents aggregated data, it must be created using an [aggregate function](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/data/fx-aggregate). Data can be aggregated on a [column-wide scope](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/data/fx-aggregate#column-aggregation-functions), a [table scope](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/data/fx-aggregate#table-aggregation-functions), or a [window scope](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/data/fx-aggregate#window-aggregation-functions). For more information, see [Supported Aggregation Functions](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/data/fx-aggregate).

Scope of data refers to the domain of data included in a custom metric - whether a whole column from the data source, or just part of the column. Self-Service Analytics always excludes data from a custom metric if it is excluded from the visual by a filter even if that data would otherwise be included in the scope of the custom metric. You can further control what data is included by choosing metric functions that match the scope you want.

You can also use row-level functions and constant values to build your formula for a custom metric. In this way, you can create custom metrics of percentages, differences, averages, and the like. For more information about row-level functions, see [Supported Row-Level Functions](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/data/fx-aggregate#supported-row-level-functions).

Custom metrics can be filtered. Filters are created using the [SQL-like expressions](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/data/fx-aggregate#supported-sql-like-expressions) WHERE and TRANSFORM and may also use [date and time filter aggregate functions](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/data/fx-aggregate). For more information about the use of filters in custom metrics, see [Apply Filters to Custom Metrics](#apply-filters-to-custom-metrics).

For information on creating and deleting custom metrics, see the following links:

* [Custom Metrics Editor](#custom-metrics-editor)
* [Create and Modify Custom Metrics](#create-and-modify-custom-metrics)
* [Supported Aggregation Functions](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/data/fx-aggregate)
* [Supported Row-Level Functions](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/data/fx-aggregate#supported-row-level-functions)
* [Apply Filters to Custom Metrics](#apply-filters-to-custom-metrics)
* [Delete Custom Metrics](#delete-custom-metrics)
* [Custom Metric Examples](#custom-metric-examples)

<h2 id="create-and-modify-custom-metrics">
  Create and Modify Custom Metrics
</h2>

Custom metrics are created and modified using the [Custom Metrics Editor](#custom-metrics-editor).

**Create or modify a custom metric**

1. Access the Custom Metrics Editor in any of the ways described in [Custom Metrics Editor](#custom-metrics-editor).

2. Enter a label for the custom metric in the space labeled **Untitled Custom Metric**.

   <Note>
     If you are using non-Latin characters in your functions, the label for your custom metric should start with a letter or an underscore (\_) symbol followed by one or more letters, numbers, underscore, or period characters. Symbols other than the underscore (\_) or period (.) are not allowed.
   </Note>

3. Enter the expression for the custom metric in the editing space. Expressions should follow standard mathematical and logical syntax and are resolved using the standard order of operations. You can manually key in expressions or you can select the elements of your expressions from the menus at the left. The expression should not be assigned to a variable because the resolved value of the expression is assigned to the custom metric, which serves as the 'variable' to which the value is assigned. That is, enter `a / b` rather than `x = a / b`.

   [Row-level expressions](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/data/fx-aggregate#supported-row-level-functions) and [aggregate functions](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/data/fx-aggregate) can be used in custom metrics. In addition, custom metrics can be [filtered](#apply-filters-to-custom-metrics) (using [date and time filter aggregate functions](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/data/fx-aggregate#date-and-time-filter-aggregation-functions) and [SQL-like expressions](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/data/fx-aggregate#supported-sql-like-expressions)).

4. To test your custom metric, select **Run**.

   The editor attempts to calculate your custom metric. Any errors are reported. Any results are shown in the Preview area of the Custom Metrics Editor.

5. When you are finished creating or modifying your custom metric definition, select **Save**.

<h2 id="delete-custom-metrics">
  Delete Custom Metrics
</h2>

You can delete custom metrics from a data source in the [Custom Metrics](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/data-source-config-fields-tab#custom-metrics-table) tab on the Fields tab, or by deleting the source entirely.

<Warning>
  If you delete a source, your custom metric can not be used by associated visuals, materialized views, actions, or chart defaults.
</Warning>

<Note>
  If you try to delete a visual, filter snippet, dashboard, self service report, dashboard link, source, or source field, Self-Service Analytics displays an error message naming any objects dependent on the item you’re trying to delete. You can delete the item after you’ve removed the association from the dependent object. See [Fields Usage](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/data-source-config-fields-tab#fields-usage).
</Note>

**Delete custom metrics from a data source while editing the data source configuration**

1. Edit the data source configuration in the UI. See [Edit a Data Source](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/data-source-config-overview#edit-a-data-source).

2. Select the **Output** node.

3. Select **Custom Metrics** to open the Custom Metrics tab.

   <img src="https://mintcdn.com/insightsoftware/1fCfZrK84x8KmAw8/simba-embedded-analytics/docs/self-service-analytics/26.3/images/v26/work-areas/sources/custom-metrics-del-sm-26.png?fit=max&auto=format&n=1fCfZrK84x8KmAw8&q=85&s=0edc134806e33596fe47d091a47c0400" alt="user this work area to find, view, and add custom metrics. select expanded view to open a larger work area." width="725" height="418" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/v26/work-areas/sources/custom-metrics-del-sm-26.png" />

4. Locate the custom metric in the Custom Metrics table that you would like to remove.

5. Select the delete icon in the Actions column.

6. Select **Delete** in the pop-up confirmation dialog. The custom metric is deleted if it is not in use.

<h2 id="custom-metrics-editor">
  Custom Metrics Editor
</h2>

Self-Service Analytics provides a Custom Metrics Editor to help you create and test custom metrics for a data source.

To define custom metrics for a data source, you must have:

* Read permission for the data source and the [**Edit Calculations** privilege](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/aaa-ov#group-privilege-reference), or
* Write permission for the data source.

The Custom Metrics Editor is shown below. For every source added, the custom metric **Volume**, using a `Count(*)` expression is created.

<img src="https://mintcdn.com/insightsoftware/GTXU--ZlYc3DodOR/simba-embedded-analytics/docs/self-service-analytics/26.3/images/datasources/build-custom-metric-84.png?fit=max&auto=format&n=GTXU--ZlYc3DodOR&q=85&s=68ae5b818bf67cdd95cc458c294eaa1e" alt="Use this work area to build, test, and preview custom metrics" width="1277" height="842" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/datasources/build-custom-metric-84.png" />

The numbered regions are:

1. Custom Metric Label: Mandatory, fewer than 255 characters long.
2. Editing space: Build your expression in this space. Syntax highlighting improves the readability of your expression.
3. Expression Builder work area: Includes a Function Library, Row Level Functions, and Fields to help you build your custom metric.
4. Preview space: Shows a preview of the results of your expression.
5. Calculation Help: Provides more detailed information about the types of metrics Self-Service Analytics supports.

Create a custom metric by defining a formula composed of metrics and attributes that include row level functions and aggregation functions. You can include existing custom metrics in your new custom metric formula, and control the visibility of each metric.

Custom Metrics Editor Features:

* Syntax highlighting improves the readability of your expressions to provide visual clues about the items being used and their validity.

  Parts of an expression are highlighted in different colors or with different text treatments:

  * function names, both row level and aggregate
  * fields and metrics
  * keywords such as CASE and IN
  * example parameters
  * date period constants such as `year`
  * values such as numbers and `true` or `false`
  * strings
  * arithmetic operators such as `+`

  References to fields that do not exist in the data source or are otherwise not usable in an expression are interpreted as values. These are shown in black, alerting you to possible typos or other issues.

* Limit the number of records shown in **Preview** by adjusting the **Rows per Page**.

* The Function Library, Row Level Functions and Fields sections always appear in the Expression Builder.

* Autocomplete functionality is included: Type two letters and a list of possible auto-completions appears.

  1. Function completions provide the type of function, the name of the function, the description of the function, and an example of how the function is used, including parameters.
  2. Field completions are available by typing either the field ID or the field label. The field ID appears in square brackets next to the field label when the two are different. Field completions provide the type of the field, the field label and ID.
  3. Metric completions provide the metric label and the expression that will be inserted into the editor when the metric is selected.

* Syntax and validation errors are shown in the Preview area.

* When you're creating or editing an expression, select **Cancel** to return your expression to the initial state.

* Self-Service Analytics disables the **Save** button, preventing you from saving a custom metric unless it has a successfully run expression.

* When you close the editor with unsaved changes, Self-Service Analytics displays a confirmation message.

  * Select **Cancel** to continue editing or changing the text of the label for your custom metric.
  * Select **Discard** to discard your changes. If you are editing an existing item, your last saved version remains in Self-Service Analytics.
  * If you select **Discard** while creating a new expression, Self-Service Analytics returns you to the source work area.

Access the Custom Metrics Editor in the following ways:

* [Access the Custom Metrics Editor from a Data Source Configuration](#access-the-custom-metrics-editor-from-a-data-source)
* [Access the Custom Metrics Editor from the Metric Selection Dialog](#access-the-custom-metrics-editor-from-the-metric-selection)
* [Access the Custom Metrics Editor from the Group Selection Dialog](#access-the-custom-metrics-editor-from-the-group-selection-dialog)
* [Access the Custom Metrics Editor from the Color Sidebar](#access-the-custom-metrics-editor-from-the-color-sidebar)
* [Access the Custom Metrics Editor from the Filters Sidebar](#access-the-custom-metrics-editor-from-the-filters-sidebar)

<h2 id="access-the-custom-metrics-editor-from-the-color-sidebar">
  Access the Custom Metrics Editor from the Color Sidebar
</h2>

**Access the Custom Metrics Editor from the Color sidebar of a visual**

1. Select <img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/more-menu.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=1471c7a569a7e100cd7fa4083b04551a" alt="Selet the three dots icon to open a show more menu or take actions for the named column" width="21" height="12" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '21px', height: '12px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/more-menu.png" /> and then **Color** from the [visual drop-down menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup#use-the-visual-drop-down-menu) to access the Color sidebar.

   <img src="https://mintcdn.com/insightsoftware/b9ogX_L4Mqut_Uxb/simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/color-simple1-new.png?fit=max&auto=format&n=b9ogX_L4Mqut_Uxb&q=85&s=629a3f744a75d53b31d0c9f96fec3955" alt="" width="395" height="776" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/color-simple1-new.png" />

2. Select the **Color Attribute** box on the Color sidebar. A list of attribute, number, and time fields you can select for the color attribute appears in the Color sidebar.

   <img src="https://mintcdn.com/insightsoftware/1fCfZrK84x8KmAw8/simba-embedded-analytics/docs/self-service-analytics/26.3/images/v26/work-areas/sources/custom-met-visual-26.png?fit=max&auto=format&n=1fCfZrK84x8KmAw8&q=85&s=9ac96620848973830b09f494268899be" alt="add custom metric option from a visual color menu" width="402" height="500" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/v26/work-areas/sources/custom-met-visual-26.png" />

3. Select the add button in the Attribute, Number, or Time fields section of the sidebar. A menu opens with two options: **Add Derived Field** and **Add Custom Metric**.

4. Select **Add Custom Metric** to access the [Custom Metrics Editor](#custom-metrics-editor) and create a custom metric.

<h2 id="access-the-custom-metrics-editor-from-the-filters-sidebar">
  Access the Custom Metrics Editor from the Filters Sidebar
</h2>

**Access the Custom Metrics Editor from the Filters sidebar of a visual or dashboard**

1. Access the visual filter sidebar or the dashboard filter sidebar.

   * To access the visual filter sidebar, select the filter icon (<img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/filter-vis.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=0a044ea0662c55e06133074a55d93cd9" alt="select the filter icon to open the filters sidebar and add or edit filters" width="17" height="17" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '17px', height: '17px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/filter-vis.png" />) on the visual or select <img src="https://mintcdn.com/insightsoftware/cQU1Auv4yvPMjcip/simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/sidebar-filter.png?fit=max&auto=format&n=cQU1Auv4yvPMjcip&q=85&s=4b06f0c1f1b48c50da73f73672d5b1c6" alt="" width="20" height="21" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '20px', height: '21px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/sidebar-filter.png" /> on the [sidebar menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup#use-the-visual-sidebar-menu). If the visual is in a dashboard, select **Settings** from the [visual menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup#use-the-visual-drop-down-menu) (<img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/more-menu.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=1471c7a569a7e100cd7fa4083b04551a" alt="Selet the three dots icon to open a show more menu or take actions for the named column" width="21" height="12" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '21px', height: '12px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/more-menu.png" />), then select the filter icon <img src="https://mintcdn.com/insightsoftware/cQU1Auv4yvPMjcip/simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/sidebar-filter.png?fit=max&auto=format&n=cQU1Auv4yvPMjcip&q=85&s=4b06f0c1f1b48c50da73f73672d5b1c6" alt="" width="20" height="21" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '20px', height: '21px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/sidebar-filter.png" /> on the [sidebar menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup#use-the-visual-sidebar-menu).
   * To access the dashboard filter sidebar, select the dashboard filter icon (<img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/filter-dash.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=68279f203a0950b32bfab88e7273d5ba" alt="" width="20" height="19" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '20px', height: '19px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/filter-dash.png" />) next to the dashboard title. The dashboard-level filter icon is available only when all the visuals are from the same data source.

   The Filters sidebar appears. Add or edit a filter.

2. Select the add icon <img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/add.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=9a24b95d9385f23950764407d5e9111a" alt="add icon" width="16" height="16" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '16px', height: '16px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/add.png" /> at the top of the Attribute, Number, or Time sections on the Row or Group tab. A menu opens with two options: **Add Derived Field** and **Add Custom Metric**.

3. Select **Add Custom Metric** to access the [Custom Metrics Editor](#custom-metrics-editor) and create a custom metric.

<h2 id="access-the-custom-metrics-editor-from-the-group-selection-dialog">
  Access the Custom Metrics Editor from the Group Selection Dialog
</h2>

**Access the Custom Metrics Editor from the Group selection dialog of a visual**

1. On a visual, select the group label (x-axis label) to view the Group selection dialog.

   <img src="https://mintcdn.com/insightsoftware/b9ogX_L4Mqut_Uxb/simba-embedded-analytics/docs/self-service-analytics/26.3/images/v26/work-areas/visuals/group-selection-panel-26.png?fit=max&auto=format&n=b9ogX_L4Mqut_Uxb&q=85&s=43ecaeb674dd8138336f00a03c233dd8" alt="use this work area to select a group for the selected access" width="348" height="590" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/v26/work-areas/visuals/group-selection-panel-26.png" />

2. Select the add button in the Attributes, Number or Time section of the dialog. A menu opens with two options: **Add Derived Field** and **Add Custom Metric**.

3. Select **Add Custom Metric** to access the [Custom Metrics Editor](#custom-metrics-editor) and create a custom metric.

<h2 id="access-the-custom-metrics-editor-from-the-metric-selection">
  Access the Custom Metrics Editor from the Metric Selection Dialog
</h2>

**Access the Custom Metrics Editor from the metric selection dialog of a visual**

1. On a visual, select the metric label (y-axis label) to view the Metric selection dialog.

   <img src="https://mintcdn.com/insightsoftware/b9ogX_L4Mqut_Uxb/simba-embedded-analytics/docs/self-service-analytics/26.3/images/v26/work-areas/visuals/custom-metric-y-26.png?fit=max&auto=format&n=b9ogX_L4Mqut_Uxb&q=85&s=c72319ea87c3d93ff7b621ad5638bdb2" alt="add or edit custom metrics" width="358" height="373" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/v26/work-areas/visuals/custom-metric-y-26.png" />

2. Select the add icon in the Number or Custom Metric section of the dialog. A menu opens with two options: **Add Derived Field** and **Add Custom Metric**.

3. Select **Add Custom Metric** to access the [Custom Metrics Editor](#custom-metrics-editor) and create a custom metric.

You can also access the [Custom Metrics Editor](#custom-metrics-editor) when you edit any custom metric listed on the Metric selection dialog. See the following steps.

**Edit a custom metric**

1. On a visual, select the metric label (y-axis label) to view the Metric selection dialog.

2. Locate a custom metric listed on the Metric selection dialog and select the ellipsis (<img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/more-menu.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=1471c7a569a7e100cd7fa4083b04551a" alt="Selet the three dots icon to open a show more menu or take actions for the named column" width="21" height="12" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '21px', height: '12px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/more-menu.png" />) next to it. The following menu appears:

   <img src="https://mintcdn.com/insightsoftware/b9ogX_L4Mqut_Uxb/simba-embedded-analytics/docs/self-service-analytics/26.3/images/v26/work-areas/visuals/y-axis-edit-metric-26.png?fit=max&auto=format&n=b9ogX_L4Mqut_Uxb&q=85&s=5a8c6b5fa9e74f3d171596b8170ede0b" alt="use this work area to format, edit, or remove a custom meric" width="346" height="282" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/v26/work-areas/visuals/y-axis-edit-metric-26.png" />

3. Select **Edit** on the menu to edit the custom metric. The [Custom Metrics Editor](#custom-metrics-editor) appears.

<h2 id="access-the-custom-metrics-editor-from-a-data-source">
  Access the Custom Metrics Editor from a Data Source Configuration
</h2>

**Access the Custom Metrics Editor from a data source configuration**

1. Edit the data source configuration in the UI. See [Edit a Data Source](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/data-source-config-overview#edit-a-data-source).

2. Select the **Output** node.

3. Select **Custom Metrics** to open the Custom Metrics tab, and **Expand View** to open a larger work area.

   <img src="https://mintcdn.com/insightsoftware/1fCfZrK84x8KmAw8/simba-embedded-analytics/docs/self-service-analytics/26.3/images/v26/work-areas/sources/custom-metrics-sm-26.png?fit=max&auto=format&n=1fCfZrK84x8KmAw8&q=85&s=c763b02441b1c71e5e72f0982b3349ed" alt="user this work area to find, view, and add custom metrics. select expanded view to open a larger work area." width="725" height="418" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/v26/work-areas/sources/custom-metrics-sm-26.png" />

   <img src="https://mintcdn.com/insightsoftware/1fCfZrK84x8KmAw8/simba-embedded-analytics/docs/self-service-analytics/26.3/images/v26/work-areas/sources/custom-metrics-exp-26.png?fit=max&auto=format&n=1fCfZrK84x8KmAw8&q=85&s=305dcf410197ec6a1d84601ad09a5cb1" alt="use this work area to manage your custom metrics" width="1203" height="667" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/v26/work-areas/sources/custom-metrics-exp-26.png" />

4. Select **Add Custom Metric** to add a custom metric.

5. Optionally, select an existing custom metric to modify the metric.

<h2 id="custom-metric-examples">
  Custom Metric Examples
</h2>

The following commonly used custom metrics demonstrate custom metric syntax. These examples work with your data source only if your data source contains fields of the same name and type. Change the fields to make them work with your data sources.

The following custom metric is the sum of a metric (`totallatearrivals`) between a specific date (`2018-01-01`) and the current date:

```
SUM(totallatearrivals) WHERE eventdate BETWEEN '2018-01-01' AND DATE()
```

in which:

* `totallatearrivals` can be replaced by your own metric
* `eventdate` can be replaced by your own date attribute
* `2018-01-01` can be replaced by a different specific date

The following aggregated field formula is the sum of a metric (`totallatearrivals`) from the previous period:

```
SUM(totallatearrivals) TRANSFORM eventdate = PreviousPeriod()
```

in which:

* `totallatearrivals` can be replaced by your own metric
* `eventdate` can be replaced by your own date attribute

The following custom metric produces the difference between the current sum of a metric (`totallatearrivals`) and the sum of the same metric from the previous period:

```
SUM(totallatearrivals) - (SUM(totallatearrivals) TRANSFORM eventdate = PreviousPeriod())
```

in which:

* `totallatearrivals` can be replaced by your own metric

<h2 id="apply-filters-to-custom-metrics">
  Apply Filters to Custom Metrics
</h2>

You can apply filters to your custom metrics. This means that attributes from the data can be applied as filter parameters to further refine and narrow your results. Specifying a filter lets you perform a calculation within a predefined range, for example, determining sales results within a certain period of time or within a certain demographic.

This topic covers the application of filters to custom metrics and provides instructions covering the operators and syntax for integrating a filter into your custom metrics.

### Filter Syntax

To create a custom metric that includes filters, operators or expressions are required.

When integrating a filter within a custom metric, keep in mind that Self-Service Analytics supports certain operators and follows a logical structure. In general, creating a filtered custom metric entails selecting the appropriate function variable, integrating the desired attribute or metric, using the appropriate filter operators and Date function, and entering a date in the correct format. Self-Service Analytics custom metrics use one of the following general structures:

```xml theme={null}
<agg-function> WHERE <field> <operator> <values>
<agg-function> TRANSFORM <field> PreviousPeriod([offset,numPeriods])
```

where:

* `<agg-function>` is any of the aggregate functions described in [Supported Aggregation Functions](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/data/fx-aggregate).

* WHERE or TRANSFORM is the appropriate [SQL-like expression](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/data/fx-aggregate#supported-sql-like-expressions) used for custom metric filtering. TRANSFORM is used specifically with the `PreviousPeriod` [date and time filter aggregation function](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/data/fx-aggregate#date-and-time-filter-aggregation-functions). WHERE and TRANSFORM filters are always applied to the broadest possible expression. For example, the following two expressions are both valid, but the first applies the filters to both SUMs, while the second expression applies the filter only to `SUM(Sales)`.

  ```
  SUM(Profit)/SUM(Sales) WHERE zipcode IN (90210,94107,92101)
  SUM(Profit)/(SUM(Sales) WHERE zipcode IN (90210,94107,92101))
  ```

  WHERE clauses can include row-level functions and expressions.

* `<field>` is a field (metric or attribute) in the data.

* `<operator>` is one of the operators shown in the following table:

  <table>
    <thead>
      <tr>
        <th colSpan={3} scope="col">Filters</th>
      </tr>

      <tr>
        <th scope="col">Capability</th>
        <th>Operators</th>
        <th>Notes</th>
      </tr>
    </thead>

    <tbody>
      <tr>
        <td>Filtering on attribute options</td>

        <td>
          NULL check: IS NULL, IS NOT NULL

          <br />

          Single value: =, !=, STARTS WITH, ENDS WITH, CONTAINS

          <br />

          Multiple values: IN(), NOT IN()
        </td>

        <td>
          * Non-numeric fields such as Name, Address and State can be used as a filter.

          <br />

          * References to an attribute in a field must be enclosed in single quotation marks. For example:

          <br />

          ```
          SUM(Sales) WHERE State = ‘Florida’
          ```

          <br />

          * Values specified for STARTS WITH, ENDS WITH, and CONTAINS are case-sensitive. The following example would show sales for states that include the lowercase letters `ia`, such as California and Louisiana (and others):

          <br />

          ```
          SUM(Sales) WHERE State CONTAINS 'ia'
          ```
        </td>
      </tr>

      <tr>
        <td>Filtering on date field options</td>
        <td>Date range operator: BETWEEN</td>

        <td>
          * Standard date formats (see [Convert Attributes to Time Fields in Data Source Field Specifications](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/data/data-number-formatting#convert-attributes-to-time-fields-in-data-source-field)) are supported (such as 'yyyy-mm-dd', 'dd/mm/yyyy' including 'hh-mm-ss') .
          * Date (‘01-01-2015’) must be enclosed in single quotation marks.
          * Supported time periods are YEAR, MONTH, WEEK, or DAY
        </td>
      </tr>

      <tr>
        <td>Filtering on numeric fields and custom metric options</td>
        <td>>, \<, =, !=</td>

        <td>
          * References to a numeric field must be enclosed in single quotation marks
          * References can be made to other custom metrics (using the custom metric label)
        </td>
      </tr>
    </tbody>
  </table>

* `<value>` is an appropriate value, based on the requirements of the [SQL-like expression](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/data/fx-aggregate#supported-sql-like-expressions). Values can be specific numbers or dates, or one of the [date and time filter aggregation functions](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/data/fx-aggregate#date-and-time-filter-aggregation-functions).

### Examples

The following table provides examples of filtered custom metrics.

<table>
  <thead>
    <tr>
      <th colSpan={2} scope="col">Filtered Custom Metric Examples</th>
    </tr>

    <tr>
      <th scope="col">Capability</th>
      <th>Example</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>Filtering on Attribute options</td>

      <td>
        ```
        SUM(Sales) WHERE State = ‘California’
        SUM(Profit)/SUM(Sales) WHERE zipcode IN (90210,94107,92101)
        ```
      </td>
    </tr>

    <tr>
      <td>Filtering on Date field options</td>

      <td>
        ```
        MIN(Margin) WHERE Sale_Date BETWEEN ‘2013-01-01’ AND DateADD(MONTH, 6, ‘01-01-2014’))
        ```
      </td>
    </tr>

    <tr>
      <td>Filtering on numeric fields and custom metric options</td>

      <td>
        ```
        SUM(Sales)/(SUM(Sales) WHERE User_Income = ‘0 to $25000’)
        ```

        <br />

        To calculate year over year growth:

        <br />

        ```
        ((SUM(price) WHERE sale_date BETWEEN '2014-01-01' AND '2015-01-01') - (SUM(price) WHERE sale_date BETWEEN '2013-01-01' AND '2014-01-01')) / (SUM(price) WHERE sale_date BETWEEN '2012-01-01' AND '2013-01-01') * 100
        ```
      </td>
    </tr>

    <tr>
      <td>Comparing the difference between the current period to last period</td>

      <td>
        Compare this period's deliveries to last period's deliveries:

        <br />

        ```
        SUM(deliveries) TRANSFORM delivery_date = PreviousPeriod()
        ```
      </td>
    </tr>

    <tr>
      <td>Using a row-level expression or function in a filter</td>

      <td>
        ```
        SUM(plannedsales) WHERE maxage - age > 30
        SUM(plannedsales) WHERE UPPER(gender) = 'MALE'
        ```
      </td>
    </tr>
  </tbody>
</table>

<h2 id="metrics">
  Metrics
</h2>

In Self-Service Analytics, a metric is a numeric or attribute field that has been aggregated. Numeric fields can be aggregated using aggregation methods Distinct Count, Count, SUM, AVG, MIN, MAX, and LAST VALUE. An attribute field can only be aggregated using Distinct Count and Count. See [Distinct Counts](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/data/fx-aggregate#distinct-counts). See also [Metric Aggregation Functions](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/data/fx-aggregate#metric-aggregation-functions).

After a numeric or attribute field becomes a metric by aggregation, it can be used in the y-axis of visuals (that support a y-axis). You can also change the aggregation of a metric in tables using the table context menu and the Table Settings sidebar. See [Change Metric Aggregation in Tables](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/rdt#change-metric-aggregation-in-tables).
