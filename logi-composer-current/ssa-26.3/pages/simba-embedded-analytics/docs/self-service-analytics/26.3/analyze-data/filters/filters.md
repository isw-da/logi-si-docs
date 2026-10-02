> ## Documentation Index
> Fetch the complete documentation index at: https://insightsoftware.mintlify.site/llms.txt
> Use this file to discover all available pages before exploring further.

# Filter Data

You can use filters to quickly find and display data on your dashboard [visuals](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup#use-the-visual-sidebar-menu) and in [filter snippets](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/widgets/fltrsnp-ov#use-the-filter-snippet-sidebar-menu).

* To filter on attributes in your data, use row-level filters. These filters can be saved, reused, or shared with others in your environment. For more information, see [Apply Row-Level Filters](#apply-row-level-filters).

* To filter your data using hierarchical fields, use hierarchy filters. These filters can be saved, reused, or shared with others in your environment. For more information, see [Filter by Hierarchy Field](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/filters/filters-attr#filter-by-hierarchy-field).

* Cross-visual filters are filters that are created from same-source and [cross-source link](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/filters/using-cross-source-links#define-cross-source-links) fields. Visuals publish links to share with other visuals on the same dashboard and subscribe to links that are shared with them by other visuals. When a filter is created using the context menu from a link field, it becomes a *cross-visual filter* and is applied to all visuals that subscribe to the link, except the visual that created the filter. For more information, see [Control How Cross-Visual Filters Interact in a Dashboard](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/filters/pubsub-ov).

* Wildcard filters can also be used to filter the data on your dashboard visuals. Wildcard filters are row-level filters that allow you to filter and analyze the data in a visual that matches specific combinations of character patterns. For more information, see [Apply Wildcard Filters to a Visual, Filter Snippet, or Dashboard](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/filters/filters-attr#apply-wildcard-filters-to-a-visual-filter-snippet-or-dashboard).

* Keysets are collections of unique data values that can be saved and used in further data analysis across data sources. They allow you to perform multipass and multisource filtering of the data. You can create a keyset by selecting a single field for the keyset from visual data. Filtering the visual data before creating the keyset limits the unique data values the keyset includes. The field you select for the keyset is known as the keyset's *key field*. Keysets can be applied as filters to other visuals that use the same or different data sources. For more information about keysets, see [Use Keysets](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/filters/keysets-overview).

* To filter on metrics and custom metrics, use aggregates, known as *group filters*. For more information about group filters, see [Group Filters](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/filters/group-filters).

* You can restrict the data available to specific user groups using data source *row security filters*. See [Restrict Access to Data Using Row and Column Security](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/ds-security-row).

* Alternatively, use Filter Snippets to filter the data of your dashboard's visuals. See [Filter Snippets](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/widgets/fltrsnp-ov).

  <Note>
    Dashboard data is automatically refreshed when you make filter changes. If you have a large data set, you may be able to disable auto refresh temporarily or permanently for some dashboards. See [Auto Data Refresh](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/filters/auto-refresh-filters).
  </Note>

Row-level, keyset, and group filters can be combined on a visual to provide the detail you need.

<Note>
  When working with multiple filter types on the same visual, row-level filters (including wildcard filters) are applied first to a visual, keyset filters are applied next, and group filters are applied last on the aggregated result set.
</Note>

When multiple values are specified for a single filter, the values are processed using OR processing. The records in the visual or filter snippet need only meet one of the filter value criteria to be selected for processing by the filter. However, when multiple filters are specified, AND processing is used. Records used must meet all filter criteria to be selected for use.

You can create and modify derived fields and custom metrics on the Filters sidebar while you are applying filters to your data. See [Maintain Custom Metrics](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/data/custom-metrics) and [Maintain Derived Fields](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/data/derived-fields).

Controls for filter use by end users are provided using the interactivity sidebar. See [Control How Users Interact With a Visual](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-interactivity).

The following links contain more detailed instructions and examples for using filters.

* [Apply Row-Level Filters](#apply-row-level-filters)
* [Group Filters](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/filters/group-filters)
* [Save and Maintain Filters](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/filters/saved-filters-maintaining)
* [Apply a Saved Filter to a Visual, Filter Snippet, or Dashboard](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/filters/saved-filters-maintaining#apply-a-saved-filter-to-a-visual-filter-snippet-or-dashboard)
* [Use Keysets](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/filters/keysets-overview)
* [Remove a Filter from a Visual, Filter Snippet or Dashboard](#remove-a-filter-from-a-visual-filter-snippet-or-dashboard)
* [Viewing the Applied Filters for a Visual or Filter Snippet](#viewing-the-applied-filters-for-a-visual-or-filter-snippet)

<h2 id="the-filters-sidebar">
  The Filters Sidebar
</h2>

Use the Filters sidebar to:

* Apply and remove filters on a visual or dashboard
* Review and save filters that are applied to a visual or dashboard
* Add, modify, and delete custom metrics
* Add, modify, and delete derived fields

You can not delete a custom metric if it is used by any visuals, filter snippets, materialized views, actions, or chart defaults.

<Note>
  If you try to delete a visual, filter snippet, dashboard, self service report, dashboard link, source, or source field, Self-Service Analytics displays an error message naming any objects dependent on the item you’re trying to delete. You can delete the item after you’ve removed the association from the dependent object. See [Fields Usage](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/data-source-config-fields-tab#fields-usage).
</Note>

**Access the** **Filters sidebar**

Select the filter icon on the [visual](#apply-a-row-level-filter-to-a-visual-or-filter-snippet), filter snippet, or [dashboard](#apply-a-row-level-filter-to-a-dashboard) to access the appropriate filter sidebar.

* To access the filter sidebar, select its filter icon (<img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/filter-vis.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=0a044ea0662c55e06133074a55d93cd9" alt="select the filter icon to open the filters sidebar and add or edit filters" width="17" height="17" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '17px', height: '17px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/filter-vis.png" />) or select **Settings** from the [menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup#use-the-visual-drop-down-menu) (<img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/more-menu.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=1471c7a569a7e100cd7fa4083b04551a" alt="Selet the three dots icon to open a show more menu or take actions for the named column" width="21" height="12" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '21px', height: '12px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/more-menu.png" />) and then select <img src="https://mintcdn.com/insightsoftware/cQU1Auv4yvPMjcip/simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/sidebar-filter.png?fit=max&auto=format&n=cQU1Auv4yvPMjcip&q=85&s=4b06f0c1f1b48c50da73f73672d5b1c6" alt="" width="20" height="21" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '20px', height: '21px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/sidebar-filter.png" /> on the [sidebar menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup#use-the-visual-sidebar-menu).
* To access the dashboard filter sidebar, select its filter icon (<img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/filter-dash.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=68279f203a0950b32bfab88e7273d5ba" alt="" width="20" height="19" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '20px', height: '19px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/filter-dash.png" />). The dashboard-level filter icon is available only when all the visuals are from the same data source.

The Filters sidebar appears showing any filters that have been applied.

When you first access the Filters sidebar, it shows the active (applied) filters, if there are any. Cross-visual filters that have been applied from same-source and cross-source links are listed separately from filters that are applied from the Filters sidebar.

<img src="https://mintcdn.com/insightsoftware/b9ogX_L4Mqut_Uxb/simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/filter-view-save1.png?fit=max&auto=format&n=b9ogX_L4Mqut_Uxb&q=85&s=6a82e9585b8768a9b45e88c2ec34b8e6" alt="" width="439" height="659" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/filter-view-save1.png" />

If there are not any applied filters, the filters sidebar shows three tabs: **Row**, **Group**, and **Saved** and the dashboard filters sidebar shows two tabs: **Row** and **Saved**.

You can add, review, and save filter sets using the Filters sidebar.

See the following topics:

* [Apply Row-Level Filters](#apply-row-level-filters)
* [Apply Wildcard Filters to a Visual, Filter Snippet, or Dashboard](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/filters/filters-attr#apply-wildcard-filters-to-a-visual-filter-snippet-or-dashboard)
* [Group Filters](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/filters/group-filters)
* [Save and Maintain Filters](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/filters/saved-filters-maintaining)
* [Use Keysets](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/filters/keysets-overview)
* [Remove a Filter from a Visual, Filter Snippet or Dashboard](#remove-a-filter-from-a-visual-filter-snippet-or-dashboard)

<h2 id="viewing-the-applied-filters-for-a-visual-or-filter-snippet">
  Viewing the Applied Filters for a Visual or Filter Snippet
</h2>

You can view the filters that have been applied to a visual or filter snippet using the Filters sidebar or directly on the visual or filter snippet. Note that the filters are categorized into row-level filters and cross-visual filters. Row-level filters are saved with the visual and filter snippet; cross-visual filters are not.

**View filters on the Filters sidebar**

* To access the filter sidebar, select its filter icon (<img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/filter-vis.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=0a044ea0662c55e06133074a55d93cd9" alt="select the filter icon to open the filters sidebar and add or edit filters" width="16" height="16" noZoom data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/filter-vis.png" />) or select**Settings** from the [menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup#use-the-visual-drop-down-menu) (<img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/more-menu.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=1471c7a569a7e100cd7fa4083b04551a" alt="Selet the three dots icon to open a show more menu or take actions for the named column" width="21" height="12" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '21px', height: '12px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/more-menu.png" />) and then select <img src="https://mintcdn.com/insightsoftware/cQU1Auv4yvPMjcip/simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/sidebar-filter.png?fit=max&auto=format&n=cQU1Auv4yvPMjcip&q=85&s=4b06f0c1f1b48c50da73f73672d5b1c6" alt="" width="20" height="21" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '20px', height: '21px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/sidebar-filter.png" /> on the [sidebar menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup#use-the-visual-sidebar-menu).

  The Filters sidebar appears showing any filters that have been applied.

  <img src="https://mintcdn.com/insightsoftware/b9ogX_L4Mqut_Uxb/simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/filters-applied2.png?fit=max&auto=format&n=b9ogX_L4Mqut_Uxb&q=85&s=f73eb3d17f23a39fb208b1ce90421d58" alt="" width="438" height="737" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/filters-applied2.png" />

**View filters directly on the visual or filter snippet**

* Hover over the filter icon (<img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/filter-vis.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=0a044ea0662c55e06133074a55d93cd9" alt="select the filter icon to open the filters sidebar and add or edit filters" width="17" height="17" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '17px', height: '17px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/filter-vis.png" />) on the visual or filter snippet.

  The Filters sidebar appears showing any filters that have been applied. The following example shows a visual with three filters applied: a row level filter by sales category, a cross-visual filter for the state of Pennsylvania, and a time bar filter.

  <Note>
    Time bar filters are not included in the total filter count shown in the green circle.
  </Note>

  <img src="https://mintcdn.com/insightsoftware/b9ogX_L4Mqut_Uxb/simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/filters-applied.png?fit=max&auto=format&n=b9ogX_L4Mqut_Uxb&q=85&s=c81c36dd02210bcf4ebdacdbfea5c98e" alt="" width="933" height="479" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/filters-applied.png" />

<h2 id="remove-a-filter-from-a-visual-filter-snippet-or-dashboard">
  Remove a Filter from a Visual, Filter Snippet or Dashboard
</h2>

You can remove row-level and cross-visual filters for the data in a visual. When all the visuals in a dashboard use data from the same data source, you can remove row-level filters for all the visuals and filter snippets in the dashboard.

The process for removing a filter from a visual, filter snippet, or dashboard is the same for [row-level filters](#apply-row-level-filters), [wildcard filters](#apply-row-level-filters), [group filters,](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/filters/group-filters) [cross-visual filters](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/filters/pubsub-ov#use-cross-visual-links-for-cross-visual-filtering), and filters applied by a [keyset](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/filters/keysets-overview) or a [saved filter](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/filters/saved-filters-maintaining). The applied filters for a visual, filter snippet, or dashboard appear on the Filters sidebar and are removed in the same way. To delete a saved filter or a keyset from your environment, see [Save and Maintain Filters](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/filters/saved-filters-maintaining) and [Use Keysets](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/filters/keysets-overview).

**Remove a filter from a visual or dashboard**

1. Select the filter icon on the [visual](#apply-a-row-level-filter-to-a-visual-or-filter-snippet), filter snippet, or [dashboard](#apply-a-row-level-filter-to-a-dashboard) to access the appropriate filter sidebar.

   * To access the filter sidebar, select its filter icon (<img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/filter-vis.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=0a044ea0662c55e06133074a55d93cd9" alt="select the filter icon to open the filters sidebar and add or edit filters" width="17" height="17" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '17px', height: '17px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/filter-vis.png" />) or select **Settings** from the [menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup#use-the-visual-drop-down-menu) (<img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/more-menu.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=1471c7a569a7e100cd7fa4083b04551a" alt="Selet the three dots icon to open a show more menu or take actions for the named column" width="21" height="12" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '21px', height: '12px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/more-menu.png" />) and then select <img src="https://mintcdn.com/insightsoftware/cQU1Auv4yvPMjcip/simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/sidebar-filter.png?fit=max&auto=format&n=cQU1Auv4yvPMjcip&q=85&s=4b06f0c1f1b48c50da73f73672d5b1c6" alt="" width="20" height="21" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '20px', height: '21px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/sidebar-filter.png" /> on the [sidebar menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup#use-the-visual-sidebar-menu).
   * To access the dashboard filter sidebar, select its filter icon (<img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/filter-dash.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=68279f203a0950b32bfab88e7273d5ba" alt="" width="20" height="19" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '20px', height: '19px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/filter-dash.png" />). The dashboard-level filter icon is available only when all the visuals are from the same data source.

   The Filters sidebar appears showing any filters that have been applied.

2. Locate the filter you want to remove on the Filters sidebar.

3. Select <img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/delete-open.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=02c9cbe530b9f34bd9a73851fdf499e2" alt="" width="16" height="18" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '16px', height: '18px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/delete-open.png" /> associated with the filter. If you remove the filter at the dashboard level, it is removed from all the visuals and filter snippets in the dashboard. Otherwise, it is removed only from the selected (active) visual or filter snippet.

<h2 id="apply-row-level-filters">
  Apply Row-Level Filters
</h2>

You can apply row-level filters and saved filters for the data in a visual. When all the visuals in a dashboard use data from the same data source, you can apply row-level and saved filters for the data in all the visuals on the dashboard.

* [Apply a Row-Level Filter to a Visual or Filter Snippet](#apply-a-row-level-filter-to-a-visual-or-filter-snippet)
* [Apply a Row-Level Filter to a Dashboard](#apply-a-row-level-filter-to-a-dashboard)
* [Attribute Filters](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/filters/filters-attr)
* [Set a Numeric Field Filter](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/filters/filters-attr#set-a-numeric-field-filter)
* [Set a Time Field Filter](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/filters/filters-attr#set-a-time-field-filter)
* [Apply a Saved Filter to a Visual, Filter Snippet, or Dashboard](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/filters/saved-filters-maintaining#apply-a-saved-filter-to-a-visual-filter-snippet-or-dashboard)

<h2 id="apply-a-row-level-filter-to-a-dashboard">
  Apply a Row-Level Filter to a Dashboard
</h2>

When all the visuals in a dashboard use data from the same data source, you can apply row-level filters to the data on all the visuals in the dashboard. When more than one filter is applied to a visual (either via a dashboard filter or via the [specific visual](#apply-a-row-level-filter-to-a-visual-or-filter-snippet)), the filter conditions are ANDed. In other words, both filter conditions must be met for the data to appear in the visual.

**Apply a row-level filter to a dashboard**

1. Select the filter icon <img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/filter-vis.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=0a044ea0662c55e06133074a55d93cd9" alt="select the filter icon to open the filters sidebar and add or edit filters" width="17" height="17" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '17px', height: '17px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/filter-vis.png" /> on the dashboard (to the left of the dashboard title). The dashboard-level filter icon is available only when all the visuals are from the same data source.

   The Dashboard Filters sidebar appears showing any dashboard filters that have been applied.

   <img src="https://mintcdn.com/insightsoftware/2cXq_sDOxrDVXUcv/simba-embedded-analytics/docs/self-service-analytics/26.3/images/dashboards/dashboard-filters.png?fit=max&auto=format&n=2cXq_sDOxrDVXUcv&q=85&s=69f6265b78f3d25010de4f456054fe58" alt="" width="396" height="647" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/dashboards/dashboard-filters.png" />

   Two tabs are available on the Dashboard Filters sidebar, allowing you to create a row-level filter or a saved filter. If these tabs do not appear, select **Add Filter** to see them.

   | Tab | Description |
   | - | - |
   | **Row** | The **Row** tab allows you to create a row-level filter, as described in the rest of this topic. |
   | **Saved** | The **Saved** tab shows saved filters that you can apply to the dashboard or visual. See [Save and Maintain Filters](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/filters/saved-filters-maintaining). |

2. Select the Row tab and then select the filter attribute, number, or time field you want to use from the list. The process of creating a row-level filter varies based on the type of field you select.

   * If you select an attribute field, see [Attribute Filters](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/filters/filters-attr).
   * If you select a numeric field, see [Set a Numeric Field Filter](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/filters/filters-attr#set-a-numeric-field-filter).
   * If you select a time field, see [Set a Time Field Filter](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/filters/filters-attr#set-a-time-field-filter).

   You can also select the add icon <img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/add.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=9a24b95d9385f23950764407d5e9111a" alt="add icon" width="16" height="16" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '16px', height: '16px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/add.png" /> to access the [Derived Field Editor](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/data/derived-fields#derived-field-editor) or the [Custom Metrics Editor](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/data/custom-metrics#custom-metrics-editor) to create or modify derived fields and custom metrics to be used as filters. See [Access the Derived Field Editor from the Filters Sidebar](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/data/derived-fields#access-the-derived-field-editor-from-the-filters-sidebar) and [Access the Custom Metrics Editor from the Filters Sidebar](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/data/custom-metrics#access-the-custom-metrics-editor-from-the-filters-sidebar).

3. After the filter specifics have been defined, select **Continue**. The filter is applied to all the visuals in the dashboard. Note that a number appears in a green circle next to the filter icon on the visuals to which the filter has been applied. The number represents the number of filters applied to the visual. After confirming your changes, select **Apply**.

<h2 id="apply-a-row-level-filter-to-a-visual-or-filter-snippet">
  Apply a Row-Level Filter to a Visual or Filter Snippet
</h2>

You can apply row-level filters for the data in a visual or filter snippet. When more than one filter is applied (either via the visual or filter snippet itself or via a [dashboard filter](#apply-a-row-level-filter-to-a-dashboard)), the filter conditions are ANDed. In other words, both filter conditions must be met for the data to appear in the visual or filter snippet.

**Apply a row-level filter to a visual or filter snippet**

1. To access the filter sidebar, select its filter icon <img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/filter-vis.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=0a044ea0662c55e06133074a55d93cd9" alt="select the filter icon to open the filters sidebar and add or edit filters" width="16" height="16" noZoom data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/filter-vis.png" /> or select **Settings** from the [menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup#use-the-visual-drop-down-menu) (<img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/more-menu.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=1471c7a569a7e100cd7fa4083b04551a" alt="Selet the three dots icon to open a show more menu or take actions for the named column" width="21" height="12" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '21px', height: '12px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/more-menu.png" />) and then select <img src="https://mintcdn.com/insightsoftware/cQU1Auv4yvPMjcip/simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/sidebar-filter.png?fit=max&auto=format&n=cQU1Auv4yvPMjcip&q=85&s=4b06f0c1f1b48c50da73f73672d5b1c6" alt="" width="20" height="21" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '20px', height: '21px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/sidebar-filter.png" /> on the [sidebar menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup#use-the-visual-sidebar-menu).

   The Filters sidebar appears showing any filters that have been applied.

2. Three tabs are appear on the Filters sidebar, allowing you to create a row-level filter, a group filter, or a saved filter. If these tabs do not appear, select **Add Filter** to see them.

   <table>
     <thead>
       <tr>
         <th>Tab</th>
         <th>Description</th>
       </tr>
     </thead>

     <tbody>
       <tr>
         <td>**Row**</td>
         <td>The **Row** tab allows you to create a row-level filter, as described in the rest of this topic.</td>
       </tr>

       <tr>
         <td>**Group**</td>

         <td>
           The **Group** tab allows you to create and use a group filter. See [Group Filters](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/filters/group-filters).

           <br />

           If you are using a KPI, raw data, histogram, or map markers visual, the **Group** tab is not available because all filters on these visuals are row-level filters.
         </td>
       </tr>

       <tr>
         <td>**Saved**</td>
         <td>The **Saved** tab shows saved filters that you can apply to the dashboard, filter snippet, or visual. See [Save and Maintain Filters](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/filters/saved-filters-maintaining).</td>
       </tr>
     </tbody>
   </table>

3. Select the Row tab and then select the filter attribute, number, or time field you want to use from the list. The process of creating a row-level filter varies based on the type of field you select.

   * If you select an attribute field, see [Attribute Filters](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/filters/filters-attr).
   * If you select a numeric field, see [Set a Numeric Field Filter](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/filters/filters-attr#set-a-numeric-field-filter).
   * If you select a time field, see [Set a Time Field Filter](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/filters/filters-attr#set-a-time-field-filter).

   You can also select the add icon <img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/add.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=9a24b95d9385f23950764407d5e9111a" alt="add icon" width="16" height="16" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '16px', height: '16px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/add.png" /> to access the [Derived Field Editor](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/data/derived-fields#derived-field-editor) or the [Custom Metrics Editor](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/data/custom-metrics#custom-metrics-editor) to create or modify derived fields and custom metrics to be used as filters. See [Access the Derived Field Editor from the Filters Sidebar](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/data/derived-fields#access-the-derived-field-editor-from-the-filters-sidebar) and [Access the Custom Metrics Editor from the Filters Sidebar](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/data/custom-metrics#access-the-custom-metrics-editor-from-the-filters-sidebar).

4. After the filter specifics have been defined, select **Continue**. The filter is applied to the selected (active) visual or filter snippet. Note that a number appears in a green circle next to the filter icon on the visuals to which the filter has been applied. The number represents the number of filters applied to the visual.

To view the filters applied, see [Viewing the Applied Filters for a Visual or Filter Snippet](#viewing-the-applied-filters-for-a-visual-or-filter-snippet).

### Example

Suppose you want to learn what the planned sales are for different product categories for male customers in San Francisco. You might apply a series of row-level filters using the following steps.

1. On your sales visual, select **Group** (x-axis) and then select **Product Category** from the list. The visual data is grouped by product category purchases.

2. On your sales visual, select **Planned Sales** for the **Metric** (y-axis). Your visual might look like this:

   <img src="https://mintcdn.com/insightsoftware/cQU1Auv4yvPMjcip/simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/planned-sales3.png?fit=max&auto=format&n=cQU1Auv4yvPMjcip&q=85&s=788c9f22cde854d748280c17ecd34529" alt="" width="1599" height="657" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/planned-sales3.png" />

3. Select the filter icon (<img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/filter-vis.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=0a044ea0662c55e06133074a55d93cd9" alt="select the filter icon to open the filters sidebar and add or edit filters" width="17" height="17" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '17px', height: '17px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/filter-vis.png" />) on the visual.

4. Select **Add Filter**, then on the Row tab, select **City**.

5. On the next page, select the **Value** tab and ensure **Include** is selected on the tab. Then locate and select **San Francisco** from the list of available attribute values.

6. Select **Continue**, then **Apply**. Your filter is now displayed on the Filters sidebar and is applied to your visual. The visual shows all planned purchases in San Francisco by category.

7. In the Filters sidebar, select **Add Filter** again.

8. Select the **Gender** attribute on the Row tab.

9. On the next page, select the **Value** tab and ensure **Include** is selected. Then select **Male** from the list of available attribute values.

10. Select **Continue**, then **Apply**. The Filters sidebar shows both filters you have applied to your visual. The visual shows all planned purchases in San Francisco by men. The purchases are grouped by category and might look like this:

    <img src="https://mintcdn.com/insightsoftware/cQU1Auv4yvPMjcip/simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/planned-sales4.png?fit=max&auto=format&n=cQU1Auv4yvPMjcip&q=85&s=d6d4cac443f575cd8b6f0d38b402dbf8" alt="" width="1598" height="654" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/planned-sales4.png" />

11. Filters are not saved automatically. To save your filter, select **Save Filters** on the Filters sidebar. The Save Filter Set dialog appears.

    <img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/filters/save-filter-set.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=1226a268be1aadf322729000784832e6" alt="" width="323" height="322" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/filters/save-filter-set.png" />

    Enter a name for the saved filter and, optionally, a description. If you want to share your filter, slide the **Share Filter Set** switch on (to the right). This shares the filter with other users when they view dashboards created using that same source.
