> ## Documentation Index
> Fetch the complete documentation index at: https://insightsoftware.mintlify.site/llms.txt
> Use this file to discover all available pages before exploring further.

# Configure Visual Names, Descriptions, and Properties

## Visual Names and Display Names

Visual names are the unique name of a visual in the Visual Gallery; you assign the name when you create it, are names you assign to a visual when you create it or add it to the visual gallery from a dashboard. The visual name is used by Self-Service Analytics to track the visual throughout the environment and must be unique. Local visuals do not use visual names.

Display names are the unique name you assign to a visual in a dashboard when you create a local visual, or inherit when you add a visual gallery visual. This display name is shown in the header of the visual.

<Note>
  The field Default Title is now Display Name. Visual Names are no longer editable in the visual information sidebar when you open a specific visual in a dashboard. Edit the visual name when you open the visual in the Visual Gallery.
</Note>

* When you change a visual name, this change is reflected throughout the environment in the Visual Name field. See this change in the [visual information sidebar](#modify-visual-names-display-names-and-descriptions).
* When you change a display name, this change is reflected in the dashboard where the visual is included. If you convert a local visual to a visual gallery visual, the display name is inherited by the visual name field. View the visual name or display name in the [visual information sidebar](#modify-visual-names-display-names-and-descriptions).

The minimum length of visual names and display names is one character; the maximum length is 255 characters. Names can start with and contain numbers, special characters, and uppercase and lowercase characters. Names can contain spaces, but cannot start with a space. Names can not be empty, contain only spaces, or include leading or trailing spaces.

If a display or visual name is not unique, Self-Service Analytics generally saves your visual by adding a number in parentheses `(<n>)` at the end of the name to make it unique for that circumstance. If Self-Service Analytics returns an error, change the name manually and save it.

### Change the Visual Name for a Visual Gallery Visual

Change the Visual Name for a visual gallery visual in the Visual Gallery at any time. This does not affect the display name for visuals included in existing dashboards.

<img src="https://mintcdn.com/insightsoftware/cQU1Auv4yvPMjcip/simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/visual-name-example-23-2.png?fit=max&auto=format&n=cQU1Auv4yvPMjcip&q=85&s=aa3ce963453f39c5f581d5f8b2db7ad9" alt="change the visual name for a visual in the visual gallery" width="1104" height="618" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/visual-name-example-23-2.png" />

Visual names must be unique.

* If you try to save a visual in the Visual Gallery that has the same name as another visual, an error message appears and your visual is not saved. Rename the new visual to save it.
* If you try to add a visual to the Visual Gallery from a dashboard that has the same name as another visual, the visual is saved with an incremented number in parentheses `(<n>)` at the end of the name.

### Change the Display Name for a Visual

Change the Display Name for a visual in a dashboard at any time, using [visual information sidebar](#modify-visual-names-display-names-and-descriptions), or by editing the name in the header of the visual. This only affects this specific instance of the visual in this dashboard, and does not affect the Visual Name field for visual gallery visuals.

<img src="https://mintcdn.com/insightsoftware/b9ogX_L4Mqut_Uxb/simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/display-name-example-23-2.png?fit=max&auto=format&n=b9ogX_L4Mqut_Uxb&q=85&s=66674162db931b01c5a9d1a285c6ccf4" alt="edit the display name here" width="1105" height="618" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/display-name-example-23-2.png" />

The following table describes the behavior for specifying or changing a visual name or display name.

<table>
  <thead>
    <tr>
      <th>From the...</th>
      <th>Action</th>
      <th>Visual Name and Display Name Behavior</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td rowSpan={2}>Visual Gallery</td>
      <td>Create a visual</td>

      <td>
        When you create a visual using the [Visual Gallery](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-gallery), but do not assign a name, its visual name is **Untitled Visual**. The **Display Name** is also **Untitled Visual**.

        <br />

        * Change the visual name directly on the visual or on the [visual information sidebar](#modify-visual-names-display-names-and-descriptions).
        * The display name is inherited and cannot be changed here.
      </td>
    </tr>

    <tr>
      <td>Edit a visual</td>

      <td>
        When you edit a visual using the Visual Gallery:

        <br />

        * If you change the visual name, the visual name changes in the Visual Gallery and in the Visual Name field for every dashboard that includes the visual.
        * If you change the visual name, the Display Name for existing visual instances in dashboards remain unchanged, whether the Display Name is **Untitled Visual** or the same as the previous visual name.
        * New visual instances added to a dashboard after a visual name changes use the updated Visual Name as the Display Name when added to a dashboard, until you change the Display Name in the dashboard.
      </td>
    </tr>

    <tr>
      <td rowSpan={2}>Dashboard</td>
      <td>Create a visual</td>

      <td>
        When you create a new local visual while creating or updating a dashboard, its initial Display Name is the same as the name of the data source used for the visual.

        <br />

        * Edit the Display Name directly on the visual or using the [visual information sidebar](#modify-visual-names-display-names-and-descriptions).
        * There is no Visual Name for local visuals.
        * If you add a local visual to the visual gallery, define the Visual Name in the Save Options dialog.
      </td>
    </tr>

    <tr>
      <td>Edit a visual</td>

      <td>
        When you edit a visual in a dashboard and change the Display Name, the change only affects that instance of the visual. No other occurrences of the visual on other dashboards are affected.

        <br />

        You cannot change the Visual Name for visual gallery visuals using the dashboard. Edit the visual name in the [Visual Gallery](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-gallery). View the visual name on the [visual information sidebar.](#modify-visual-names-display-names-and-descriptions)
      </td>
    </tr>
  </tbody>
</table>

<h2 id="descriptions">
  Descriptions
</h2>

Descriptions give you an opportunity to provide more information about resources in your standalone or embedded environment for all or some of your users.

You can provide descriptions for most major objects that make up your environment:

* Sources: Add a Description when you create or update a source in your environment. This information is viewable and searchable from the Sources work area. See [Add or edit the Description for a source](#descriptions).
* Visuals: Add a Visual Description to shared visuals in the Visual Gallery. This information is viewable and searchable from the Visual Gallery work area. See [Add or edit the Visual Description for a visual](#descriptions).
* Dashboards: Add a Description to dashboards in your Library. This information is viewable and searchable from the Library work area. See [Add or edit the Description for a dashboard](#descriptions).
* Reports: Add a Description to reports in your Library. This information is viewable and searchable from the Library work area. See [Add or edit the Description for a report](#descriptions).
* Widgets: Add a Description to any widget on a dashboard: visuals, text snippets, or filter snippets. For shared visuals from the Visual Gallery, this does not replace the Visual Description. See [Add or edit the Description for a widget](#descriptions).

**Add or edit the Description for a source**

1. Create or edit a data source.

2. Edit the Description field in the Source Definition work area, then select **Save** to save your changes.

3. Open the Sources work area, then select the info icon (<img src="https://mintcdn.com/insightsoftware/1fCfZrK84x8KmAw8/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/sidebar-info.png?fit=max&auto=format&n=1fCfZrK84x8KmAw8&q=85&s=e50f9664c34c2358b460dde018b9c41d" alt="" width="25" height="22" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '25px', height: '22px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/sidebar-info.png" />) to view the description for this source.

   Optionally, use the **Search** field to search for a source by information in its description.

**Add or edit the Visual Description for a visual**

You can manually create

1. Create or edit a visual in the Visual Gallery.

2. Select the info icon (<img src="https://mintcdn.com/insightsoftware/1fCfZrK84x8KmAw8/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/sidebar-info.png?fit=max&auto=format&n=1fCfZrK84x8KmAw8&q=85&s=e50f9664c34c2358b460dde018b9c41d" alt="" width="25" height="22" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '25px', height: '22px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/sidebar-info.png" />) to open the info sidebar menu.

3. Edit the Visual Description field in the info work area, then select **Save** to save your changes.

4. Select the save icon (<img src="https://mintcdn.com/insightsoftware/2cXq_sDOxrDVXUcv/simba-embedded-analytics/docs/self-service-analytics/26.3/images/dashboards/dash-save.png?fit=max&auto=format&n=2cXq_sDOxrDVXUcv&q=85&s=c373f07d0546e540baff9fcabe9866af" alt="select the save icon to save your changes" width="21" height="20" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '21px', height: '20px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/dashboards/dash-save.png" />) to save the visual.

5. Open the Visual Gallery work area, then select the info icon (<img src="https://mintcdn.com/insightsoftware/1fCfZrK84x8KmAw8/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/sidebar-info.png?fit=max&auto=format&n=1fCfZrK84x8KmAw8&q=85&s=e50f9664c34c2358b460dde018b9c41d" alt="" width="25" height="22" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '25px', height: '22px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/sidebar-info.png" />) to view the visual description.

   Optionally, use the Search field to search for a visual by information in its visual description.

   <Note>
     Alternatively, you can add or edit the Visual Description when you save a visual, use Save As to rename a visual, and when you convert a local visual to a shared visual.
   </Note>

<Note>
  The Visual Description you can access here is not the same as the generated visual summary description you can generate and add to a rich text snippet in a dashboard. See [Describe Visual (Generate Visual Summary Description)](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/widgets/rts-ov#describe-visual-generate-visual-summary-description)
</Note>

**Add or edit the Description for a dashboard**

1. Create or edit a dashboard.

2. With the dashboard open, select Save or Save As to save the dashboard. The appropriate Save dialog opens.

3. Edit the Description field, then select **Save** to save your changes.

4. Open the Library, then select the info icon (<img src="https://mintcdn.com/insightsoftware/1fCfZrK84x8KmAw8/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/sidebar-info.png?fit=max&auto=format&n=1fCfZrK84x8KmAw8&q=85&s=e50f9664c34c2358b460dde018b9c41d" alt="" width="25" height="22" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '25px', height: '22px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/sidebar-info.png" />) to view the description for this dashboard.

   Optionally, use the **Search** field to search for a dashboard by the information in its description.

   <Note>
     Select the info icon (<img src="https://mintcdn.com/insightsoftware/1fCfZrK84x8KmAw8/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/sidebar-info.png?fit=max&auto=format&n=1fCfZrK84x8KmAw8&q=85&s=e50f9664c34c2358b460dde018b9c41d" alt="" width="25" height="22" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '25px', height: '22px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/sidebar-info.png" />) in the dashboard tool bar to show or hide the dashboard description for viewers.
   </Note>

**Add or edit the Description for a report**

1. Create or edit a report.

2. With the report open, select Save or Save As to save the report. The appropriate Save dialog opens.

3. Edit the Description field, then select **Save** to save your changes.

4. Open the Library, then select the info icon (<img src="https://mintcdn.com/insightsoftware/1fCfZrK84x8KmAw8/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/sidebar-info.png?fit=max&auto=format&n=1fCfZrK84x8KmAw8&q=85&s=e50f9664c34c2358b460dde018b9c41d" alt="" width="25" height="22" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '25px', height: '22px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/sidebar-info.png" />) to view the description for this report.

   Optionally, use the **Search** field to search for a report by the information in its description.

**Add or edit the Description for a widget**

1. Select a widget in your dashboard, then select Settings to open the sidebar menu. The menu opens to the Widget Settings panel.
2. Edit the Description field, then select **Apply** to apply your changes.
3. Select the save icon (<img src="https://mintcdn.com/insightsoftware/2cXq_sDOxrDVXUcv/simba-embedded-analytics/docs/self-service-analytics/26.3/images/dashboards/dash-save.png?fit=max&auto=format&n=2cXq_sDOxrDVXUcv&q=85&s=c373f07d0546e540baff9fcabe9866af" alt="select the save icon to save your changes" width="21" height="20" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '21px', height: '20px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/dashboards/dash-save.png" />) to save the dashboard.

<h2 id="modify-visual-names-display-names-and-descriptions">
  Modify Visual Names, Display Names, and Descriptions
</h2>

Update the information about your visuals in the Visual Gallery easily to organize and display extended information about these visuals. This includes:

* Visual Name - The name of the visual as saved in the visual gallery. View on the Info panel in the visual gallery.
* Visual Description - A short description of the visual. Searchable in the Visual Gallery. View on the Info panel in the visual gallery.
* Display Name - The name of the visual as displayed in dashboards. View and edit in the Widget Settings panel in a dashboard.
* Description - A short description of the widget. View and edit in the Widget Settings panel in a dashboard.

<Note>
  To modify Descriptions for other resources in your environment, see [Descriptions](#descriptions).
</Note>

<Note>
  The Visual Description you can access here is not the same as the generated visual summary description you can generate and add to a rich text snippet in a dashboard. See [Describe Visual (Generate Visual Summary Description)](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/widgets/rts-ov#describe-visual-generate-visual-summary-description)
</Note>

This information is included and used in your dashboards, but can be edited as needed.

**Edit the Visual Name and Visual Description in Visual Gallery**

1. Select the visual to edit in the Visual Gallery.

2. Select the info option (<img src="https://mintcdn.com/insightsoftware/1fCfZrK84x8KmAw8/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/sidebar-info.png?fit=max&auto=format&n=1fCfZrK84x8KmAw8&q=85&s=e50f9664c34c2358b460dde018b9c41d" alt="" width="25" height="22" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '25px', height: '22px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/sidebar-info.png" />) on the [sidebar menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup#use-the-visual-sidebar-menu) for the visual. The Info sidebar opens.

   <img src="https://mintcdn.com/insightsoftware/cQU1Auv4yvPMjcip/simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/sidebar-visinfo-visgallery-23-2.png?fit=max&auto=format&n=cQU1Auv4yvPMjcip&q=85&s=d81377e4e839c4b026e87b9c7f3720fb" alt="update a visual name and visual description here" width="350" height="495" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/sidebar-visinfo-visgallery-23-2.png" />

   The data source and visual type are shown here, but can not be changed here.

3. Change the visual name in the **Visual Name** field. You can also change the name of a visual by selecting the name in the visual itself. See Configure Visual Names, Descriptions, and Properties.

4. Optionally, add a visual description, or edit an existing one in the **Visual Description** field, up to 750 characters. You can search for the visual using this information in the Visual Gallery.

5. Select **Save** to save your changes in the sidebar menu, then the Save icon (<img src="https://mintcdn.com/insightsoftware/2cXq_sDOxrDVXUcv/simba-embedded-analytics/docs/self-service-analytics/26.3/images/dashboards/dash-save.png?fit=max&auto=format&n=2cXq_sDOxrDVXUcv&q=85&s=c373f07d0546e540baff9fcabe9866af" alt="select the save icon to save your changes" width="21" height="20" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '21px', height: '20px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/dashboards/dash-save.png" />) for the visual to save all of your changes.

**Edit the Display Name and Description in a dashboard**

1. Select a local visual or a shared visual on a dashboard.

2. Select **Settings** on the [visual drop-down menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup#use-the-visual-drop-down-menu) to access the [sidebar menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup#use-the-visual-sidebar-menu) for the visual.

3. Select widget settings (<img src="https://mintcdn.com/insightsoftware/1fCfZrK84x8KmAw8/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/widget-settings.png?fit=max&auto=format&n=1fCfZrK84x8KmAw8&q=85&s=710ead7b74f25358cef38f216eb75583" alt="" width="23" height="22" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '23px', height: '22px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/widget-settings.png" />). The Widget Settings sidebar opens. Edit Widget Settings or Position settings as needed.

   <img src="https://mintcdn.com/insightsoftware/cQU1Auv4yvPMjcip/simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/sidebar-widget-settings-dashboard-23-2.png?fit=max&auto=format&n=cQU1Auv4yvPMjcip&q=85&s=a99995917a69b112405a74eee320961d" alt="update the display name and description here; show or hide the header, pickers, and position a resized widget within a cell" width="351" height="510" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/sidebar-widget-settings-dashboard-23-2.png" />

   <Note>
     Change the display name in the **Display Name** field. You can also change the display name by selecting the title in the dashboard. See Configure Visual Names, Descriptions, and Properties.
   </Note>

4. Change the description in the **Description** field, up to 750 characters. There is no description by default.

5. Select a header behavior. The default setting is **Show**; this displays the header at all times.

   * **Show** (default) displays the header at all times.
   * **Show on Hover** hides the header in [Viewer mode](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/dashboards/dash-layout#use-dashboard-view-mode) unless users perform a hover action over the widget where the header is temporarily hidden.
   * **Hide** completely hides the header in [Viewer mode](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/dashboards/dash-layout#use-dashboard-view-mode).

6. Customize the picker behavior, if applicable. The default setting is **Show**; this displays the picker at all times.

   * **Show** (default) displays the picker at all times.
   * **Hide** completely hides the header in [Viewer mode](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/dashboards/dash-layout#use-dashboard-view-mode).
   * **Custom** allows you to show or hide attributes such as colors, axis labels, and other available attributes or metrics. When disabled, an attribute or metric is hidden in [Viewer mode](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/dashboards/dash-layout#use-dashboard-view-mode).

7. Adjust the **Position** of the content in the widget, if applicable. See [Position Resized Widgets](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/dashboards/dash-layout#position-resized-widgets) .

8. Select the **Save** button to save the changes you made in the sidebar menu for the instance of this visual, then the **Save** icon (<img src="https://mintcdn.com/insightsoftware/2cXq_sDOxrDVXUcv/simba-embedded-analytics/docs/self-service-analytics/26.3/images/dashboards/dash-save.png?fit=max&auto=format&n=2cXq_sDOxrDVXUcv&q=85&s=c373f07d0546e540baff9fcabe9866af" alt="select the save icon to save your changes" width="21" height="20" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '21px', height: '20px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/dashboards/dash-save.png" />) for the dashboard to save your changes.

## Save Visuals With Their Current Names

When you have finished making changes to a visual on a dashboard, you can save it with its original name. Changes you have made to the visual will appear on all dashboards that use the visual.

<Note>
  If you are editing the visual in a dashboard, you can save the visual with its current name when you save the dashboard. However, the default is not to save them when you save the dashboard. You must explicitly elect to save them on the dashboard Save Options dialog. See [Save a Dashboard](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/dashboards/dash-manage#save-a-dashboard).
</Note>

<Note>
  To save visuals, you must be logged in a user with [write permissions](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-auth) for the visual or with the **Administer Visuals** [group privilege](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/aaa-ov#group-privilege-reference).
</Note>

**Save a visual with its current name**

1. Select the visual on a dashboard or in the Visual Gallery. When selected on a dashboard, a blue border appears around the visual. If you select a visual with a streaming data source, the [time bar](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/time-bar) (Data DVR) appears.

2. Select save (<img src="https://mintcdn.com/insightsoftware/2cXq_sDOxrDVXUcv/simba-embedded-analytics/docs/self-service-analytics/26.3/images/dashboards/dash-save.png?fit=max&auto=format&n=2cXq_sDOxrDVXUcv&q=85&s=c373f07d0546e540baff9fcabe9866af" alt="select the save icon to save your changes" width="21" height="20" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '21px', height: '20px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/dashboards/dash-save.png" />) in the upper right corner of the visual.

   * If you are editing the visual in the Visual Gallery, the Save Options dialog appears.

     <img src="https://mintcdn.com/insightsoftware/cQU1Auv4yvPMjcip/simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/vis-save-options-dialog-82.png?fit=max&auto=format&n=cQU1Auv4yvPMjcip&q=85&s=23db1e0385b0679125b7461c889ca57a" alt="" width="500" height="175" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/vis-save-options-dialog-82.png" />

     Optionally, specify a new visual name in the **Visual Name** box and select **Save**. The visual is saved.

   * If you are editing the visual in a dashboard, a warning appears indicating that the visual changes will occur for all dashboards that use the visual.

     <img src="https://mintcdn.com/insightsoftware/cQU1Auv4yvPMjcip/simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/save-warn.png?fit=max&auto=format&n=cQU1Auv4yvPMjcip&q=85&s=ae344e8a459bad13028042a7726e6aa8" alt="save visual warning - affect all dashboards" width="398" height="145" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/save-warn.png" />

     Select **OK** on the warning dialog. The visual is saved.

<h2 id="save-visuals-with-new-names">
  Save Visuals With New Names
</h2>

All visuals have a visual name and display name. When you use the Save As option for a shared visual gallery visual, you affect the visual name. Self-Service Analytics makes a copy of the visual in the visual gallery. The original visual is replaced with the newly named visual if you save a visual with a new name while editing a dashboard.

<Note>
  To change the display name of a visual, see Configure Visual Names, Descriptions, and Properties.
</Note>

<table>
  <thead>
    <tr>
      <th>Action</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>Save As in the Visual Gallery</td>

      <td>
        Open a visual in the visual gallery, select Save As, provide a new name, and Save your changes.

        <br />

        * If there are no changes in the visual from a previous save, Self-Service Analytics adds a copy of the visual with the new name to the visual gallery.
        * If there are unsaved changes in the visual after a previous save, Self-Service Analytics adds a copy of the visual with the new name and the changes to the visual gallery.

        <br />

        <Note>
          You can also add a searchable **Visual Description** for this visual.
        </Note>
      </td>
    </tr>

    <tr>
      <td>Save As in a dashboard</td>
      <td>Select a visual in the dashboard, select Save As from the [visual drop-down menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup#use-the-visual-drop-down-menu), provide a new name, and Save your changes. Self-Service Analytics adds a copy of the visual with the new name to the visual gallery. The visual in the dashboard is replaced by the new visual.</td>
    </tr>
  </tbody>
</table>

<Note>
  You can create a local visual by selecting the **Copy** option for a shared visual using [visual drop-down menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup#use-the-visual-drop-down-menu). See [Copy Visuals](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-add-dash#copy-visuals).
</Note>

<Note>
  To save visuals with a new visual name in the Visual Gallery, you must be logged in as an administrator or as a user with the **Create Visuals** or **Administer Visuals** [group privilege](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/aaa-ov#group-privilege-reference).
</Note>

**Save a visual with a new name in the visual gallery**

1. Select the visual in the Visual Gallery.

2. Select **Save As** in the (<img src="https://mintcdn.com/insightsoftware/GTXU--ZlYc3DodOR/simba-embedded-analytics/docs/self-service-analytics/26.3/images/dashboards/save-as.png?fit=max&auto=format&n=GTXU--ZlYc3DodOR&q=85&s=d812e74df4f8c2d8e318d41bc16f3d34" alt="select to save the item as a copy with a new name and your changes" width="25" height="27" noZoom data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/dashboards/save-as.png" />) in upper right corner of the visual.

   <img src="https://mintcdn.com/insightsoftware/cQU1Auv4yvPMjcip/simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/vis-save-as-options-dialog-82-23-2.png?fit=max&auto=format&n=cQU1Auv4yvPMjcip&q=85&s=13c47e938d9768d06e1d20f7f3a03833" alt="" width="498" height="251" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/vis-save-as-options-dialog-82-23-2.png" />

3. Specify a new visual name in the **Visual Name** box and select **Save**. Self-Service Analytics adds a copy of the visual with the new name to the visual gallery.

   The original visual still exists with its original visual name in the system.

**Save a visual with a new name while editing a dashboard**

1. Select a visual in the dashboard.

2. Select **Save As** from the [visual drop-down menu.](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup#use-the-visual-drop-down-menu)

3. <img src="https://mintcdn.com/insightsoftware/cQU1Auv4yvPMjcip/simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/vis-save-as-options-dialog-82-23-2.png?fit=max&auto=format&n=cQU1Auv4yvPMjcip&q=85&s=13c47e938d9768d06e1d20f7f3a03833" alt="" width="498" height="251" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/vis-save-as-options-dialog-82-23-2.png" />

4. Specify a new visual name in the **Visual Name** field, optionally add or edit the **Visual Description**, and select **Save**. Self-Service Analytics adds a copy of the visual with the new name to the visual gallery.

   The visual in the dashboard is replaced by the new visual.

<h2 id="delete-and-remove-visuals">
  Delete and Remove Visuals
</h2>

You can remove visuals from dashboards and delete them from the Self-Service Analytics instance in the Visual Gallery. You cannot delete a visual if it is used by any dashboard.

<Note>
  If you try to delete a visual, filter snippet, dashboard, self service report, dashboard link, source, or source field, Self-Service Analytics displays an error message naming any objects dependent on the item you’re trying to delete. You can delete the item after you’ve removed the association from the dependent object. See [Fields Usage](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/data-source-config-fields-tab#fields-usage).
</Note>

### Remove a Visual From a Dashboard

**Remove a visual from your dashboard**

1. Edit the dashboard. See [Edit a Dashboard](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/dashboards/dash-manage#edit-a-dashboard).

2. Select the visual to be removed.

3. Select **Remove Widget** on the [visual drop-down (<img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/more-menu.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=1471c7a569a7e100cd7fa4083b04551a" alt="Selet the three dots icon to open a show more menu or take actions for the named column" width="21" height="12" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '21px', height: '12px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/more-menu.png" />) menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup#use-the-visual-drop-down-menu). A removal confirmation dialog opens.

   To control whether a visual can be removed, use the interactivity sidebar. See [Control How Users Interact With a Visual](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-interactivity).

4. Select **Delete** on the warning dialog to confirm the removal.

   <Note>
     [Local visuals](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-add-dash#add-local-visuals-to-a-dashboard) are deleted completely. Visual gallery visuals remain in the visual gallery.
   </Note>

### Delete a Visual from the Visual Gallery

A visual can only be deleted from the [Visual Gallery](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-gallery) when it is not used in any dashboard. If the **Usage** column for a visual in the Visual Gallery shows any number except zero, the option to delete the visual is disabled.

To delete visuals, you must be logged in as an administrator or as a user belonging to a group with the [privilege **Administer Visuals**](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/aaa-ov#group-privilege-reference) enabled.

**Delete a visual from the Visual Gallery**

1. Access the [Visual Gallery](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-gallery). See [Use the Visual Gallery](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-gallery).
2. Locate the visual in the Visual Gallery.
3. Select the delete icon (<img src="https://mintcdn.com/insightsoftware/1fCfZrK84x8KmAw8/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/trashcan.png?fit=max&auto=format&n=1fCfZrK84x8KmAw8&q=85&s=2f005e6454f4553621ce9f5926d15d6a" alt="" width="17" height="19" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '17px', height: '19px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/trashcan.png" />) in the **Actions** column associated with the visual. A pop-up dialog is shown, verifying the deletion.
4. Select **Delete** on the warning dialog to confirm the deletion.
