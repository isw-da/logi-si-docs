---
title: "Logi Info v12.8 Enhancements "
id: 4406822488471
section: "Release Notes - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406822488471-Logi-Info-v12-8-Enhancements
updated_at: 2022-04-06T06:10:44Z
---

# Logi Info v12.8 Enhancements 

# Logi Info v12.8 Enhancements

This topic introduces the significant features of Logi Info in this release:

* [Drill To Dashboard Capability](#Drill_To_Dashboard_Capability)
* [Rapid Excel/CSV Export](#Rapid_Excel/CSV_Export)
* [Support FIPS Compatible Algorithm for Obfuscation](#Support_FIPS_Compatible_Algorithm_for_Obfuscation)
* [508 PDF Framework Support (.Net and Java)](#508_PDF_Framework_Support_(.Net))
* [Function.AppPhysicalPath](#Function.AppPhysicalPath)
* ["Like" and "Not Like" Filters](#%22Like%22_and_%22Not_Like%22_Filters)
* ["Current Hour" and "Last Hour" Sliding Filters](#%22Current_Hour%22_and_%22Last_Hour%22_Sliding_Filters)
* [Automated Cleanup of Scheduler Logs](#Automated_Cleanup_of_Scheduler_Logs)
* [Scheduler Error Notifications](#Scheduler_Error_Notifications)
* [Scheduler Custom Table and Schema](#Scheduler_Custom_Table_and_Schema)
* [Stacked Percentage Series Value](#Stacked_Percentage_Series_Value)
* [AutoComplete Search](#AutoComplete_Search)
* [Shared Notification](#Shared_Folders__Notification)
* [Folder Item Count](#Folder_Item_Count)
* [Copy XPath](#Copy_XPath)
* [Chart Canvas Legend Show All Caption](#Chart_Canvas_Legend_Show_All_Caption)
* [Radio Button Save in Local Storage](#Radio_Button_Save_in_Local_Storage)
* [SSRM - Sharing with UserId, Searching by Name](#SSRM_-_Sharing_with_UserId,_Searching_by_Name)
* [SSRM- Author Report Export to Excel](#SSRM-_Author_Report_Export_to_Excel)
* [Input Check Box List Search Capability](#Input_check%20boxlist_Search_Capability)
* [Custom Aggregation Select All](#Custom_Aggregation_Select_All)
* [Multiple Conditional Group Filters](#Multiple_Conditional_Group_Filters)
* [Group Summary Row -Append Blank Rows](#Group_Summary_Row_-Append_Blank_Rows)
* [MultiPolygon Support - WKT Format](#MultiPolygon_Support_-_WKT_Format)
* [Support for Log4Net and Log4J](#Log4Net_Support_for_.Net)
* [Support Windows Server 2019](#Support_Windows_2019)
* [Chart Angular Container Sizing](#Chart_Angular_Container_Sizing)
* [What's Fixed?](#What's_Fixed?)

## Drill To Dashboard Capability

You can now drill into Dashboards in SSRM to gain a deeper insight of the data, without leaving the context of the Dashboard Author. The Drill To feature is useful when reviewing underlying data, which makes up the aggregated number, to answer questions like: of my National sales figures, which states are performing better in the United States, and within each state, which territories are driving revenue?

![](https://devnet.logianalytics.com/hc/article_attachments/5263096689047/noteicon.png) This feature is optional and only available in the Dashboard Author, not the Report Author.

![](https://devnet.logianalytics.com/hc/article_attachments/5263089436311/select_drill_to.png)

The Drill To feature is available for the following charts:

* Bar
* Pie- date columns cannot be added
* Heat Map- date columns cannot be added

The Drill To path displays as a breadcrumb menu at the top of the panel. If there is not enough space on the chart, the breadcrumb menu will show the first and last node with an ellipses. Additionally, if you re-size the chart, the breadcrumb menu will automatically adjust the Drill To path to reflect these changes.

![](https://devnet.logianalytics.com/hc/article_attachments/5263067987479/select_ellipses.png)

When editing a visualization from the Dashboard, Info keeps your Drill To State intact as long as there are no changes made to the column currently used by the chart. For example, if your chart displays Freight x Order Date and you edit the visualization to display Freight Sum instead of Freight Average, the breadcrumb menu remains intact. However, if you edit the visualization to display Ship Region x Freight, Info resets the breadcrumb menu.

For more information, see [Drill To Dashboard Data](https://devnet.logianalytics.com/hc/en-us/articles/4406817240471-Drill-To-Dashboard-Data).

This feature is enabled by default. To disable the ability to drill to dashboard, set the constant "ChartCanvasAutoDrillTo" value to "False". For more information, see [Configuring InfoGo Constants](https://devnet.logianalytics.com/hc/en-us/articles/4406822192535-Configuring-InfoGo-Constants).

## Rapid Excel/CSV Export

A new Rapid Excel Export option is available in the Data Table and Analysis Grid in Info Studio. Use this feature if you are a Consumer or Self-Service user who exports tabular data in Excel and CSV format for further analysis outside of Info. In comparison to the existing Native Excel option, the Rapid Export option greatly improves the performance of exporting large data. This new feature honors basic formatting (bold, font, italics, etc), but it does not apply custom styling or group aggregation.

Currently, we provide a plug-in, but in order to use it you have to make changes in the Info application and compile it on .NET or Java. In Info Studio, you can set the new attribute on the Target .NativeExcel and Target.CSV elements called "Export Data Preference" (Formatted/Empty {default} | Rapid ), as shown here:

![](https://devnet.logianalytics.com/hc/article_attachments/5263089455127/export_excel1.png)

In SSRM/Infogo, there is a global constant "rdExportDataPreference" in the \_Settings file, as shown below, that you can set to export data preference on an application level.

![](https://devnet.logianalytics.com/hc/article_attachments/5263107106839/rapid_export.png)

Notes:

* You cannot set this global constant on a per report/bookmark level.
* You cannot export a report with more than one Data Table.

For more information, see [Rapid Excel Export](https://devnet.logianalytics.com/hc/en-us/articles/4406822485527-Rapid-Excel-Export) and [Rapid CSV Export](https://devnet.logianalytics.com/hc/en-us/articles/4406817807383-Rapid-CSV-Export).

## Support FIPS Compatible Algorithm for Obfuscation

Application Obfuscation is now compatible with Federal Information Processing Standards (FIPS) security in .NET environments. With this enhancement, LogiObfuscate can encrypt reports, whether or not FIPS encryption is enabled.

For more information, see [Obfuscating Definitions](https://devnet.logianalytics.com/hc/en-us/articles/4406818012055-Obfuscating-Definitions).

## 508 PDF Framework Support (.Net and Java)

You now have the ability to add accessibility tagging within PDF outputs, per section 508 guidelines. The options you can set include: images, labels, and paragraphs of the exported document.

For more information, see [Accessible Logi Applications](https://devnet.logianalytics.com/hc/en-us/articles/4406816897559-Accessible-Logi-Applications).

## Function.AppPhysicalPath

You can now call plugins within the application directory by setting the path as @Function.AppPhysicalPath~/.
You can also use other tokens, such as @Request, @Sessions, and @Constant, to call plugins within the application directory by setting the path.

For more information on this enhancement, see [DataLayer.Plugin](https://devnet.logianalytics.com/hc/en-us/articles/4406816911767-DataLayer-Plugin).

## "Like" and "Not Like" Filters

When you use the Compare Filter, "Like" and "Not Like" now display in the drop-down list of Compare Types. This feature makes filtering data in the Analysis Grid more efficient by narrowing down values that are like, or not like, the comparison. By using this filter, the value of the selected column is checked. If it returns True, the corresponding record will remain. Otherwise, Info discards the record.

For more information, see [Compare Filter Attributes](https://devnet.logianalytics.com/hc/en-us/articles/4406817186967-Compare-Filter-Attributes).

## "Current Hour" and "Last Hour" Sliding Filters

When you use the Analysis Grid DateTime column, sliding filters now include "Current hour", as well as "Last hour". Previously, you could not configure chart function and crosstab function time intervals in Logi SSRM by less than the current day. Now, when you select the DateTime columm for the "Filter Columns" and choose "Sliding Date" from the Value Column, the second select drop-down list contains the additional values "Current hour" and "Last hour".

For more information, see [Analysis Grid - Filtering Rows](https://devnet.logianalytics.com/hc/en-us/articles/4406822101271-Analysis-Grid-Filtering-Rows).

## Automated Cleanup of Scheduler Logs

You can now incorporate three attributes into the scheduler settings file to automate the cleanup of Scheduler logs: rdCleanUpSchedulerLog, rdSchedulerLogCleanupInterval, and rdSchdulerLogLifespan. The "rdCleanUpSchedulerLog" attribute enables or disables the Scheduler Log clean up. The default value of this constant is "False", no clean up of Scheduler Logs. If you want to automate the clean up logs from the scheduler, set this value to "True". The "rdSchedulerLogCleanupInterval" attribute is triggered by scheduler pings. The Default Value of this interval is 5 and the unit of measurement is minutes. The "rdSchedulerLogLifespan" attribute accounts for the minimum file age, in minutes, before a file qualifies to be deleted when the clean up runs. The default value for this attribute is 60, and the unit of measurement is minutes.

For more information, see [Scheduler Results and Logging](https://devnet.logianalytics.com/hc/en-us/articles/4406818027287-Scheduler-Results-and-Logging).

## Scheduler Error Notifications

If you are a Self-Service administrator who schedules reports to be sent out through SSRM scheduling, Info can now notify you when there is an error. This feature enables you to proactively respond to scheduler or report errors. ​ If the Scheduler service has access to @Session error messages, you can use that to write custom logic accordingly.

You can enable this feature by adding the constant "SchedulerErrorEmail" in application \_Settings. The value of this constant is the admin's email address; however, multiple addresses are supported, separated by ";". If there is no constant or the value is empty, Info disables this function.

Note: If the receiving email address is invalid, the error will be also logged in Scheduler task log file and Info does not send the error message email.

Info uses the first SMTP connection in application \_Settings to send an error message email. If there is no SMTP connection, Info logs an error in the Scheduler task log file.

You can customize error message email content (send and receive email address, subject, body) by creating DMF rdWeb1/\_SupportFiles/rdSchedulerEmail\_DMF.xml Initial content can be customized like this:

<ScheduleMods>

<SetAttribute XPath="." AttributeName="EmailSubject" Value="Failed to schedule task" />

<SetAttribute XPath="." AttributeName="EmailBody" Value="Error message: " />

<SetAttribute XPath="." AttributeName="FromEmailAddress" Value="" />

<SetAttribute XPath="." AttributeName="ToEmailAddress" Value="" />

</ScheduleMods>

For more information, see [Scheduler Results and Logging](https://devnet.logianalytics.com/hc/en-us/articles/4406818027287-Scheduler-Results-and-Logging).

## Scheduler Custom Table and Schema

If you do not want to use the default table "Tasks", you have the option to use a custom table and schema in your database. First you must add two new attributes, "Schema" and "Table", to the Connection element via the settings file: %LogiXML Scheduler ServiceHome%/\_Settings.lgx.

Note: By default, no Connection element is required. Java installations default to the embedded Derby database and DotNet installations default to the embedded VistaDB database.

If you want to use a networked database, then a Connection element is necessary. Choose one of the elements (Schema or Table) and supply the necessary local information. Place it inside the <Setting></Setting> tag to activate it, for example:

![](https://devnet.logianalytics.com/hc/article_attachments/5263068038423/custom_table__1041x537.png)

For MYSQL Server, Oracle, SQL Server, and PostgreSQL sample connections, see [Scheduled Task Data Storage Options](https://devnet.logianalytics.com/hc/en-us/articles/4406818026135-Scheduled-Task-Data-Storage-Options).

## Stacked Percentage Series Value

You can now use the @Chart.rdStackedChartPercentage~ token to show the percentage of stacked Bar Charts and Crosstab Charts. With this token, each bar that has stacking set to "StackedPercentage" will display the percentage when hovered over. Info displays the format of the percentage according to the property in the QuickTipRow. If the format is empty, Info uses the default format "Percent" (0.00%).

![](https://devnet.logianalytics.com/hc/article_attachments/5263107141271/stacked_percentage1.png)

For more information, see [Series.Bar - Using the Quicktips Element](https://devnet.logianalytics.com/hc/en-us/articles/4406817058199-Series-Bar-Using-the-Quicktips-Element).

## AutoComplete Search

AutoComplete can now be set to begin searching only after X number of characters have been typed. The number of characters is configurable by adding a value in the "Minimum Length" attribute. Currently, the Auto Complete starts to search after the first character is typed, causing the system to return more items than necessary and lowering performance. With this enhancement, you have the option to configure the number of characters entered to trigger the items returned, enabling a quicker, more efficient search.

![](https://devnet.logianalytics.com/hc/article_attachments/5263107144215/min1.png)

For more information, see [Using AutoComplete](https://devnet.logianalytics.com/hc/en-us/articles/4406822665879-Using-AutoComplete).

## Shared Notification

If your application has been configured for it, Info now notifies you if a new item has been shared with you since the last session:

![](https://devnet.logianalytics.com/hc/article_attachments/5263107150359/new_bell_icon5.png)

Select the bell icon to see information about the Author sharing the changes, as well as a time stamp and link. To access the item, select the link:

![](https://devnet.logianalytics.com/hc/article_attachments/5263089492759/actionable_notification_folder_share3.png)

For more information, see [Sharing Bookmark Folders](https://devnet.logianalytics.com/hc/en-us/articles/4406822407959-Sharing-Bookmark-Folders).

Disable this feature by setting the new constant, goNotificationsEnabled, to 'False' in Studio. The default value for this constant is 'True'. For more information about configuration, see [Configuring InfoGo Constants](https://devnet.logianalytics.com/hc/en-us/articles/4406822192535-Configuring-InfoGo-Constants).

## Folder Item Count

You now have the option to display a folder count for each folder listed on your SSRM Home page (My Items, My Visualizations, Global Menu, and Shared with Me). Enable this feature by setting the "goBookmarkShowItemCount" attribute to "True":

![](https://devnet.logianalytics.com/hc/article_attachments/5263068073111/bookmark_show_item_count.png)

Note: By default, the value for this constant is "False".

Sub-folders show item counts, as well. However, parent folders show their own number, not including the items from its sub folder. Info updates this number automatically when a new item gets added to or deleted from the specific folder.

![](https://devnet.logianalytics.com/hc/article_attachments/5263107176983/show_item_count_new_371x305.png)

For more information about the SSRM folder counts, see [InfoGo - Home Page](https://devnet.logianalytics.com/hc/en-us/articles/4406817957783-InfoGo-Home-Page) or [Configuring InfoGo Constants](https://devnet.logianalytics.com/hc/en-us/articles/4406822192535-Configuring-InfoGo-Constants).

In Studio, two new, optional attributes represent this new feature via BookmarkOrganizer: "BookmarkDatalayerLinkID" and "ShowItemCount". By default, the "BookmarkDataLayerLinkID" attribute is empty, as shown below, and the Show Item Count works as usual. If "BookmarkDataLayerLinkID" has a value, the DataTable to which the DatalayerLink belongs to is the same as the DataTable specified by DataTableID.

![](https://devnet.logianalytics.com/hc/article_attachments/5263097463319/info_show_item_count_448x212.png)

![](https://devnet.logianalytics.com/hc/article_attachments/5263059448087/image_405x178.png)

For more information about configuring Info to display folder counts, see [Enable Item Counts](https://devnet.logianalytics.com/hc/en-us/articles/4406822404247-Enable-Item-Counts).

## Copy XPath

Finding the XPath of a particular element in a report or template is now easier than ever; just right-click the element and select "Copy XPath":

![](https://devnet.logianalytics.com/hc/article_attachments/5263059466775/copy_xpath.png)

Selecting this option directs Info to copy the direct XPath of that element, the tag name, and ID attribute (if available) to the Clipboard, which you can then use in a Template Modifier File.

For more information, see [Using XPath Notation](https://devnet.logianalytics.com/hc/en-us/articles/4406822533527-Using-XPath-Notation).

## Chart Canvas Legend Show All Caption

When you select legend items, Info refreshes the Chart Canvas element and changes the other appropriate legend objects' color attributes from HEX codes to "CCC", creating a dimmed appearance. By default, the legend filtering is set to "Show All," and in turn, the Show All feature is dimmed. As you select legend items to display in the chart, the Show All legend object will redisplay and become actionable:

![](https://devnet.logianalytics.com/hc/article_attachments/5263107244951/show_all_caption_642x396.png)

For more information, see [Legend Filtering](https://devnet.logianalytics.com/hc/en-us/articles/4406822107031-Legend-Filtering).

## Radio Button Save in Local Storage

The "Save in Local Storage" feature now supports the Radio Button Input Element. You can enable this feature with by setting the "SaveInLocalStorage" attribute to "True".

![](https://devnet.logianalytics.com/hc/article_attachments/5263096689047/noteicon.png) Values from LocalStorage are over-ridden by values in DefaultValue; therefore, you should not use LocalStorage and DefaultValue together.

![](https://devnet.logianalytics.com/hc/article_attachments/5263073273751/radio_button_store.png)

For more information, see [Re-displaying Entered Values](https://devnet.logianalytics.com/hc/en-us/articles/4406822664983-Re-displaying-Entered-Values).

## SSRM - Sharing with UserId, Searching by Name

The SharingCollectionDisplayColumn property was added to the SharingList element to enable the ability to search for users by their first/last name. The default value is empty, but you can set the property value in goCustomizations.goBookmarkSharingUserlist.lgx. If the property value is set to share in the pop-up panel, users can be found by their display name. Once shared, the display name is saved in the bookmark and reflected in the Shared With list. If the username corresponding to the found display name already exists in the Shared With list, and you attempt to re-share, you will be prompted "Already shared with XXX(displayname)".

For more information, see [Setting Up Sharing](https://devnet.logianalytics.com/hc/en-us/articles/4406817205143-Setting-Up-Sharing).

## SSRM- Author Report Export to Excel

As a Report author, you can now insert an export to Excel link into a report, like the existing export to PDF link does.

![](https://devnet.logianalytics.com/hc/article_attachments/5263089578391/new_excel_link_669x526.png)

The report downloads automatically, or will open within the browser, depending on your Excel application settings. Excel results will be HTML-based output.

For more information, see [Exporting Visuals](https://devnet.logianalytics.com/hc/en-us/articles/4406817814935-Exporting-Visuals).

## Input Check Box List Search Capability

The Input check box List is now searchable. If the check box List Dropdown attribute is set to *True*, then the drop-down element is rendered. When the drop-down is rendered, you can utilize the search feature via input box. The search will be performed every time the search content changes. Basic conditions are: ignoring case, not full word matching, and the search content will not be treated as regular.

![](https://devnet.logianalytics.com/hc/article_attachments/5263089583511/search_input_checkbox_list.png)

![](https://devnet.logianalytics.com/hc/article_attachments/5263059512983/search_input_checkbox_list_2.png)

For more information, see [Input Check Box List](https://devnet.logianalytics.com/hc/en-us/articles/4406817984151-Input-Check-Box-List).

## Custom Aggregation Select All

When working with data-specific custom aggregations, all custom aggregates for all columns are now available on the drop-down list when you edit any of the existing aggregates:

![](https://devnet.logianalytics.com/hc/article_attachments/5263068182679/select_data_types.png)

![](https://devnet.logianalytics.com/hc/article_attachments/5263096689047/noteicon.png) The @CurrentColumn will be replaced with the column on which it's being applied. Also, if the "Enable Aggregations" check box is cleared for a given column in the metadata, you will not be able to apply the custom aggregation to this column, regardless of where the Data Type matches.

For more information, see [Analysis Grid - Creating Custom Aggregations](https://devnet.logianalytics.com/hc/en-us/articles/4406816995479-Analysis-Grid-Creating-Custom-Aggregations).

## Multiple Conditional Group Filters

With this enhancement, the Include Condition will be checked prior to the datalayer. More than one group filter can be put under any level, specified by the attribute "IncludeCondition" for each group filter. This enhancement will allow the use of top-level Group Filter A if a condition is met or top-level Group Filter B if the condition is not met. For example, @Request.GroupColumn~ = 'City' or IncludeCondition =@Request.GroupColumn~ = 'Sales'. Once the Report is run without an error, there will be different grouping based on the given token value 'City' or 'Sales'.

![](https://devnet.logianalytics.com/hc/article_attachments/5263089594519/group_filter_replacement.png)

In this case, the token value set in the parameters was 'City' grouping the filter by City:

![](https://devnet.logianalytics.com/hc/article_attachments/5263097609239/filtered_list_replacement_255x168.png)

For more information, see [Conditional Grouping](https://devnet.logianalytics.com/hc/en-us/articles/4406822353687-Conditional-Grouping).

## Group Summary Row -Append Blank Rows

In a Data Table report, when Append Blank Rows to the Group Summary Row is set, the width of the newly added blank rows will be the same as the largest width in the existing Table Row.

For more information, see [Using Group Header and Group Summary Rows](https://devnet.logianalytics.com/hc/en-us/articles/4406817510295-Using-Group-Header-and-Group-Summary-Rows).

## MultiPolygon Support - WKT Format

You can now use maps with Well-Known Text (WKT) formatted polygons that are stored in the database, so that you can use them directly without extra steps to convert before the rendering. With this enhancement, GoogleMapPolygons and GoogleMapPolylines can now retrieve their coordinates from any DataLayer with the column rdCoordinates containing WKT formatted polygons and multipolygons.

![](https://devnet.logianalytics.com/hc/article_attachments/5263089614487/map_polygons.png)

Geocode Columns can also be used in DataLayers for Google Map Polygons and Google Map Polylines, to automatically obtain polygon data when used with a Nominatim connection.

For more information, see [Using Data from SQL Server](https://devnet.logianalytics.com/hc/en-us/articles/4406822465687-Using-Data-from-SQL-Server) or [Google Map Polylines](https://devnet.logianalytics.com/hc/en-us/articles/4406817486615-Google-Map-Polylines).

## Support for Log4Net and Log4J

You now have the flexibility to integrate modern logging framework for .Net and Java environments. With the use of two new attributes, "Enable Log4J Logging" and "Log4J Property Location", you can now pull all runtime error and debug information into log files directly.

Enable this feature by setting the attribute "Enable Log4J Logging" to "True" and entering a file location:

![](https://devnet.logianalytics.com/hc/article_attachments/5263068217879/enable_log4j_logging.png)

![](https://devnet.logianalytics.com/hc/article_attachments/5263068232855/log4j_property_location.png)

![](https://devnet.logianalytics.com/hc/article_attachments/5263096722455/criticalicon.png) You must update to Log4j v2.15 to mitigate this 0 day vulnerability. For more information about this vulnerability, refer to [this statement](https://devnet.logianalytics.com/hc/en-us/articles/4415781801751).

For more information, see [Using the Debugging Features](https://devnet.logianalytics.com/hc/en-us/articles/4406817357975-Using-the-Debugging-Features).

## Chart Angular Container Sizing

You can now customize the size of a Guage.Angular Chart by adjusting the "Gauge Size Adjustment" attribute:

![](https://devnet.logianalytics.com/hc/article_attachments/5263068283159/gauge.angular_1114x593.png)

The value displays in percent, with a default value of 85%, so a value of 100 leaves the gauge in its natural size. Use a value greater than 100 to have a portion of the gauge get pushed outside the gauge window, so it does not appear.

For more information, see [Gallery of Classic Chart and Gauge Elements](https://devnet.logianalytics.com/hc/en-us/articles/4406822444823-Gallery-of-Classes-Chart-and-Gauge-Elements).

## Support Windows Server 2019

Logi Info now supports Windows Server 2019 as a certified environment. For more information, see [Logi Apps General Requirements](https://devnet.logianalytics.com/hc/en-us/articles/4406816947479-Logi-Apps-General-Requirements).

## What's Fixed?

For information on bug fixes, please see [this page](https://clm.logianalytics.com/rdPage.aspx?rdReport=RelNotesINF).
