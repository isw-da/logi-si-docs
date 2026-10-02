> ## Documentation Index
> Fetch the complete documentation index at: https://insightsoftware.mintlify.site/llms.txt
> Use this file to discover all available pages before exploring further.

# Even Time Intervals

Even time intervals allow you to include all time groupings from your data source on a dashboard that have date or time data. You can select whether you want to display all time data, or just the data that returns a value. If time groups include a NULL value, these values are included. Filter by row as needed:

* Apply `Is not NULL` to hide null values
* Apply `Is NULL` to include only null values

Even time interval grouping is only available on dashboards that use a data source with date and time fields. It is also not available for KPI charts or maps.

Even time intervals can be displayed in live mode and historical playback using the time bar. See [Live Mode and Historical Playback](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/time-bar#live-mode-and-historical-playback).

See the following topics:

* [Apply Even Time Intervals on Most Visuals](#apply-even-time-intervals-on-most-visuals)
* [Apply Even Time Intervals on Pivot Tables](#apply-even-time-intervals-on-pivot-tables)
* [Apply Even Time Intervals on Tables](#apply-even-time-intervals-on-tables)

<h2 id="apply-even-time-intervals-on-most-visuals">
  Apply Even Time Intervals on Most Visuals
</h2>

For more information about even time intervals, see Even Time Intervals.

**Apply even time intervals to data on bar, box plot, donut, floating bubble, heat map, line, packed bubble, pie, scatter, tree map, and word cloud visuals**

1. [Edit](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/dashboards/dash-manage#edit-a-dashboard) a dashboard with one of these visual types that uses a data source containing date or time fields.

2. Select a time attribute for the visual Group (x-axis).

3. Select the Time Granularity box on the x-axis.

   <img src="https://mintcdn.com/insightsoftware/GTXU--ZlYc3DodOR/simba-embedded-analytics/docs/self-service-analytics/26.3/images/dashboards/even-time-intervals.png?fit=max&auto=format&n=GTXU--ZlYc3DodOR&q=85&s=1dad4d7d180236609173b9024989e206" alt="" width="189" height="233" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/dashboards/even-time-intervals.png" />

4. Slide **Include Blanks** on to request even time intervals. By default, the ability to show all values is disabled and only attributes with a value greater than NULL are displayed.

   If this is a line chart, you can also select the **Display null as zero** checkbox to request that null values display as zeros on the chart:

   <img src="https://mintcdn.com/insightsoftware/GTXU--ZlYc3DodOR/simba-embedded-analytics/docs/self-service-analytics/26.3/images/dashboards/even-time-intervals-linecht.png?fit=max&auto=format&n=GTXU--ZlYc3DodOR&q=85&s=569722041e519794082d1d75abcd0f04" alt="" width="237" height="344" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/dashboards/even-time-intervals-linecht.png" />

The dashboard updates to include all values from the data source.

<h2 id="apply-even-time-intervals-on-pivot-tables">
  Apply Even Time Intervals on Pivot Tables
</h2>

For more information about even time intervals, see Even Time Intervals.

**Apply even time intervals to data on pivot tables**

1. [Edit](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/dashboards/dash-manage#edit-a-dashboard) a dashboard with a pivot table that uses a data source containing date or time fields.

2. If you are editing the visual in a dashboard, select **Settings** from the [visual drop-down menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup#use-the-visual-drop-down-menu). The [sidebar menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup#use-the-visual-sidebar-menu) for the visual appears.

   If you are editing the visual from the Visual Gallery, the sidebar appears to the right of the visual.

3. Select settings <img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/sidebar-chtsettings.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=74af55ee44cca52b9f7f4ae157440a81" alt="Select the settings icon on the sidebar menu to open settings options" width="28" height="33" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '28px', height: '33px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/sidebar-chtsettings.png" /> on the [sidebar menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup#use-the-visual-sidebar-menu). The Pivot Table Settings sidebar for the visual appears.

   <img src="https://mintcdn.com/insightsoftware/cQU1Auv4yvPMjcip/simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/pivot-settings.png?fit=max&auto=format&n=cQU1Auv4yvPMjcip&q=85&s=4ff63ad2d254925f91913879d45d97fa" alt="" width="351" height="647" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/pivot-settings.png" />

4. On the sidebar, select edit <img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/edit.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=e8c7d89552adf3d133e97050d5a2d000" alt="" width="20" height="22" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '20px', height: '22px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/edit.png" /> in **Rows** or **Columns** and select a time field for the row or column. Select **OK**.

   The time field is selected and expands so you can select its granularity and even time intervals setting.

   <img src="https://mintcdn.com/insightsoftware/cQU1Auv4yvPMjcip/simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/pivot-table-timeflds.png?fit=max&auto=format&n=cQU1Auv4yvPMjcip&q=85&s=5fe1e7efcc429c6d6b306798bf972387" alt="" width="287" height="119" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/pivot-table-timeflds.png" />

5. Select the granularity for the time field.

6. Slide **Include Blanks** on to request even time intervals. By default, the ability to show all values is disabled and only attributes with a value greater than NULL are displayed.

7. Select **Apply** to apply the changes to the pivot table.

8. Optionally, select Filter to include a Null filter on the Range tab as needed:

   * Apply `Is not NULL` to hide null values
   * Apply `Is NULL` to include only null values

   <img src="https://mintcdn.com/insightsoftware/b9ogX_L4Mqut_Uxb/simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/filter-time-nulls.png?fit=max&auto=format&n=b9ogX_L4Mqut_Uxb&q=85&s=7479e6e1003792b17630ff8610399348" alt="set a time range, or apply appropriate NULL filter" width="391" height="578" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/filter-time-nulls.png" />

   Select **Continue** to add the filter, then **Apply** to apply your changes to the pivot table.

<h2 id="apply-even-time-intervals-on-tables">
  Apply Even Time Intervals on Tables
</h2>

If you group a table by a time field, you can select even time intervals for that time field. For more information about even time intervals, see Even Time Intervals.

**Apply even time intervals to a time field on a table from the table context menu**

1. [Edit](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/dashboards/dash-manage#edit-a-dashboard) a dashboard with a table that uses a data source containing date or time fields.

2. Group the table by a time field in the data. See [Group and Ungroup Table Data](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/rdt#group-and-ungroup-table-data).

3. Select <img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/more-menu.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=1471c7a569a7e100cd7fa4083b04551a" alt="Selet the three dots icon to open a show more menu or take actions for the named column" width="21" height="12" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '21px', height: '12px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/more-menu.png" /> next to the time field column heading to access the table context menu.

   <img src="https://mintcdn.com/insightsoftware/cQU1Auv4yvPMjcip/simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/rdt-contextmenu-time.png?fit=max&auto=format&n=cQU1Auv4yvPMjcip&q=85&s=6be5f164bd0a7907559577f441863a72" alt="" width="308" height="304" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/rdt-contextmenu-time.png" />

4. Select **Include Blanks** on the context menu. A check mark appears next to it.

   Even time intervals are applied for the time field.

5. [Save](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/dashboards/dash-manage#save-a-dashboard) the dashboard.

**Apply even time intervals to a time field using the sidebar menus**

1. [Edit](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/dashboards/dash-manage#edit-a-dashboard) a dashboard with a table that uses a data source containing date or time fields. At least one field must be grouped.

2. If you are editing the visual in a dashboard, select **Settings** from the [visual drop-down menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup#use-the-visual-drop-down-menu). The [sidebar menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup#use-the-visual-sidebar-menu) for the visual appears.

   If you are editing the visual from the Visual Gallery, the sidebar appears to the right of the visual.

3. Select settings <img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/sidebar-chtsettings.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=74af55ee44cca52b9f7f4ae157440a81" alt="Select the settings icon on the sidebar menu to open settings options" width="28" height="33" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '28px', height: '33px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/sidebar-chtsettings.png" /> on the [sidebar menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup#use-the-visual-sidebar-menu). The Table Settings sidebar for the visual appears.

   <img src="https://mintcdn.com/insightsoftware/cQU1Auv4yvPMjcip/simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/sidebar-table-settings-82.png?fit=max&auto=format&n=cQU1Auv4yvPMjcip&q=85&s=8c4c9e39929c8c24af88bb1c39f4f3d6" alt="" width="401" height="435" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/sidebar-table-settings-82.png" />

4. On the sidebar, select a time field in **Groups**.

   The time field is selected and expands so you can select its granularity and even time intervals setting.

   <img src="https://mintcdn.com/insightsoftware/cQU1Auv4yvPMjcip/simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/ship-date-82.png?fit=max&auto=format&n=cQU1Auv4yvPMjcip&q=85&s=e11bd40ce05ab1380d7a287aa3a06882" alt="" width="331" height="135" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/ship-date-82.png" />

5. Select the granularity for the time field.

6. Slide **Include Blanks** on to request even time intervals. By default, the ability to show all values is disabled and only attributes with a value greater than NULL are displayed.

7. Select **Apply** to apply the changes to the table.

8. Optionally, select Filter to include a Null filter for this field on the Range tab as needed:

   * Apply `Is not NULL` to hide null values
   * Apply `Is NULL` to include only null values

   <img src="https://mintcdn.com/insightsoftware/b9ogX_L4Mqut_Uxb/simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/filter-time-nulls-82.png?fit=max&auto=format&n=b9ogX_L4Mqut_Uxb&q=85&s=1d2a212c394350b706a3239591263c4c" alt="set a time range, or apply appropriate NULL filter" width="409" height="460" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/filter-time-nulls-82.png" />

   Select **Continue** to add the filter, then **Apply** to apply your changes to the table.
