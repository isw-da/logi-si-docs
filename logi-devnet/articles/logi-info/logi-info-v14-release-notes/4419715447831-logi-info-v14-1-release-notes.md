---
title: "Logi Info v14.1 Release Notes"
id: 4419715447831
section: "Logi Info v14 Release Notes"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419715447831-Logi-Info-v14-1-Release-Notes
updated_at: 2022-09-01T14:52:18Z
---

# Logi Info v14.1 Release Notes

# Logi Info v14.1 Release Notes

Please select the following link to view a Chrome browser update likely to affect all Info customers this year: [Critical Chrome Browser Update](https://devnet.logianalytics.com/hc/en-us/articles/4415831044375).

This topic describes feature enhancements, resolved issues, and important information for Logi Info v14.1, released on January 24th, 2022.

NOTE: If you upgrade an existing installation of one of our products, or an existing Logi application, from one major version to another major version, for example v12 to v14.0, you will need a new license key and file for the new product/application. If you have an active maintenance contract with Logi, we've already created licenses for your license point of contact, which you can find on DevNet by selecting **Support > License Manager**. Contact [Customer Service](mailto:CustomerService@LogiAnalytics.com) if you want to upgrade and need a new license.

To purchase this product, contact [US Sales](mailto:salesteam@logianalytics.com?subject=I%20am%20interested%20in%20purchasing%20this%20product,%20please%20contact%20me. "US Sales email address.") or [UK Sales](mailto:emea_sales@logianalytics.com?subject=I%20am%20interested%20in%20purchasing%20this%20product.%20Please%20contact%20me. "Email address for UK sales team.").

* [Logi Info v14.1 Service Pack 4 Resolved Issues](#h_01GAKYYZ6RKMGK3ZRFQXWKMDB6)
* [Logi Info v14.1 Service Pack 3 Resolved Issues](#Logi_Info_v14.1_Service_Pack_3_Resolved_Issues)
* [Logi Info v14.1 Service Pack 2 Resolved Issues](#Logi_Info_v14.1_Service_Pack_2_Resolved_Issues)
* [Logi Info v14.1 Service Pack 1 Resolved Issues](#Logi_Info_v14.1_Service_Pack_1_Release_Notes)
* [Logi Info v14.1 Feature Enhancements](#Feature "List of Enhancements in this release.")
* [Logi Info v14.1 Resolved Issues](#Resolved "List of Bug Fixes and other problems resolved in this release.")

To view the Release Notes for this product version, along with previous product versions, see the [Info Release Notes page](https://clm.logianalytics.com/rdPage.aspx?rdReport=RelNotesINF).

## Logi Info v14.1 Service Pack 4 Resolved Issues

| Title | Description |
| --- | --- |
| Procedure.Export Element | Adding more than one Procedure.Export elements underneath a Procedure.If element no longer causes an ‘Object reference not set to an instance of an object’ error when the Process runs with the scheduler. |
| AG - Aggregate Filter | You no longer receive an error when configuring an Aggregate Filter in your Analysis Grid. |
| AG - Elements | Setting the rdAgDisableExcelAutoFormats constant to ‘True’ saves the ExcelFormat attribute of the ExcelColumnFormat element, as expected. |
| AG - Filters | Filters now display correctly when used in a new visual that was created by duplicating and editing an existing analysis. |
| Dashboard | Adding a chart to your Dashboard no longer returns an error. |
| Java Plugin | You no longer receive a Java Plugin error when updating to Logi Info v14. |
| AG - simpleReplace Filter | The simpleReplace filter function no longer displays a ‘Bookmark file not found’ error message when opening a shared Analysis Grid. |
| SSRM - Bookmark Organizer | The Bookmark Organizer folder no longer returns an AJAX error when a Report Title with special characters has a Scheduler. |

## Logi Info v14.1 Service Pack 3 Resolved Issues

| Title | Description |
| --- | --- |
| Java PDF | When exporting to PDF in Java instances, the column names now appear as static text, as expected. |
| AG - Crosstab Summary | The Crosstab Summary function no longer causes the table to disappear. |

## Logi Info v14.1 Service Pack 2 Resolved Issues

| Title | Description |
| --- | --- |
| Scheduled Tasks | You no longer receive a 500 internal error when running scheduled tasks in Info v14.1. |
| AG - Request Tokens | Set the constant rdAgRefreshSqlTokens to ‘False’ to prevent @Request tokens in the SQL query from being refreshed after the initial load. |
| Info License | The Info license grace period warning message no longer causes an invalid XHTML error on AJAX refresh calls. Adding elements to the visual gallery, sharing reports, and other actions no longer result in this error. |
| Bar Chart Label | The flame emoji now renders correctly in the label of a Bar Chart using a JSON datalayer. |
| AG - Resizing | You no longer receive an error when resizing Analysis Grid columns on a touch screen device. |
| Well-Known Text (WKT) | Well-Known Text (WKT) within the GoogleMapPolygons and GoogleMapPolylines elements now displays properly. |

## Logi Info v14.1 Service Pack 1 Resolved Issues

| Title | Description |
| --- | --- |
| AG - Saved File | You no longer receive the error ‘StartIndex cannot be less than zero’ when trying to load a saved Analysis Grid file. |
| DevNet Information Panel | The Logi Studio DevNet Information Panel now displays, as expected. |
| SSRM - Chart Label Color | The color value is now retained when you type in the color for a chart’s label. |
| SSRM - Local Data | Local data in a Dashboard is no longer called twice when running on an SSRM application. |
| Reports | Info no longer displays XSLT compile errors when you run reports containing a Dashboard and Crosstab. |
| DataColumnSummary Element | DataColumnSummary element values now display the SummaryRow and HeaderRow, as expected. |
| DataLayer.SQL | DataLayer.SQL using an OLAP connection no longer returns the following error: ‘This version of DataLayer.ActiveSQL does not currently support OLAP syntax.' |

## Logi Info v14.1 Feature Enhancements

| Title | Description |
| --- | --- |
| [Bookmark Confirmation](https://devnet.logianalytics.com/hc/en-us/articles/4419723128599-Logi-Info-v14-1-Enhancements#Bookmark_Confirmation) | A confirmation dialog now notifies report consumers that a bookmark they are deleting has an existing schedule. |
| [SSRM - Batch Duplicate Bookmarks](https://devnet.logianalytics.com/hc/en-us/articles/4419723128599-Logi-Info-v14-1-Enhancements#SSRM_-_Batch_Duplicate_Bookmarks) | A new constant, goAllowBatchBookmarkDuplication, controls the ability to use our new batch duplicate feature, which allows Self-Service users to batch duplicate bookmarks in their original folder. |
| [DataLayer.REST Support Pagination](https://devnet.logianalytics.com/hc/en-us/articles/4419723128599-Logi-Info-v14-1-Enhancements#Datalayer.REST_Support_Pagination) | As a report developer, you can now utilize result pagination from your restful data source. |
| [REST Call Response](https://devnet.logianalytics.com/hc/en-us/articles/4419723128599-Logi-Info-v14-1-Enhancements#REST_Call_Response) | As a report developer, you can now access detailed error information from the response content of the REST call. |
| [DataLayer Error Tokens](https://devnet.logianalytics.com/hc/en-us/articles/4419723128599-Logi-Info-v14-1-Enhancements#DataLayer_If_Data_Error) | Developers can now retrieve error messages using the "If Data Error" element and capture all of the error information in the new token element, @DataLayerError. |
| [SSRM/AG - Edit Labels and Captions in Charts](https://devnet.logianalytics.com/hc/en-us/articles/4419723128599-Logi-Info-v14-1-Enhancements#Edit_Labels_and_Captions_in_SSRM_Charts) | You can now customize the label format and edit captions for the X and Y-axis associated with your Analysis Grid or SSRM charts. |
| [SSRM - Crosstab Grouping](https://devnet.logianalytics.com/hc/en-us/articles/4419723128599-Logi-Info-v14-1-Enhancements#SSRM_-_Secondary_Label_Column) | SSRM now supports multiple grouping on Crosstabs via the Secondary Label Column. |
| [SSRM - Characters in Email Addresses](https://devnet.logianalytics.com/hc/en-us/articles/4419723128599-Logi-Info-v14-1-Enhancements#SSRM_-_Single_Quotes_in_Email_Field) | Scheduler now supports email addresses following RFC 5322. The following characters are fully tested: !#$%&'+-^`~ |
| [Data Table Enhancements](https://devnet.logianalytics.com/hc/en-us/articles/4419723128599-Logi-Info-v14-1-Enhancements#Data_Table_Enhancements) | Data Table introduces a new attribute, 'No Data Caption', and sub-element, 'No Data Caption Style', that assign a specific text and style to indicate that there is no data available for a given Data Table. Additionally, the value "Scrollbar" was added to the Caption Type attribute to enable scrolling and lock Data Table column headers. |
| [Enhanced Charting Capabilities](https://devnet.logianalytics.com/hc/en-us/articles/4419723128599-Logi-Info-v14-1-Enhancements#Enhanced_Charting_Capabilities) | As a report developer, you can now customize your Chart Canvas to add gradients using CSS in styled mode, specify how many ticks are rendered on your chart axes, and enable tick auto rotation to prevent overlapping labels on your horizontal axis. |
| [AG - Cell Colors for Group Aggregate Values](https://devnet.logianalytics.com/hc/en-us/articles/4419723128599-Logi-Info-v14-1-Enhancements#AG_-_Cell_Colors_for_Group_Aggregate_Values) | Analysis Grid now offers the ability to format cell colors at the group level. |
| [Chart Canvas Series.Pie Custom Data Values](https://devnet.logianalytics.com/hc/en-us/articles/4419723128599-Logi-Info-v14-1-Enhancements#Chart_Canvas_Series.Pie_Custom_Data_Values) | Your Series.Pie chart can now be configured to display two data values simultaneously. |
| [HTML Attributes Params](https://devnet.logianalytics.com/hc/en-us/articles/4419723128599-Logi-Info-v14-1-Enhancements#Additional_HTML_Attributes_Tags) | As a report developer, you can now add HTML Attribute Params to Crosstab, Data Table, Data Table Columns, and User Input elements to apply your application to work with other framework or libraries easier. |
| [Performance Improvements](https://devnet.logianalytics.com/hc/en-us/articles/4419723128599-Logi-Info-v14-1-Enhancements#Performance_Improvements) | Load time improved with Bookmarks, Global Filters, and Dashboards. We also introduce a new metadata caching mechanism so that visualizations using the same metadata can be verified by a single shared and cached metadata. |
| Open Edge Upgrade | Logi Info and SSRM are now certified with Progress Open Edge 12.2. |
| [New for 14.1 Sharing Permissions](https://devnet.logianalytics.com/hc/en-us/articles/4419723011735-Sharing-Bookmarks#Sharing_Permissions) | As a content creator, you can now manage access for content shared with other users. To enable sharing, set the constant goSharePermissionEnable to "True". As a self-service user, you now have the ability to interact, schedule, and filter the content being shared with you. |

## Logi Info v14.1 Resolved Issues

| Title | Description |
| --- | --- |
| Animated Maps | Animated maps inside pop-up panels now render correctly. |
| Animated Maps | Animated maps now work appropriately when accessed via a @Chart token. |
| Action.Report | Action.Report now functions as expected on Animated Maps. |
| Chrome 92 | All JavaScript dialogs (alert, confirm, and prompt) have been replaced with custom dialogs to enable iFrame compatibility with the latest version of Chrome. |
| SSRM - Analysis Charts and Tables | Analysis Charts and Tables no longer return different results when using inner joins containing grouping and distinct count. |
| Datalayer.Linked Removal | DataLayer.Linked is not longer a child element of ChartCanvas and the various Series elements. |
| DataCalendar | DataCalendar no longer ignores Data Calendar Date in the calendar display when the Time Period is set to Week with interactive paging. |
| Internet Explorer 11/Edge | The ‘Save’ button in the Save Bookmark dialog window now works when using Internet Explorer 11/Edge. |
| SSRM - Pie Charts | Adding Pie Charts to reports and Dashboards with Custom Format values now retains the values. |
| AG - Adding Filters | Adding an additional filter after exporting your Analysis Grid no longer returns a JSON error. |
| Column Span | ColumnSpanFirst and ColumnSpanLast in More Info Row supports both @Data and non-@Data tokens, as expected. |
| Wait Panel | The wait panel now appears, as expected, when a sub-report contains an action button in a pop-up window. |
| Bookmark Formulas | Editing a formula in your bookmark and reopening the same bookmark no longer returns a “One or more columns is unavailable” error. |
| Selection Event | Using InputSelectionEvent.Point with the Selection Event applied no longer prevents Link Parameters from being resolved. |
| SSRM - Tables | You can now use two tables with the same column name and select a column from the Formula tab that displays the correct value. |
| SSRM - Formula Removal Error Message | Removing a formula that is used in another formula now prompts the following error message: Cannot remove this column. Used in a formula. |
| AG - Data | The most recent data now displays accordingly when updating an existing Analysis Grid. |
| Scheduler | Logi Scheduler no longer creates a new database connection for each attempt when the task table schema is incorrect. |
| Cross-Domain Embedding | The CORS issue with rdScript.min.js for cross-domain embedded Logi Info applications using 14.0 SP1 was resolved. |
| DataColumns | You no longer receive an ‘Index was outside the bounds of the array' error when exporting reports with DataColumns in the group header row that exceed 11. |
| SSRM - Shared Bookmarks | Export and Add to Gallery options are now available for shared bookmarks. |
| SSRM - Select Data Combo Box | Selecting the ‘Apply Column Selection’ button no longer generates duplicate values in the second combo box when creating a new Analysis. |
| REST Connection | You no longer receive the error ‘The request was aborted: Could not create SSL/TLS secure channel’ when attempting to connect to an HTTPS enabled REST endpoint. |
| Joins | The Friendly Name of the join in the live metadata now takes precedence in the Select Data drop-down when creating a new Analysis with Joins. |
| CORS Error | You no longer receive a CORS error triggered by getTextDimensions when using ‘inputCheckboxList’ in an embedded application. |
| AG - Data Columns | Data columns with special characters (like &) in the Friendly Column Name no longer return an XSL parse error in the Analysis Grid. |
| AG - Loading Icon | The Analysis Grid now displays a loading icon while opening or updating a chart, as expected. |
| SSRM - Aggregate Filter | You no longer receive an error when adding an Aggregate Filter while using a custom query. |
| Cell Bar | The Cell bar now displays the correct value range when using a Crosstab, Group Filter, and Sort Filter in your datalayer. |
| REST Connection | You no longer receive the error ‘The request was aborted: Could not create SSL/TLS secure channel’ when attempting to connect to an HTTPS enabled REST endpoint. |
| SSRM - Crosstab Tables | Crosstab Tables now match the behavior of Data Tables by removing Summary Rows when there is no data. |
| Request Forwarding | Request Forwarding now works as intended when passing a multi-select Input Select List of values. |
| DataLayer.Web Scraper | You no longer receive an error when using DataLayer.Web Scraper. |
| AG - Analysis Grid Filters | Dashboard panel content no longer adds unwanted filters when creating or editing an Analysis Grid with filters. |
| Procedure.SQL | Procedure.SQL functionality was repaired to produce @Request token values properly. |
| AG - Global Chart Export | The accurate title now displays when exporting Analysis Grid charts to image files using Global Chart Export. |
| AG - Gauge Number | The Gauge number no longer displays inconsistent data when using a Join data set. |
| AG - Gauge Number | The HTML caption for Gauge numbers now work as expected. |
| MongoDB Aggregates | The logic for processing aggregates in MongoDB using the DataLayer.Run command element was enhanced to support different aggregate results. |
| Globalization Element | The correct date now displays when Java users export to Excel using the Globalization element. |
| ResizeableColumns | Dashboard tables with ResizeableColumns in the first tab no longer shrink when moving between tabs. |
| Excel Column Format | When using Tomat and Linux, Excel column format now displays dates as MM/YYYY, as expected. |
| Rapid Export | The rdFileDownloadComplete cookie is no longer retained after exporting via Rapid Export, enabling your downloads to display the wait page. |
| Chart Canvas Charts | Chart Canvas Charts that use a linked datalayer from a local data element can now utilize cross-origin access for embedded reports at the external level. |
| SSRM - Export to Excel | Exporting a table to Excel with an empty or null value no longer displays an ‘Ascii160’ text in the empty column. |
