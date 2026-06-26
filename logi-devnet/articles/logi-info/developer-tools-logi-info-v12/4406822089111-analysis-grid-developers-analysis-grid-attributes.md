---
title: "Analysis Grid Developers - Analysis Grid Attributes"
id: 4406822089111
section: "Developer Tools - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406822089111-Analysis-Grid-Developers-Analysis-Grid-Attributes
updated_at: 2022-04-06T06:03:08Z
---

# Analysis Grid Developers - Analysis Grid Attributes

# Analysis Grid Developers - Analysis Grid Attributes

The Analysis Grid element has the following attributes:

| Attribute | Description |
| --- | --- |
| ID | (Required) Specifies a unique element ID. |
| AJAX Paging and Sorting | Enables AJAX-style table paging and sorting. When the user moves to another table page, or sorts a column, only the table is updated. This method prevents the web page from flickering or losing the scroll position. This alters the behavior of the browser's "Back" button because the page history does not get updated with AJAX Paging. The default value is *False*. |
| Allow Pause Data Retrieval | Specifies whether or not to display an extra button on the Analysis Grid which, when clicked, temporarily halts data retrieval from the server. This feature is useful when data retrieval is slow and the user prefers to make several changes to the Analysis Grid without having to wait for data after each change. With data retrieval paused, the user can make all changes, then click the **Resume** button to resume retrieval. The default value is *False*. |
| Alternating Row Class | Specifies a CSS class to be used for every other row of the table. If you're using a Theme, the class *ThemeAlternatingRow* can be used. |
| Batch Selection | Specifies whether Analysis Grid charts and tables are updated as the user makes individual interface choices. When *True*, allows the user to select a number of options and then click an OK button to show the selections. This can improve performance by reducing the number of server requests. Users may need to click the OK button when the page is first displayed in order to get charts to render (even if no changes are made). The default value is *False*. |
| Caption | Specifies the title that will appear above the Analysis Grid. |
| Class | Specifies the CSS class to be used by the element. When set, this class will also be used by all child elements that don't have their own class. Generally not used if a Theme is being used. |
| Current Page Class | When paging is being used for a table, specifies the CSS class to be used by the "current page number" indicator. |
| Disable Replace Confirmation | Specifies whether pop-up confirmation prompts will appear when replacing Formula Columns, Filters, and Sort Orders. Set to *True* to disable the prompts.The default value is *False*. |
| Disable Show All Rows | Specifies whether the "Show all rows" option will appear in the Paging controls at runtime. If your users work with very large datasets, you may not want them to be able to use this option. Set to *True* to hide the option. The default value is *False*. |
| Draggable Panels | Specifies whether the panels that visualizations appear in can be rearranged at runtime by dragging them. The default value is *True*. |
| Exclude Details Rows Default | When rows are grouped within the Analysis Grid table, specifies whether detail rows are shown. In the table's configuration area, a check box allows excluding detail rows. Setting this attribute to *True* causes detail rows to be initially excluded (hidden). In some cases, especially when working with very large databases, performance may be better without detail rows. The default value is *False*. |
| Filter Case Sensitivity | Specifies if runtime Filters will be case-sensitive or case-insensitive. If set to *Insensitive*, values are compared without regard to upper and lower case. When set to *Sensitive*, case must match exactly. The default value is *blank*. In this case, the "Starts With" and "Contains" comparisons are case-insensitive, and the other comparisons are case-sensitive.  This attribute is ignored when using DataLayer.ActiveSQL with a SQL Server database and filters are always treated as *Insensitive*. |
| Hide Aggregates | Specifies whether the Aggregate feature will be hidden from view in the Table configuration and all column header drop-down options. The default value is *False*. |
| Hide Charts | Specifies whether the Chart tab or button in the Controls panel and all Table column header drop-down options will be hidden from view. The default value is *False*. |
| Hide Crosstabs | Specifies whether the Crosstab tab or button in the Controls panel and all Table column header drop-down options will be hidden from view. The default value is *False*. |
| Hide Exports | Specifies whether or not the Export iconwill be hidden from view. The default value is *False*. |
| Hide Filters | Specifies whether the Filter tab or button in the Controls panel and all Table column header drop-down options will be hidden from view. The default value is *False*. |
| Hide Formatting | Specifies whether the Format option in all Table column drop-down options lists will be hidden from view. The default value is *False*. |
| Hide Formulas | Specifies whether the Formula tab or button in the Controls panel will be hidden from view. The default value is *False*. |
| Hide Function Names Default | When using aggregations, specifies whether the names of the aggregating functions are displayed with the aggregated values in the tablesummary row. |
| Hide Grouping | Specifies whether the Group tab or button in the Controls panel and all Table column header drop-down options will be hidden from view. The default value is *False*. |
| Hide Layout | Specifies whether the Columns feature in the Table configuration area will be hidden from view. The default value is *False*. |
| Hide Menu | Specifies whether the Controls panel itself will be hidden from view. The default value is *False*. |
| Hide Paging | Specifies whether the Paging tab or button in the Table configuration area will be hidden from view. The default value is *False*. |
| Hide Sort Order | Specifies whether the Sort feature in the Table configuration area and al Table column header drop-down options will be hidden from view. The default value is *False*. |
| Max Rows Export | Specifies a limit for the number of rows that will be exported and whether exporting is enabled. When working with very large data sets, exports may not be practical. If standard datalayers are being used, exports will only be enabled if the number of rows in the Analysis Grid's table does not exceed this limit. The default is *100,000* rows.  If the special value -1 is entered, the default maximum limit is removed, allowing *all**rows* to be exported.  If DataLayer.ActiveSQL or the Active Query Builder is being used, exports will not be disabled because the row count cannot always be known. |
| Numbered Page Count | Specifies how many number links will appear as paging controls when the Show Page Number attribute is set to *Numbered*. The default value is *10*. |
| Page Row Count | Specifies how many rows of data will be shown in each "page" of the table. |
| Saved Analysis Grid Folder | Specifies the name of a folder where users' Analysis Grid options can be saved using the Procedure.Save Analysis Grid element. See [Analysis Grid Developers - Customizing Analysis Grid Appearance](https://devnet.logianalytics.com/hc/en-us/articles/4406822091927-Analysis-Grid-Developers-Customizing-Analysis-Grid-Appearance). |
| Security Right ID | When using Logi Security, specifies one or more Security Right IDs, separated by commas. Users with these Security Right IDs will be able to view the Analysis Grid, users without them will not. |
| Show Page Number | Specifies whether, and in what format, paging controls will appear. Options include:  *True* - Displays page number in the format "Page 1 of N". Users can navigate pages by clicking icons or by typing in a page number.  *Numbered* - (default) Displays a series of page number links in the format "1 2 3 N". The number of links is set using the Numbered Page Count attribute. The Current Page Class attribute can be used to emphasize the current page number.  *False* - No paging controls will be shown. |
| Sort Arrows | Specifies whether sort direction indicators (arrows) are displayed when the user clicks a column heading to sort the table. The default value is *False*. |
| Template Modifier File | Specifies the name, with file extension, of a [Template Modifier Files](https://devnet.logianalytics.com/hc/en-us/articles/4406817877655-Template-Modifier-Files) to be applied to the Analysis Grid at runtime. This is an XML file that can be used to change the underlying template used to create the Analysis Grid. Template Modifier files can be in any folder accessible to the application; if a folder isn't specified, the \_SupportFiles folder is assumed. |
| Width | Specifies the width of the Analysis Grid, in units set in the Width Scale attribute. |
| Width Scale | Specifies the width units of the Width attribute, either *px* for pixels or *%* for percent. |
