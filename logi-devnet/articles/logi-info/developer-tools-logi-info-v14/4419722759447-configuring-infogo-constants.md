---
title: "Configuring InfoGo Constants"
id: 4419722759447
section: "Developer Tools - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419722759447-Configuring-InfoGo-Constants
updated_at: 2022-07-17T02:08:40Z
---

# Configuring InfoGo Constants

# Configuring InfoGo Constants

The application's \_Settings definition includes several InfoGo constants you may want to configure. These constants are:

| Constant | Description |
| --- | --- |
| ChartAutoZoom | Specifies whether chart zoom is enabled/disabled for Bar Charts, Line Charts, Curve Lines, and Scatter Plots. Default value: *False*. |
| ChartCanvasAutoDrillTo | Specifies whether or not Self-Service users can drill into data on the Dashboard. Default value: *True*, Drill To feature enabled. To disable, set value to *False*. |
| New for 14.1goAllowBatchBookmarkDuplication | Specifies whether or not Self-Service users can batch duplicate SSRM bookmarks in their original folder. Default value: *False*. To enable, set value to *True*. |
| goAllowPauseDataRetrieval | Specifies whether or not to display an extra button on the Analysis tool which, when clicked, temporarily halts data retrieval from the server. This feature is useful when data retrieval is slow and the user prefers to make several changes to the Analysis without having to wait for data after each change. With data retrieval paused, the user can make any desired changes, then click the **Resume** button to resume retrieval. Default value: *False*.  New for 14.2 When set to *True*, you can also automatically apply Pause Data Retrieval at the application level using the constant rdAgDataRetrievalPaused. |
| goAllowSharing | Specifies whether bookmark folder sharing is enabled. Default value: *False* |
| goAnalysisType | (Used only when DM is installed) Specifies the analysis tool options that will appear on the menu. Possible values and effects include:  *AnalysisGrid* (or if left blank) - The Analysis Grid will be used, and the goAnalysisGrid definition will be shown when this option is selected. *Discovery -* The Thinkspace will be used, and the DM's goDiscovery definition will be shown when this option is selected. *UserSelectable -* Both options will be displayed, allowing the user to choose their analysis tool. |
| goBatchSelection | Specifies when changes made to chart and table options in analyses will be applied. When *True*, users can make several changes, then click an OK button to apply them. When *False*, changes are applied immediately as each change is made. The batch approach may make for a smoother user experience, especially with large data sets. Default value (or if no such constant exists): *False* |
| goBookmarkShowItemCount | Specifies whether folders will show item count. Default value: *False*. When *True*, a folder count will display for each folder listed on the SSRM Home page (My Items, My Visualizations, Global Menu, and Shared with Me). |
| goCustomTableSessionVars | Specifies an optional comma-separated list of session variable names to be saved when adding new bookmarks. Do not enter tokens themselves, just the variable names.  These variables will be saved as static "resolved" values in the bookmark's custom SQL query, rather than being saved as tokens. |
| goDashboardFilters | Specifies whether Dashboard panels with Analysis Filters, and/or those generated from Analysis Grid analyses that use the Active Query Builder element, will have panel and global filters created for them automatically. Default value: *False.* |
| goDashboardFiltersFromChartDisabled | When the goDashboardFilters constant is set to *True*, this constant can be used to prevent global filters from being added when Dashboard panel charts are clicked. |
| New for 14.1goDashboardFiltersOnDemand | Specifies whether the server prepares filter information and user interface components on demand. Default value: *False*. To reduce load time when opening your Dashboard, set this constant to *True*. |
| goDashboardPanelEditing | Specifies whether editing of visualizations in Dashboard panels at runtime is enabled. When *True*, the Edit option will appear in a panel's gear icon menu (assuming the visualization data source is a candidate for editing). See [Enabling Panel Content Editing](https://devnet.logianalytics.com/hc/en-us/articles/4419722769431-Enabling-Panel-Content-Editing) for more information. |
| goDefaultAnalysisName | Specifies the default title that will be used for each new Analysis created. Default value: *Untitled Analysis.* |
| goDefaultBookmarkCollection | This constant is used by the global features. It's created, and its value is set, by the application. Do not alter it. |
| goDefaultBookmarkID | This constant is used by the global features. It's created, and its value is set, by the application. Do not alter it. |
| goDefaultBookmarkReportName | This constant is used by the global features. It's created, and its value is set, by the application. Do not alter it. |
| goDefaultBookmarkUserName | This constant is used by the global features. It's created, and its value is set, by the application. Do not alter it. |
| goDefaultDashboardName | Specifies the default title that will be used for each new Dashboard created. Default value: *Untitled Dashboard.* |
| goDefaultExcludeDetailRows | Specifies whether detail rows will be shown when rows are grouped within the table when using the Analysis Grid. In the table's configuration area, a check box allows excluding of detail rows. Setting this attribute to *True* causes detail rows to be initially excluded (hidden). In some cases, especially when working with very large databases, performance may be better without detail rows. Default value: *False*. |
| goDefaultHideFunctionNames | When using the Analysis Grid and aggregations in the table, specifies whether the names of the aggregating functions are displayed with the aggregated values in the table summary row. |
| goDefaultReportName | Specifies the default title that will be used for each new Report created. Default value: *Untitled Report.* |
| goDefaultSharedBookmarkID | This constant is used by the global features. It's created, and its value is set, by the application. Do not alter it. |
| goHideColumnSelection | Specifies whether the column selection panel will be shown in the Analysis page's Data tab after a table is selected. When set to *False*, all columns are automatically selected. Default value: *True.* |
| goHomeName | Specifies the title of the Home page. Default value: *Home.* |
| goMetadataIDsAnalysisGrid | Specifies a comma-separated list of one or more IDs of Metadata elements, defined for connections in the \_Settings definition, to be used with the Analysis Grid. If left blank, *all* Metadata element IDs from \_Settings will be used. This constant is used in the Active Query Builder in the goAnalysisGrid definition. |
| goMetadataIDsDiscovery | (Used only when DM is installed) Specifies a comma-separated list of one or more IDs of Metadata elements, defined for connections in the \_Settings definition, to be used with the DM. If left blank, *all* Metadata element IDs from \_Settings will be used. This constant is used in the Active Query Builder in the goDiscovery definition. |
| goNotificationsEnabled | Controls whether the Notification icon is enabled. When enabled, shared/unshared messages will be generated and recorded. Default value: *True*, disable by setting to *False.* |
| goReportStarterFile | Specifies a file to be used as the initial Save File for the Report Author in cases when the Save File does not exist yet. For example, when the Save File is different for each user, the Save File Starter file can include a set of default tabs and panels. Example:  @Function.AppPhysicalPath~\SaveFile\InitialReport.xml  Create a Save File Starter file by setting a Save File value, then opening and working with the Report Author to create the desired default set of tabs and panels, then moving and/or renaming the Save File into the Save File Starter location. |
| goSchedulerEnabled | Controls whether the Schedule icon appears in the Home page list of reports. Default value: *False.* |
| goSchedulerSessionVars | Specifies a comma-separated list of Session variables to be passed by the Logi Scheduler to a scheduled task during execution. |
| New for 14.1 goSharePermissionEnable | Specifies whether users can use interactive permissions. Default value: *False*. To enable sharing permissions, set this constant to *True*. |
| goThemeEditorEnabled | Specifies whether custom theme editing is enabled and visible in the Admin menu. Default value: *False*, enable by setting to *True*. See [Customizing Appearance](https://devnet.logianalytics.com/hc/en-us/articles/4419707420567-Customizing-Appearance). |
| New for 14.2 rdActiveSqlAggregateJoinExclusion | Controls automatic join exclusion for aggregates in ActiveSQL. Default value *False*, aggregates will be calculated after all joins have occurred. To exclude joins and prevent inflation, set this constant to *True*. |
| New for 14.2rdAgDataRetrievalPaused | Controls the initial status of the Analysis Grid's "Pause Data Retrieval" button. Default value: *False*, data pause is controlled on an individual basis. To automatically pause data retrieval, set this constant to *True*. |
| rdCalculationsIncludeNulls | By default, columns with Null values are excluded by default when making aggregations. If you want them to be included, create this constant and set it to *True*. |
| New for 14.2rdDashboardMaxPanelCount | Limits the number of panels that can appear in a Dashboard. If there is no constant, or its value is empty, this function is disabled. |
| New for 14.2rdDashboardMaxPanelsPerTab | Limits the number of panels that can appear in a Dashboard tab. If there is no constant, or its value is empty, this function is disabled. |
| rdDisableMetaDataColumnCheck | Controls the ability to disable checking the metadata at runtime. Setting this constant to *True* allows access to bookmarks that reference columns not defined in the metadata source file. Default value: *False.*  When enabled, bookmarks only use the metadata as it existed when it was created, with the exception of the Data tab because that is where the metadata, tables, and columns are selected or changed, and the metadata stored in the bookmark only contains the tables and columns that have already been selected.  When enabled, if you edit the metadata and add or remove Security Right IDs at runtime, those Security Right IDs will be ignored for existing bookmarks. |
| New for 14.1rdDisableURLMetadataCache | Controls the metadata caching mechanism so that visualizations using the same metadata can be verified by a single shared and cached metadata. Default value: *False*. Setting this constant to *True* closes the caching mechanism. |
| rdExportDataPreference | Specifies the export preference. Options include: Empty (default), Rapid, and Formatted. Set this global constant to *Rapid* to enable rapid Excel and CSV exports. |
| New for 14.1rdHideDataTableHeaderIfNoData | Controls the ability to hide the Data Table/Crosstab Table header when there is no data to show. Default value: *False*. To hide the header when there is no data, set this constant to *True*. |
| New for 14.2 rdOutputHtmlDivTagDefault | Specifies the default rendering results when the Output HTML DIV Tag of the Division tag is not set explicitly. Default value: *Empty* (False). When set to *True*, the default rendering result is <div>. |
| New for 14.2rdIncludeFilterInfoInExport | Controls the ability to display filter information in your Excel, PDF, or CSV exports. Default value: *False*. To display filters in your export, set this constant to *True*. |
| New for 14.2rdIncludeReportTitleInExport | Controls the ability to display the report title in your Excel, PDF, or CSV exports. Default value: *False*. To display the report title in your export, set this constant to *True*. |
| New for 14.1rdNoDataCaption | Specifies the message that displays in the Data Table/Crosstab Table when there is no data to display. Default value: *None*, no message displays. Enter a custom message as the value for this constant, or, enter "Default" and users will receive the message "No data to display". |
| New for 14.2 rdRapidExportIncludeGroups | Controls whether Group or Summary information is included when exporting via Rapid Excel or Rapid CSV. Default value: *False*. To display Group or Summary information in the Excel/CSV result, set this constant to *True*. |
| SchedulerApplicationID | Specifies the ID that will be used for this task in the Logi Scheduler. Default value: *InfoGo.* |
| SchedulerErrorEmail | Specifies the admin email address to send an automatic error notification when a Scheduler Report errors. If there is no constant, or its value is empty, this function is disabled. Multiple addresses are supported, separated by ";". |

Other constants, unrelated to InfoGo, may also exist.
