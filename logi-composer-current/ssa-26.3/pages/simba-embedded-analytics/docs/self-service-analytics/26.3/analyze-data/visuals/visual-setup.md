> ## Documentation Index
> Fetch the complete documentation index at: https://insightsoftware.mintlify.site/llms.txt
> Use this file to discover all available pages before exploring further.

# Visuals Work Areas

Self-Service Analytics includes a wide array of different visual types and tools you can use visualize and explore your data.

Visuals take data from your data sources so you can present information in an easy to view, adjust, and update layout. You can create visuals that are used in multiple dashboards, stored and shared among Self-Service Analytics users in the Visual Gallery, or local visuals unique to a single dashboard.

| Icon | Description |
| - | - |
| <img src="https://mintcdn.com/insightsoftware/1fCfZrK84x8KmAw8/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/visual-shared.png?fit=max&auto=format&n=1fCfZrK84x8KmAw8&q=85&s=8f2882bddad018bea849230503ec30ce" alt="" width="30" height="30" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '30px', height: '30px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/visual-shared.png" /> | **Visual Gallery visuals** are visuals created by users and saved in the Visual Gallery. Share these visuals with other users to use in multiple dashboards. Any changes you make and save to a visual are reflected on all dashboards that include the shared visual. |
| <img src="https://mintcdn.com/insightsoftware/1fCfZrK84x8KmAw8/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/visual-local.png?fit=max&auto=format&n=1fCfZrK84x8KmAw8&q=85&s=4639cd098713ec6fab97be31326c0efd" alt="" width="30" height="30" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '30px', height: '30px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/visual-local.png" /> | **Local visuals** are visuals created by users directly on a dashboard. These visuals are unique to the dashboard. Any changes you make are saved when you save the dashboard. |

<h2 id="the-visual-interface">
  The Visual Interface
</h2>

Self-Service Analytics's canvas provides a comprehensive suite of tools to help you conduct in-depth analysis, filter data points, and discover needed insights quickly and efficiently.

### Tools in the Visual Interface

<img src="https://mintcdn.com/insightsoftware/cQU1Auv4yvPMjcip/simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/visual-layout-annotated-23-1.png?fit=max&auto=format&n=cQU1Auv4yvPMjcip&q=85&s=e951dfa18f691d282f1cae1ff3f3928c" alt="Use this work area to adjust your visuals" width="1119" height="649" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/visual-layout-annotated-23-1.png" />

1. **Display Name**: By default, a visual's display name is the name of the data source used for the visual for local visuals, or the display name for a visual from the visual gallery. Select the title to edit.

2. **Dashboard Name or Title**: The dashboard name if editing a visual in a dashboard. Select the name to edit it or save the dashboard to be prompted for a dashboard name. The default name of the dashboard is **Untitled dashboard**.

3. Indicates whether the dashboard has been saved. This information is not available if you are editing a visual from the Visual Gallery.

4. Indicates whether a visual gallery visual has been saved.

   * If the visual is a local visual, this area is blank. All local visuals are saved when you save the dashboard.

5. **Time Bar** and **Time Controls**:

   * Filter your data by a time attribute.
   * Zoom into specific period within the selected date range.
   * Explore the dynamics of your data using the **Play/Pause** button.

   See [Use the Time Bar](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/time-bar).

6. **X-** and **Y- Axis Labels** and the **Color Metric** (availability varies, depending on the visual type): Select an axis label to change an attribute or metric. See [Change the Axes](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/colors-and-axes/colors#change-the-axes) and [Change the Visual Color Metric](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/colors-and-axes/colors#change-the-visual-color-metric).

   If you disable the Volume property in a data source configuration, it does not appear in visual tooltips. The only exception to this is in histograms which plot the volume or number of records.

7. **Legend:** By default, a legend is available for supported visual types, and can be switched on or off in the Colors sidebar menu.

8. The dashboard icon bar. Use the options here to manage the dashboard. See [Use the Dashboard Icons](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/dashboards/dash-layout#use-the-dashboard-icons). This is only available on a dashboard; not on a visual edited from the [Visual Gallery](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-gallery).

9. Select <img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/expand-2.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=4e0acb99d6bff1a2f72cf35d1f4b4edd" alt="" width="20" height="20" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '20px', height: '20px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/expand-2.png" /> to expand a visual on a dashboard. This allows you to get a closer look at it. This is only available on a dashboard; not on a visual edited from the [Visual Gallery](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-gallery).

10. The <img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/more-menu.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=1471c7a569a7e100cd7fa4083b04551a" alt="Selet the three dots icon to open a show more menu or take actions for the named column" width="21" height="12" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '21px', height: '12px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/more-menu.png" /> at the top right of a visual displays the [visual drop-down menu](#use-the-visual-drop-down-menu). This menu includes an option to open **Settings** for the visual, and its [sidebar menu](#use-the-visual-sidebar-menu).

11. The visual [sidebar menu](#use-the-visual-sidebar-menu). Select a sidebar menu option to open an appropriate sidebar for a visual. See [Use the Visual Sidebar Menu](#use-the-visual-sidebar-menu).

12. Select <img src="https://mintcdn.com/insightsoftware/1fCfZrK84x8KmAw8/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/undo-new.png?fit=max&auto=format&n=1fCfZrK84x8KmAw8&q=85&s=339dcc3e9a29558b45ea3487f699e52c" alt="" width="22" height="19" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '22px', height: '19px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/undo-new.png" /> to undo the most recent change you made to a visual.

13. Visual-specific options:

    1. Select <img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/filter-vis.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=0a044ea0662c55e06133074a55d93cd9" alt="select the filter icon to open the filters sidebar and add or edit filters" width="17" height="17" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '17px', height: '17px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/filter-vis.png" /> to filter the data on a visual.
    2. Select <img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/dash-interact.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=363d120a7c4e016429e394b06d6d713d" alt="" width="26" height="18" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '26px', height: '18px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/dash-interact.png" /> to view published filters.
    3. The visual icon indicates if a visual is local (<img src="https://mintcdn.com/insightsoftware/1fCfZrK84x8KmAw8/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/visual-local.png?fit=max&auto=format&n=1fCfZrK84x8KmAw8&q=85&s=4639cd098713ec6fab97be31326c0efd" alt="" width="20" height="20" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '20px', height: '20px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/visual-local.png" />) or a visual gallery visual (<img src="https://mintcdn.com/insightsoftware/1fCfZrK84x8KmAw8/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/visual-shared.png?fit=max&auto=format&n=1fCfZrK84x8KmAw8&q=85&s=8f2882bddad018bea849230503ec30ce" alt="" width="20" height="20" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '20px', height: '20px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/visual-shared.png" />).

14. Dashboard-specific options:

    1. Select <img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/filter-vis.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=0a044ea0662c55e06133074a55d93cd9" alt="select the filter icon to open the filters sidebar and add or edit filters" width="17" height="17" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '17px', height: '17px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/filter-vis.png" /> to filter the data on a dashboard. The dashboard-level filter icon is available only when all visuals on a dashboard are from the same data source.
    2. Select <img src="https://mintcdn.com/insightsoftware/1fCfZrK84x8KmAw8/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/sidebar-interactive.png?fit=max&auto=format&n=1fCfZrK84x8KmAw8&q=85&s=5068072b72f71db3c65f6eed78658798" alt="select the interactivity icon to adjust the interactivity settings for this item" width="20" height="20" noZoom data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/sidebar-interactive.png" /> to open dashboard and visual interactivity settings.
    3. Select <img src="https://mintcdn.com/insightsoftware/1fCfZrK84x8KmAw8/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/viewer-editor-toggle.png?fit=max&auto=format&n=1fCfZrK84x8KmAw8&q=85&s=16859ffbaed0453d0d2a8dbb4201c5f9" alt="select to toggle between edit and view modes" width="20" height="21" noZoom data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/viewer-editor-toggle.png" /> to toggle dashboard view mode between [Viewer and Editor](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/dashboards/dash-layout#use-dashboard-view-mode) modes.
    4. Select <img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/locking-layout-toggle.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=c1addc6e9fec50faff646c2559330d57" alt="" width="20" height="20" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '20px', height: '20px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/locking-layout-toggle.png" /> to enable and disable locking the dashboard layout.
    5. Select <img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/responsive-toggle-32-1.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=3868d9104614b7aeeaf1f0221b679e28" alt="" width="20" height="20" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '20px', height: '20px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/responsive-toggle-32-1.png" /> to enable and disable responsive layout for this dashboard. See [Use the Responsive Dashboard Layout](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/dashboards/dash-layout#use-the-responsive-dashboard-layout).

15. The context menu. Use menu options to view or adjust data. See [Use the Context Menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-interactivity#use-the-context-menu).

## Visual Setup

Control visuals available for each data source configuration you create using the Available Visual Types work area. See [Available Visual Types](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/available-visual-types).

After saving a data source definition, adjust settings applicable to new visuals on the [Global Settings Work Areas](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/data-source-config-global-settings-tab).

To add a visual, see:

* [Create Dashboards](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/dashboards/dash-manage#create-dashboards)
* [Create and Add Visuals to the Visual Gallery](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-add-dash#create-and-add-visuals-to-the-visual-gallery)
* [Manage Visuals](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-add-dash)
* [Add Local Visuals to a Dashboard](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-add-dash#add-local-visuals-to-a-dashboard)
* [Add Existing Visuals to a Dashboard](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-add-dash#add-existing-visuals-to-a-dashboard)

After you create a visual, you can alter its settings. See [The Visual Interface](#the-visual-interface).

<h2 id="edit-visuals">
  Edit Visuals
</h2>

Edit visuals directly on a Self-Service Analytics dashboard or in the Visual Gallery. When you modify a visual from the Visual Gallery and save your changes, the changes are made to the visual in the Visual Gallery and everywhere the visual is used on dashboards.

To edit a visual, you must be logged in as a user belonging to a group with the [privilege **Administer Visuals**](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/aaa-ov#group-privilege-reference) enabled.

**Edit a visual**

1. Select the visual on a dashboard or in the Visual Gallery. When selected on a dashboard, a blue border appears around the visual. If you select a visual with a streaming data source, the [time bar](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/time-bar) (Data DVR) appears.

2. Depending on the edits you need to make, select an item on the visual drop-down menu (<img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/more-menu.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=1471c7a569a7e100cd7fa4083b04551a" alt="Selet the three dots icon to open a show more menu or take actions for the named column" width="21" height="12" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '21px', height: '12px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/more-menu.png" />) or one of the [sidebars](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/available-visual-types#use-the-re-visualize-sidebar) for the visual. You can also use the [axes labels](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/colors-and-axes/colors#change-the-axes) on the visual to change what is displayed and the [context menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-interactivity#use-the-context-menu) to visualize the data on your visual, adjust the settings, and more.

   Some of the options described here can be performed in the Visual Gallery, some only when editing the visual in a dashboard, and some in both.

   | Edit Option | Procedure | Visual Gallery/ Dashboard/Both |
   | - | - | - |
   | Change the data shown | Depending on the style of the visual, select new data fields in the axes labels. See [Change the Axes](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/colors-and-axes/colors#change-the-axes) | Both |
   | Change the visual type | Select the re-visualize icon <img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/sidebar-chttype.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=559a7028c6be23336aa84a37bdb73f20" alt="" width="26" height="25" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '26px', height: '25px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/sidebar-chttype.png" /> on the [sidebar menu](#use-the-visual-sidebar-menu). See [Re-Visualize (Change a Visual Type)](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/available-visual-types#re-visualize-change-a-visual-type). | Both |
   | Modify the colors | Select <img src="https://mintcdn.com/insightsoftware/1fCfZrK84x8KmAw8/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/sidebar-color.png?fit=max&auto=format&n=1fCfZrK84x8KmAw8&q=85&s=23086f978c60bc7f5eaff8f93de81ae3" alt="" width="28" height="28" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '28px', height: '28px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/sidebar-color.png" />on the [sidebar menu](#use-the-visual-sidebar-menu). A corresponding sidebar appears. See [Change Color Schemes](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/colors-and-axes/colors). | Both |
   | Modify the rulers and reference lines | Select <img src="https://mintcdn.com/insightsoftware/1fCfZrK84x8KmAw8/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/sidebar-ruler.png?fit=max&auto=format&n=1fCfZrK84x8KmAw8&q=85&s=cd5637e5e6fa36eb5d66445f626f44b4" alt="" width="22" height="26" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '22px', height: '26px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/sidebar-ruler.png" />on the [sidebar menu](#use-the-visual-sidebar-menu). A corresponding sidebar appears. See [Rulers and Reference Lines](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/rulers) and [Use Reference Lines](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/rulers#use-reference-lines). | Both |
   | Modify visual information | Select <img src="https://mintcdn.com/insightsoftware/1fCfZrK84x8KmAw8/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/sidebar-info.png?fit=max&auto=format&n=1fCfZrK84x8KmAw8&q=85&s=e50f9664c34c2358b460dde018b9c41d" alt="" width="25" height="22" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '25px', height: '22px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/sidebar-info.png" /> or <img src="https://mintcdn.com/insightsoftware/1fCfZrK84x8KmAw8/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/widget-settings.png?fit=max&auto=format&n=1fCfZrK84x8KmAw8&q=85&s=710ead7b74f25358cef38f216eb75583" alt="" width="23" height="22" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '23px', height: '22px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/widget-settings.png" /> on the [sidebar menu](#use-the-visual-sidebar-menu). A corresponding sidebar appears. See [Modify Visual Names, Display Names, and Descriptions](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-save#modify-visual-names-display-names-and-descriptions). | Both |
   | Modify visual settings | Select <img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/sidebar-chtsettings.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=74af55ee44cca52b9f7f4ae157440a81" alt="Select the settings icon on the sidebar menu to open settings options" width="28" height="33" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '28px', height: '33px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/sidebar-chtsettings.png" />on the [sidebar menu](#use-the-visual-sidebar-menu). A corresponding sidebar appears. See [Change Visual Settings](#change-visual-settings). | Both |
   | Manage the visual time bar | Select <img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/dashboard-schedule.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=9e7a1179faaedda7e8026e3ccd40ddcd" alt="select the schedule report icon to schedule a dashboard or report with others" width="18" height="18" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '18px', height: '18px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/dashboard-schedule.png" /> on the [sidebar menu](#use-the-visual-sidebar-menu). A corresponding sidebar appears. See [Use the Time Bar](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/time-bar). | Both |
   | Sort or otherwise limit the visual | Select <img src="https://mintcdn.com/insightsoftware/1fCfZrK84x8KmAw8/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/sidebar-sort.png?fit=max&auto=format&n=1fCfZrK84x8KmAw8&q=85&s=4fc0c54db55344620adb5335ad462296" alt="" width="15" height="22" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '15px', height: '22px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/sidebar-sort.png" />on the [sidebar menu](#use-the-visual-sidebar-menu). See [Sort and Limit Visual Data](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/sortlimit-composer) | Both |
   | Apply new or saved filters to your visual | Select <img src="https://mintcdn.com/insightsoftware/cQU1Auv4yvPMjcip/simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/sidebar-filter.png?fit=max&auto=format&n=cQU1Auv4yvPMjcip&q=85&s=4b06f0c1f1b48c50da73f73672d5b1c6" alt="" width="19" height="20" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '19px', height: '20px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/sidebar-filter.png" /> to the left of the visual name or select <img src="https://mintcdn.com/insightsoftware/cQU1Auv4yvPMjcip/simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/sidebar-filter.png?fit=max&auto=format&n=cQU1Auv4yvPMjcip&q=85&s=4b06f0c1f1b48c50da73f73672d5b1c6" alt="" width="19" height="20" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '19px', height: '20px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/sidebar-filter.png" /> on the [sidebar menu](#use-the-visual-sidebar-menu) to display the Filters sidebar. Use the Filters sidebar to add and apply a new filter to your data or to select a saved filter to apply to your data. See [Filter Data](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/filters/filters). | Both |
   | Apply Conditional Formatting | Select <img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/cdntl-format-22-4.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=ac8100f01d82ac00cba95a8a2993c796" alt="" width="24" height="24" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '24px', height: '24px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/cdntl-format-22-4.png" /> on the [sidebar menu](#use-the-visual-sidebar-menu) to display the Conditional Formatting sidebar. Apply color and text formats based on conditional rules. See [Use the Conditional Formatting Sidebar](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/rdt-condt-format-using). | Both |
   | Adjust visual interactivity | Select <img src="https://mintcdn.com/insightsoftware/1fCfZrK84x8KmAw8/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/sidebar-interactive.png?fit=max&auto=format&n=1fCfZrK84x8KmAw8&q=85&s=5068072b72f71db3c65f6eed78658798" alt="select the interactivity icon to adjust the interactivity settings for this item" width="27" height="27" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '27px', height: '27px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/sidebar-interactive.png" /> on the [sidebar menu](#use-the-visual-sidebar-menu). See [Control How Users Interact With a Visual](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-interactivity). | Visual Gallery |
   | Create a keyset | Select <img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/more-menu.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=1471c7a569a7e100cd7fa4083b04551a" alt="Selet the three dots icon to open a show more menu or take actions for the named column" width="21" height="12" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '21px', height: '12px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/more-menu.png" /> and **Create Keyset** from the [visual drop-down menu](#use-the-visual-drop-down-menu). See [Create a Keyset](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/filters/keysets-overview#create-a-keyset). | Both |
   | Invoke an action | Select <img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/more-menu.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=1471c7a569a7e100cd7fa4083b04551a" alt="Selet the three dots icon to open a show more menu or take actions for the named column" width="21" height="12" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '21px', height: '12px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/more-menu.png" /> and **Actions** from the [visual drop-down menu](#use-the-visual-drop-down-menu). See [Invoke an Action](/simba-embedded-analytics/docs/self-service-analytics/26.3/embed-and-extend/actions-overview#invoke-an-action). | Both |
   | Export the visual | Select <img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/more-menu.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=1471c7a569a7e100cd7fa4083b04551a" alt="Selet the three dots icon to open a show more menu or take actions for the named column" width="21" height="12" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '21px', height: '12px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/more-menu.png" /> and **Export** from the [visual drop-down menu](#use-the-visual-drop-down-menu). See [Export Visuals](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-export-23). | Both |
   | Copy the visual | Select <img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/more-menu.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=1471c7a569a7e100cd7fa4083b04551a" alt="Selet the three dots icon to open a show more menu or take actions for the named column" width="21" height="12" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '21px', height: '12px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/more-menu.png" /> and **Copy Visual** from the [visual drop-down menu](#use-the-visual-drop-down-menu). See [Copy Visuals](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-add-dash#copy-visuals). | Dashboard |
   | Save the visual | Select <img src="https://mintcdn.com/insightsoftware/2cXq_sDOxrDVXUcv/simba-embedded-analytics/docs/self-service-analytics/26.3/images/dashboards/dash-save.png?fit=max&auto=format&n=2cXq_sDOxrDVXUcv&q=85&s=c373f07d0546e540baff9fcabe9866af" alt="select the save icon to save your changes" width="21" height="20" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '21px', height: '20px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/dashboards/dash-save.png" />. Changes are saved in the dashboard and in the Visual Gallery. | Dashboard |
   | Remove a visual from the dashboard | Select <img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/more-menu.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=1471c7a569a7e100cd7fa4083b04551a" alt="Selet the three dots icon to open a show more menu or take actions for the named column" width="21" height="12" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '21px', height: '12px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/more-menu.png" /> and **Remove Widget** from the [visual drop-down menu](#use-the-visual-drop-down-menu). See [Delete and Remove Visuals](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-save#delete-and-remove-visuals). | Dashboard |
   | Add or view widget comments | Select <img src="https://mintcdn.com/insightsoftware/1fCfZrK84x8KmAw8/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/widget-comments.png?fit=max&auto=format&n=1fCfZrK84x8KmAw8&q=85&s=82e6b86404260af6ee0ea3bcbf3296b2" alt="" width="20" height="20" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '20px', height: '20px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/widget-comments.png" /> from the [sidebar menu](#use-the-visual-sidebar-menu). See [Widget Comments](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/widgets/widget-cmts-ov). | Dashboard |

3. Optionally, edit the number or date and time format for this visual. See [Number and Date Formatting for Visuals](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/vis-number-formatting) and [Configure Date and Time Formatting](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/vis-number-formatting#configure-date-and-time-formatting).

4. Make your changes.

5. When you have finished making changes to your visual, be sure to save it. See [Configure Visual Names, Descriptions, and Properties](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-save).

<h2 id="use-the-visual-sidebar-menu">
  Use the Visual Sidebar Menu
</h2>

Self-Service Analytics's visual canvas provides a comprehensive suite of tools to help you tailor visuals quickly so they provide the information you need in the best way for you to analyze your data. These tools are available from the [visual menu](#use-the-visual-drop-down-menu) and from the visual sidebar menu. This topic discusses the visual sidebar menu.

The visual sidebar menu appears to the right of every visual edited from the Visual Gallery. With the exception of the visual interactivity option, it is also available when you select **Settings** on the [visual menu](#use-the-visual-drop-down-menu) when editing a visual in a dashboard.

Selecting options on the visual sidebar menu opens and closes sidebars that allow you to control:

* The type of a selected visual
* The settings used for a selected visual
* The configuration of pivot tables and tables of raw data
* The filters used for a selected visual
* Time bar settings for a visual
* Sort and limit options for a selected visual
* Ruler and reference line settings for a selected visual
* Colors for a selected visual
* Interactivity settings for a selected visual (only available in the Visual Gallery)
* General information for a selected visual
* View and manage comments, if applicable, for a visual or widget

### Visual Sidebar Menu

When you are editing a visual on a dashboard, you must first select a visual (a blue border appears around the selected visual) and then select **Settings** on the [visual drop-down menu](#use-the-visual-drop-down-menu). This makes the visual sidebar menu available.

If an option on the visual sidebar menu cannot be selected, the settings controlled by that sidebar are not available for the visual type you have selected.

The following visual sidebar menu options are available:

<table>
  <thead>
    <tr>
      <th>Menu Option</th>
      <th>Opens Sidebar</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        <img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/sidebar-chttype.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=559a7028c6be23336aa84a37bdb73f20" alt="" width="26" height="25" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '26px', height: '25px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/sidebar-chttype.png" />
      </td>

      <td>
        Opens or closes the Re-Visualize (was *Visual Style*) sidebar. Use this sidebar to change the visual type used for the selected visual (for example, to change a pie chart to a donut chart).

        <br />

        See [Use the Re-Visualize Sidebar](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/available-visual-types#use-the-re-visualize-sidebar).

        <br />

        This option is not available for [list filter visuals](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/list-filter-widget).
      </td>
    </tr>

    <tr>
      <td>
        <img src="https://mintcdn.com/insightsoftware/1fCfZrK84x8KmAw8/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/sidebar-sort.png?fit=max&auto=format&n=1fCfZrK84x8KmAw8&q=85&s=4fc0c54db55344620adb5335ad462296" alt="" width="15" height="22" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '15px', height: '22px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/sidebar-sort.png" />
      </td>

      <td>
        Opens or closes the Sort & Limit sidebar. Use this sidebar to sort and limit the data for the selected visual.

        <br />

        See [Sort and Limit Visual Data](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/sortlimit-composer).

        <br />

        This option is not available for [list filter visuals](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/list-filter-widget).
      </td>
    </tr>

    <tr>
      <td>
        <img src="https://mintcdn.com/insightsoftware/cQU1Auv4yvPMjcip/simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/sidebar-filter.png?fit=max&auto=format&n=cQU1Auv4yvPMjcip&q=85&s=4b06f0c1f1b48c50da73f73672d5b1c6" alt="" width="19" height="20" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '19px', height: '20px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/sidebar-filter.png" />
      </td>

      <td>
        Opens or closes the Filter sidebar. Use this sidebar to filter the data for the selected visual.

        <br />

        See [Apply Row-Level Filters](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/filters/filters#apply-row-level-filters), [Apply Wildcard Filters to a Visual, Filter Snippet, or Dashboard](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/filters/filters-attr#apply-wildcard-filters-to-a-visual-filter-snippet-or-dashboard), [Group Filters](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/filters/group-filters), [Create a Keyset From a CSV File](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/filters/keysets-overview#create-a-keyset-from-a-csv-file), and [Review and Apply a Keyset as a Visual Filter](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/filters/keysets-overview#review-and-apply-a-keyset-as-a-visual-filter).
      </td>
    </tr>

    <tr>
      <td>
        <img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/dashboard-schedule.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=9e7a1179faaedda7e8026e3ccd40ddcd" alt="select the schedule report icon to schedule a dashboard or report with others" width="18" height="18" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '18px', height: '18px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/dashboard-schedule.png" />
      </td>

      <td>
        Opens or closes the Time Bar sidebar. Use this sidebar to control the time bar for the selected visual.

        <br />

        See [Use the Time Bar Sidebar](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/time-bar#use-the-time-bar-sidebar).

        <br />

        This option is not available for [list filter visuals](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/list-filter-widget).
      </td>
    </tr>

    <tr>
      <td>
        <img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/sidebar-chtsettings.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=74af55ee44cca52b9f7f4ae157440a81" alt="Select the settings icon on the sidebar menu to open settings options" width="28" height="33" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '28px', height: '33px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/sidebar-chtsettings.png" />
      </td>

      <td>
        Opens or closes an appropriate Visual Settings sidebar. Use this sidebar to change settings for the selected visual. Different settings can be altered for different visual types. In addition, some visual types do not have any settings you can control in this way; this icon is disabled for these visual types.

        <br />

        See [Change Visual Settings](#change-visual-settings).
      </td>
    </tr>

    <tr>
      <td>
        <img src="https://mintcdn.com/insightsoftware/1fCfZrK84x8KmAw8/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/sidebar-ruler.png?fit=max&auto=format&n=1fCfZrK84x8KmAw8&q=85&s=cd5637e5e6fa36eb5d66445f626f44b4" alt="" width="22" height="26" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '22px', height: '26px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/sidebar-ruler.png" />
      </td>

      <td>
        Opens or closes the Ruler sidebar. Use this sidebar to control the rulers and reference lines on the selected visual. See [Rulers and Reference Lines](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/rulers) and [Use Reference Lines](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/rulers#use-reference-lines).

        <br />

        This option is not available for [list filter visuals](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/list-filter-widget).
      </td>
    </tr>

    <tr>
      <td>
        <img src="https://mintcdn.com/insightsoftware/1fCfZrK84x8KmAw8/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/sidebar-color.png?fit=max&auto=format&n=1fCfZrK84x8KmAw8&q=85&s=23086f978c60bc7f5eaff8f93de81ae3" alt="" width="28" height="28" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '28px', height: '28px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/sidebar-color.png" />
      </td>

      <td>
        Opens or closes the Color sidebar. Use this sidebar to change the color settings for the selected visual. Different color settings are available for different chart styles. See [Change Color Schemes](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/colors-and-axes/colors).

        <br />

        This option is not available for [list filter visuals](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/list-filter-widget).
      </td>
    </tr>

    <tr>
      <td>
        <img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/cdntl-format-22-4.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=ac8100f01d82ac00cba95a8a2993c796" alt="" width="24" height="24" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '24px', height: '24px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/cdntl-format-22-4.png" />
      </td>

      <td>
        Opens or closes the Conditional Formatting sidebar. Use this sidebar to define table formatting for specific data based on the attributes and conditions you set.

        <br />

        See [Use the Conditional Formatting Sidebar](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/rdt-condt-format-using).
      </td>
    </tr>

    <tr>
      <td>
        <img src="https://mintcdn.com/insightsoftware/1fCfZrK84x8KmAw8/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/sidebar-interactive.png?fit=max&auto=format&n=1fCfZrK84x8KmAw8&q=85&s=5068072b72f71db3c65f6eed78658798" alt="select the interactivity icon to adjust the interactivity settings for this item" width="27" height="27" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '27px', height: '27px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/sidebar-interactive.png" />
      </td>

      <td>
        Opens or closes the visual interactivity sidebar. Use this sidebar to control how users can interact with the selected visual. See [Control How Users Interact With a Visual](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-interactivity).

        <br />

        This option is only available for a visual when you are viewing it in the Visual Gallery.
      </td>
    </tr>

    <tr>
      <td>
        <img src="https://mintcdn.com/insightsoftware/1fCfZrK84x8KmAw8/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/sidebar-info.png?fit=max&auto=format&n=1fCfZrK84x8KmAw8&q=85&s=e50f9664c34c2358b460dde018b9c41d" alt="" width="25" height="22" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '25px', height: '22px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/sidebar-info.png" />
      </td>

      <td>
        Opens or closes the visual information sidebar. Use this sidebar to view basic information for the selected visual, and edit the Visual Description when opened in the Visual Gallery.

        <br />

        <Note>
          The Visual Description you can access here is not the same as the generated visual summary description you can generate and add to a rich text snippet in a dashboard. See [Describe Visual (Generate Visual Summary Description)](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/widgets/rts-ov#describe-visual-generate-visual-summary-description)
        </Note>
      </td>
    </tr>

    <tr>
      <td>
        <img src="https://mintcdn.com/insightsoftware/1fCfZrK84x8KmAw8/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/widget-settings.png?fit=max&auto=format&n=1fCfZrK84x8KmAw8&q=85&s=710ead7b74f25358cef38f216eb75583" alt="" width="23" height="22" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '23px', height: '22px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/widget-settings.png" />
      </td>

      <td>
        Opens or closes the widget settings sidebar. Use this sidebar to edit basic information and reposition a widget in a widget cell for the selected visual.

        <br />

        See [Modify Visual Names, Display Names, and Descriptions](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-save#modify-visual-names-display-names-and-descriptions) and [Position Resized Widgets](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/dashboards/dash-layout#position-resized-widgets) .
      </td>
    </tr>

    <tr>
      <td>
        <img src="https://mintcdn.com/insightsoftware/1fCfZrK84x8KmAw8/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/widget-comments.png?fit=max&auto=format&n=1fCfZrK84x8KmAw8&q=85&s=82e6b86404260af6ee0ea3bcbf3296b2" alt="" width="20" height="20" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '20px', height: '20px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/widget-comments.png" />
      </td>

      <td>
        Opens or closes the comments sidebar. View comments, or add and manage comments, depending on your dashboard access role. Use this sidebar to edit basic information for the selected visual.

        <br />

        See [Widget Comments](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/widgets/widget-cmts-ov).
      </td>
    </tr>
  </tbody>
</table>

<h2 id="use-the-visual-drop-down-menu">
  Use the Visual Drop-Down Menu
</h2>

Self-Service Analytics's visual canvas provides a comprehensive suite of tools to help you tailor visuals quickly and provide the information you need in the best way for you to analyze your data. These tools are available from the visual drop-down menu or from the [visual sidebar menu](#use-the-visual-sidebar-menu). This topic discusses the drop-down menu.

The visual drop-down menu lists options that help you modify and use your visuals more effectively. Access by selecting the Visual Menu, labeled as the Show more menu (<img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/more-menu.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=1471c7a569a7e100cd7fa4083b04551a" alt="Selet the three dots icon to open a show more menu or take actions for the named column" width="21" height="12" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '21px', height: '12px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/more-menu.png" />) icon in the upper right corner of a visual.

The menu options are described in the following table. Some options are only available for specific visual types. Some options are available when you are working with a visual in a dashboard and are not available when you are working with a visual in the Visual Gallery. Controls for some of these options are available on the interactivity sidebar. See [Control How Users Interact With a Visual](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-interactivity).

The list of options available on an embedded visual's drop-down menu depends on:

* The mode setting for the dashboard. If the embed mode is [`readonly` or](/simba-embedded-analytics/docs/self-service-analytics/26.3/embed-and-extend/embed/embed-javascript-embedmanager-methods#embedded-dashboard-properties-and-objects) [**Read Only**](/simba-embedded-analytics/docs/self-service-analytics/26.3/embed-and-extend/embed/dash-embed-gencode-dashboard), no menu is available at all.
* The [visual interactivity settings](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-interactivity) specified in the visual definition.
* The [dashboard interactivity settings](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/dashboards/dash-interactivity) specified for the dashboard, if those settings include override interactivity settings for all visuals in the dashboard.

When options are shown for a visual in an embedded dashboard, they may be shown in the [visual sidebar menu](#use-the-visual-sidebar-menu) or within the visual drop-down menu itself, depending on the setting of the [`editor.placement`](/simba-embedded-analytics/docs/self-service-analytics/26.3/embed-and-extend/embed/embed-javascript-embedmanager-methods#embedded-dashboard-properties-and-objects) property.

* If [`editor.placement`](/simba-embedded-analytics/docs/self-service-analytics/26.3/embed-and-extend/embed/embed-javascript-embedmanager-methods#embedded-dashboard-properties-and-objects) is set to `dockRight`, the options appear in sidebars using the [visual sidebar menu](#use-the-visual-sidebar-menu) and the resulting sidebar editing panels.

  If [`editor.placement`](/simba-embedded-analytics/docs/self-service-analytics/26.3/embed-and-extend/embed/embed-javascript-embedmanager-methods#embedded-dashboard-properties-and-objects) is set to `modals`, the options appear in the visual drop-down menu itself and the resulting floating dialogs.

<h3 id="visual-drop-down-menu">
  Visual Drop-Down Menu
</h3>

<table>
  <thead>
    <tr>
      <th>Option</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>Add to Visual Gallery</td>

      <td>
        Add a local visual to the Visual Gallery.

        <br />

        See [Convert Visual Gallery Visuals and Local Visuals](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-add-dash#convert-visual-gallery-visuals-and-local-visuals).
      </td>
    </tr>

    <tr>
      <td>Actions</td>

      <td>
        Invoke an action if an action template has been enabled for the visual's data source.

        <br />

        See [Invoke an Action](/simba-embedded-analytics/docs/self-service-analytics/26.3/embed-and-extend/actions-overview#invoke-an-action).
      </td>
    </tr>

    <tr>
      <td>Convert to Local</td>

      <td>
        Make a copy of a visual gallery visual as a local visual on the dashboard.

        <br />

        See [Convert Visual Gallery Visuals and Local Visuals](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-add-dash#convert-visual-gallery-visuals-and-local-visuals).
      </td>
    </tr>

    <tr>
      <td>Copy Visual</td>

      <td>
        Copy a visual.

        <br />

        See [Copy Visuals](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-add-dash#copy-visuals).
      </td>
    </tr>

    <tr>
      <td>Create Keyset</td>

      <td>
        Create a keyset from the visual data.

        <br />

        See [Create a Keyset](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/filters/keysets-overview#create-a-keyset).
      </td>
    </tr>

    <tr>
      <td>Create Alert</td>

      <td>
        Create an alert from the visual data for this dashboard.

        <br />

        See [Create an Alert Definition](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/alerts/alerts-ov#create-an-alert-definition).
      </td>
    </tr>

    <tr>
      <td>Describe Visual</td>

      <td>
        Generate a visual summary description of the visual for most visual types. This visual summary description is saved at the dashboard level when you insert it into a new or existing rich text snippet. If you make changes to the visual, the changes are reflected in the visual summary description.

        <br />

        * Select **Copy Visual Summary** to copy the visual summary description to your device's clipboard; paste it where you need.

        <br />

        * Select **Create Snippet and insert** to generate the visual summary description in a new [rich text snippet](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/widgets/rts-ov#describe-visual-generate-visual-summary-description), ready to edit.

        <br />

        * Select **Insert into \[Existing Snippet Name]** to generate the visual summary description and insert it into an existing rich text snippet.

        <br />

        <Note>
          If more than one rich text snippet widget exists, you can select the appropriate snippet from a list.
        </Note>
      </td>
    </tr>

    <tr>
      <td>Export</td>

      <td>
        Export a visual or visual data.

        <br />

        See [Export Visuals](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-export-23).
      </td>
    </tr>

    <tr>
      <td>Maximize</td>
      <td>Maximize a visual on the dashboard for optimal viewing.</td>
    </tr>

    <tr>
      <td>Minimize</td>
      <td>Minimize a visual so you can see other visuals on the dashboard.</td>
    </tr>

    <tr>
      <td>Permissions</td>

      <td>
        Quickly allows you to update the user, group, and account permissions for the visual. The Visual Permissions dialog appears. See [About Visual Permissions](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-auth).

        <br />

        You can only see this option if your user account has been granted the **Manage Visual Permissions** [privilege](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/aaa-ov#group-privilege-reference).
      </td>
    </tr>

    <tr>
      <td>Remove Widget</td>

      <td>
        Remove a visual from the dashboard. This will delete local visuals, but will not delete visual gallery visuals from Self-Service Analytics.

        <br />

        For more information, see [Delete and Remove Visuals](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-save#delete-and-remove-visuals).
      </td>
    </tr>

    <tr>
      <td>Save As</td>

      <td>
        Save the visual with a new name.

        <br />

        See [Save Visuals With New Names](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-save#save-visuals-with-new-names).
      </td>
    </tr>

    <tr>
      <td>Settings</td>

      <td>
        Opens the sidebar menu for a visual.

        <br />

        See [Use the Visual Sidebar Menu](#use-the-visual-sidebar-menu). Formerly Edit.
      </td>
    </tr>

    <tr>
      <td>Undo</td>

      <td>
        Undo a change you made to the visual.

        <br />

        See [Undo a Visual Action](#undo-a-visual-action).
      </td>
    </tr>
  </tbody>
</table>

<h2 id="change-visual-settings">
  Change Visual Settings
</h2>

You can change the settings for your visual using the Visual Settings sidebar. You can only change settings for some visual types.

**Access the Visual Settings sidebar**

1. Select the visual in the dashboard for which the settings will be changed.

2. Select the visual settings icon (<img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/sidebar-chtsettings.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=74af55ee44cca52b9f7f4ae157440a81" alt="Select the settings icon on the sidebar menu to open settings options" width="28" height="33" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '28px', height: '33px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/sidebar-chtsettings.png" />) on the [sidebar menu](#use-the-visual-sidebar-menu) for the visual. If there are no settings you can modify for a specific visual type, the visual settings icon is disabled.

   An appropriate visual settings sidebar appears. The one below is for a bar chart.

   <img src="https://mintcdn.com/insightsoftware/cQU1Auv4yvPMjcip/simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/sidebar-vissettingsbar.png?fit=max&auto=format&n=cQU1Auv4yvPMjcip&q=85&s=fbffdf7fddb7ae0e62667390c5b3d9de" alt="" width="351" height="646" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/sidebar-vissettingsbar.png" />

3. Adjust the settings as needed. See the description of the specific [visual type](/simba-embedded-analytics/docs/self-service-analytics/26.3/embed-and-extend/api/application-framework/getting-started-with-the-application-framework#self-service-analytics-visual-metrics-and-attributes-reference) for more information.

<h2 id="undo-a-visual-action">
  Undo a Visual Action
</h2>

The Undo option is available for visuals only. When you alter the query for a visual, the Undo option appears on the visual drop-down (<img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/more-menu.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=1471c7a569a7e100cd7fa4083b04551a" alt="Selet the three dots icon to open a show more menu or take actions for the named column" width="21" height="12" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '21px', height: '12px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/more-menu.png" />) menu and as an icon (<img src="https://mintcdn.com/insightsoftware/1fCfZrK84x8KmAw8/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/undo.png?fit=max&auto=format&n=1fCfZrK84x8KmAw8&q=85&s=0e89d1fa4020080a86cb4392cea3d9e8" alt="" width="15" height="15" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '15px', height: '15px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/undo.png" />) in the bottom left corner of the visual. Selecting **Undo** removes the most recent action you have taken for a visual and returns it to its previous state.

Undo is only available if you alter the visual query. This can include adding filters for a visual, changing its attributes, sorting its data, changing the visual type by re-visualizing the visual, changing the colors, and adjusting the time bar. The query is not altered if you export the visual, change its name or change its general information.
