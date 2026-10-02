> ## Documentation Index
> Fetch the complete documentation index at: https://insightsoftware.mintlify.site/llms.txt
> Use this file to discover all available pages before exploring further.

# Attribute Filters

You can filter data by the values in an attribute field.

## Set a Filter in a Visual or Dashboard

1. Select the filter icon on the [visual](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/filters/filters#apply-a-row-level-filter-to-a-visual-or-filter-snippet) or [dashboard](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/filters/filters#apply-a-row-level-filter-to-a-dashboard) to access the appropriate filter sidebar.

   * To access the filter sidebar, select its filter icon <img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/filter-vis.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=0a044ea0662c55e06133074a55d93cd9" alt="select the filter icon to open the filters sidebar and add or edit filters" width="16" height="16" noZoom data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/filter-vis.png" /> or select **Settings** from the Show More [menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup#use-the-visual-drop-down-menu) (<img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/more-menu.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=1471c7a569a7e100cd7fa4083b04551a" alt="Selet the three dots icon to open a show more menu or take actions for the named column" width="21" height="12" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '21px', height: '12px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/more-menu.png" />) and then select the filter <img src="https://mintcdn.com/insightsoftware/cQU1Auv4yvPMjcip/simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/sidebar-filter.png?fit=max&auto=format&n=cQU1Auv4yvPMjcip&q=85&s=4b06f0c1f1b48c50da73f73672d5b1c6" alt="" width="20" height="21" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '20px', height: '21px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/sidebar-filter.png" /> on the [sidebar menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup#use-the-visual-sidebar-menu).
   * To access the dashboard filter sidebar, select its filter icon <img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/filter-vis.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=0a044ea0662c55e06133074a55d93cd9" alt="select the filter icon to open the filters sidebar and add or edit filters" width="16" height="16" noZoom data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/filter-vis.png" />. The dashboard-level filter icon is available only when all the visuals are from the same data source.

   The Filters sidebar opens, showing currently applied filters, if any.

2. Select **Add Filter**. An Add Filter work area opens to the Row tab, and includes Group and Saved tabs.

3. Select the Row tab. If the style of your visual is an arc gauge, KPI chart, table (raw data), histogram, or map markers chart, the Group tab is available, but you cannot create a group filter because all filters for these visual types are row-level filters. If you are using the dashboard filters sidebar, the Group tab is not available.

   The Saved tab shows saved filters that you can apply to a dashboard or visual. See [Save and Maintain Filters](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/filters/saved-filters-maintaining).

4. On the Row tab, select the filter attribute you want to use from the list of available attributes. A Select Values work area opens that you can use to select values and define this filter's specifics. See the table below for available options.

   <table>
     <thead>
       <tr>
         <th>Tab</th>
         <th>Description</th>
       </tr>
     </thead>

     <tbody>
       <tr>
         <td>Value</td>

         <td>
           The Value tab allows you to select:

           <br />

           * A filter operator (**Include** or **Exclude**, depending on whether you want to include or exclude the value from the data).
           * An optional custom value. To create and select a custom value, enter the value in the **Customize** field and select **Add**. Your custom field is added and selected in the list of possible values. To remove the custom value, uncheck it in the list of possible values. It is removed from the filter and from the list of possible values for the filter.
           * One or more values from the list of available values for the attribute you selected. To select all values, select **Select All**.

           <br />

           Use the search bar to quickly find a value. You can type the name of the value in the Search bar (or characters in the value name) to limit the list of values. A maximum of 1000 values are listed. If no values are listed or if you cannot find your value, type the exact name of the value (as stored in your data) into the Search bar and select the add icon <img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/add.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=9a24b95d9385f23950764407d5e9111a" alt="add icon" width="16" height="16" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '16px', height: '16px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/add.png" /> to select it. This will force your instance to use this value when sending the query to the data store.

           <br />

           See [Apply Row-Level Filters](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/filters/filters#apply-row-level-filters).
         </td>
       </tr>

       <tr>
         <td>Wildcard</td>
         <td>The Wildcard tab allows you to specify a wildcard filter for the attribute. See [Apply Wildcard Filters to a Visual, Filter Snippet, or Dashboard](#apply-wildcard-filters-to-a-visual-filter-snippet-or-dashboard).</td>
       </tr>

       <tr>
         <td>Keyset</td>
         <td>The Keyset tab allows you to select a keyset filter for the attribute. See [Use Keysets](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/filters/keysets-overview) for instructions on using keysets in a filter.</td>
       </tr>
     </tbody>
   </table>

   <Note>
     You can also select the add icon <img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/add.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=9a24b95d9385f23950764407d5e9111a" alt="add icon" width="16" height="16" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '16px', height: '16px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/add.png" /> to access the [Derived Field Editor](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/data/derived-fields#derived-field-editor) or the [Custom Metrics Editor](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/data/custom-metrics#custom-metrics-editor) to create or modify derived fields and custom metrics to be used as filters. See [Access the Derived Field Editor from the Filters Sidebar](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/data/derived-fields#access-the-derived-field-editor-from-the-filters-sidebar) and [Access the Custom Metrics Editor from the Filters Sidebar](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/data/custom-metrics#access-the-custom-metrics-editor-from-the-filters-sidebar).
   </Note>

5. After you have defined the filter specifics, select **Continue**. After confirming your changes, select **Apply**.

   * Filters you create at the dashboard level are applied to all the visuals in the dashboard that use that source.
   * Filters you create at the visual level apply only to the selected (active) visual.

<Note>
  Optionally, nest multiple filters for more targeted filtering results. Select **Nest Filters**, then link multiple filters using `AND` and `OR` filtering.
</Note>

## Additional Attribute Filters in a Filter Snippet

When you create a [new filter snippet](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/widgets/fltrsnp-ov#add-filter-snippets-to-a-dashboard), you define the initial data type, operator, data source, and value column to use in [Data Settings](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/widgets/fltrsnp-ov#data-settings). You can add additional filters, including nested filters, as needed.

1. Open your existing filter snippet.

2. Select the Filters option from the [Filter Snippet sidebar](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/widgets/fltrsnp-ov#filters).

3. Select **Add Filter**. An Add Filter work area opens to the Row tab, and includes Group and Saved tabs.

4. Select or create a field to filter from available options on the Row or Group tab.

   * Select an existing available field from Attribute, [Number](#set-a-numeric-field-filter), [Time](#set-a-time-field-filter), or [Hierarchy](#filter-by-hierarchy-field) and define appropriate options to use.
   * Alternatively, elect the add icon to add a [derived field](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/data/derived-fields#derived-field-editor) or [custom metric](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/data/custom-metrics#custom-metrics-editor), and define appropriate options to use.

5. After you have defined the filter specifics, select **Continue**. After confirming your changes, select **Apply**.

<Note>
  Optionally, nest multiple filters for more targeted filtering results. Select Nest Filters, then link multiple filters using `AND` and `OR` filtering.
</Note>

<h2 id="set-a-numeric-field-filter">
  Set a Numeric Field Filter
</h2>

You can filter visual data by the values in a numeric field.

<h3 id="set-a-numeric-field-filter-set-a-filter-in-a-visual-or-dashboard">
  Set a Filter in a Visual or Dashboard
</h3>

1. Select the filter icon on the [visual](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/filters/filters#apply-a-row-level-filter-to-a-visual-or-filter-snippet) or [dashboard](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/filters/filters#apply-a-row-level-filter-to-a-dashboard) to access the appropriate filter sidebar.

   * To access the filter sidebar, select its filter icon <img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/filter-vis.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=0a044ea0662c55e06133074a55d93cd9" alt="select the filter icon to open the filters sidebar and add or edit filters" width="16" height="16" noZoom data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/filter-vis.png" /> or select **Settings** from the Show More [menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup#use-the-visual-drop-down-menu) (<img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/more-menu.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=1471c7a569a7e100cd7fa4083b04551a" alt="Selet the three dots icon to open a show more menu or take actions for the named column" width="21" height="12" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '21px', height: '12px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/more-menu.png" />) and then select the filter <img src="https://mintcdn.com/insightsoftware/cQU1Auv4yvPMjcip/simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/sidebar-filter.png?fit=max&auto=format&n=cQU1Auv4yvPMjcip&q=85&s=4b06f0c1f1b48c50da73f73672d5b1c6" alt="" width="20" height="21" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '20px', height: '21px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/sidebar-filter.png" /> on the [sidebar menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup#use-the-visual-sidebar-menu).
   * To access the dashboard filter sidebar, select its filter icon <img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/filter-dash.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=68279f203a0950b32bfab88e7273d5ba" alt="" width="20" height="19" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '20px', height: '19px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/filter-dash.png" />. The dashboard-level filter icon is available only when all the visuals are from the same data source.

   The Filters sidebar opens, showing currently applied filters, if any.

2. Select **Add Filter**. An Add Filter work area opens to the Row tab, and includes Group and Saved tabs.

3. Select the Row tab. If the style of your visual is an arc gauge, KPI chart, table (raw data), histogram, or map markers chart, the Group tab is available, but you cannot create a group filter because all filters for these visual types are row-level filters. If you are using the dashboard filters sidebar, the Group tab is not available.

   The Saved tab shows saved filters that you can apply to a dashboard, visual, or filter snippet. See [Save and Maintain Filters](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/filters/saved-filters-maintaining).

4. On the Row tab, select the numeric field you want to use from the list of available number fields. A Select Values work area opens that you can use to select values and define this filter's specifics. See the table below for available options.

   <table>
     <thead>
       <tr>
         <th>Tab</th>
         <th>Description</th>
       </tr>
     </thead>

     <tbody>
       <tr>
         <td>Range</td>

         <td>
           Select a relational comparison operator in the **Operator** selection box. Data is included in the visual when the data in the filter field meets the condition set by the relational operator and the numeric values you specify. Valid numeric operators are described in [Operators](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/data/fx-aggregate#operators).

           <br />

           The Range tab initially shows the full range of values available. It provides an **Operator** selection box and **From** and **To** boxes for you to use to select the range of values. Use the arrows in the **From** and **To** boxes to increase and decrease the maximum and minimum values.
         </td>
       </tr>

       <tr>
         <td>Keyset</td>
         <td>The Keyset tab allows you to select a keyset to apply as the filter (see [Use Keysets](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/filters/keysets-overview)).</td>
       </tr>
     </tbody>
   </table>

   <Note>
     You can also select the add icon <img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/add.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=9a24b95d9385f23950764407d5e9111a" alt="add icon" width="16" height="16" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '16px', height: '16px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/add.png" /> to access the [Derived Field Editor](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/data/derived-fields#derived-field-editor) or the [Custom Metrics Editor](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/data/custom-metrics#custom-metrics-editor) to create or modify derived fields and custom metrics to be used as filters. See [Access the Derived Field Editor from the Filters Sidebar](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/data/derived-fields#access-the-derived-field-editor-from-the-filters-sidebar) and [Access the Custom Metrics Editor from the Filters Sidebar](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/data/custom-metrics#access-the-custom-metrics-editor-from-the-filters-sidebar).
   </Note>

5. After you have defined the filter specifics, select **Continue**. After confirming your changes, select **Apply**.

   * Filters you create at the dashboard level are applied to all the visuals in the dashboard that use that source.
   * Filters you create at the visual level apply only to the selected (active) visual.

<Note>
  Optionally, nest multiple filters for more targeted filtering results. Select **Nest Filters**, then link multiple filters using `AND` and `OR` filtering.
</Note>

### Additional Numeric Field Filters in a Filter Snippet

When you create a [new filter snippet](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/widgets/fltrsnp-ov#add-filter-snippets-to-a-dashboard), you define the initial data type, operator, data source, and value column to use in [Data Settings](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/widgets/fltrsnp-ov#data-settings). You can add additional filters, including nested filters, as needed.

1. Open your existing filter snippet.

2. Select the Filters option from the [Filter Snippet sidebar](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/widgets/fltrsnp-ov#filters).

3. Select **Add Filter**. An Add Filter work area opens to the Row tab, and includes Group and Saved tabs.

4. Select or create a field to filter from available options on the Row or Group tab.

   * Select an existing available field from Attribute, Number, [Time](#set-a-time-field-filter), or [Hierarchy](#filter-by-hierarchy-field) and define appropriate options to use.
   * Alternatively, elect the add icon to add a [derived field](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/data/derived-fields#derived-field-editor) or [custom metric](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/data/custom-metrics#custom-metrics-editor), and define appropriate options to use.

5. After you have defined the filter specifics, select **Continue**. After confirming your changes, select **Apply**.

<Note>
  Optionally, nest multiple filters for more targeted filtering results. Select Nest Filters, then link multiple filters using `AND` and `OR` filtering.
</Note>

<h2 id="set-a-time-field-filter">
  Set a Time Field Filter
</h2>

When you select a time attribute for a visual or filter snippet, you can filter the time range you display.

<Note>
  If you are using a field that has time zone information disabled (select **Not Specified**), only the time-related information is shown in the user interface and exported with your data. Time zone labels are not included.
</Note>

<h3 id="set-a-time-range-for-a-time-field-filter-in-a-visual-or">
  Set a Time Range for a Time Field Filter in a Visual or Dashboard
</h3>

1. Select the filter icon on the [visual](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/filters/filters#apply-a-row-level-filter-to-a-visual-or-filter-snippet) or [dashboard](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/filters/filters#apply-a-row-level-filter-to-a-dashboard) to access the appropriate filter sidebar.

   * To access the filter sidebar, select its filter icon <img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/filter-vis.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=0a044ea0662c55e06133074a55d93cd9" alt="select the filter icon to open the filters sidebar and add or edit filters" width="17" height="17" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '17px', height: '17px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/filter-vis.png" /> or select**Settings** from the Show More [menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup#use-the-visual-drop-down-menu) <img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/more-menu.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=1471c7a569a7e100cd7fa4083b04551a" alt="Selet the three dots icon to open a show more menu or take actions for the named column" width="21" height="12" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '21px', height: '12px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/more-menu.png" /> and then select the filter icon <img src="https://mintcdn.com/insightsoftware/cQU1Auv4yvPMjcip/simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/sidebar-filter.png?fit=max&auto=format&n=cQU1Auv4yvPMjcip&q=85&s=4b06f0c1f1b48c50da73f73672d5b1c6" alt="" width="20" height="21" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '20px', height: '21px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/sidebar-filter.png" /> on the [sidebar menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup#use-the-visual-sidebar-menu).
   * To access the dashboard filter sidebar, select its filter icon <img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/filter-vis.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=0a044ea0662c55e06133074a55d93cd9" alt="select the filter icon to open the filters sidebar and add or edit filters" width="16" height="16" noZoom data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/filter-vis.png" />. The dashboard-level filter icon is available only when all the visuals are from the same data source.

   The Filters sidebar opens, showing currently applied filters, if any.

2. Select**Add Filter**. An Add Filter work area opens to the Row tab, and includes Group and Saved tabs.

3. Select the Row tab. If the style of your visual is an arc gauge, KPI chart, table (raw data), histogram, or map markers chart, the Group tab is available, but you cannot create a group filter because all filters for these visual types are row-level filters. If you are using the dashboard filters sidebar, the Group tab is not available.

   The Saved tab shows saved filters that you can apply to a dashboard or visual. See [Save and Maintain Filters](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/filters/saved-filters-maintaining).

4. On the Row tab, select a time field you want to use from the list of available time fields. A Select Values work area opens that you can use to select values and define this filter's specifics on Range and Keysets tabs.

5. On the Range tab, you can optionally apply a null filter to the full time range. Select an **Operator** option as needed:

   * Apply `Between` to specify a time range
   * Apply `Not Between` to exclude a specified time range
   * Apply `Is NULL` to include only null values
   * Apply `Is not NULL` to hide null values

   <img src="https://mintcdn.com/insightsoftware/b9ogX_L4Mqut_Uxb/simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/filter-time-nulls-24.png?fit=max&auto=format&n=b9ogX_L4Mqut_Uxb&q=85&s=984b74290d930f0273df5de2cbecfd14" alt="set a time range, or apply appropriate NULL filter" width="350" height="460" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/filter-time-nulls-24.png" />

6. If you did not apply a `Null` filter, you can use the**From** and**To** boxes to specify the time range for the filter. You can set the range in static time, dynamic time, use variables, or use preset ranges provided.

   * Select**Static Time**,**Dynamic Time**, or**Variables** in the drop-down menu.

     <img src="https://mintcdn.com/insightsoftware/cQU1Auv4yvPMjcip/simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/time-bar-range-types-24.png?fit=max&auto=format&n=cQU1Auv4yvPMjcip&q=85&s=d6ed132442aba9854b69353802cb0992" alt="select a time range value" width="335" height="203" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/time-bar-range-types-24.png" />

     If you select**Static Time**, the**From** and**To** boxes are filled with default dates and times. Use the boxes to select specific from and to times

     If you select**Dynamic Time**, the**From** and**To** boxes are filled with**Start of Data Set** and**End of Data Set** automatically. Use the**Condition** boxes to select different dynamic from and to times:

     <img src="https://mintcdn.com/insightsoftware/b9ogX_L4Mqut_Uxb/simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/filter-time-range-dynamic-24.png?fit=max&auto=format&n=b9ogX_L4Mqut_Uxb&q=85&s=621a2d5216dd9f01c4b0b7705383f3b1" alt="Define condtions and offset of dynamic time ranges here" width="339" height="518" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/filter-time-range-dynamic-24.png" />

     If you select**Variables**, define a variable for use in filtering.

   * Alternatively, select**Presets** to fill the**From** and**To** boxes with predefined time ranges provided.

     <img src="https://mintcdn.com/insightsoftware/cQU1Auv4yvPMjcip/simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/time-bar-presets.png?fit=max&auto=format&n=cQU1Auv4yvPMjcip&q=85&s=d66f913c6ebb431641a6bef56c43cbe0" alt="" width="191" height="339" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/time-bar-presets.png" />

     Use the filter box at the top of the presets list to locate the preset setting you want. Descriptions of each of the preset options are provided in [Preset Time Ranges](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/data/data-number-formatting#preset-time-ranges).

7. Alternatively, select a keyset on the **Keysets** tab to use for the filter. See [Use Keysets](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/filters/keysets-overview).

8. After you have defined the filter specifics, select**Continue**. After confirming your changes, select**Apply**.

   * Filters you create at the dashboard level are applied to all the visuals in the dashboard that use that source.
   * Filters you create at the visual level apply only to the selected (active) visual.

<Note>
  Optionally, nest multiple filters for more targeted filtering results. Select **Nest Filters**, then link multiple filters using `AND` and `OR` filtering.
</Note>

### Additional Time Field Filters in a Filter Snippet

When you create a [new filter snippet](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/widgets/fltrsnp-ov#add-filter-snippets-to-a-dashboard), you define the initial data type, operator, data source, and value column to use in [Data Settings](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/widgets/fltrsnp-ov#data-settings). You can add additional filters, including nested filters, as needed.

1. Open your existing filter snippet.

2. Select the Filters option from the [Filter Snippet sidebar](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/widgets/fltrsnp-ov#filters).

3. Select **Add Filter**. An Add Filter work area opens to the Row tab, and includes Group and Saved tabs.

4. Select or create a field to filter from available options on the Row or Group tab.

   * Select an existing available field from Attribute, [Number](#set-a-numeric-field-filter), Time, or [Hierarchy](#filter-by-hierarchy-field) and define appropriate options to use.
   * Alternatively, elect the add icon to add a [derived field](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/data/derived-fields#derived-field-editor) or [custom metric](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/data/custom-metrics#custom-metrics-editor), and define appropriate options to use.

5. After you have defined the filter specifics, select **Continue**. After confirming your changes, select **Apply**.

<Note>
  Optionally, nest multiple filters for more targeted filtering results. Select Nest Filters, then link multiple filters using `AND` and `OR` filtering.
</Note>

<h2 id="filter-by-hierarchy-field">
  Filter by Hierarchy Field
</h2>

You can filter your data by the values in a hierarchy field. The source used by the visual, visuals, dashboard (when only one source is in use) or associated filter snippet must be set up to include a hierarchy field. See [Hierarchical Fields and Structures](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/hierarchical-fields-ov).

<h3 id="filter-in-a-visual-or-dashboard">
  Filter in a Visual or Dashboard
</h3>

1. Select the filter icon on the [visual](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/filters/filters#apply-a-row-level-filter-to-a-visual-or-filter-snippet) or [dashboard](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/filters/filters#apply-a-row-level-filter-to-a-dashboard) to access the appropriate filter sidebar.

   * To access the filter sidebar, select its filter icon <img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/filter-vis.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=0a044ea0662c55e06133074a55d93cd9" alt="select the filter icon to open the filters sidebar and add or edit filters" width="16" height="16" noZoom data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/filter-vis.png" /> or select **Settings** from the Show More [menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup#use-the-visual-drop-down-menu) <img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/more-menu.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=1471c7a569a7e100cd7fa4083b04551a" alt="Selet the three dots icon to open a show more menu or take actions for the named column" width="21" height="12" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '21px', height: '12px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/more-menu.png" /> and then select the filter icon <img src="https://mintcdn.com/insightsoftware/cQU1Auv4yvPMjcip/simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/sidebar-filter.png?fit=max&auto=format&n=cQU1Auv4yvPMjcip&q=85&s=4b06f0c1f1b48c50da73f73672d5b1c6" alt="" width="20" height="21" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '20px', height: '21px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/sidebar-filter.png" /> on the [sidebar menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup#use-the-visual-sidebar-menu).
   * To access the dashboard filter sidebar, select its filter icon <img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/filter-vis.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=0a044ea0662c55e06133074a55d93cd9" alt="select the filter icon to open the filters sidebar and add or edit filters" width="16" height="16" noZoom data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/filter-vis.png" />. The dashboard-level filter icon is available only when all the visuals are from the same data source.

   The Filters sidebar opens, showing currently applied filters, if any.

2. Select **Add Filter**. An Add Filter work area opens to the Row tab, and includes Group and Saved tabs.

3. On the Row tab, select an available hierarchy field to use to filter your data. A Select Values work area opens.

4. Select a filter **Operator** for your data.

   1. When you select **Include**, you can individually select hierarchical values in the filter to be included. This allows exclusion of specific descendent data from a parent as needed.
   2. When you select **Equals or Descendents of**, you can select groups of data quickly and easily; select a top level node and all of its descendents are included by default.

5. Select one or more nodes to filter your data. At least one filter value is required.

   * Use the **Search** box to find specific nodes.
   * Select the node indicators to expand and collapse nodes, or select and deselect **Expand All** to expand and collapse all nodes.

6. After you have defined your filter specifics, select **Continue**.

   * If you create the filter at the dashboard level, it is applied to all the visuals and filter snippets in the dashboard.
   * Otherwise, it is applied only to the selected (active) visual or filter snippet. After confirming your changes, select **Apply.**

<h3 id="create-a-filter-snippet-hierarchy-data-type">
  Create a Filter Snippet - Hierarchy Data Type
</h3>

1. Create a [new filter snippet](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/widgets/fltrsnp-ov#add-filter-snippets-to-a-dashboard).

2. Define the **Data Settings** to use a Data Type of **Hierarchy**.

3. Select an **Operator** for your data.

   1. When you select **Include**, you and your users can individually select hierarchical values in the filter to be included. This allows exclusion of specific descendent data from a parent as needed.
   2. When you select **Equals or Descendents of**, you and your users can select groups of data quickly and easily; select a top level node and all of its descendents are included by default.

4. Select an available **Source**. Any visuals in this dashboard that use this source can be affected by this filter snippet.

5. Select an available **Value Column**, then select **Apply**.

6. Your filter snippet updates, allowing users to filter data for widgets you connect to this filter snippet.

After you have connected the filter snippet to widgets, users can filter data in the filter snippet. They can:

* Use the **Search** box to find specific nodes.
* Select and deselect **Expand All** to expand and collapse all nodes.
* Select the node indicators to expand and collapse individual nodes and their descendents.

### Additional Hierarchy Filters in a Filter Snippet

When you create a [new filter snippet](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/widgets/fltrsnp-ov#add-filter-snippets-to-a-dashboard), you define the initial data type, operator, data source, and value column to use in [Data Settings](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/widgets/fltrsnp-ov#data-settings). You can add additional filters, including nested filters, as needed.

1. Open your existing filter snippet.

2. Select the Filters option from the [Filter Snippet sidebar](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/widgets/fltrsnp-ov#filters).

3. Select **Add Filter**. An Add Filter work area opens to the Row tab, and includes Group and Saved tabs.

4. Select or create a field to filter from available options on the Row or Group tab.

   * Select an existing available field from Attribute, [Number](#set-a-numeric-field-filter), [Time](#set-a-time-field-filter), or Hierarchy and define appropriate options to use.
   * Alternatively, elect the add icon to add a [derived field](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/data/derived-fields#derived-field-editor) or [custom metric](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/data/custom-metrics#custom-metrics-editor), and define appropriate options to use.

5. After you have defined the filter specifics, select **Continue**. After confirming your changes, select **Apply**.

<Note>
  Optionally, nest multiple filters for more targeted filtering results. Select Nest Filters, then link multiple filters using `AND` and `OR` filtering.
</Note>

<h2 id="apply-wildcard-filters-to-a-visual-filter-snippet-or-dashboard">
  Apply Wildcard Filters to a Visual, Filter Snippet, or Dashboard
</h2>

Wildcard filters are row-level filters you can use to filter the data on your dashboard visuals or filter snippets. Wildcard filters allow you to filter and analyze the data that matches specific combinations of character patterns.

<Note>
  When working with multiple filter types on the same visual, row-level filters (including wildcard filters) are applied first to a visual, keyset filters are applied second, and group filters are applied last on the aggregated result set.
</Note>

Many connectors support wildcard filters, but support for case-sensitivity in wildcard filters varies depending on the connector's data store.

Support for this feature by connector is shown in the following table.

<strong>Key:</strong>**Y** - Supported; **N** - Not Supported; N/A - not applicable

| Connector | Supported? |
| - | - |
| [Amazon Redshift](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-amazon-redshift) | **Y** |
| [Amazon S3](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-amazon-s3) | **Y** |
| [Apache Drill](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-apache-drill) | **Y** |
| [Apache Phoenix](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-apache-phoenix) | **Y** |
| [Apache Phoenix Query Server (QS)](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-apache-phoenix) | **Y** |
| [Apache Solr](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-solr) | **Y** |
| [BigQuery](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-bigquery) | **Y** |
| [Business Central Jet](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connect-to-biz-central) | **Y** |
| [Cloudera Impala](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/cloudera-ov#manage-the-impala-connector) | **Y** |
| [Cloudera Search](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/cloudera-search) | **Y** |
| [Couchbase](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/couchbase) | **Y** |
| [Dremio](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-dremio) | **Y** |
| [Dundas BI (Managed)](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/dbi) | source-dependent |
| [Elasticsearch 7.0](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-elastic-search) | **Y** |
| [Elasticsearch 8.0](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-elastic-search) | **Y** |
| [File Upload (Upload API)](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/uploading-a-flat-file) | **Y** |
| [HDFS](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/hdfs) | **Y** |
| [Hive](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/hive) | **Y** |
| [Jira](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-jira) | **Y** |
| [MemSQL](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-memsql) | **Y** |
| [Microsoft SQL Server](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-sql-server) | **Y** |
| [MongoDB](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-mongodb) | **Y** |
| [MySQL](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-mysql) | **Y** |
| [OpenSearch](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-opensearch) | **Y** |
| [Oracle](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-oracle) | **Y** |
| [PostgreSQL](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-postgresql) | **Y** |
| [Python](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-python) | **Y** |
| [Real Time Sales](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/enabling-real-time-sales-demo-source) | **Y** |
| [Salesforce](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-salesforce) | **Y** |
| [SAP Hana](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-sap-hana) | **Y** |
| [SAP S/4HANA](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-saps-4hana) | **N** |
| [SAP IQ](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-sap-iqsql) | **Y** |
| [Spark SQL](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-sparksql) | **Y** |
| [Snowflake](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-snowflake) | **Y** |
| [Teradata](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-teradata) | **Y** |
| [TIBCO DV](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/tibcodv) | **Y** |
| [Trino](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-trino) | **Y** |
| [File Upload (Upload API)](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/uploading-a-flat-file) | **Y** |
| [Vertica](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-vertica) | **Y** |

See [Wildcard Case-Insensitive Filters](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connector-feature-support#wildcard-case-insensitive-filters) and [Wildcard Case-Sensitive Filters](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connector-feature-support#wildcard-case-sensitive-filters) to determine whether case-insensitive or case-sensitive wildcards are supported.

**Apply a wildcard filter**

1. Select the filter icon on the [visual](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/filters/filters#apply-a-row-level-filter-to-a-visual-or-filter-snippet), filter snippet, or [dashboard](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/filters/filters#apply-a-row-level-filter-to-a-dashboard) to access the appropriate filter sidebar.

   * To access the filter sidebar, select its filter icon <img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/filter-vis.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=0a044ea0662c55e06133074a55d93cd9" alt="select the filter icon to open the filters sidebar and add or edit filters" width="17" height="17" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '17px', height: '17px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/filter-vis.png" /> or select **Settings** from the [menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup#use-the-visual-drop-down-menu) <img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/more-menu.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=1471c7a569a7e100cd7fa4083b04551a" alt="Selet the three dots icon to open a show more menu or take actions for the named column" width="21" height="12" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '21px', height: '12px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/more-menu.png" /> and then select <img src="https://mintcdn.com/insightsoftware/cQU1Auv4yvPMjcip/simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/sidebar-filter.png?fit=max&auto=format&n=cQU1Auv4yvPMjcip&q=85&s=4b06f0c1f1b48c50da73f73672d5b1c6" alt="" width="20" height="21" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '20px', height: '21px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/sidebar-filter.png" /> on the [sidebar menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup#use-the-visual-sidebar-menu).

   * To access the dashboard filter sidebar, select its filter icon <img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/filter-dash.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=68279f203a0950b32bfab88e7273d5ba" alt="" width="20" height="19" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '20px', height: '19px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/filter-dash.png" />. The dashboard-level filter icon is available only when all the visuals are from the same data source.

   The Filters sidebar appears showing any filters that have been applied.

2. Select the Row tab. If the style of your visual is an arc gauge, KPI chart, table (raw data), histogram, or map markers chart, the Group tab is available, but you cannot create a group filter because all filters for these visual types are row-level filters. If you are using the dashboard filters sidebar, the Group tab is not available.

   The Saved tab shows saved filters that you can apply to a dashboard, visual, or filter snippet. See [Save and Maintain Filters](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/filters/saved-filters-maintaining).

3. On the Row tab, select the filter attribute you want to use from the list of available attributes. A second page with three tabs appears in the Filters sidebar.

   * The Value tab allows you to select a filter value for the attribute. See [Apply Row-Level Filters](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/filters/filters#apply-row-level-filters) for instructions on using a regular row-level filter.
   * The Wildcard tab allows you to specify a wildcard filter for the attribute. Continue following the steps in these instructions.
   * The Keyset tab allows you to select a keyset filter for the attribute. See [Use Keysets](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/filters/keysets-overview) for instructions on using keysets in a filter.

   You can also select the add icon <img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/add.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=9a24b95d9385f23950764407d5e9111a" alt="add icon" width="16" height="16" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '16px', height: '16px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/add.png" /> to access the [Derived Field Editor](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/data/derived-fields#derived-field-editor) or the [Custom Metrics Editor](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/data/custom-metrics#custom-metrics-editor) to create or modify derived fields and custom metrics to be used as filters. See [Access the Derived Field Editor from the Filters Sidebar](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/data/derived-fields#access-the-derived-field-editor-from-the-filters-sidebar) and [Access the Custom Metrics Editor from the Filters Sidebar](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/data/custom-metrics#access-the-custom-metrics-editor-from-the-filters-sidebar).

4. Select the Wildcard tab to create a row-level wildcard filter.

5. Select an operator from the drop-down menu for the **Operator** box on the **Wildcard** tab.

   | Operator | Data is included in the visual... |
   | - | - |
   | Contains | When the data in the filter attribute you selected contains the wildcard string you will specify in the next step. |
   | Does Not Contain | When the data in the filter attribute you selected does *not* contain the wildcard string you will specify in the next step. |
   | Begins With | When the data in the filter attribute you selected begins with the wildcard string you will specify in the next step. |
   | Does Not Begin With | When the data in the filter attribute you selected does **not** begin with the wildcard string you will specify in the next step. |
   | Ends With | When the data in the filter attribute you selected ends with the wildcard string you will specify in the next step. |
   | Does Not End With | When the data in the filter attribute you selected does **not** end with the wildcard string you will specify in the next step. |

6. In the **Value** box, type a string of characters that represents the wildcard string for the filter. Data is included in the visual when the data in the filter field meets the condition set by this operator and the wildcard string you specify.

7. By default the **Case Sensitive** slider is on (selected). When this option is selected, the wildcard filter includes data in the visual only if the filter attribute data exactly matches both the value of the wildcard string and the case of the wildcard string value. Slide the option off if you do not care if the visual data exactly matches the case of the wildcard string.

8. If you want to specify another wildcard value, select the add icon <img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/add.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=9a24b95d9385f23950764407d5e9111a" alt="add icon" width="16" height="16" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '16px', height: '16px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/add.png" /> next to the **Values** title on the Wildcard tab. Then repeat Steps 5-7 above for the new wildcard value. Multiple wildcard values are treated as OR operations. A record can meet the filter criteria specified by any of the wildcard values to be selected for filter processing.

9. Select **Apply**. If you create the filter at the dashboard level, it is applied to all the visuals in the dashboard. Otherwise, it is applied only to the selected (active) visual.

10. Optionally, repeat these steps to apply additional filters to the visual or dashboard.

See [Remove a Filter from a Visual, Filter Snippet or Dashboard](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/filters/filters#remove-a-filter-from-a-visual-filter-snippet-or-dashboard) for information on removing a wildcard filter from a visual or dashboard.

## Control Filter Dialog Values

You can control the behavior of filter dialogs by data source. These controls are set in the [Fields tab](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/data-source-config-fields-tab) of the [data source](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/data-source-config-overview).

* For attribute fields, you can require your users to manually enter attribute values to include in the visual or dashboard, instead of letting them select values from a list. See [Control Attribute Field Filters](#control-attribute-field-filters).
* For number fields, you can specify the initial (default) minimum and maximum values available for selection as filters. See [Control Number Field Filters](#control-number-field-filters).
* For time fields, you can specify the initial (default) minimum and maximum dates and times for the filter or, when shown on the time bar, the initial (default) time range shown. You can change these settings by manipulating the filters and time bar on the visual. See [Control Time Field Filters](#control-time-field-filters).

<Note>
  In this release, when your admin enables the Enhanced Experience user interface, you will see changes to workflows you may have used in previous releases. If you are running an earlier release or your admin has not enabled the new interface, see [Filters in Earlier Releases](#filters-in-earlier-releases) .
</Note>

<h3 id="control-attribute-field-filters">
  Control Attribute Field Filters
</h3>

**Control attribute field filters**

1. Edit the data source for which you want to control attribute field filters. See [Edit a Data Source](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/data-source-config-overview#edit-a-data-source).
2. Select the Output in your source, then **Expand View** of the [Fields tab](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/data-source-config-fields-tab) to access the Filter Values panel.
3. Locate your field (Data Type: Attribute) and select it.
4. Select (check) **Only Allow Custom Values** in the sidebar menu.
5. When your changes are complete, select **Save**.

To test this, create a new dashboard visual or filter snippet using the data source. Then filter the data on the visual by the attribute. You will be required to enter the values to filter. Add at least one value or custom value for the attribute to the filter.

<img src="https://mintcdn.com/insightsoftware/b9ogX_L4Mqut_Uxb/simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/filter-manual4.png?fit=max&auto=format&n=b9ogX_L4Mqut_Uxb&q=85&s=e49d39ccb51f94180fb9f403dcdd08a6" alt="Use to select values, wildcard, or keyset filter information" width="351" height="488" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/filter-manual4.png" />

**Add a value**

1. Select **Include** or **Exclude** using the drop-down menu in the **Operator** box.

2. Type a value into the search box and select the add icon <img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/add.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=9a24b95d9385f23950764407d5e9111a" alt="add icon" width="16" height="16" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '16px', height: '16px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/add.png" />. Be sure to specify the values using the proper sentence case. For example, if the values are stored in lowercase letters only, but you enter a value with starting a capital letter, the search will not work.

   <img src="https://mintcdn.com/insightsoftware/b9ogX_L4Mqut_Uxb/simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/filter-manual5.png?fit=max&auto=format&n=b9ogX_L4Mqut_Uxb&q=85&s=72412e4647b20b1ccb406a2933eaead3" alt="Enter a value, such as rings, to add" width="350" height="336" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/filter-manual5.png" />

3. The value is added to the list of selected values.

   <img src="https://mintcdn.com/insightsoftware/b9ogX_L4Mqut_Uxb/simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/filter-manual6.png?fit=max&auto=format&n=b9ogX_L4Mqut_Uxb&q=85&s=89545fc3d1ec85c6dc583dae6037be89" alt="Review your included values, deselect or remove if needed" width="352" height="491" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/filter-manual6.png" />

4. When you are finished setting your filter values, select **Continue** and examine your updates. If they are correct, select **Apply**.

   For more information about setting attribute filters, see Attribute Filters.

<h3 id="control-number-field-filters">
  Control Number Field Filters
</h3>

**Control number field filters**

1. Edit the data source for which you want to control number field filters. See [Edit a Data Source](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/data-source-config-overview#edit-a-data-source).

2. Select the Output in your source, then **Expand View** of the [Fields tab](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/data-source-config-fields-tab) to access the Filter Values panel.

3. Locate your field (Data Type: Number) and select it.

4. Select to enable **Custom Range** in the Filter Values panel.

5. Specify minimum and maximum values for the filter ranges for the field. You can type the numbers directly in the **Min** and **Max** boxes or use the arrows in the boxes to increment and decrement the values.

   <Note>
     Custom range values can be numbers or numbers with scientific notation.
   </Note>

6. Select **Save** to apply the custom filter range.

<Note>
  If a [Custom Range](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/data-source-config-fields-tab#filter-values-panel-fields-tab) has been defined for a field, the minimum and maximum fields used in filters remain unchanged when you refresh source data. These fields are shown with cache actions disabled on the [Cache tab](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/data-source-config-global-settings-tab#cache-tab).
</Note>

To test this, create a new dashboard visual or filter snippet using the data source. Then filter the data by the number field you specified a custom range for. The values show as default in the filter are the custom range you specified in the data source configuration.

<img src="https://mintcdn.com/insightsoftware/b9ogX_L4Mqut_Uxb/simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/filter-config-num-25-4.png?fit=max&auto=format&n=b9ogX_L4Mqut_Uxb&q=85&s=3d970a5ecfb1d4a3e828e81e3f211dd2" alt="Define your range of values here" width="337" height="365" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/filter-config-num-25-4.png" />

When you are finished setting your filter values, select **Continue** and examine your updates. If they are correct, select **Apply**.

For more information about setting numeric filters, see [Set a Numeric Field Filter](#set-a-numeric-field-filter).

<h3 id="control-time-field-filters">
  Control Time Field Filters
</h3>

**Control the default time field filter and time bar ranges**

1. Edit the data source for which you want to control time field filters. See [Edit a Data Source](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/data-source-config-overview#edit-a-data-source).

2. Select the Output in your source, then **Expand View** of the [Fields tab](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/data-source-config-fields-tab) to access the Filter Values panel.

3. Locate your field (Data Type: Time) and select it.

4. Change **Source of Filter Values** to **Static Override** to enable Custom Range in the Filter Values panel.

5. Specify minimum and maximum values for the filter ranges for the time field in the **From** and **To** boxes.

   Select the value in the **From** or **To** time fields to select a new date and time in the resulting calendar pop-up.

   <img src="https://mintcdn.com/insightsoftware/2cXq_sDOxrDVXUcv/simba-embedded-analytics/docs/self-service-analytics/26.3/images/connectors/calendar-popup.png?fit=max&auto=format&n=2cXq_sDOxrDVXUcv&q=85&s=3442dccc3a0da57d939679f5b08116ad" alt="select a date and time for your filter" width="237" height="262" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/connectors/calendar-popup.png" />

6. Select **Save** to apply the custom filter range.

<Note>
  If a [Custom Range](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/data-source-config-fields-tab#filter-values-panel-fields-tab) has been defined for a field, the minimum and maximum fields used in filters remain unchanged when you refresh source data. These fields are shown with cache actions disabled on the [Cache tab](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/data-source-config-global-settings-tab#cache-tab).
</Note>

To test this, create a new dashboard visual or filter snippet using the data source. Then filter the data by the time field. The values you can select for the filter are restricted to the custom range you specified in the data source configuration. For more information about specifying time filters, see [Set a Time Field Filter](#set-a-time-field-filter).

<img src="https://mintcdn.com/insightsoftware/b9ogX_L4Mqut_Uxb/simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/filter-cfg-time-25-4.png?fit=max&auto=format&n=b9ogX_L4Mqut_Uxb&q=85&s=f5fc47970d2926336de7d674c79776b8" alt="Set the start and end time of your data set for this filter" width="348" height="460" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/filter-cfg-time-25-4.png" />

When you are finished setting your filter values, select **Continue** and examine your updates. If they are correct, select **Apply**.

<h3 id="filters-in-earlier-releases">
  Filters in Earlier Releases
</h3>

You can control the behavior of filter dialogs by data source. These controls are set on the [Fields tab](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/data-source-config-fields-tab) of the [data source configuration](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/data-source-config-overview).

* For attribute fields, you can require your users to manually enter attribute values to include in the visual or dashboard, instead of letting them select values from a list. See [Controlling Attribute Field Filters](#controlling-attribute-field-filters).
* For number fields, you can specify the initial (default) minimum and maximum values available for selection as filters. See [Controlling Number Field Filters](#controlling-number-field-filters).
* For time fields, you can specify the initial (default) minimum and maximum dates and times for the filter or, when shown on the time bar, the initial (default) time range shown. You can change these settings by manipulating the filters and time bar on the visual. See [Controlling Time Field Filters](#controlling-time-field-filters).

<h4 id="controlling-attribute-field-filters">
  Controlling Attribute Field Filters
</h4>

**Control attribute field filters**

1. Edit the data source configuration for which you want to control attribute field filters. See [Edit a Data Source](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/data-source-config-overview#edit-a-data-source).
2. Select the [Fields tab](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/data-source-config-fields-tab) in the data source work area.
3. Locate the attribute field in the field table on the Fields tab.
4. Select (check) **Only Allow Custom Values** in the sidebar menu.
5. When your changes are complete, select **Save**.

To test this, create a new dashboard visual or filter snippet using the data source. Then filter the data on the visual by the attribute. You will be required to enter the values to filter. Add at least one value or custom value for the attribute to the filter.

<img src="https://mintcdn.com/insightsoftware/b9ogX_L4Mqut_Uxb/simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/filter-manual4.png?fit=max&auto=format&n=b9ogX_L4Mqut_Uxb&q=85&s=e49d39ccb51f94180fb9f403dcdd08a6" alt="Use to select values, wildcard, or keyset filter information" width="351" height="488" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/filter-manual4.png" />

**Add a value**

1. Select **Include** or **Exclude** using the drop-down menu in the **Operator** box.

2. Type a value into the search box and select the add icon <img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/add.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=9a24b95d9385f23950764407d5e9111a" alt="add icon" width="16" height="16" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '16px', height: '16px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/add.png" />. Be sure to specify the values using the proper sentence case. For example, if the values are stored in lowercase letters only, but you enter a value with starting a capital letter, the search will not work.

   <img src="https://mintcdn.com/insightsoftware/b9ogX_L4Mqut_Uxb/simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/filter-manual5.png?fit=max&auto=format&n=b9ogX_L4Mqut_Uxb&q=85&s=72412e4647b20b1ccb406a2933eaead3" alt="Enter a value, such as rings, to add" width="350" height="336" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/filter-manual5.png" />

3. The value is added to the list of selected values.

   <img src="https://mintcdn.com/insightsoftware/b9ogX_L4Mqut_Uxb/simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/filter-manual6.png?fit=max&auto=format&n=b9ogX_L4Mqut_Uxb&q=85&s=89545fc3d1ec85c6dc583dae6037be89" alt="Review your included values, deselect or remove if needed" width="352" height="491" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/filter-manual6.png" />

4. When you are finished setting your filter values, select **Continue** and examine your updates. If they are correct, select **Apply**.

   For more information about setting attribute filters, see Attribute Filters.

<h4 id="controlling-number-field-filters">
  Controlling Number Field Filters
</h4>

**Control number field filters**

1. Edit the data source configuration for which you want to control number field filters. See [Edit a Data Source](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/data-source-config-overview#edit-a-data-source).
2. Select the [Fields tab](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/data-source-config-fields-tab) in the data source creation work area.
3. Locate the number field in the field table on the **Fields** tab.
4. Select to enable Custom Range in the sidebar menu.
5. Specify minimum and maximum values for the filter ranges for the field. You can type the numbers directly in the **From** and **To** boxes or use the arrows in the boxes to increment and decrement the values. Custom range values can be numbers or numbers with scientific notation.
6. Select **Save** to apply the custom filter range.

<Note>
  If a [Custom Range](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/data-source-config-fields-tab#filter-values-panel-fields-tab) has been defined for a field, the minimum and maximum fields used in filters remain unchanged when you refresh source data. These fields are shown with cache actions disabled on the [Cache tab](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/data-source-config-global-settings-tab#cache-tab).
</Note>

To test this, create a new dashboard visual or filter snippet using the data source. Then filter the data by the number field you specified a custom range for. The values show as default in the filter are the custom range you specified in the data source configuration.

<img src="https://mintcdn.com/insightsoftware/b9ogX_L4Mqut_Uxb/simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/filter-configure-num1.png?fit=max&auto=format&n=b9ogX_L4Mqut_Uxb&q=85&s=ab6180f9ac8d7fbc8ef5c20625e82462" alt="Define your range of values here" width="350" height="514" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/filter-configure-num1.png" />

When you are finished setting your filter values, select **Continue** and examine your updates. If they are correct, select **Apply**.

For more information about setting numeric filters, see [Set a Numeric Field Filter](#set-a-numeric-field-filter).

<h4 id="controlling-time-field-filters">
  Controlling Time Field Filters
</h4>

**Control the default time field filter and time bar ranges**

1. Edit the data source configuration for which you want to control time field filters. See [Edit a Data Source](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/data-source-config-overview#edit-a-data-source).

2. Select the [Fields tab](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/data-source-config-fields-tab) in the data source configuration.

3. Locate the time field in the field table on the **Fields** tab.

4. Select to enable Custom Range in the sidebar menu.

5. Specify minimum and maximum values for the filter ranges for the time field in the **From** and **To** boxes.

   Select the value in the **From** or **To** time fields to select a new date and time in the resulting calendar pop-up.

   <img src="https://mintcdn.com/insightsoftware/2cXq_sDOxrDVXUcv/simba-embedded-analytics/docs/self-service-analytics/26.3/images/connectors/calendar-popup.png?fit=max&auto=format&n=2cXq_sDOxrDVXUcv&q=85&s=3442dccc3a0da57d939679f5b08116ad" alt="select a date and time for your filter" width="237" height="262" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/connectors/calendar-popup.png" />

6. Select **Save** to apply the custom filter range.

<Note>
  If a [Custom Range](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/data-source-config-fields-tab#filter-values-panel-fields-tab) has been defined for a field, the minimum and maximum fields used in filters remain unchanged when you refresh source data. These fields are shown with cache actions disabled on the [Cache tab](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/data-source-config-global-settings-tab#cache-tab).
</Note>

To test this, create a new dashboard visual or filter snippet using the data source. Then filter the data by the time field. The values you can select for the filter are restricted to the custom range you specified in the data source configuration. For more information about specifying time filters, see [Set a Time Field Filter](#set-a-time-field-filter).

<img src="https://mintcdn.com/insightsoftware/b9ogX_L4Mqut_Uxb/simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/filter-configure-time1.png?fit=max&auto=format&n=b9ogX_L4Mqut_Uxb&q=85&s=902cf1358cd6e44207666ac2df96b716" alt="Set the start and end time of your data set for this filter" width="348" height="483" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/filter-configure-time1.png" />

When you are finished setting your filter values, select **Continue** and examine your updates. If they are correct, select **Apply**.

<h2 id="apply-a-filter-to-dashboard-visuals-using-the-context-menu">
  Apply a Filter to Dashboard Visuals Using the Context Menu
</h2>

You can filter visuals on a dashboard that use the same source or linked cross source simultaneously using the context menu of one of the visuals when the visuals are subscribed to the links. These filters are cross-visual filters. See [Subscribe a Visual to a Link](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/filters/published-enable#subscribe-a-visual-to-a-link) for more information about subscribing to dashboard links.

<Note>
  Unlike row-level filters, cross-visual filters are not saved with the visual.
</Note>

Example:

* You have a bar chart, pie chart, and table that show data from the same product sales data source (same source link) and are all subscribed to the same source link. In this scenario, you can use the context menu to simultaneously filter the data in two of the three visuals by any field in the data source. The visual you use to select the filter is not affected.
* You add a donut chart to the three visuals above in the same dashboard, but the donut chart uses data from a different sales data source. Cross-source link the two data sources by a field (for example, State) to subscribe all of the visuals to the cross-source link. When you use the context menu to filter one of the visuals by State, the subscribed visuals are all filtered. The visual you use to select the filter is not affected.

Controls for use of filters by end users are provided using the interactivity sidebar. See [Control How Users Interact With a Visual](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-interactivity).

To view the filters applied to a visual, see [Viewing the Applied Filters for a Visual or Filter Snippet](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/filters/filters#viewing-the-applied-filters-for-a-visual-or-filter-snippet).

#### Apply A Context Menu Filter

**Apply a context menu filter to all dashboard visuals that subscribe to a same source or cross-source link**

1. Open the dashboard and select one of the data points in one of the visuals. The context menu appears.

2. Select **Filter** on the context menu. The filter is applied to all of the visuals subscribed to the link. The visual you use to select the filter is not affected.

   The **Filter** option on the context menu is only available when the visual publishes a link for the field it is also using for its visual grouping. It is *not* available if the published cross-visual links for the visual are muted. See [Mute a Published Link](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/filters/published-enable#mute-a-published-link).

<h2 id="filters-and-time-bar-interaction">
  Filters and Time Bar Interaction
</h2>

Using the filters and the time bar, you can examine your data in different dimensions. You can add time attributes when you create a new filter and control the filter from the time bar. This allows you to narrow the scope of the data by time. You can also set a filter directly in the time bar.

Filters applied in the Filters menu override any filters you set in the time bar.

The filters you create and the time bar actions you set influence the data shown on your visual. Depending on the filter settings and how they interact, it is possible that the combined results return no data. This is because the time filters that you set and the filters in the time bar are mutually exclusive. As a result, there is no data to display, so the intersection of the two time filters produces no result.

<h2 id="display-all-unique-elements-for-a-selected-filter-panel">
  Display All Unique Elements for a Selected Filter Panel Attribute
</h2>

### Resolution

The reason that only some, and not all, of the available attribute elements are showing on the filter panel is due to how Self-Service Analytics samples the data by default during the initial source creation. To have the filter panel populate with all the field elements, please refresh the field from within the data source so all the data is sampled. To do this:

1. Ensure you are logged into Self-Service Analytics as an administrator.

2. Select the Source card on your home page or Data Sources from the main menu. The [Sources](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/data-source-config-overview#data-sources-page) page appears.

3. Scroll down the list of connected data sources, select the target source and navigate to the **Fields** page.

4. Scroll to the field on which the filter is being applied.

5. Under the **Statistics** column, select the **Refresh** button.

   This ensures that all the values for that specific field will appear on the filter panel of the visuals or filter snippet.
