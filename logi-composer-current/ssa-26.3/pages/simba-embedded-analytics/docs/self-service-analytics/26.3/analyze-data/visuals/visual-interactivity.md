> ## Documentation Index
> Fetch the complete documentation index at: https://insightsoftware.mintlify.site/llms.txt
> Use this file to discover all available pages before exploring further.

# Control How Users Interact With a Visual

You can control how users can interact with a visual. You can control their ability to:

* Change metrics, rulers, colors, visual types, or otherwise modify a visual
* Group, filter, or sort visual data
* Use context menu options
* Copy, export, or delete the visual
* Create keysets from visual data
* Export visual data
* Integrate a visual into external applications
* Change the defaults set for a visual in the data source configuration visual defaults

<Warning>
  User attributes are not resolved when previewing interactivity settings, and default fallbacks will be used in the Preview mode.
</Warning>

You can control user interactivity using the interactivity sidebar of a visual from the Visual Gallery.

<Note>
  Individual visual interactivity settings can be overridden by [dashboard interactivity](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/dashboards/dash-interactivity) settings. When a dashboard overrides the interactivity settings specified for an individual visual, the visual's interactivity settings are not changed, but they are ignored, and the visual interactivity settings specified by the dashboard are used.
</Note>

<Note>
  You can include several controls for embedded visuals, allowing users to select and deselect favorite visuals, as well as filter the list of visuals in the embedded Visual Gallery by favorite status. See [Use the Visual Gallery](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-gallery).
</Note>

Control user interactions with a visual

1. Select the visual in the Visual Gallery.

2. Select the interactivity option (<img src="https://mintcdn.com/insightsoftware/1fCfZrK84x8KmAw8/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/sidebar-interactive.png?fit=max&auto=format&n=1fCfZrK84x8KmAw8&q=85&s=5068072b72f71db3c65f6eed78658798" alt="select the interactivity icon to adjust the interactivity settings for this item" width="27" height="27" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '27px', height: '27px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/sidebar-interactive.png" />) on the [sidebar menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup#use-the-visual-sidebar-menu) for the visual. The interactivity sidebar opens.

   <img src="https://mintcdn.com/insightsoftware/b9ogX_L4Mqut_Uxb/simba-embedded-analytics/docs/self-service-analytics/26.3/images/v26/work-areas/visuals/sidebar-interact-26-2.png?fit=max&auto=format&n=b9ogX_L4Mqut_Uxb&q=85&s=7c63c8241c1852fa3fde0f5a6ddfff21" alt="use to define interactive options for your visuals" width="389" height="515" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/v26/work-areas/visuals/sidebar-interact-26-2.png" />

   By default, all interactivity settings are activated (on) for a visual. Each interaction is controlled by a switch. Slide the switches to the right to turn a setting on; slide them to the left to turn the setting off.

   In addition, you can use the **Preview Interactivity Settings** option to test the visual interactivity settings. When this switch is turned on, the visual behaves as it will when it is embedded. The **Preview Interactivity Settings** switch is a temporary switch: by default it is off each time you access the visual. It is not saved with the visual; so if you turn it on and save the visual, it will still be off the next time you edit the visual.

   Each visual interactivity setting is described in the following table.

   <table>
     <thead>
       <tr>
         <th>Visual Feature Group</th>
         <th>UI Setting</th>
         <th>JavaScript Setting</th>
         <th>Controls the ability to...</th>
       </tr>
     </thead>

     <tbody>
       <tr>
         <td rowSpan={5}>**Data Interactivity**</td>
         <td>Metrics</td>
         <td>`METRICS`</td>
         <td>Change metric fields (other than a metric that might be in the **Group** field) on the axes for the visual. This setting also controls whether a user can control the aggregation method (SUM, AVG, MIN, MAX, etc.) used for [metrics](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/data/custom-metrics#metrics) in a table.</td>
       </tr>

       <tr>
         <td>Group</td>
         <td>`GROUPING`</td>
         <td>Change the **Group** field on the x-axis of the visual. This setting also controls whether a user can group tables.</td>
       </tr>

       <tr>
         <td>Filter</td>
         <td>`FILTER`</td>
         <td>Filter data using the **Filter** option from the [visual drop-down menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup#use-the-visual-drop-down-menu) and to the left of the visual name on a visual, or a display name if viewed in a dashboard. (To fully remove filtering functionality for a visual, be sure to turn off the **Filter** switch in the Context Menu settings on the interactivity sidebar too.)</td>
       </tr>

       <tr>
         <td>Sort</td>
         <td>`SORT`</td>
         <td>Sort and limit the data in a visual. The sort and limit (<img src="https://mintcdn.com/insightsoftware/1fCfZrK84x8KmAw8/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/sidebar-sort.png?fit=max&auto=format&n=1fCfZrK84x8KmAw8&q=85&s=4fc0c54db55344620adb5335ad462296" alt="" width="15" height="22" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '15px', height: '22px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/sidebar-sort.png" />) [visual sidebar menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup#use-the-visual-sidebar-menu) option is disabled when this switch is off and you cannot access the Sort & Limit sidebar.</td>
       </tr>

       <tr>
         <td>Format</td>
         <td>`FORMAT`</td>
         <td>[Format specific data](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/rdt#format-numeric-table-data-using-the-table-context-menu) in a visual. These formatting options are disabled when the switch is off.</td>
       </tr>

       <tr>
         <td rowSpan={7}>**Context Menu**</td>
         <td>Drill Down</td>
         <td>`ZOOM_ACTION`</td>
         <td>Drill down into a selected data point on a visual using the **Drill Down** (formerly *Zoom*) option on the [context menu](#use-the-context-menu).</td>
       </tr>

       <tr>
         <td>Filter</td>
         <td>`FILTER_ACTION`</td>
         <td>Filter data using the **Filter** option on the [context menu](#use-the-context-menu). (To fully remove filtering functionality for a visual, be sure to turn off the **Filter** switch in the Data Interactivity settings on the interactivity sidebar too.)</td>
       </tr>

       <tr>
         <td>Details</td>
         <td>`DETAILS_ACTION`</td>
         <td>Display additional information about a specific visual data element using the **Details** option on the [context menu](#use-the-context-menu).</td>
       </tr>

       <tr>
         <td>Trend</td>
         <td>`TREND_ACTION`</td>
         <td>View trends for a selected data point using the **Trend** option on the [context menu](#use-the-context-menu).</td>
       </tr>

       <tr>
         <td>Keyset</td>
         <td>`KEYSET_ACTION`</td>
         <td>Create a keyset from a selected data point using the **Keyset** option on the [context menu](#use-the-context-menu). (To fully remove keyset functionality for a visual, be sure to turn off the **Create Keyset** switch in the Visualization settings on the interactivity sidebar too.)</td>
       </tr>

       <tr>
         <td>Actions</td>
         <td>`ACTIONS_ACTION`</td>
         <td>Invoke an action using the **Actions** option on the [context menu](#use-the-context-menu). (To fully remove actions functionality for a visual, be sure to turn off the **Actions** switch in the Visualization settings on the interactivity sidebar too.)</td>
       </tr>

       <tr>
         <td>Link</td>
         <td>`LINK_ACTION`</td>
         <td>Link to another dashboard using the **Link** option on the [context menu](#use-the-context-menu).</td>
       </tr>

       <tr>
         <td rowSpan={16}>**Visualization**</td>
         <td>Settings</td>
         <td>`SETTINGS`</td>
         <td>Specify settings for the visual. The visual settings (<img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/sidebar-chtsettings.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=74af55ee44cca52b9f7f4ae157440a81" alt="Select the settings icon on the sidebar menu to open settings options" width="28" height="33" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '28px', height: '33px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/sidebar-chtsettings.png" />) [visual sidebar menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup#use-the-visual-sidebar-menu) option is disabled when this switch is off and you cannot access the visual settings sidebar.</td>
       </tr>

       <tr>
         <td>Rulers</td>
         <td>`RULERS`</td>
         <td>Add visual reference lines and customize the markers used on the metric axis. The ruler settings (<img src="https://mintcdn.com/insightsoftware/1fCfZrK84x8KmAw8/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/sidebar-ruler.png?fit=max&auto=format&n=1fCfZrK84x8KmAw8&q=85&s=cd5637e5e6fa36eb5d66445f626f44b4" alt="" width="22" height="26" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '22px', height: '26px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/sidebar-ruler.png" />) [sidebar menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup#use-the-visual-sidebar-menu) option is disabled when this switch is off and you cannot access the ruler sidebar.</td>
       </tr>

       <tr>
         <td>Colors</td>
         <td>`COLORS`</td>
         <td>Change the color palette used by the visual. The color settings (<img src="https://mintcdn.com/insightsoftware/1fCfZrK84x8KmAw8/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/sidebar-color.png?fit=max&auto=format&n=1fCfZrK84x8KmAw8&q=85&s=23086f978c60bc7f5eaff8f93de81ae3" alt="" width="28" height="28" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '28px', height: '28px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/sidebar-color.png" />) [visual sidebar menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup#use-the-visual-sidebar-menu) option is disabled when this switch is off and you cannot access the color sidebar.</td>
       </tr>

       <tr>
         <td>Conditional Formatting</td>
         <td>`CONDITIONAL_FORMATTING`</td>
         <td>Apply conditional formatting to data in the visual. The conditional formatting (<img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/cdntl-format-22-4.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=ac8100f01d82ac00cba95a8a2993c796" alt="" width="24" height="24" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '24px', height: '24px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/cdntl-format-22-4.png" />) [visual sidebar menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup#use-the-visual-sidebar-menu) option is disabled when disabled.</td>
       </tr>

       <tr>
         <td>Create Keyset</td>
         <td>`KEYSET`</td>
         <td>Create a keyset from the visual data using the **Create Keyset** option from the [visual drop-down menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup#use-the-visual-drop-down-menu). (To fully remove keyset functionality for a visual, be sure to turn off the **Keyset** switch in the Context Menu settings on the interactivity sidebar too.)</td>
       </tr>

       <tr>
         <td>Save</td>
         <td>`SAVE`</td>
         <td>Save the visual.</td>
       </tr>

       <tr>
         <td>Save As</td>
         <td>`SAVE_AS`</td>
         <td>Save the visual using a new name.</td>
       </tr>

       <tr>
         <td>Copy</td>
         <td>`COPY`</td>
         <td>Copy a visual using the **Copy Visual** option from the [visual drop-down menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup#use-the-visual-drop-down-menu).</td>
       </tr>

       <tr>
         <td>Actions</td>
         <td>`ACTIONS`</td>
         <td>Invoke an action using the **Actions** option from the [visual drop-down menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup#use-the-visual-drop-down-menu). (To fully remove actions functionality for a visual, be sure to turn off the **Actions** switch in the Context Menu settings on the interactivity sidebar too.)</td>
       </tr>

       <tr>
         <td>Remove</td>
         <td>`REMOVE`</td>
         <td>Remove a visual using the **Remove Visual** option from the [visual drop-down menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup#use-the-visual-drop-down-menu).</td>
       </tr>

       <tr>
         <td>Re-Visualize (formerly *Visual Style*)</td>
         <td>`VISUAL_STYLE`</td>
         <td>Change a visual's type. The re-visualize (was *visual style*) (<img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/sidebar-chttype.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=559a7028c6be23336aa84a37bdb73f20" alt="" width="26" height="25" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '26px', height: '25px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/sidebar-chttype.png" />) [visual sidebar menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup#use-the-visual-sidebar-menu) option is disabled when this switch is off and you cannot access this sidebar.</td>
       </tr>

       <tr>
         <td>Select Time Bar Field</td>
         <td>`TIMEBAR_FIELD`</td>
         <td>Change the time field on the [time bar](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/time-bar).</td>
       </tr>

       <tr>
         <td>Maximize</td>
         <td>`MAXIMIZE`</td>
         <td>Maximize a visual for optimal viewing.</td>
       </tr>

       <tr>
         <td>Rename</td>
         <td>`RENAME`</td>
         <td>Rename a visual.</td>
       </tr>

       <tr>
         <td>Show Time Bar Panel</td>
         <td>`TIMEBAR_PANEL`</td>
         <td>Show the [time bar](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/time-bar) for the visual.</td>
       </tr>

       <tr>
         <td>Info</td>
         <td>`INFO`</td>
         <td>Allow users to edit information in the Info sidebar menu.</td>
       </tr>

       <tr>
         <td rowSpan={3}>**Exporting**</td>
         <td>Export to PNG/PDF</td>
         <td>`EXPORT_PNG_PDF`</td>
         <td>Export a visual to PNG/PDF using the **Export** option from the [visual drop-down menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup#use-the-visual-drop-down-menu).</td>
       </tr>

       <tr>
         <td>Export to CSV</td>
         <td>`EXPORT_CSV`</td>
         <td>Export a visual to a CSV file using the **Export** option from the [visual drop-down menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup#use-the-visual-drop-down-menu).</td>
       </tr>

       <tr>
         <td>Export to XLSX</td>
         <td>`EXPORT_XLSX`</td>
         <td>Export a visual to an XLSX file using the **Export** option from the [visual drop-down menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup#use-the-visual-drop-down-menu).</td>
       </tr>
     </tbody>
   </table>

3. Slide the switches on or off for the interactivity settings you want to change.

4. Optionally, preview the behavior with the interactivity settings applied. Slide the **Preview Interactivity Settings** switch on (to the right).

5. Select <img src="https://mintcdn.com/insightsoftware/2cXq_sDOxrDVXUcv/simba-embedded-analytics/docs/self-service-analytics/26.3/images/dashboards/dash-save.png?fit=max&auto=format&n=2cXq_sDOxrDVXUcv&q=85&s=c373f07d0546e540baff9fcabe9866af" alt="select the save icon to save your changes" width="21" height="20" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '21px', height: '20px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/dashboards/dash-save.png" /> to save the visual.

<h2 id="use-the-context-menu">
  Use the Context Menu
</h2>

Users can use the context menu on all visuals to view more information about specific data points in visuals. This menu provides streamlined options for working with data.

To access the context menu, select any data point in the visual, grouped or ungrouped, to explore or drill down into that data element.

<img src="https://mintcdn.com/insightsoftware/b9ogX_L4Mqut_Uxb/simba-embedded-analytics/docs/self-service-analytics/26.3/images/v26/work-areas/visuals/ctx-menu-26-2.png?fit=max&auto=format&n=b9ogX_L4Mqut_Uxb&q=85&s=61eb89f8172f846f36e9701d73e4cae7" alt="use the context menu to drill deeper into text for any available data element" width="1093" height="581" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/v26/work-areas/visuals/ctx-menu-26-2.png" />

Define how to embed the context menu in your Self-Service Analytics instance by specifying default options for right and left mouse selection. If needed, you can also add custom controls to the context menu for embedded visuals. See Control How Users Interact With a Visual.

The following options are available in the context menu. You will only see the options applicable the specific visual you are working in.

* [Details](#details)
* [Create Alert](#create-alert)
* [Filter](#filter)
* [Keyset](#keyset)
* [Trend](#trend)
* [Drill Down (Formerly Zoom)](#drill-down-formerly-zoom)
* [Link](#link)
* [Actions](#actions)
* [Remove](#remove)
* [Settings](#settings)

<h3 id="details">
  Details
</h3>

To display additional information about specific data elements, select **Details**. The details for the element are displayed in a table.

<img src="https://mintcdn.com/insightsoftware/b9ogX_L4Mqut_Uxb/simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/context-menu-details-22-4.png?fit=max&auto=format&n=b9ogX_L4Mqut_Uxb&q=85&s=96da149aff4155c8757092b749f0b718" alt="view the details that make up this element" width="1008" height="532" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/context-menu-details-22-4.png" />

The table header contains the following:

1. Attribute whose details you have selected to view
2. Metric
3. Volume metric
4. Time attribute and the selected time interval on the time bar
5. Data source

Select **Export Raw Data** to export your data set to a CSV file. If the **Table** visual type is enabled for your data source, you can select **Open in Table** to view your information.

You can also view the information in a pop-out window over your visual. Select the collapse icon to minimize the window.

<h3 id="create-alert">
  Create Alert
</h3>

Use **Create Alert** to create an alert for this visual and data element. See [Create an Alert Definition](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/alerts/alerts-ov#create-an-alert-definition).

<h3 id="filter">
  Filter
</h3>

Use **Filter** to filter other visuals in the dashboard that are subscribed to same-source or cross-source links by the data point you have selected. For more information, see [Apply a Filter to Dashboard Visuals Using the Context Menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/filters/filters-attr#apply-a-filter-to-dashboard-visuals-using-the-context-menu).

The context menu can be used to apply cross-visual filters to all visuals in a dashboard. If a visual subscribes to a link field, a context menu filter for the field from a different visual in the same dashboard will also be applied to the first visual. For example, if Visuals A and B are both subscribed to a link for field Z, and you use the context menu to apply a filter for field Z on Visual B, the filter will also be applied to Visual A. For information about controlling the publish and subscribe link settings for a visual, see [Control How Cross-Visual Filters Interact in a Dashboard](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/filters/pubsub-ov).

<Note>
  Unlike row-level filters, cross-visual filters are not saved with the visual.
</Note>

In addition, **Filter** is only available in the context menu when the visual publishes a link for the field it is also using for its visual grouping. It is *not* available if the published cross-visual links for the visual are muted. See [Mute a Published Link](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/filters/published-enable#mute-a-published-link).

<h3 id="keyset">
  Keyset
</h3>

Use **Keyset** to create a keyset from the selected data point. See [Create a Keyset](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/filters/keysets-overview#create-a-keyset).

<h3 id="trend">
  Trend
</h3>

Use **Trend** to view trends for a selected data point. **Trend** is not available for: Line and Bars Trend, Line Trend: Attribute Values, and Line Trend: Multiple Metrics.

<h3 id="drill-down-formerly-zoom">
  Drill Down (Formerly Zoom)
</h3>

Use **Drill Down** (formerly *Zoom*) to focus on the selected data point and filter the results by another filter attribute in the data source. When you select **Drill Down**, a menu appears from which you select the second filter attribute.

For example, if you wanted to see the actual sales for every county in the Electronics Product Group, select Electronics in the bar chart to bring up the context menu, select **Drill Down**, and then select the County attribute from the resulting menu. The result set in the bar chart might look like this:

<img src="https://mintcdn.com/insightsoftware/b9ogX_L4Mqut_Uxb/simba-embedded-analytics/docs/self-service-analytics/26.3/images/v26/work-areas/visuals/ctx-menu-drill-26-2.png?fit=max&auto=format&n=b9ogX_L4Mqut_Uxb&q=85&s=2650c001a121c6fcba839c528ffe1e7d" alt="use the context menu to drill deeper into text for any available data element; this shows the result of drilling down to sales by county in electronics" width="1075" height="1303" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/v26/work-areas/visuals/ctx-menu-drill-26-2.png" />

<h3 id="link">
  Link
</h3>

Use **Link** to quickly access a dashboard that has been linked to this visual. **Link** is only available if a dashboard link has been defined for a visual. See [Link a Dashboard](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/dashboards/dash-interactivity#link-a-dashboard).

<h3 id="actions">
  Actions
</h3>

<Note>
  You must be logged in as an administrator or as a user with the **Invoke Actions** [privilege](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/aaa-ov#group-privilege-reference).
</Note>

Use **Actions** to invoke an action. If this menu option does not appear on the context menu, an action template is either not defined or is not enabled for the data source used by the visual.

The invoked action:

* Creates a query definition based on the filters applied to the visual and on the data and limit specifications in the associated action template.
* Sends the query definition to your application. Your application can use the Self-Service Analytics API to run the query and display or use the data that it collects.

To invoke an action, see [Invoke an Action](/simba-embedded-analytics/docs/self-service-analytics/26.3/embed-and-extend/actions-overview#invoke-an-action).

<h3 id="remove">
  Remove
</h3>

Select **Remove** to exclude the selected data element from your visual.

<h3 id="settings">
  Settings
</h3>

Select **Settings** to open the [visual sidebar menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup#use-the-visual-sidebar-menu).
