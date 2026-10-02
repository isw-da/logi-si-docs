> ## Documentation Index
> Fetch the complete documentation index at: https://insightsoftware.mintlify.site/llms.txt
> Use this file to discover all available pages before exploring further.

# Control How Users Interact With a Dashboard

You can control how users can interact with a dashboard, and access to self service reports. Control their ability to:

* Resize or move visuals in a dashboard
* Add visuals, text snippets, and filter snippets to a dashboard
* Refresh, save or delete a dashboard
* Filter a dashboard
* Rename a dashboard
* Mark the dashboard as a favorite
* Link a dashboard or set up cross-source links in the dashboard
* Export a dashboard

You can also apply a global set of visual interactivity settings to all of the visuals on the dashboard that overrides the interactivity settings for the individual visuals on the dashboard.

<Warning>
  User attributes are not resolved when previewing interactivity settings, and default fallbacks will be used in the Preview mode.
</Warning>

**Control user interactions with a dashboard and its visuals**

1. Select the visual on the dashboard or in the Visual Gallery.

2. Select the interactivity option button to the left of the dashboard title.

   <img src="https://mintcdn.com/insightsoftware/2cXq_sDOxrDVXUcv/simba-embedded-analytics/docs/self-service-analytics/26.3/images/dashboards/dash-interactive-icon-23-2.png?fit=max&auto=format&n=2cXq_sDOxrDVXUcv&q=85&s=6a1fd73284c44cebe67d276d5b4a770d" alt="select the interactivity icon to adjust dashboard interactivty settings" width="285" height="130" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/dashboards/dash-interactive-icon-23-2.png" />

   The dashboard interactivity panel appears.

   <img src="https://mintcdn.com/insightsoftware/2cXq_sDOxrDVXUcv/simba-embedded-analytics/docs/self-service-analytics/26.3/images/dashboards/dash-interactivity-23-2.png?fit=max&auto=format&n=2cXq_sDOxrDVXUcv&q=85&s=7eb476e796cb7ab2bbaa54e2409fea5a" alt="Adjust interactivity settings for a dashboard and its visuals here" width="401" height="646" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/dashboards/dash-interactivity-23-2.png" />

   By default, all interactivity settings are activated (enabled) for a dashboard. Each setting is controlled by a toggle switch. Slide the switch to the right to turn an interactivity setting on; slide them to the left to turn a setting off.

   There are two tabs on the dashboard interactivity panel: **Dashboard** and **Visuals**. The settings on each tab are described at the end of these instructions.

   In addition, you can use the **Preview Interactivity Settings** option to test the dashboard and visual interactivity settings. When this switch is turned on, the dashboard and visuals behave as they will when the dashboard is embedded, based on the interactivity settings for the dashboard and its visuals. The **Preview Interactivity Settings** switch is a temporary switch: by default it is off each time you access the dashboard. It is not saved with the dashboard; so if you turn it on and save the dashboard, it will still be off the next time you edit the dashboard.

3. Slide the switch on or off for the interactivity settings you want to change on the **Dashboard** tab. See [Dashboard Interactivity Settings (Dashboard Tab)](#dashboard-interactivity-settings-dashboard-tab).

4. Slide the switch on or off for the interactivity settings you want to change on the **Visuals** tab. See [Visual Interactivity Settings (Visuals Tab)](#visual-interactivity-settings-visuals-tab).

5. Select **Save** to save the interactivity settings.

6. Optionally, preview the behavior with the interactivity settings applied. Slide the **Preview Interactivity Settings** switch on (to the right).

   <Note>
     Custom attributes are not evaluated in Preview mode. If custom attributes are used, Self-Service Analytics uses defaults to preview the interactivity settings. Customer attributes will be applied correctly in an embedded workflow.
   </Note>

7. [Save](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/dashboards/dash-manage#save-a-dashboard) the dashboard. When you save a dashboard (Save option), the dashboard interactivity settings are also saved (if there are any). If there are no dashboard interactivity settings or if they have not been changed, they are not saved. When you save a dashboard with a new name (Save As option), the dashboard interactivity settings are saved to the new dashboard, but the interactivity settings for the original dashboard remain unchanged.

<h2 id="dashboard-interactivity-settings-dashboard-tab">
  Dashboard Interactivity Settings (Dashboard Tab)
</h2>

Each dashboard interactivity setting is described in the following table.

<table>
  <thead>
    <tr>
      <th>Dashboard Feature Group</th>
      <th>Setting</th>
      <th>Controls the ability to...</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td rowSpan={16}>**Editing**</td>
      <td>Change Layout</td>
      <td>Resize or move visuals and rich text snippet widgets in the dashboard.</td>
    </tr>

    <tr>
      <td>Add Existing Visuals</td>
      <td>Add existing visuals to the dashboard.</td>
    </tr>

    <tr>
      <td>Add New Visuals</td>
      <td>Add new visuals to the dashboard.</td>
    </tr>

    <tr>
      <td>Add Text Snippets</td>
      <td>Add text snippets to the dashboard.</td>
    </tr>

    <tr>
      <td>Add Filter Snippets</td>
      <td>Add filter snippets to the dashboard.</td>
    </tr>

    <tr>
      <td>Delete</td>
      <td>Delete the dashboard. When this setting is turned off, the <img src="https://mintcdn.com/insightsoftware/2cXq_sDOxrDVXUcv/simba-embedded-analytics/docs/self-service-analytics/26.3/images/dashboards/dash-delete.png?fit=max&auto=format&n=2cXq_sDOxrDVXUcv&q=85&s=c083bb7faa9c686e4c8572cc5c69aa4f" alt="" width="19" height="21" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '19px', height: '21px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/dashboards/dash-delete.png" /> [dashboard icon](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/dashboards/dash-layout#use-the-dashboard-icons) is not available.</td>
    </tr>

    <tr>
      <td>Save</td>
      <td>Save the dashboard. When this setting is turned off, the <img src="https://mintcdn.com/insightsoftware/2cXq_sDOxrDVXUcv/simba-embedded-analytics/docs/self-service-analytics/26.3/images/dashboards/dash-save.png?fit=max&auto=format&n=2cXq_sDOxrDVXUcv&q=85&s=c373f07d0546e540baff9fcabe9866af" alt="select the save icon to save your changes" width="21" height="20" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '21px', height: '20px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/dashboards/dash-save.png" /> [dashboard icon](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/dashboards/dash-layout#use-the-dashboard-icons) is not available.</td>
    </tr>

    <tr>
      <td>Save As</td>
      <td>Save the dashboard and unsaved changes as a dashboard using a different name. When this setting is turned off, the <img src="https://mintcdn.com/insightsoftware/2cXq_sDOxrDVXUcv/simba-embedded-analytics/docs/self-service-analytics/26.3/images/dashboards/dash-save-as.png?fit=max&auto=format&n=2cXq_sDOxrDVXUcv&q=85&s=0a1f29aed30da7ee353c14aac6c1c591" alt="" width="18" height="20" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '18px', height: '20px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/dashboards/dash-save-as.png" /> [dashboard icon](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/dashboards/dash-layout#use-the-dashboard-icons) is not available.</td>
    </tr>

    <tr>
      <td>Filter</td>
      <td>Apply filters to the dashboard. When this setting is turned off, the <img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/filter-dash.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=68279f203a0950b32bfab88e7273d5ba" alt="" width="20" height="19" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '20px', height: '19px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/filter-dash.png" />[dashboard icon](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/dashboards/dash-layout#use-the-dashboard-icons) is not available. You can still apply filters to the visuals, however.</td>
    </tr>

    <tr>
      <td>Rename</td>
      <td>Rename the dashboard.</td>
    </tr>

    <tr>
      <td>Change Description</td>
      <td>Allow users to change the description on the Info sidebar menu if one exists.</td>
    </tr>

    <tr>
      <td>Add to Favorites</td>
      <td>Mark the dashboard as a favorite. When this setting is turned off, the <img src="https://mintcdn.com/insightsoftware/2cXq_sDOxrDVXUcv/simba-embedded-analytics/docs/self-service-analytics/26.3/images/dashboards/dash-fav.png?fit=max&auto=format&n=2cXq_sDOxrDVXUcv&q=85&s=b316dd7cb31ab07c459eb50f712f6211" alt="select the favorite icon to add or remove the item from your favorited items" width="35" height="34" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '35px', height: '34px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/dashboards/dash-fav.png" /> [dashboard icon](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/dashboards/dash-layout#use-the-dashboard-icons) is not available.</td>
    </tr>

    <tr>
      <td>Share Filter Sets</td>
      <td>Share saved filter sets with other users. When this setting is turned off, other users cannot view or use the filter sets for the dashboard.</td>
    </tr>

    <tr>
      <td>Schedule Reports</td>
      <td>Schedule reports for the dashboard.</td>
    </tr>

    <tr>
      <td>Share Dashboard</td>
      <td>Share the dashboard with specific users.</td>
    </tr>

    <tr>
      <td>Comments</td>
      <td>Allow users with Commenter access or higher to create, view, and manage their own comments. See [Widget Comments](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/widgets/widget-cmts-ov).</td>
    </tr>

    <tr>
      <td rowSpan={4}>**Data**</td>
      <td>Set Up Dashboard Link</td>
      <td>Link dashboards. When this setting is turned off, the <img src="https://mintcdn.com/insightsoftware/2cXq_sDOxrDVXUcv/simba-embedded-analytics/docs/self-service-analytics/26.3/images/dashboards/dash-link.png?fit=max&auto=format&n=2cXq_sDOxrDVXUcv&q=85&s=6b46f3f4e6fa2bdc72ae8dee012401c0" alt="select to manage dashboard links and visual links" width="21" height="21" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '21px', height: '21px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/dashboards/dash-link.png" /> [dashboard icon](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/dashboards/dash-layout#use-the-dashboard-icons) is not available.</td>
    </tr>

    <tr>
      <td>Refresh</td>
      <td>Refresh the dashboard data. When this setting is turned off, the <img src="https://mintcdn.com/insightsoftware/2cXq_sDOxrDVXUcv/simba-embedded-analytics/docs/self-service-analytics/26.3/images/dashboards/dash-refresh.png?fit=max&auto=format&n=2cXq_sDOxrDVXUcv&q=85&s=53cc532b6fce4e41f7756425d1b87639" alt="select to refresh the underlying data behind an object, or the specific field" width="34" height="34" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '34px', height: '34px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/dashboards/dash-refresh.png" /> [dashboard icon](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/dashboards/dash-layout#use-the-dashboard-icons) is not available.</td>
    </tr>

    <tr>
      <td>Change Dashboard Interactions</td>
      <td>Link fields between disparate data sources to create cross-source links. When this setting is turned off, the <img src="https://mintcdn.com/insightsoftware/2cXq_sDOxrDVXUcv/simba-embedded-analytics/docs/self-service-analytics/26.3/images/dashboards/dash-xsourcelink.png?fit=max&auto=format&n=2cXq_sDOxrDVXUcv&q=85&s=a0bac4bcf53aa484043898173bc91e9b" alt="select to manage cross source links in your environment" width="23" height="22" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '23px', height: '22px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/dashboards/dash-xsourcelink.png" /> [dashboard icon](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/dashboards/dash-layout#use-the-dashboard-icons) is not available.</td>
    </tr>

    <tr>
      <td>Set Up Dashboard Alerts</td>
      <td>Define alerts for the dashboard.</td>
    </tr>

    <tr>
      <td rowSpan={3}>**Exporting**</td>
      <td>Export to PNG/PDF</td>
      <td>Export the dashboard as a PNG or PDF file. When this setting is turned off, the [Export dialog](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/dashboards/dash-import#export-dashboards) no longer provides an option to export an image. If all settings for **Exporting** are turned off, the <img src="https://mintcdn.com/insightsoftware/2cXq_sDOxrDVXUcv/simba-embedded-analytics/docs/self-service-analytics/26.3/images/dashboards/dash-export.png?fit=max&auto=format&n=2cXq_sDOxrDVXUcv&q=85&s=e8b1d12ba47dbfb0aa811319cc4af59b" alt="select to export this item" width="23" height="24" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '23px', height: '24px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/dashboards/dash-export.png" /> [dashboard icon](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/dashboards/dash-layout#use-the-dashboard-icons) is not available.</td>
    </tr>

    <tr>
      <td>Export Configuration</td>
      <td>Export the JSON configuration for the dashboard. When this setting is turned off, the [Export dialog](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/dashboards/dash-import#export-dashboards) no longer provides an option to export the configuration. If all settings for **Exporting** are turned off, the <img src="https://mintcdn.com/insightsoftware/2cXq_sDOxrDVXUcv/simba-embedded-analytics/docs/self-service-analytics/26.3/images/dashboards/dash-export.png?fit=max&auto=format&n=2cXq_sDOxrDVXUcv&q=85&s=e8b1d12ba47dbfb0aa811319cc4af59b" alt="select to export this item" width="23" height="24" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '23px', height: '24px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/dashboards/dash-export.png" /> [dashboard icon](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/dashboards/dash-layout#use-the-dashboard-icons) is not available.</td>
    </tr>

    <tr>
      <td>Export Data</td>
      <td>Export the dashboard in Excel (XLSX) format as raw data or visual data. When this setting is turned off, the [Export dialog](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/dashboards/dash-import#export-dashboards) no longer provides an option to export the dashboard in this format. If all settings for **Exporting** are turned off, the <img src="https://mintcdn.com/insightsoftware/2cXq_sDOxrDVXUcv/simba-embedded-analytics/docs/self-service-analytics/26.3/images/dashboards/dash-export.png?fit=max&auto=format&n=2cXq_sDOxrDVXUcv&q=85&s=e8b1d12ba47dbfb0aa811319cc4af59b" alt="select to export this item" width="23" height="24" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '23px', height: '24px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/dashboards/dash-export.png" /> [dashboard icon](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/dashboards/dash-layout#use-the-dashboard-icons) is not available.</td>
    </tr>
  </tbody>
</table>

<h2 id="visual-interactivity-settings-visuals-tab">
  Visual Interactivity Settings (Visuals Tab)
</h2>

The Visuals tab allows you to override the interactivity settings for the individual visuals in the dashboard. When the **Override Visual Interactivity** switch is turned on, the individual visual interactivity settings for each visual on the dashboard are overridden and ignored and the visual interactivity settings set for the dashboard are used for all of the visuals in the dashboard.

These settings are only applied to the visuals while they are used in this dashboard and not universally. The interactivity settings for the visuals themselves are not affected when used elsewhere. In other words, if a visual is used in one dashboard (Dashboard A) with **Override Visual Interactivity** turned on and is also used in a second dashboard (Dashboard B) with **Override Visual Interactivity** turned off, the individual visual interactivity settings are not honored in Dashboard A, but are honored in Dashboard B.

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
      <td>Drill down into a selected data point on a visual using the **Drill Down** (formerly *Zoom*) option on the [context menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-interactivity#use-the-context-menu).</td>
    </tr>

    <tr>
      <td>Filter</td>
      <td>`FILTER_ACTION`</td>
      <td>Filter data using the **Filter** option on the [context menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-interactivity#use-the-context-menu). (To fully remove filtering functionality for a visual, be sure to turn off the **Filter** switch in the Data Interactivity settings on the interactivity sidebar too.)</td>
    </tr>

    <tr>
      <td>Details</td>
      <td>`DETAILS_ACTION`</td>
      <td>Display additional information about a specific visual data element using the **Details** option on the [context menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-interactivity#use-the-context-menu).</td>
    </tr>

    <tr>
      <td>Trend</td>
      <td>`TREND_ACTION`</td>
      <td>View trends for a selected data point using the **Trend** option on the [context menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-interactivity#use-the-context-menu).</td>
    </tr>

    <tr>
      <td>Keyset</td>
      <td>`KEYSET_ACTION`</td>
      <td>Create a keyset from a selected data point using the **Keyset** option on the [context menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-interactivity#use-the-context-menu). (To fully remove keyset functionality for a visual, be sure to turn off the **Create Keyset** switch in the Visualization settings on the interactivity sidebar too.)</td>
    </tr>

    <tr>
      <td>Actions</td>
      <td>`ACTIONS_ACTION`</td>
      <td>Invoke an action using the **Actions** option on the [context menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-interactivity#use-the-context-menu). (To fully remove actions functionality for a visual, be sure to turn off the **Actions** switch in the Visualization settings on the interactivity sidebar too.)</td>
    </tr>

    <tr>
      <td>Link</td>
      <td>`LINK_ACTION`</td>
      <td>Link to another dashboard using the **Link** option on the [context menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-interactivity#use-the-context-menu).</td>
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

<h2 id="link-a-dashboard">
  Link a Dashboard
</h2>

While working with your dashboard, you may need to analyze data from other dashboards. You can link a visual from your dashboard to another dashboard. This allows you to quickly access other dashboards with related information. To link dashboards, you must have permissions to share and link dashboards. When linking one dashboard to another, you can elect to have the target dashboard inherit the filters from the source dashboard.

**Link a dashboard visual to another dashboard**

1. Open the dashboard you want to link.

2. Select dashboard links <img src="https://mintcdn.com/insightsoftware/2cXq_sDOxrDVXUcv/simba-embedded-analytics/docs/self-service-analytics/26.3/images/dashboards/dash-link.png?fit=max&auto=format&n=2cXq_sDOxrDVXUcv&q=85&s=6b46f3f4e6fa2bdc72ae8dee012401c0" alt="select to manage dashboard links and visual links" width="21" height="21" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '21px', height: '21px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/dashboards/dash-link.png" /> on the [dashboard icon bar](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/dashboards/dash-layout#use-the-dashboard-icons). The Dashboard Links dialog appears.

   <img src="https://mintcdn.com/insightsoftware/2cXq_sDOxrDVXUcv/simba-embedded-analytics/docs/self-service-analytics/26.3/images/dashboards/dashboard-links-dialog-710.png?fit=max&auto=format&n=2cXq_sDOxrDVXUcv&q=85&s=4eb41a4e93dc31a8367dd473e00aa399" alt="" width="776" height="652" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/dashboards/dashboard-links-dialog-710.png" />

3. Select **Add Link**. The Select Link dialog opens.

   <img src="https://mintcdn.com/insightsoftware/GTXU--ZlYc3DodOR/simba-embedded-analytics/docs/self-service-analytics/26.3/images/dashboards/dashboard-select-links-dialog-710.png?fit=max&auto=format&n=GTXU--ZlYc3DodOR&q=85&s=47cc2e04385f49511aa77c1d868da9af" alt="" width="778" height="653" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/dashboards/dashboard-select-links-dialog-710.png" />

4. Select a visual and dashboard to link, then select **Apply**. The Dashboard Link dialog opens, showing the visual and dashboard links.

   <img src="https://mintcdn.com/insightsoftware/GTXU--ZlYc3DodOR/simba-embedded-analytics/docs/self-service-analytics/26.3/images/dashboards/dashboard-manage-links-dialog-710.png?fit=max&auto=format&n=GTXU--ZlYc3DodOR&q=85&s=2d0a0857abf385dbc41edf77d00b1764" alt="" width="778" height="653" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/dashboards/dashboard-manage-links-dialog-710.png" />

5. By default, **Inherit Visual Filter** is enabled, and the dashboard passes the filters currently used on the dashboard (or the filters applied based on what is selected when the dashboard link occurs) to the linked dashboard. If you do not want the filters from the dashboard carried over, disable **Inherit Visual Filter**. The filters are only carried over if the dashboards are using the same data source configuration.

6. Close the dialog.

7. [Save](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/dashboards/dash-manage#save-a-dashboard) the dashboard to save the dashboard link settings.

8. On the [visual drop-down menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup#use-the-visual-drop-down-menu) for the linked visual, a new option in the following format appears:

   <img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/link-new.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=c7b0d543978cc3f8c80b0ed21929fcc4" alt="" width="20" height="16" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '20px', height: '16px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/link-new.png" />**Go to "\<dashboard>"**

   Select this option to jump to the linked dashboard.

**Navigate to a linked dashboard**

* Select the <img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/link-new.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=c7b0d543978cc3f8c80b0ed21929fcc4" alt="" width="20" height="16" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '20px', height: '16px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/link-new.png" />**Go to "\<dashboard>"** link on the [visual drop-down menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup#use-the-visual-drop-down-menu).
* You can also navigate to the linked dashboard by selecting **LINK** on the dashboard [context menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-interactivity#use-the-context-menu).

**Delete a dashboard link**

1. Open the dashboard containing the visual you want to unlink.

2. Select <img src="https://mintcdn.com/insightsoftware/2cXq_sDOxrDVXUcv/simba-embedded-analytics/docs/self-service-analytics/26.3/images/dashboards/dash-link.png?fit=max&auto=format&n=2cXq_sDOxrDVXUcv&q=85&s=6b46f3f4e6fa2bdc72ae8dee012401c0" alt="select to manage dashboard links and visual links" width="21" height="21" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '21px', height: '21px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/dashboards/dash-link.png" /> on the [dashboard icon bar](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/dashboards/dash-layout#use-the-dashboard-icons). The Dashboard Links dialog appears showing the links to other dashboards.

   <img src="https://mintcdn.com/insightsoftware/GTXU--ZlYc3DodOR/simba-embedded-analytics/docs/self-service-analytics/26.3/images/dashboards/dashboard-manage-links-dialog-710.png?fit=max&auto=format&n=GTXU--ZlYc3DodOR&q=85&s=2d0a0857abf385dbc41edf77d00b1764" alt="" width="778" height="653" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/dashboards/dashboard-manage-links-dialog-710.png" />

3. On the Dashboard Links dialog, select the visual and select the remove (<img src="https://mintcdn.com/insightsoftware/GTXU--ZlYc3DodOR/simba-embedded-analytics/docs/self-service-analytics/26.3/images/dashboards/link-delete-710.png?fit=max&auto=format&n=GTXU--ZlYc3DodOR&q=85&s=36ed3b6a0baaa934cb9446d3df898ea9" alt="" width="18" height="18" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '18px', height: '18px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/dashboards/link-delete-710.png" />) icon. The link is removed.

   You must remove all links to a dashboard before you can delete the dashboard.

4. [Save](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/dashboards/dash-manage#save-a-dashboard) the dashboard to save the dashboard link settings.
