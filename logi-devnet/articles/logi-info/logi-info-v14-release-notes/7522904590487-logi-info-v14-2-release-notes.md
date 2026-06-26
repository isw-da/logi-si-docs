---
title: "Logi Info v14.2 Release Notes"
id: 7522904590487
section: "Logi Info v14 Release Notes"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/7522904590487-Logi-Info-v14-2-Release-Notes
updated_at: 2023-12-01T18:23:59Z
---

# Logi Info v14.2 Release Notes

# Logi Info v14.2 Release Notes

Please select the following link to view a Chrome browser update likely to affect all Info customers this year: [Critical Chrome Browser Update](https://devnet.logianalytics.com/hc/en-us/articles/4415831044375).

This topic describes feature enhancements, resolved issues, and important information for Logi Info v14.2, released on July, 2022.

NOTE: If you upgrade an existing installation of one of our products, or an existing Logi application, from one major version to another major version, for example v12 to v14.0, you will need a new license key and file for the new product/application. If you have an active maintenance contract with Logi, we've already created licenses for your license point of contact, which you can find on DevNet by selecting **Support > License Manager**. Contact [Customer Service](mailto:CustomerService@LogiAnalytics.com) if you want to upgrade and need a new license.

To purchase this product, contact [US Sales](mailto:salesteam@logianalytics.com?subject=I%20am%20interested%20in%20purchasing%20this%20product,%20please%20contact%20me. "US Sales email address.") or [UK Sales](mailto:emea_sales@logianalytics.com?subject=I%20am%20interested%20in%20purchasing%20this%20product.%20Please%20contact%20me. "Email address for UK sales team.").

* [Logi Info v14.2 Service Pack 6 Resolved Issues](#01H81Y772ZA8NYNJ9CKF0PP56M)
* [Logi Info v14.2 Service Pack 5 Resolved Issues](#h_01GQ0BRAM3VNSZHDBWTAB8CEV3)
* [Logi Info v14.2 Service Pack 4 Resolved Issues](#h_01GQ0BRAM3VNSZHDBWTAB8CEV3)
* [Logi Info v14.2 Service Pack 3 Resolved Issues](#h_01GK4MKYQKN60QKKQRET8VQVDJ)
* [Logi Info v14.2 Service Pack 2 Resolved Issues](#h_01GCW2DTWG3YJH1V9EJBHGKC9Y)
* [Logi Info v14.2 Service Pack 1 Resolved Issues](#h_01GCW2DTWG3YJH1V9EJBHGKC9Y)
* [Logi Info v14.2 Feature Enhancements](#Logi_Info_v14.2_Feature_Enhancements)
* [Logi Info v14.2 Resolved Issues](#Logi_Info_v14.2_Resolved_Issues)

To view the Release Notes for this product version, along with previous product versions, see the [Info Release Notes page](https://clm.logianalytics.com/rdPage.aspx?rdReport=RelNotesINF).

## Logi Info v14.2 Service Pack 6 Resolved Issues

| Title | Description |
| --- | --- |
| SSRM - Aggregate Filter | Null values no longer count toward distinct count when applying an aggregate filter on a left joined table. |
| SSRM - Upgrade | You can now upgrade from SSRM v12.6 to v14.1 without any disruption to your Dashboard visuals' filters. |

## Logi Info v14.2 Service Pack 5 Resolved Issues

| Title | Description |
| --- | --- |
| Connection Issue | A sporadic MySQL connection issue that could potentially arise in certain scenarios was resolved. |
| Schedule Element | You can now add additional parameters in the Schedule element. |
| Report Author | The Add Visual pop-up window in Report Author only displays one add link, as intended. |
| Export to Excel | Exporting a dashboard to Excel honors the date settings of your Internet browser, as expected. |
| AG - Filters | Filtering an Analysis Grid that uses a formula column from a joined table no longer returns an error. |
| Dashboard Tabs | Dashboard tabs now display properly when upgrading from a previous version of Logi Info. |
| AG - Excel Dates | Dates now display properly in Excel when filtering using the Excel Column Format element in a Java environment. |

## Logi Info v14.2 Service Pack 4 Resolved Issues

| Title | Description |
| --- | --- |
| SSRM - Global Filters | Global filters now work, as expected, when applying an aggregate filter to a table and adding it to your Visual Gallery. |
| AG - Aggregate Filters | Aggregate filters that utilize a column with a distinct count now work while using date range comparison in the filter. |
| SSRM - Dashboard | The size of the table added to a Dashboard is not modified when the blank area in the panel is selected. |
| Group Drillthrough | The Group Drill Through element of Chart Canvas now works as expected in Info v14. |
| AG - DateTime Column | Time is now respected when filtering an Analysis Grid report by a DateTime column that uses time as part of the filter criteria. |
| DMF Workaround | An issue with sorting and then removing one or more formulas in shared bookmarks has been resolved. |
| Chart Drill Down | Chart drill down using action.link now functions properly when secure key is turned on. |
| rdGroupEndRow | Table grouping with rdGroupEndRow now persists even after cache times out. |

## 

## Logi Info v14.2 Service Pack 3 Resolved Issues

| Title | Description |
| --- | --- |
| SSRM - Shared Analysis | Opening a Shared Analysis no longer locks Analysis Grids in Read-Only mode. |
| SSRM - Column Headers | Column headers display, as expected, when adding to your Dashboard. |
| SSRM - Dashboard | Charts now display in Dashboards, as expected, when using the free-form layout. |
| Filter Condition | All date values now displays in the Filter Condition text. |
| CheckBox List Branch | The CheckBox List Branch now functions properly after multiple selections of child elements. |
| Timenextrun | An issue with get column “timenextrun” when using a postgres schedule database in Java has been resolved. |
| AG - Hide Aggregates | Setting Hide Aggregates to ‘True’ no longer returns an object reference error when upgrading. |

## Logi Info v14.2 Service Pack 2 Resolved Issues

| Title | Description |
| --- | --- |
| AG - Paging | Paging now accommodates the “Sensitive” filter case sensitivity when using MySQL datasources. |
| AG/SSRM - Editing Visualizations | The Description column now displays, as expected, when editing a Visualization in your Visual Gallery. |
| Event Handlers | Adding an Event Handler to a label now decodes special characters in its child, Link Parameters. |
| SSRM - Formulas | Removing a column used in a formula no longer returns an error. |
| AG- Aggregate Filters | You no longer receive an error when adding an aggregate filter to an Analysis Grid that contains a formula |
| AG - Percent of Total | Number of Decimal Places now applies when excluding detail rows an Analysis Grid with a “Percent of Total” formatted column. |
| AG - Formula Naming | The Analysis Grid no longer allows you to create multiple Formula columns with the same non-unique name. |
| SSRM - Rapid Excel Export | Exporting a shared analysis using Rapid Excel no longer throws an object reference error in .NET or a Java null exception in Java. |
| Gauge Angular | Gauge Angular charts now display the gauge ring colors, as expected. |
| AG - Export Excel | The correct filters now display in the exported report when using the constant rdIncludeFilterInfoInExport. |

## Logi Info v14.2 Service Pack 1 Resolved Issues

| Title | Description |
| --- | --- |
| AG - Filters | Using a filter after pausing data retrieval in your Analysis Grid no longer causes an error. |
| Java Connection Error | You no longer receive a ‘Connection is already open’ error when using bookmarks stored in a database in Info v14.2 in a Java environment. |
| Link Parameter | Selecting ‘Refresh’ no longer causes the value of the local data layer to encode spaces as %20. |
| AG - simpleReplace Filter | The simpleReplace filter function no longer triggers a ‘bookmark file not found’ error message. |
| AG - ExcelColumnFormat Element | The ExcelFormat attribute of the ExcelColumnFormat element now saves both new and existing Analysis Grid reports when the rdAGDisableExcelAutoFormats constant is set to 'True'. |

## Logi Info v14.2 Feature Enhancements

| Title | Description |
| --- | --- |
| [SSRM/AG - Customizable Sliding Date Options](https://devnet.logianalytics.com/hc/en-us/articles/7522860288407-Logi-Info-v14-2-Enhancements-#SSRM_-_Sliding_Date) | You can now customize your Sliding Date options when filtering an analysis by date/time. |
| [Customizable @Date Token](https://devnet.logianalytics.com/hc/en-us/articles/7522860288407-Logi-Info-v14-2-Enhancements-#Customizable_Date_Tokens) | Studio now supports customized @Date tokens. |
| [Default DIV Output Tag](https://devnet.logianalytics.com/hc/en-us/articles/7522860288407-Logi-Info-v14-2-Enhancements-#Default_DIV_Output_Tag) | As a report developer, you now have the ability to specify the Output HTML DIV Tag attribute for all elements that are not set manually at the application level. |
| [Dashboard Panel/Tab Max Count](https://devnet.logianalytics.com/hc/en-us/articles/7522860288407-Logi-Info-v14-2-Enhancements-#Dashboard_Panel/Tab_Max_Count) | Developers and system administrators can now limit the number of panels that appear in a Dashboard, as well as the number of panels in a Dashboard tab. |
| Data Table Lazy Loading | Info v14.1 introduced the "Scrollbar" value to the Caption Type attribute, enabling users to scroll through their Data Table results. This release extends the Scrollbar functionality to incorporate lazy loading. |
| [Remove Empty Grouped Rows](https://devnet.logianalytics.com/hc/en-us/articles/7522860288407-Logi-Info-v14-2-Enhancements-#Remove_Empty_Grouped_Rows) | The Target.NativeExcel element has a new attribute, Remove Empty Group Row, that allows you to remove blank rows from your Excel output when there is no detail data under a particular group. |
| [InfoGo - Rapid Excel/CSV Export Grouping](https://devnet.logianalytics.com/hc/en-us/articles/7522860288407-Logi-Info-v14-2-Enhancements-#InfoGo_-_Rapid_Excel_Export_Grouping) | Developers can now elect to include Group or Summary information in Rapid Excel and Rapid CSV exports. |
| [AG - Table Enhancements](https://devnet.logianalytics.com/hc/en-us/articles/7522860288407-Logi-Info-v14-2-Enhancements-#AG_-_Table_Enhancements) | This release provides additional flexibility to customize your Analysis Grid table including new configuration options to allow conditional grouping on aggregate rows, interactive paging improvements, conditional styling, the ability to reset the Analysis Grid, re-arrange sorting and grouping, and extended data formatting options. |
| [AG - Pause Data Retrieval Globally](https://devnet.logianalytics.com/hc/en-us/articles/7522860288407-Logi-Info-v14-2-Enhancements-#AG_-_Pause_Data_Retrieval) | A new global constant, rdAgDataRetrievalPaused, allows you to pause data retrieval prior to opening a bookmark. |
| [SSRM - Scheduler Last Day of the Month(s)](https://devnet.logianalytics.com/hc/en-us/articles/7522860288407-Logi-Info-v14-2-Enhancements-#SSRM_-_Scheduler_Last_Day_of_the_Month(s)) | Scheduler now supports running tasks on the last day of the month(s) when operating on a monthly cadence. |
| [SSRM - Specify Components for Scheduled Reports](https://devnet.logianalytics.com/hc/en-us/articles/7522860288407-Logi-Info-v14-2-Enhancements-#SSRM_-_Specify_Component_Report_Scheduling) | A new configuration option is available in SSRM's Report Author that allows you to exclude objects from scheduled tasks. |
| [SSRM - Match Boolean Format with Conditional Colors](https://devnet.logianalytics.com/hc/en-us/articles/7522860288407-Logi-Info-v14-2-Enhancements-#SSRM_-_Customized_Bit_Field_Format_in_Filter) | The conditional color filter logic was enhanced to consider the boolean format. |
| [Configure Data Values in Tooltip](https://devnet.logianalytics.com/hc/en-us/articles/7522860288407-Logi-Info-v14-2-Enhancements-#Data_Values_in_Tooltip) | You now have the ability to configure the tooltip to display values for any available column in the datalayer. |
| [Input Check Box List Item Count Search](https://devnet.logianalytics.com/hc/en-us/articles/7522860288407-Logi-Info-v14-2-Enhancements-#InputCheckbox_List_Item_Count_Search) | You can now dynamically control the Input Check Box List search box visibility based on the current item count. |
| [SSRM/AG - Display Values for Additional Columns](https://devnet.logianalytics.com/hc/en-us/articles/7522860288407-Logi-Info-v14-2-Enhancements-#Additional_Column_Show_Value) | Charts that utilize an Additional Column can now display their value on the chart. |
| [Enhanced Charting Capabilities](https://devnet.logianalytics.com/hc/en-us/articles/7522860288407-Logi-Info-v14-2-Enhancements-#Enhanced_Charting_Capabilities) | This release offers enhanced functionality of the latest charting library, new attributes, and modules to customize chart behavior. |
| Oracle 19c | Logi Info and SSRM now support Oracle 19c databases. |
| Control Aggregate Join Exclusion | Developers can now control automatic join exclusion for aggregates in ActiveSQL at the application level using the constant rdActiveSqlAggregateJoinExclusion. |
| SSRM - Set Default Time Zone | SSRM v14.0 introduced the ability to customize the time zone when scheduling reports. Now, you can set a default time zone for your scheduled reports using Template Modifier Files (TMF). |
| SSRM - No Data Access Permission | Your dashboard now displays a unified error prompt when you do not have the necessary data access permissions. |

## Logi Info v14.2 Resolved Issues

| Title | Description |
| --- | --- |
| Action.Refresh | Values containing special characters in the Link Parameters are no longer cut when the parameter is passed through Action.Refresh and the Action element is located underneath a table column. |
| W3Schools Links | The W3Schools links in the Analysis Grid formula help page no longer return a 404 error when using SQL Server. |
| Web Services | There is no longer a memory leak when accessing Web Services via a built-in Logi DataLayer connector. |
| SSRM - Report Author | The Report Author Color Picker pop-up now renders in the correct position in v12.7. |
| SSRM - Analysis Grid Template Modifier Files | Analysis Grid Template Modifier Files are now applied properly after refreshing existing bookmarks. |
| SSRM - Local Data | Local data in Dashboard is no longer called twice when running on an SSRM application. |
| Studio Documentation Links | All documentation links from Logi Studio v12.8 SP3 and v14 now resolve correctly. |
| Procedure.Export | Adding more than one Procedure.Export elements underneath a Procedure.If element no longer returns an ‘Object reference not set to an instance of an object’ error when the process is run with the Scheduler. |
| AG - CSV and Excel Exports | Certain edge case scenarios in Java environments no longer receive a null pointer exception error trace appended to CSV and Excel exports from the Analysis Grid. |
| Tokenized Colors | Tokenized colors now work in the legend's color box when the Crosstab chart has only one Crosstab Value column. |
| Y-Axis | Y-Axis now displays values with <abbr></abbr> tags. |
| AG - Resizing Columns | You no longer receive an error when resizing Analysis Grid columns on a touch screen device. |
| Google Fonts | Exporting a report that uses Google Fonts now renders the Java PDF page number/count correctly. |
| DataLayer.SQL | DataLayer.SQL using an OLAP connection no longer returns the following error message: This version of DataLayer.ActiveSQL does not currently support OLAP syntax. |
| macOS BigSur | .Net and Java versions now behave the same when downloading CSVs with Safari on macOS BigSur. |
| AG - Saved File | You no longer receive the error 'StartIndex cannot be less than zero.' when trying to load a saved Analysis Grid file that you do not have the security rights to view. |
| Procedure.Copy | Procedure.Copy file is now listed as a possible child element of Procedure.If and Procedure.Else. |
| ShowMode | Multiple maps in a popup panel with one ShowMode division set as ‘None’ now render properly. Additionally, you can now show the hidden map by switching to Action.Show without receiving a JavaScript error in the FusionCharts library. |
| DataColumnSummary | DataColumnSummary element values now display the SummaryRow and HeaderRow, as expected. |
| Reports | Info no longer displays XSLT compile errors when you run reports containing a Dashboard and Crosstab. |
| AG - Crosstab Summary | The Crosstab Summary function no longer causes the table to disappear. |
| Scheduled Tasks | Upgrading to Info v14.1 no longer causes your scheduled tasks to fail with a 500 internal error. |
| AG - Custom Aggregation | The Custom Aggregation function pop-up window no longer returns an error for defined formulas when using a @Session token in the Connection ID to dictate the source of the query. |
| Wait Panel | You can now view the Wait Panel on both Target.Report and in the General element in the \_Settings file, when Crawler Friendly is set to True while working with Action.Report. |
| Event Element ID Filter | The Event Element ID Filter attribute now works as expected. |
| PD4ML Tags | You can no longer add and execute PD4ML tags in column names, as they have been disabled by the engine. |
| AG - Colors | Colors set using Template Modifier Files are no longer overwritten by goVisual and goReport. |
| Resizable Columns | Updated column widths no longer revert after a page refresh. |
| Metadata | Info no longer displays an error when using a plugin that creates metadata files based on a user's security group. |
| AG - Filters | Filters are now applied to subsequent pages in an Analysis Grid, as expected. |
| Global Filters | Case-sensitive attributes in the Analysis filter now work with global filters, as expected. |
| MoreInfoRow | You can now close inputDate when editing a date in the MoreInfoRow element. |
| Input Check Box List | You no longer receive an error when using the default request parameter for Input Check Box List. |
| Rapid Excel Export Token Resolution | Rapid Excel Export now supports token resolution. |
| Thumbnails | Thumbnails now work with File to Database Mapping-stored visuals after the application is deployed elsewhere, as expected. |
| AG - Count Aggregate Function | The count aggregate function now displays the correct value at both the group and table level. |
