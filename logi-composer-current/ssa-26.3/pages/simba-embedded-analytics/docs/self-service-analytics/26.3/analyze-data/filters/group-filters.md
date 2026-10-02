> ## Documentation Index
> Fetch the complete documentation index at: https://insightsoftware.mintlify.site/llms.txt
> Use this file to discover all available pages before exploring further.

# Group Filters

You can use group filters to filter the aggregated result set of a visual or filter snippet. Group filters are filters based on metrics and custom metrics, rather than fields (row-level filters).

You can create custom metrics or derived fields to use as a group filter on the fly. See [Access the Derived Field Editor from the Filters Sidebar](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/data/derived-fields#access-the-derived-field-editor-from-the-filters-sidebar) and [Access the Custom Metrics Editor from the Filters Sidebar](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/data/custom-metrics#access-the-custom-metrics-editor-from-the-filters-sidebar) for information on how to access the Derived Field Editor or the Custom Metrics Editor from the Filters sidebar.

Group filters are applied in the same way row-level filters are applied. Using group filters, you can filter on saved custom metrics that are not applied to your visual or filter snippet. Metrics and custom metrics can be limited at the data source level. If the Filters sidebar does not display all fields, refresh the field at the data source to display all elements within the data. For steps, see [Display All Unique Elements for a Selected Filter Panel Attribute](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/filters/filters-attr#display-all-unique-elements-for-a-selected-filter-panel).

The following visual types do not support group filters:

* [Arc gauges](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/arc)
* [KPI charts](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/arc#kpi-charts)
* [Histograms](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/bar-standard#bars-histograms)
* [Marker maps](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/map-chart-styles#marker-maps)
* [Tables of raw data](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/rdt)

Global dashboard filters do not include group filters that may be applied to the visuals or filter snippets in the dashboard, even if all items on the dashboard use the same data source. You also cannot apply a group filter to your dashboard; only row-level filters (and keyset filters) can be applied globally to a dashboard.

<Note>
  When working with multiple filter types, row-level filters are applied first to a visual, keyset filters are applied next, and group filters are applied last on the aggregated result set.
</Note>

Read the following topics for more information:

* [Apply a Group Filter from a Metric](#apply-a-group-filter-from-a-metric)
* [Apply a Group Filter from a Custom Metric](#apply-a-group-filter-from-a-custom-metric)

<h2 id="apply-a-group-filter-from-a-metric">
  Apply a Group Filter from a Metric
</h2>

Suppose you want to find product sales greater than \$200,000 for the last quarter within the greater Los Angeles area. You might create a group filter using the following steps. This example requires that you have already applied a row-level filter for the city of Los Angeles.

Group filters can only be applied from a specific visual or filter snippet. They cannot be applied to a dashboard.

**Create the group filter**

1. Select the filter icon (<img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/filter-vis.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=0a044ea0662c55e06133074a55d93cd9" alt="select the filter icon to open the filters sidebar and add or edit filters" width="17" height="17" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '17px', height: '17px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/filter-vis.png" />) or select **Settings** from the [menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup#use-the-visual-drop-down-menu) (<img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/more-menu.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=1471c7a569a7e100cd7fa4083b04551a" alt="Selet the three dots icon to open a show more menu or take actions for the named column" width="21" height="12" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '21px', height: '12px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/more-menu.png" />) and then select <img src="https://mintcdn.com/insightsoftware/cQU1Auv4yvPMjcip/simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/sidebar-filter.png?fit=max&auto=format&n=cQU1Auv4yvPMjcip&q=85&s=4b06f0c1f1b48c50da73f73672d5b1c6" alt="" width="20" height="21" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '20px', height: '21px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/sidebar-filter.png" /> on the [sidebar menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup#use-the-visual-sidebar-menu).

   The Filters sidebar appears showing any filters that have been applied.

2. Select **Add Filter**. A work area opens for applying Row, Group, and Saved filters.

3. Select the Group tab and select the numeric field **Sales** on the tab.

   The Range tab appears in the Filters sidebar. By default, the Aggregation function is set to Sum. You can select other values from the drop-down list.

4. Select the **Greater Than** operator in the Operator selection box. This allows you to input a threshold value, rather than a value range.

5. Specify a threshold value of 200000 in the Value box.

6. Select **Apply**.

7. After the visual updates, select **Group** and then select **Product Category**. This displays all sales of products totally over \$200,000.

8. Remember to [save your filter](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/filters/saved-filters-maintaining).

<h2 id="apply-a-group-filter-from-a-custom-metric">
  Apply a Group Filter from a Custom Metric
</h2>

Suppose you want to find product purchases made by males within certain areas of Los Angeles, while also comparing their income levels. Specifically, you are interested in men whose sales average more than \$100,000. You might create a filter using the following steps. This example requires that you have already applied a row-level filter for the city of Los Angeles.

Since you do not have a custom metric created yet for average sales, one needs to be created.

**Create the custom metric**

1. Select the filter icon on the [visual](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/filters/filters#apply-a-row-level-filter-to-a-visual-or-filter-snippet), [filter snippet](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/widgets/fltrsnp-ov), or [dashboard](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/filters/filters#apply-a-row-level-filter-to-a-dashboard) to access the appropriate filter sidebar.

   * To access the filter sidebar, select its filter icon (<img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/filter-vis.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=0a044ea0662c55e06133074a55d93cd9" alt="select the filter icon to open the filters sidebar and add or edit filters" width="17" height="17" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '17px', height: '17px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/filter-vis.png" />) or select **Settings** from the [menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup#use-the-visual-drop-down-menu) (<img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/more-menu.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=1471c7a569a7e100cd7fa4083b04551a" alt="" width="19" height="11" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '19px', height: '11px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/more-menu.png" />) and then select <img src="https://mintcdn.com/insightsoftware/cQU1Auv4yvPMjcip/simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/sidebar-filter.png?fit=max&auto=format&n=cQU1Auv4yvPMjcip&q=85&s=4b06f0c1f1b48c50da73f73672d5b1c6" alt="" width="20" height="21" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '20px', height: '21px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/sidebar-filter.png" /> on the [sidebar menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup#use-the-visual-sidebar-menu).
   * To access the dashboard filter sidebar, select its filter icon (<img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/filter-dash.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=68279f203a0950b32bfab88e7273d5ba" alt="" width="20" height="19" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '20px', height: '19px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/filter-dash.png" />). The dashboard-level filter icon is available only when all the visuals are from the same data source.

   The Filters sidebar appears showing any filters that have been applied.

2. Select **Add Filter**. A work area opens for applying Row, Group, and Saved filters.

3. Select an add icon <img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/add.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=9a24b95d9385f23950764407d5e9111a" alt="add icon" width="16" height="16" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '16px', height: '16px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/add.png" /> and select **Add Custom Metric** from the resulting menu. The Custom Metrics Editor appears.

4. In the Function Library, double-select **AVG(field)**.

5. In Fields, select **Sales**.

6. Select **Run** to see a preview of the results.

7. Name your custom metric and select **Save**.

8. Close the Custom Metrics Editor.

Now that you have created and successfully saved the custom metric you want to use, you can apply it to the visual, filter snippet, or dashboard.

**Filter your data by the aggregated field**

1. Select the filter icon on the [visual](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/filters/filters#apply-a-row-level-filter-to-a-visual-or-filter-snippet), [filter snippet](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/widgets/fltrsnp-ov), or [dashboard](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/filters/filters#apply-a-row-level-filter-to-a-dashboard) to access the appropriate filter sidebar.

   * To access the filter sidebar, select its filter icon (<img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/filter-vis.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=0a044ea0662c55e06133074a55d93cd9" alt="select the filter icon to open the filters sidebar and add or edit filters" width="17" height="17" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '17px', height: '17px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/filter-vis.png" />) or select **Settings** from the [menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup#use-the-visual-drop-down-menu) (<img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/more-menu.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=1471c7a569a7e100cd7fa4083b04551a" alt="Selet the three dots icon to open a show more menu or take actions for the named column" width="21" height="12" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '21px', height: '12px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/more-menu.png" />) and then select <img src="https://mintcdn.com/insightsoftware/cQU1Auv4yvPMjcip/simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/sidebar-filter.png?fit=max&auto=format&n=cQU1Auv4yvPMjcip&q=85&s=4b06f0c1f1b48c50da73f73672d5b1c6" alt="" width="20" height="21" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '20px', height: '21px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/sidebar-filter.png" /> on the [sidebar menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup#use-the-visual-sidebar-menu).
   * To access the dashboard filter sidebar, select its filter icon (<img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/filter-dash.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=68279f203a0950b32bfab88e7273d5ba" alt="" width="20" height="19" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '20px', height: '19px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/filter-dash.png" />). The dashboard-level filter icon is available only when all the visuals are from the same data source.

   The Filters sidebar appears showing any filters that have been applied.

2. Select **Add Filter**.

3. Ensure that the row-level filter for males in Los Angeles is applied.

4. Select **Add Filter**.

5. From the list of available attributes, select **Zipcode**.

6. Choose the zip codes you want to include in your results. For example, all the 900 zip codes or 90211, 90305, and 90701.

7. Select **Apply**.

8. Select **Add Filter**.

9. Select the **Group** tab.

10. Select your saved custom metric from the list of available custom metrics for use.

11. Select the **Operator** tab and then select the greater-than (>)operator.

12. In the value field, enter 100 and then select **Apply**. In the Filters sidebar , you can see all the filters you have applied thus far.

13. On the visual canvas, select **Group** and ensure **Product Category** is selected for an attribute.

14. To view the differences in average sales for products, simply filter on different income brackets. For example, apply a filter for incomes between \$100 to \$1000.
