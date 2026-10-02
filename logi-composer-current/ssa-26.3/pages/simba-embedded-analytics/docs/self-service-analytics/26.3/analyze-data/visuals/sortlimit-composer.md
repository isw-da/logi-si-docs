> ## Documentation Index
> Fetch the complete documentation index at: https://insightsoftware.mintlify.site/llms.txt
> Use this file to discover all available pages before exploring further.

# Sort and Limit Visual Data

You can sort the data within a visual by the available metrics or attributes for most visuals. You can also limit the amount of data that is displayed to show a more detailed view of your data.

Some of the options and settings vary based on the **Sort by** field that is selected. In addition, these settings may appear multiple times on the Sort & Limit sidebar if more than one sort field can be specified for a visual.

Sorting and limiting data is not available for all visual types. The visual types for which you cannot sort and limit data are arcs, histograms, KPI charts, pivot tables, tables of raw data, and maps. Pivot table and raw table data can be sorted, but not in the manner described here. See [Pivot Tables](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/pivot-tables) and [Tables](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/rdt). For information on how this functionality works in visuals that use two attribute group-bys, such as floating bubble charts and heat maps, see [Sort & Limit Processing for Visuals With Two Attribute Group-By Fields](#sort-limit-processing-for-visuals-with-two-attribute-group-by).

Administrators and users with editing rights to data source configurations can also set the default sort order and limits in data source configurations. For additional information, see [Create and Manage Data Sources](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/data-source-config-overview).

**Sort or limit your visual data on a dashboard**

1. Select the visual in the Visual Gallery or on a dashboard.

2. If you selected the visual on a dashboard, select **Settings** on the [visual drop-down menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup#use-the-visual-drop-down-menu) to access the [sidebar menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup#use-the-visual-sidebar-menu) for the visual.

3. Select the sort and limit option (<img src="https://mintcdn.com/insightsoftware/1fCfZrK84x8KmAw8/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/sidebar-sort.png?fit=max&auto=format&n=1fCfZrK84x8KmAw8&q=85&s=4fc0c54db55344620adb5335ad462296" alt="" width="15" height="22" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '15px', height: '22px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/sidebar-sort.png" />) on the [sidebar menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup#use-the-visual-sidebar-menu) for the visual. The Sort & Limit sidebar opens.

   <img src="https://mintcdn.com/insightsoftware/cQU1Auv4yvPMjcip/simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/sidebar-sortlimit-710.png?fit=max&auto=format&n=cQU1Auv4yvPMjcip&q=85&s=7843b13f79b1c242ea9bb29af7c463d9" alt="" width="352" height="489" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/sidebar-sortlimit-710.png" />

4. Select a field to sort by from the drop-down menu in the **Sort by** box. If more than one sort field is used in your visual, more than one **Sort by** box appears on the sidebar.

5. For numeric **Sort by** fields:

   * Indicate how the data should be aggregated for the visual by selecting an **Aggregation** option. These include: SUM, AVG, MIN, MAX, or LAST VALUE, Count, and Distinct Count. For explanations, see [Metric Aggregation Functions](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/data/fx-aggregate#metric-aggregation-functions).
   * The option **No Aggregation** is available if you group and sort by the same field. When you use No Aggregation, you can select the sort Order of as Alphabetical (A-Z) or Reverse Alphabetical (Z-A).

6. For attribute **Sort by** fields:

   * If you're sorting by the same attribute field used in groups, you can select an **Aggregation** option of No Aggregation, Count, or Distinct Count.
   * If you are sorting by a field not used in groups, you can select an **Aggregation** option of Count, or Distinct Count.

7. Select a sorting option from the drop-down menu in the **Order** box (for example, **Descending** or **Ascending**). Different sorting options are available, depending on the **Sort by** field you select. If the selected **Sort by** field is a metric, you can sort the data in ascending or descending order. If the selected **Sort by** field is an attribute, you can sort the data in alphabetical or reverse-alphabetical order. For time attribute-based visuals, you can sort in chronological or reverse-chronological order.

8. To limit the amount of data displayed in the visual, enter or specify a number in the **Limit** box. This number is the number of data points shown on the visual. (For example, for bar charts, this represents the number of bars.) Valid values range from 1 to 999999999. If this setting is set too large, browser performance may be affected and the visual may not be able to render the data effectively.

9. Select **Apply** to apply your changes to the visual.

<h2 id="sort-limit-processing-for-visuals-with-two-attribute-group-by">
  Sort & Limit Processing for Visuals With Two Attribute Group-By Fields
</h2>

The logic used for sort and limit processing for visuals that use two attribute group-by fields (such as heat maps or floating bubble charts) requires additional explanation. The sort and limit logic used in Self-Service Analytics are linked to each other and are not global. Thus, the unique entries available for group 2 sort and limit processing depend on the number of unique entries produced by group 1 sort and limit processing.

### Limit Processing

In general, when two attribute group-by fields are used in a visual, the limit for group 1 affects the maximum number of elements available to be limited by group 2. So the limit for group 1 is applied first and the limit for group 2 is applied to the results of the limit for group 1. This limits the maximum number of subgroup elements within each group element.

#### Heat Map Examples

In heat maps, you can apply a limit for both group 1 and group 2. The limit for group 2 depends on the results of the group 1 limit. The results from a group 1 limit should always match the limit set, but the results from a group 2 limit might match, but also might be less than the limit set. For example, if the limit for group 1 is 10, there should be 10 rows and columns in the result passed to the group 2 limit processing. So, if the limit for group 2 is also 10, fewer than 10 rows and columns may result from the group 2 limit processing.

Here is another heat map example. Suppose your heat map has:

* A group 1 limit of 10 and a group 2 limit of 5.
* From an absolute perspective, there are 100 unique group 1 values and 10 unique group 2 values.

Based on the first 10 unique group 1 values shown on the heat map, there might only actually be 4 corresponding unique group 2 values and thus, 4 will show for group 2 even though it has a limit of 5.

Now assume that the group 1 limit is increased to 25, but the group 2 limit is still 5. The first 25 unique group 1 values might have 5 or more unique group 2 values, in which case only 5 will show for group 2 because that is its limit. However, if the first 25 unique group 1 values still only have 4 corresponding unique group 2 values, group 2 will only have 4 rows and columns on the heat map.

Now assume that the group 1 limit is increased to 100 and the group 2 limit is increased to 10. As all the group 1 values are shown (there are only 100 unique group 1 values), all 10 unique group 2 values should show on the heat map, unless there is not enough space to render the full heat map. If this happens, the number of rows and columns for group 1 and group 2 respectively might be smaller.

### Sort Processing

In general, when two attribute group-by fields are used in a visual, the sort for group 1 sorts all the data and the sort applied by group 2 sorts the subgroup (group 2 elements) within each group 1 element. To verify that sorting has happened correctly, compare the aggregate results of each group 1 element using whatever metric function or calculation logic applied, but compare the group 2 subgroup elements within the same group 1 element to make sure group 2 sorting is correct. Do not rely on the individual results shown on the tooltip when hovering over a data point -- but look at the aggregate values for each group 1 element when verifying the sort logic.

For example, assume you have a heat map where group 1 refers to rows and group 2 refers to columns. In one row (we will call it A) has one column with a really large value. however, if another row (B) has multiple columns that sum up to a larger value than the value in A), the B row will sort higher than the A row (assuming you are sorting in descending order by Sum). Here's an extreme heat map example. Suppose row A has a single column point with a value of 1,000,000 and row B has 12 column points (subgroup elements) with values of 100,000 each. If you are sorting in descending order by this same metric on group 1, row B will sort higher than row A. Thus there might be a data point in the middle of the heat map that appears with a much higher individual metric value, but the chart is still sorted correctly.

#### Floating Bubble Sort Processing

Floating bubble charts have two groups and two metrics. The first group-by attribute represents data along the X-axis and the second group-by attribute is reflected along the Y-axis. Self-Service Analytics determines the correct place on a chart for a data point based on the first metric (on the Y axis). The second metric affects the size of the bubbles only. Consequently, when you sort by the first group-by attribute (X-axis), it affects the representation of data long the X-axis and when you sort by the second group-by attribute (Y-axis), it affects the representation along the Y-axis.

<Note>
  Sort and limit processing in scatter plot visuals sort and limit the data returned to the scatter plot and **not** the way the scatter plot is rendered on the screen.
</Note>
