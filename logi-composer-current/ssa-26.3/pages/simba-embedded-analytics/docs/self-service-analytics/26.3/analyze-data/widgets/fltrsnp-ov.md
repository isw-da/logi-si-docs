> ## Documentation Index
> Fetch the complete documentation index at: https://insightsoftware.mintlify.site/llms.txt
> Use this file to discover all available pages before exploring further.

# Filter Snippets

Add filter snippets to your dashboards to filter data for multiple visuals quickly and easily. Filter your data using input from one or more resources: values from sources used in your dashboard, or a [custom value](#custom-values-for-filter-snippets) to further refine visual data. Adjust and save filter selections using Attribute, Number, Time, or Hierarchy data types and highlight data across multiple visuals. Link multiple filter snippets to more flexibly filter your visuals.

Update your dashboards with filter snippets any time using the Self-Service Analytics UI or the dashboard API. Each filter snippet resides in its own widget; resize and adjust placement of snippets to complement your visuals.

<Note>
  When you create a filter snippet, it is linked to the dashboard you have added it to. If you delete a dashboard, the snippet is deleted as well.
</Note>

For more information on creating and managing filter snippets, see the following topics:

* [Add Filter Snippets to a Dashboard](#add-filter-snippets-to-a-dashboard)
* [Connect Visuals to a Filter Snippet](#connect-visuals-to-a-filter-snippet)
* [Link Filter Snippets](#link-filter-snippets)
* [Custom Values for Filter Snippets](#custom-values-for-filter-snippets)
* [Use the Filter Snippet Menu](#use-the-filter-snippet-menu)
* [Use The Filter Snippet Sidebar Menu](#use-the-filter-snippet-sidebar-menu)
* [Edit or Delete Filter Snippets](#edit-or-delete-filter-snippets)

<h2 id="add-filter-snippets-to-a-dashboard">
  Add Filter Snippets to a Dashboard
</h2>

When you create a dashboard or edit an existing dashboard, add filter snippets to allow your users to view and highlight data pulled from one or more sources in multiple visuals. Filter by three data types: Attribute, Number, or Time. Link multiple filter snippets to provide secondary and tertiary filtering on your visual data.

<Note>
  When you create a filter snippet, it is linked to the dashboard you have added it to. If you delete a dashboard, the snippet is deleted as well.
</Note>

### Create a New Filter Snippet

1. [Create](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/dashboards/dash-manage#create-dashboards) or [edit](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/dashboards/dash-manage#edit-a-dashboard) a dashboard that includes one or more visuals.

   * To add a snippet to an existing dashboard, log in as a user with `READ` and `WRITE` permissions for the dashboard.
   * If you are creating a new dashboard, log in as a user with the **Create Dashboards** or **Administer Dashboards** [group privilege](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/aaa-ov#group-privilege-reference).

2. Select the Add Filter Snippet icon <img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/add-filter-snippet.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=499601ef1705bb1d3ad3838d4b141b1a" alt="select the add filter snippet icon to add a filter snippet to a dashboard" width="24" height="22" noZoom data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/add-filter-snippet.png" /> in the [dashboard icon bar](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/dashboards/dash-layout#use-the-dashboard-icons). A new filter snippet is added in a widget on the dashboard, ready to edit.

3. Select the Settings icon <img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/gear-joins-710.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=1e5db9bf2b3879817708388c123fdc28" alt="" width="17" height="16" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '17px', height: '16px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/gear-joins-710.png" /> from the Show More menu <img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/more-menu.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=1471c7a569a7e100cd7fa4083b04551a" alt="Selet the three dots icon to open a show more menu or take actions for the named column" width="21" height="12" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '21px', height: '12px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/more-menu.png" /> to open the filter snippet sidebar menu. See [Use The Filter Snippet Sidebar Menu](#use-the-filter-snippet-sidebar-menu).

4. Define the **Data Settings** for this filter snippet by selecting a **Data Type** of [Attribute](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/filters/filters-attr), [Number](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/filters/filters-attr#set-a-numeric-field-filter), [Time](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/filters/filters-attr#set-a-time-field-filter), or [Hierarchy](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/filters/filters-attr#filter-by-hierarchy-field).

5. Select an **Operator** for your Data Type. Available operators are dependent on the data type selected.

6. Select an available **Source**. Any visuals in this dashboard that use this source can be affected by this filter snippet.

7. Select an available **Value Column**. After you have made this selection, other options may be available that allow you to define how the data is presented. After making these choices, select **Apply**.

8. Optionally, select the [Filters sidebar menu](#filters) to add more filters to the snippet that utilize the same or different sources.

9. Select **Connect Widgets** from the Show More menu <img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/more-menu.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=1471c7a569a7e100cd7fa4083b04551a" alt="Selet the three dots icon to open a show more menu or take actions for the named column" width="21" height="12" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '21px', height: '12px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/more-menu.png" /> to add visuals or to link existing filter snippets you want filtered to this filter snippet. The Connect Widgets work area opens.

10. Select **Add Widget**. Select a **Widget Name** and an available **Field**. Repeat to add as many widgets as desired.

    * Select the remove icon <img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/delete-black-open.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=2dd520b27e17cb3afb7d849272854051" alt="" width="18" height="21" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '18px', height: '21px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/delete-black-open.png" /> to remove a widget from the filter.
    * Select the connect icon to connect all widgets present in the dashboard for the data source.

11. Select **Apply** to use the selected widgets to this filter snippet. If you have added all available widgets, the work area closes and links the widgets automatically.

12. [Save](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-save) the dashboard.

<h2 id="use-the-filter-snippet-sidebar-menu">
  Use The Filter Snippet Sidebar Menu
</h2>

Use the filter snippet sidebar menu to:

* Define data settings for the filter snippet
* Define filter snippet settings
* Apply filters and hierarchical filters (if available) to the filter snippet
* Adjust widget settings for the filter snippet
* Manage comments for the filter snippet

To access the filter snippet sidebar menu, select **Settings** from the show more menu <img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/more-menu.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=1471c7a569a7e100cd7fa4083b04551a" alt="Selet the three dots icon to open a show more menu or take actions for the named column" width="21" height="12" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '21px', height: '12px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/more-menu.png" />. The filter snippet sidebar opens.

### Filter Snippet Sidebar Menus

<img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/filtersnippets/sb-menu-data-settings-24-1.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=3431b4834c747e9e208b5fac58a84254" alt="Use this work area to define filter snippet data settings" width="393" height="639" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/filtersnippets/sb-menu-data-settings-24-1.png" />

<img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/filtersnippets/sb-menu-ftl-snp-setting-24-1.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=64e869db8e7dff36fb9cd9382e0f5872" alt="Use this work area to define filter snippet options" width="393" height="639" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/filtersnippets/sb-menu-ftl-snp-setting-24-1.png" />

<img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/filtersnippets/sb-menu-filter-24-1.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=af07bbb2c17dccaa344b08c8cfb7cd5c" alt="Use this work area to define filters to apply to this filter snippet" width="393" height="639" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/filtersnippets/sb-menu-filter-24-1.png" />

<img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/filtersnippets/sb-menu-widget-setgs-24-1.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=b6ad3cdc15c131936bf026cd83244726" alt="Use this work area to define widget settings" width="393" height="638" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/filtersnippets/sb-menu-widget-setgs-24-1.png" />

<img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/filtersnippets/sb-menu-widget-cmt-24-1.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=6f06e9b7142efb1773c3a7c2e0a2c96e" alt="Use this work area to view and manage comments" width="393" height="639" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/filtersnippets/sb-menu-widget-cmt-24-1.png" />

If this is a new filter snippet, default settings are shown. If this is an existing filter snippet, current settings are shown.

<Note>
  If you are editing a filter snippet that references unavailable sources or fields, an **Unavailable** message is shown in the affected drop-down. Select a new source or fields as needed.
</Note>

<h4 id="data-settings">
  Data Settings
</h4>

Adjust the data settings for this filter snippet, then select **Apply** as needed to apply your changes to the filter snippet.

<table>
  <thead>
    <tr>
      <th>Setting</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>Data Type</td>
      <td>Select a data type to filter: **Attribute**, **Time**, **Number** or **Hierarchy**. If you select Time, you can set conditions for the time spans **Between** or **Not Between** in the widget itself if the display style is **Range**.</td>
    </tr>

    <tr>
      <td>Operator</td>

      <td>
        Select an operator to use:

        <br />

        * **Attribute**: Select **Include** or **Exclude** to include or exclude a value from the data. Select **Contains** to return only data that contains a specified value. Select **Does Not Contain** to return only data that does not return a specified value.
        * **Number**: Select **Include** or **Exclude** to include or exclude a value from the data. Select **Contains** to return only data that contains a specified value.
        * **Time**: Select **Between** or **Not Between**, then define the conditions for time spans in the widget itself.
        * **Hierarchy**: Select **Equals or Descendants Of** or **Includes**, then select a value column.
      </td>
    </tr>

    <tr>
      <td>Source</td>
      <td>Select an available source to use. After you select a source, you can select an available field from that source to use as a Value Column for the filter, and a different Display Column if needed.</td>
    </tr>

    <tr>
      <td>Value Column</td>

      <td>
        Select an available field for the Value Column. Your users can filter the data in attached widgets using these values. If you prefer to use a different column as a Display Column, disable **Use Value Column as Display Column**.

        <br />

        <Note>
          If you have Filtered a field to prevent users from seeing or exporting this data, you must disable Use Value Column as Display Column to select the column, then select a Display Column. See [Filter Data With Masked Fields](#filter-data-with-masked-fields).
        </Note>
      </td>
    </tr>

    <tr>
      <td>Display Column</td>

      <td>
        Select a different field than the Value Column to use as a display column for your users. Only visible when you disable **Use Value Column as Display Column**.

        <br />

        <Note>
          If you have Filtered a field to prevent users from seeing or exporting this data, you must disable Use Value Column as Display Column to select the column, then select a Display Column. See [Filter Data With Masked Fields](#filter-data-with-masked-fields).
        </Note>
      </td>
    </tr>

    <tr>
      <td>Granularity</td>
      <td>Available for **Time** data types. Select an available option based on the granularity of the data provided.</td>
    </tr>

    <tr>
      <td>Sort</td>

      <td>
        Select an order to sort the filter values by. Available options depend on the selected data type. The column data used to sort is listed below the Sort heading.

        <br />

        * **Attribute**, **Number**, **Hierarchy**: Options include **Alphabetical (A - Z)** and **Reverse Alphabetical (Z - A)**
        * **Time**: Options include **Chronological** and **Reverse Chronological**.
      </td>
    </tr>
  </tbody>
</table>

#### Filter Snippet Settings

Adjust the filter snippet settings in this work area. Save the dashboard to save your changes.

<table>
  <thead>
    <tr>
      <th>Setting</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>Display Style</td>

      <td>
        Select **Fixed List** to display all available selection items in a selection list.

        <br />

        * If you select **Fixed List** along with Single Number of Selections, users see a list of items and can select one.
        * If you select **Fixed List** along with Multiple Number of Selections, users see a list of items and can select multiple.

        <br />

        Select **Dropdown List** to display all available selection items in a drop-down list.

        <br />

        * If you select **Dropdown List** along with Single Number of Selections, users can filter or scroll through a list of items and can select one.
        * If you select **Dropdown List** along with Multiple Number of Selections, users can filter, select, and scroll through a list of items and can select multiple values.

        <br />

        Enable or disable the **Hide "Add" Button** toggle to control if users can add their own items.
      </td>
    </tr>

    <tr>
      <td>Number of Selections</td>

      <td>
        Specify whether only one or multiple data values can be selected in the filter snippet. Select **Single** to allow users to select only one data value; select **Multiple** to allow users to select more than one value.

        <br />

        * If you select **Fixed List** along with **Single**, users see a list of items and can select one value.
        * If you select **Dropdown List** along with **Single**, users can filter or scroll through a list of items and can select one value.
        * If you select **Fixed List** along with **Multiple**, users see a list of items and can select multiple values.
        * If you select **Dropdown List** along with **Multiple**, users can filter, select, and scroll through a list of items and can select multiple values.
      </td>
    </tr>

    <tr>
      <td>"No Selection" Label</td>

      <td>
        Visible when the **Single** option for **Number of Selections** is selected.

        <br />

        Enter text to display when no values have been selected. Default text is **None**.
      </td>
    </tr>

    <tr>
      <td>Placeholder Text</td>

      <td>
        Visible when both the **Dropdown List** and **Multiple** options are selected.

        <br />

        Enter text to display in the Search field when no values have been selected. Default text is **Search**.
      </td>
    </tr>

    <tr>
      <td>Filter Values On</td>

      <td>
        Visible when the **Multiple** option for **Number of Selections** is selected.

        <br />

        * Select **Change** to apply the filter snippet to connected visuals as selections are made.
        * Select **Submit** to apply the filter snippet to connected visuals when a user selects **Submit**.
      </td>
    </tr>

    <tr>
      <td>Submit Button Text</td>

      <td>
        Visible when the **Submit** option for **Filter Values On** is selected.

        <br />

        Enter text to display for users to apply the filter snippet to connected visuals. Default text is **Submit**.
      </td>
    </tr>
  </tbody>
</table>

<h4 id="filters">
  Filters
</h4>

Apply or create filters in this work area. Save the dashboard to save your changes.

| Setting | Description |
| - | - |
| Add Filter | Select to add a [row level filter](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/filters/filters#apply-row-level-filters), [group filter](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/filters/group-filters), [hierarchical filter](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/filters/filters-attr#filter-by-hierarchy-field), or [saved filter](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/filters/saved-filters-maintaining#apply-a-saved-filter-to-a-visual-filter-snippet-or-dashboard) to this filter snippet. |
| Save Filters | After you have created one or more filters, select [Save Filters](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/filters/saved-filters-maintaining#create-a-saved-filter) to save and reuse in your environment. |

#### Widget Settings

Adjust the widget settings for this filter snippet, then select **Apply** as needed to apply your changes to the filter snippet. Save the dashboard to save your changes.

<table>
  <thead>
    <tr>
      <th>Setting</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>Display Name</td>
      <td>The display name for this filter snippet. Change here or edit directly in the widget.</td>
    </tr>

    <tr>
      <td>Description</td>
      <td>An optional description for this filter snippet. Blank by default. Maximum 750 characters.</td>
    </tr>

    <tr>
      <td>Header</td>

      <td>
        Adjust the header behavior. The default setting is

        <br />

        * **Show**: display the header at all times. Default setting.
        * **Show on Hover**: hide the header in Viewer mode unless users perform a hover action over the widget.
        * **Hide**: completely hide the header from visibility in Viewer mode.
      </td>
    </tr>

    <tr>
      <td>Position</td>
      <td>Adjust the position of the widget content in the cell (widget footprint in the dashboard) to align vertically and horizontally as appropriate within the space. Select center, top, or bottom as needed.</td>
    </tr>
  </tbody>
</table>

#### Comments

If you have access to comments, manage them on this tab. See [Widget Comments](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/widgets/widget-cmts-ov).

<h2 id="use-the-filter-snippet-menu">
  Use the Filter Snippet Menu
</h2>

The filter snippet menu includes options that help you modify and use these snippets in your dashboard. Access it by selecting<img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/more-menu.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=1471c7a569a7e100cd7fa4083b04551a" alt="Selet the three dots icon to open a show more menu or take actions for the named column" width="21" height="12" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '21px', height: '12px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/more-menu.png" /> in the upper right corner of a snippet widget.

The menu options are described in the following table.

<table>
  <thead>
    <tr>
      <th>Option</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>Edit</td>

      <td>
        Select to edit the [custom values](#custom-values-for-filter-snippets) of a filter snippet by removing them, or if it is open for editing, put it in view mode. Select <img src="https://mintcdn.com/insightsoftware/1fCfZrK84x8KmAw8/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/trashcan-black.png?fit=max&auto=format&n=1fCfZrK84x8KmAw8&q=85&s=136b6c4981ae0ce343d31bfd990f10e8" alt="" width="17" height="20" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '17px', height: '20px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/trashcan-black.png" /> to remove a custom value.

        <br />

        You can additionally access this option by selecting the edit icon (<img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/edit3green.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=a1c340832a61f6658f2289ec95e7620c" alt="" width="24" height="24" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '24px', height: '24px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/edit3green.png" />) in the snippet header.
      </td>
    </tr>

    <tr>
      <td>Settings</td>

      <td>
        Open the sidebar menu. Use to

        <br />

        * Define data settings for the filter snippet
        * Define filter snippet settings
        * Apply filters and hierarchical filters (if available) to the filter snippet
        * Adjust widget settings for the filter snippet
        * Manage comments for the filter snippet
      </td>
    </tr>

    <tr>
      <td>Connect Widgets</td>
      <td>Select to connect visuals or filters to the filter snippet. See [Connect Visuals to a Filter Snippet](#connect-visuals-to-a-filter-snippet) and [Link Filter Snippets](#link-filter-snippets).</td>
    </tr>

    <tr>
      <td>Remove Widget</td>
      <td>Remove the selected filter snippet from the dashboard. See [Edit or Delete Filter Snippets](#edit-or-delete-filter-snippets).</td>
    </tr>
  </tbody>
</table>

<h2 id="edit-or-delete-filter-snippets">
  Edit or Delete Filter Snippets
</h2>

As the owner or editor of a dashboard, you can make several changes to the filter snippet:

* Add, remove, or change sources
* [Connect visuals](#connect-visuals-to-a-filter-snippet) to the filter snippet
* Remove the filter snippet
* Adjust the settings for the filter snippet using the [filter snippet sidebar](#use-the-filter-snippet-sidebar-menu)

<Note>
  Users with Viewer access can add custom values to the snippet to filter connected visuals.
</Note>

### Edit a Filter Snippet

1. Select the snippet on the dashboard. A blue border appears around the snippet widget.
2. Select <img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/gear-joins-710.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=1e5db9bf2b3879817708388c123fdc28" alt="" width="17" height="16" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '17px', height: '16px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/gear-joins-710.png" /> **Settings** from the Show More menu (<img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/more-menu.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=1471c7a569a7e100cd7fa4083b04551a" alt="Selet the three dots icon to open a show more menu or take actions for the named column" width="21" height="12" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '21px', height: '12px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/more-menu.png" />) to open the filter snippet sidebar menu.
3. Use the [sidebar menu](#use-the-filter-snippet-sidebar-menu) to update data settings, filter snippet settings, or widget settings.
4. When you have finished making changes to the snippet, [save](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-save) the dashboard.

### Delete a Filter Snippet

1. Edit the dashboard. See [Edit a Dashboard](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/dashboards/dash-manage#edit-a-dashboard).
2. Select the filter snippet to be removed.
3. Select **Remove Widget** in the [snippet drop-down menu](#connect-visuals-to-a-filter-snippet). A removal confirmation dialog opens.
4. Select **Delete** on the warning dialog to confirm the deletion.

<h2 id="link-filter-snippets">
  Link Filter Snippets
</h2>

You can connect multiple filter snippets to one another to further refine the data you highlight in your dashboard.

**Link filter snippets**

1. Select the snippet on the dashboard. A blue border appears around the snippet widget.

2. Select <img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/connect-visuals-23-1.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=7e1caed6f0cbdd1fe244190b3ed132d3" alt="" width="20" height="20" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '20px', height: '20px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/connect-visuals-23-1.png" /> **Connect Widgets** from the menu (<img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/more-menu.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=1471c7a569a7e100cd7fa4083b04551a" alt="Selet the three dots icon to open a show more menu or take actions for the named column" width="21" height="12" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '21px', height: '12px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/more-menu.png" />). The Connect Widgets work area opens.

   <img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/filtersnippets/link-filters-23-4.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=f2102d9bf17f77240c19ada4c4540401" alt="Link multiple filters to refine your data by multiple values" width="384" height="355" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/filtersnippets/link-filters-23-4.png" />

3. Select **Add Widget**. Select a **Widget Name** to filter and an available **Field**.

   <Note>
     Filters you link must use a data source associated with the dashboard.
   </Note>

4. Repeat to add as many filters as desired. Select the copy icon to quickly add all visuals and filter snippets from the dashboard that share the same data source.

5. Optionally, remove widgets by selecting the delete icon next to each widget.

6. Select **Apply** to connect the filters.

7. Your filters are linked and you can filter the data shown in connected visuals using both filters.

<Note>
  When you create a filter snippet, it is linked to the dashboard you have added it to. If you delete a dashboard, the snippet is deleted as well.
</Note>

<h2 id="connect-visuals-to-a-filter-snippet">
  Connect Visuals to a Filter Snippet
</h2>

Build and use filter snippets to filter and highlight data on your dashboard. To apply filters to visuals, connect a filter snippet to one or more visuals using a corresponding field from the visual's underlying source. You can also filter a filter snippet by another filter snippet.

**Connect visuals**

1. Select the snippet on the dashboard. A blue border appears around the snippet widget.

2. Select <img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/connect-visuals-23-1.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=7e1caed6f0cbdd1fe244190b3ed132d3" alt="" width="20" height="20" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '20px', height: '20px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/connect-visuals-23-1.png" />**Connect Widgets** from the menu (<img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/more-menu.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=1471c7a569a7e100cd7fa4083b04551a" alt="Selet the three dots icon to open a show more menu or take actions for the named column" width="21" height="12" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '21px', height: '12px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/more-menu.png" />). The Connect Widgets work area opens.

   <img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/filtersnippets/connect-widgets-23-4.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=b66f9334c7f3efd6d442ed8667b4acf7" alt="Add or remove visuals or filters you want to filter using this filter snippet" width="384" height="352" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/filtersnippets/connect-widgets-23-4.png" />

3. Select **Add Widget**. Select a **Widget Name** and an available **Field**.

4. Repeat to add as many visuals or filter snippets as desired. Select the copy icon to quickly add all visuals and filter snippets from the dashboard that share the same data source.

5. Optionally, remove widgets by selecting the delete icon next to each widget.

6. Select **Apply** to connect the visuals.

<Note>
  When you create a filter snippet, it is linked to the dashboard you have added it to. If you delete a dashboard, the snippet is deleted as well.
</Note>

To link filter snippets for further data refinement, see [Link Filter Snippets](#link-filter-snippets).

<h2 id="custom-values-for-filter-snippets">
  Custom Values for Filter Snippets
</h2>

All users with access to a dashboard can add custom values to a filter snippet to filter [connected visuals](#connect-visuals-to-a-filter-snippet).

* Users with Viewer access can add custom values to the snippet to filter connected visuals.
* Owners and editors can add custom values and remove custom values any user has added.

**Add custom values to a filter snippet**

1. Enter a value in the **Search** field of a filter snippet. If the value is not part of the filter, add the value by selecting **Add** or the add <img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/add.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=9a24b95d9385f23950764407d5e9111a" alt="add icon" width="16" height="16" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '16px', height: '16px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/add.png" /> icon.

2. If applicable, select the Submit button to apply your changes to the connected visuals.

   <Note>
     Users with Viewer access can delete custom values by selecting delete icon <img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/delete-black-open.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=2dd520b27e17cb3afb7d849272854051" alt="" width="18" height="21" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '18px', height: '21px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/delete-black-open.png" /> before saving the dashboard under a new name.
   </Note>

3. When you have finished making changes to the snippet, [save](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-save) the dashboard.

   1. Owners and editors can save the dashboard as is, or save it using a new name.
   2. Users with Viewer access can save the dashboard using a new name. Changes to the existing dashboard are not retained.

**Remove custom value from a filter snippet**

1. Select the snippet on the dashboard. A blue border appears around the snippet widget.
2. Select the edit icon <img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/edit4gry.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=87563143361325e376add708486db9b2" alt="" width="24" height="24" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '24px', height: '24px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/edit4gry.png" /> to edit the list of custom values.
3. All custom values you can remove have a delete icon <img src="https://mintcdn.com/insightsoftware/1fCfZrK84x8KmAw8/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/trashcan-black.png?fit=max&auto=format&n=1fCfZrK84x8KmAw8&q=85&s=136b6c4981ae0ce343d31bfd990f10e8" alt="" width="17" height="20" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '17px', height: '20px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/trashcan-black.png" />. Select to delete the value.
4. When you have finished making changes to the snippet, [save](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-save) the dashboard.

<h2 id="filter-data-with-masked-fields">
  Filter Data With Masked Fields
</h2>

Filter snippets allow your users to view and highlight data pulled from one ore more sources in multiple visuals. In some cases, however, you may want to allow your users to filter information using sensitive data without exposing that data.

To do this, disable Filtering for one or more fields in a data source, create a new filter snippet that uses one or more of those fields, and connect your visuals as needed.

Users then can view filtered data based on those fields, but the values and name of the fields are masked. If users export this information, it is presented in a masked format. If the values are included as data fields or auto-generated descriptions, they are represented by asterisks `******`.

<Warning>
  Applied filter values that later have **Filtering** disabled to not automatically mask or hide those fields. You must recreate the filter that uses these values.
</Warning>

**Disable Filtering for a field's data column**

1. Navigate to the Fields tab of your data source, then select **Bulk Field Capabilities**. The Bulk Field Capabilities work area opens.

2. Find your fields by scrolling, searching, or filtering.

3. Select the toggle in the **Filtering** column to disable (slide left) each field as needed.

4. **Save** your changes. A success message is returned.

   Next, create a filter snippet that uses this field.

**Create a new filter snippet**

1. Open and [edit](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/dashboards/dash-manage#edit-a-dashboard) a dashboard.

2. Select <img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/add-filter-snippet.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=499601ef1705bb1d3ad3838d4b141b1a" alt="select the add filter snippet icon to add a filter snippet to a dashboard" width="24" height="22" noZoom data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/add-filter-snippet.png" /> on the [dashboard icon bar](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/dashboards/dash-layout#use-the-dashboard-icons). A new filter snippet is added in a widget on the dashboard, ready to edit.

3. Select **Settings** from the more menu (<img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/more-menu.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=1471c7a569a7e100cd7fa4083b04551a" alt="Selet the three dots icon to open a show more menu or take actions for the named column" width="21" height="12" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '21px', height: '12px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/more-menu.png" />) to open the filter snippet sidebar menu. See [Use The Filter Snippet Sidebar Menu](#use-the-filter-snippet-sidebar-menu).

4. Open <img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/filter-table-23-1.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=912013217238ea83494600bf4abf5650" alt="" width="20" height="20" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '20px', height: '20px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/filter-table-23-1.png" /> **Data Settings** in the filter sidebar menu, then select your **Source**. A Value Column field appears, but you can not add your Filtered field to it.

5. Disable **Use Value Column as Display Column**. With this disabled, you can select your **Filtered** field as the **Value Column**.

6. Select a different field to use as the value for the **Display Column**.

7. Continue creating the filter snippet by connecting widgets as needed. Select **Apply** to apply your changes.

8. [Save](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-save) the dashboard.

   Users can now use the filter snippet to change how data is presented, but not see or export the values you have disabled filtering for.
