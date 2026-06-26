---
title: "Use The Filter Snippet Sidebar Menu"
id: 34932987838349
section: "Use Dashboards and Visuals in Composer 25"
product: "Logi Composer v25"
url: https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932987838349-Use-The-Filter-Snippet-Sidebar-Menu
updated_at: 2026-05-26T22:09:38Z
---

# Use The Filter Snippet Sidebar Menu

# Use The Filter Snippet Sidebar Menu

Use the filter snippet sidebar menu to:

* Define data settings for the filter snippet
* Define filter snippet settings
* Apply filters and hierarchical filters (if available) to the filter snippet
* Adjust widget settings for the filter snippet
* Manage comments for the filter snippet

To access the filter snippet sidebar menu, select **Settings** from the show more menu ![](https://logi-composer-v25.insightsoftware.com/hc/article_attachments/46167885461261). The filter snippet sidebar opens.

## Filter Snippet Sidebar Menus

![Use this work area to define filter snippet data settings](https://logi-composer-v25.insightsoftware.com/hc/article_attachments/46167169296397 "Data Settings work area - filter snippets")![Use this work area to define filter snippet options](https://logi-composer-v25.insightsoftware.com/hc/article_attachments/46167179927821 "Flter Snippet Settings work area")![Use this work area to define filters to apply to this filter snippet](https://logi-composer-v25.insightsoftware.com/hc/article_attachments/46167180112013 "Flter Snippet Filter work area")![Use this work area to define widget settings](https://logi-composer-v25.insightsoftware.com/hc/article_attachments/46167201558285 "Widget Settings work area - filter snippets")![Use this work area to view and manage comments](https://logi-composer-v25.insightsoftware.com/hc/article_attachments/46167186190605 "Widget Settings work area - filter snippets")

If this is a new filter snippet, default settings are shown. If this is an existing filter snippet, current settings are shown.

**Note:** 
If you are editing a filter snippet that references unavailable sources or fields, an **Unavailable** message is shown in the affected drop-down. Select a new source or fields as needed.

### Data Settings

Adjust the data settings for this filter snippet, then select **Apply** as needed to apply your changes to the filter snippet.

| Setting | Description |
| --- | --- |
| Data Type | Select a data type to filter: **Attribute**, **Time**, **Number** or **Hierarchy**. If you select Time, you can set conditions for the time spans **Between** or **Not Between** in the widget itself if the display style is **Range**. |
| Operator | Select an operator to use:   * **Attribute**: Select **Include** or **Exclude** to include or exclude a value from the data. Select **Contains** to return only data that contains a specified value. Select **Does Not Contain** to return only data that does not return a specified value. * **Number**: Select **Include** or **Exclude** to include or exclude a value from the data. Select **Contains** to return only data that contains a specified value. * **Time**: Select **Between** or **Not Between**, then define the conditions for time spans in the widget itself. * **Hierarchy**: Select **Equals or Descendants Of** or **Includes**, then select a value column. |
| Source | Select an available source to use. After you select a source, you can select an available field from that source to use as a Value Column for the filter, and a different Display Column if needed. |
| Value Column | Select an available field for the Value Column. Your users can filter the data in attached widgets using these values. If you prefer to use a different column as a Display Column, disable **Use Value Column as Display Column**.  **Note:** If you have Filtered a field to prevent users from seeing or exporting this data, you must disable Use Value Column as Display Column to select the column, then select a Display Column. See[Filter Data With Masked Fields](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932973019789-Filter-Data-With-Masked-Fields). |
| Display Column | Select a different field than the Value Column to use as a display column for your users. Only visible when you disable **Use Value Column as Display Column**.  **Note:** If you have Filtered a field to prevent users from seeing or exporting this data, you must disable Use Value Column as Display Column to select the column, then select a Display Column. See[Filter Data With Masked Fields](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932973019789-Filter-Data-With-Masked-Fields). |
| Granularity | Available for **Time** data types. Select an available option based on the granularity of the data provided. |
| Sort | Select an order to sort the filter values by. Available options depend on the selected data type. The column data used to sort is listed below the Sort heading.   * **Attribute**, **Number**, **Hierarchy**: Options include **Alphabetical (A - Z)** and **Reverse Alphabetical (Z - A)** * **Time**: Options include **Chronological** and **Reverse Chronological**. |

### Filter Snippet Settings

Adjust the filter snippet settings in this work area. Save the dashboard to save your changes.

| Setting | Description |
| --- | --- |
| Display Style | Select **Fixed List** to display all available selection items in a selection list.   * If you select **Fixed List** along with Single Number of Selections, users see a list of items and can select one. * If you select **Fixed List** along with Multiple Number of Selections, users see a list of items and can select multiple.   Select **Dropdown List** to display all available selection items in a drop-down list.   * If you select **Dropdown List** along with Single Number of Selections, users can filter or scroll through a list of items and can select one. * If you select **Dropdown List** along with Multiple Number of Selections, users can filter, select, and scroll through a list of items and can select multiple values.   Enable or disable the **Hide "Add" Button** toggle to control if users can add their own items. |
| Number of Selections | Specify whether only one or multiple data values can be selected in the filter snippet. Select **Single** to allow users to select only one data value; select **Multiple** to allow users to select more than one value.   * If you select **Fixed List** along with **Single**, users see a list of items and can select one value. * If you select **Dropdown List** along with **Single**, users can filter or scroll through a list of items and can select one value. * If you select **Fixed List** along with **Multiple**, users see a list of items and can select multiple values. * If you select **Dropdown List** along with **Multiple**, users can filter, select, and scroll through a list of items and can select multiple values. |
| "No Selection" Label | Visible when the **Single** option for **Number of Selections** is selected.  Enter text to display when no values have been selected. Default text is **None**. |
| Placeholder Text | Visible when both the **Dropdown List** and **Multiple** options are selected.  Enter text to display in the Search field when no values have been selected. Default text is **Search**. |
| Filter Values On | Visible when the **Multiple** option for **Number of Selections** is selected.   * Select **Change** to apply the filter snippet to connected visuals as selections are made. * Select **Submit** to apply the filter snippet to connected visuals when a user selects **Submit**. |
| Submit Button Text | Visible when the **Submit** option for **Filter Values On** is selected.  Enter text to display for users to apply the filter snippet to connected visuals. Default text is **Submit**. |

### Filters

Apply or create filters in this work area. Save the dashboard to save your changes.

| Setting | Description |
| --- | --- |
| Add Filter | Select to add a [row level filter](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932930630157-Apply-Row-Level-Filters), [group filter](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932955067661-Apply-Group-Filters), [hierarchical filter](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932931841549-Filter-by-Hierarchy-Field), or [saved filter](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932955235597-Apply-a-Saved-Filter-to-a-Visual-Filter-Snippet-or-Dashboard) to this filter snippet. |
| Save Filters | After you've created one or more filters, select [Save Filters](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932960626957-Create-a-Saved-Filter) to save and reuse in your environment. |

### Widget Settings

Adjust the widget settings for this filter snippet, then select **Apply** as needed to apply your changes to the filter snippet. Save the dashboard to save your changes.

| Setting | Description |
| --- | --- |
| Display Name | The display name for this filter snippet. Change here or edit directly in the widget. |
| Description | An optional description for this filter snippet. Blank by default. Maximum 750 characters. |
| Header | Adjust the header behavior. The default setting is   * **Show**: display the header at all times. Default setting. * **Show on Hover**: hide the header in Viewer mode unless users perform a hover action over the widget. * **Hide**: completely hide the header from visibility in Viewer mode. |
| Position | Adjust the position of the widget content in the cell (widget footprint in the dashboard) to align vertically and horizontally as appropriate within the space. Select center, top, or bottom as needed. |

### Comments

If you have access to comments, manage them on this tab. See [Manage Widget Comments](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933318308877-Manage-Widget-Comments).
