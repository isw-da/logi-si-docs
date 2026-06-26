---
title: "Configuring InfoGo Constants"
id: 4406822192535
section: "Developer Tools - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406822192535-Configuring-InfoGo-Constants
updated_at: 2022-04-06T06:04:35Z
---

# Configuring InfoGo Constants

# Configuring InfoGo Constants

The application's \_Settings definition includes several InfoGo constants you may want to configure. These constants are:

| Constant | Description |
| --- | --- |
| ChartCanvasAutoDrillTo | Specifies whether or not Self-Service users can drill into data on the dashboard. The default value is: *True*, Drill To feature enabled. To disable, set value to *False*. |
| goAllowPauseDataRetrieval | Specifies whether or not to display an extra button on the Analysis tool which, when clicked, temporarily halts data retrieval from the server. This feature is useful when data retrieval is slow and the user prefers to make several changes to the Analysis without having to wait for data after each change. With data retrieval paused, the user can make any desiredchanges, then click the **Resume** button to resume retrieval. The default value is: *False* |
| goAllowSharing | Specifies whether bookmark folder sharing is enabled. Default: *False* |
| goAnalysisType | (Used only when DM is installed) Specifies the analysis tool options that will appear on the menu. Possible values and effects include:  *AnalysisGrid* (or if left blank) - The Analysis Grid will be used, and the goAnalysisGrid definition will be shown when this option is selected. *Discovery -* The Thinkspace will be used, and the DM's goDiscovery definition will be shown when this option is selected. *UserSelectable -* Both options will be displayed, allowing the user to choose their analysis tool. |
| goBatchSelection | Specifies when changes made to chart and table options in analyses will be applied. When *True*, users can make several changes, then click an OK button to apply them. When *False*, changes are applied immediately as each change is made. The batch approach may make for a smoother user experience, especially with large data sets. The default value (or if no such constant exists): *False* |
| goBookmarkShowItemCount | Specifies whether folders will show item count. The default value is: *False*. When *True*, a folder count will display for each folder listed on the SSRM Home page (My Items, My Visualizations, Global Menu, and Shared with Me). |
| goCustomTableSessionVars | Specifies an optional comma-separated list of session variable names to be saved when adding new bookmarks. Do not enter tokens themselves, just the variable names.  These variables will be saved as static "resolved" values in the bookmark's custom SQL query, rather than being saved as tokens. |
| goDashboardFilters | Specifies whether dashboard panels with Analysis Filters, and/or those generated from Analysis Grid analyses that use the Active Query Builder element, will have panel and global filters created for them automatically. The default value is *False.* |
| goDashboardFiltersFromChartDisabled | When the goDashboardFilters constant is set to *True*, this constant can be used to prevent global filters from being added when dashboard panel charts are clicked. |
| goDashboardPanelEditing | Specifies whether editing of visualizations in dashboard panels at runtime is enabled. When *True*, the Edit option will appear in a panel's gear icon menu (assuming the visualization data source is a candidate for editing). See [Enabling Panel Content Editing](https://devnet.logianalytics.com/hc/en-us/articles/4406822196887-Enabling-Panel-Content-Editing) for more information. |
| goDefaultAnalysisName | Specifies the default title that will be used for each new Analysis created. The default value is: *Untitled Analysis.* |
| goDefaultBookmarkCollection | This constant is used by the global features. It's created, and its value is set, by the application. Do not alter it. |
| goDefaultBookmarkID | This constant is used by the global features. It's created, and its value is set, by the application. Do not alter it. |
| goDefaultBookmarkReportName | This constant is used by the global features. It's created, and its value is set, by the application. Do not alter it. |
| goDefaultBookmarkUserName | This constant is used by the global features. It's created, and its value is set, by the application. Do not alter it. |
| goDefaultDashboardName | Specifies the default title that will be used for each new Dashboard created. The default value is: *Untitled Dashboard.* |
| goDefaultExcludeDetailRows | Specifies whether detail rows will be shown when rows are grouped within the table when using the Analysis Grid. In the table's configuration area, a check box allows excluding of detail rows. Setting this attribute to *True* causes detail rows to be initially excluded (hidden). In some cases, especially when working with very large databases, performance may be better without detail rows. The default value is *False*. |
| goDefaultHideFunctionNames | When using the Analysis Grid and aggregations in the table, specifies whether the names of the aggregating functions are displayed with the aggregated values in the table summary row. |
| goDefaultReportName | Specifies the default title that will be used for each new Report created. The default value is: *Untitled Report.* |
| goDefaultSharedBookmarkID | This constant is used by the global features. It's created, and its value is set, by the application. Do not alter it. |
| goHideColumnSelection | Specifies whether the column selection panel will be shown in the Analysis page's Data tab after a table is selected. When set to *False*, all columns are automatically selected. The default value is *True.* |
| goHomeName | Specifies the title of the Home page. The default value is *Home.* |
| goMetadataIDsAnalysisGrid | Specifies a comma-separated list of one or more IDs of Metadata elements, defined for connections in the \_Settings definition, to be used with the Analysis Grid. If left blank, *all* Metadata element IDs from \_Settings will be used. This constant is used in the Active Query Builder in the goAnalysisGrid definition. |
| goMetadataIDsDiscovery | (Used only when DM is installed) Specifies a comma-separated list of one or more IDs of Metadata elements, defined for connections in the \_Settings definition, to be used with the DM. If left blank, *all* Metadata element IDs from \_Settings will be used. This constant is used in the Active Query Builder in the goDiscovery definition. |
| goNotificationsEnabled | Controls whether the Notification icon is enabled. When enabled, shared/unshared messages will be generated and recorded. The default value is *True*, enable by setting to *False.* |
| goReportStarterFile | Specifies a file to be used as the initial Save File for the Report Author in cases when the Save File does not exist yet. For example, when the Save File is different for each user, the Save File Starter file can include a set of default tabs and panels. Example:  @Function.AppPhysicalPath~\SaveFile\InitialReport.xml  Create a Save File Starter file by setting a Save File value, then opening and working with the Report Author to create the desired default set of tabs and panels, then moving and/or renaming the Save File into the Save File Starter location. |
| goSchedulerEnabled | Controls whether the Schedule icon appears in the Home page list of reports. The default value is *False.* |
| goSchedulerSessionVars | Specifies a comma-separated list of Session variables to be passed by the Logi Scheduler to a scheduled task during execution. |
| goThemeEditorEnabled | Specifies whether custom theme editing is enabled and visible in the Admin menu. The default value is *False*, enable by setting to *True*. See [Customizing Appearance](https://devnet.logianalytics.com/hc/en-us/articles/4406822195863-Customizing-Appearance). |
| rdCalculationsIncludeNulls | By default, columns with Null values are excluded by default when making aggregations. If you want them to be included, create this constant and set it to *True*. |
| rdExportDataPreference | Specifies the export preference. Options include: Empty (default), Rapid, and Formatted. Set this global constant to *Rapid* to enable rapid Excel and CSV exports. |
| SchedulerApplicationID | Specifies the ID that will be used for this task in the Logi Scheduler. The default value is *InfoGo.* |
| SchedulerErrorEmail | Specifies the admin email address to send an automatic error notification when a Scheduler Report errors. If there is no constant, or its value is empty, this function is disabled. Multiple addresses are supported, separated by ";". |

Other constants, unrelated to InfoGo, may also exist.
