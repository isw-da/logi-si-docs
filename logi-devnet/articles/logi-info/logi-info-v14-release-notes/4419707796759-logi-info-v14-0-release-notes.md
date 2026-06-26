---
title: "Logi Info v14.0 Release Notes"
id: 4419707796759
section: "Logi Info v14 Release Notes"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419707796759-Logi-Info-v14-0-Release-Notes
updated_at: 2022-07-17T02:06:34Z
---

# Logi Info v14.0 Release Notes

# Logi Info v14.0 Release Notes

Please select the following link to view a Chrome browser update likely to affect all Info customers this year: [Critical Chrome Browser Update](https://devnet.logianalytics.com/hc/en-us/articles/4415831044375).

This topic describes feature enhancements, resolved issues, and important information for Logi Info v14.0, released on June 25th, 2021.

NOTE: If you upgrade an existing installation of one of our products, or an existing Logi application, from one major version to another major version, for example v12 to v14.0, you will need a new license key and file for the new product/application. If you have an active maintenance contract with Logi, we've already created licenses for your license point of contact, which you can find on DevNet by selecting **Support > License Manager**. Contact [Customer Service](mailto:CustomerService@LogiAnalytics.com) if you want to upgrade and need a new license.

To purchase this product, contact [US Sales](mailto:salesteam@logianalytics.com?subject=I%20am%20interested%20in%20purchasing%20this%20product,%20please%20contact%20me. "US Sales email address.") or [UK Sales](mailto:emea_sales@logianalytics.com?subject=I%20am%20interested%20in%20purchasing%20this%20product.%20Please%20contact%20me. "Email address for UK sales team.").

* [Logi Info v14.0 Service Pack 3 Resolved Issues](#Logi_Info_v14.0_Service_Pack_3_Resolved_Issues)
* [Logi Info v14.0 Service Pack 2 Resolved Issues](#Logi_Info_v14.0_Service_Pack_2_Resolved_Issues)
* [Logi Info v14.0 Service Pack 1 Resolved Issues](#Logi_Info_v14.0_Service_Pack_1_Resolved_Issues)
* [Logi Info v14.0 Feature Enhancements](#Feature)
* [Logi Info v14.0 Resolved Issues](#Resolved)
* [Deprecated features](#Deprecated_Features)

To view the Release Notes for this product version, along with previous product versions, see the [Info Release Notes page](https://clm.logianalytics.com/rdPage.aspx?rdReport=RelNotesINF).

## Logi Info v14.0 Service Pack 3 Resolved Issues

| Title | Description |
| --- | --- |
| Log4J | Log4J upgraded from 2.13.1 to 2.17.1. |
| SSRM - Count Aggregate | The correct Count aggregate now displays when using existing filters on an Analysis Grid. |
| AG - Count Aggregate | The correct value for the count aggregate function now displays at both the group level and table level. |
| Chrome 92 | All JavaScript dialogs (alert, confirm, and prompt) have been replaced with custom dialogs to enable iFrame compatibility with the latest version of Chrome. |
| REST Connection | You no longer receive the error message 'The request was aborted: Could not create SSL/TLS secure channel' when attempting to connect to an HTTPS enabled REST endpoint. |
| Log4Net | The Log4Net library was updated to 2.0.10, effectively excluding the CVE-2018-1285 vulnerability. |
| DataLayer.SQL | DataLayer.SQL now works when running an MDX query using Connection.OLAP. |
| Local Data | Local Data elements now run on Interactive Paging/Refresh, as expected. |
| AG - Column Resizing | You can now resize Analysis Grid columns on a touch screen device without receiving an error. |
| Procedure.Export Element | Adding more than one Procedure.Export element underneath a Procedure.If element no longer causes an 'Object reference not set to an instance of an object' error when the process is run with the scheduler. |
| AG - Grouped Column | An Analysis Grid with a grouped column no longer returns an object reference error when you access the next page's results. |
| Crosstab Legend Colors | Tokenized colors can now be used for the chart legend's color boxes when the Crosstab chart has only one Crosstab Value column. |
| Rapid Excel Export | Rapid Excel Exports no longer fail when blocking HTTP redirects on a load balanced setup. |

## Logi Info v14.0 Service Pack 2 Resolved Issues

| Title | Description |
| --- | --- |
| Datasets | The Friendly Name of the Join in the Live Metadata now takes precedence for Join selections. |
| Cross-domain Embeddding | The CORS issue with rdScript.min.js for cross-domain embedded Logi Info v14.0 SP1 applications has been resolved. |
| Licensing | The trial license prompt now works appropriately in Logi Studio v14. |
| Drill To | Drilling to a chart with forecast definition no longer produces an unexpected column in the Drill To column list. |
| Dashboard | The panel filter and global filter now work as expected when re-opening a Dashboard from your Home page. |
| Chart Canvas Charts | Secondary X or Y Axis in Chart Canvas Charts now display properly. |
| AG - Analysis Grid | Your Analysis Grid table header now displays as expected in a Dashboard or Report. |
| SSRM - Analysis Grid | You can now add an aggregate to your Analysis Grid table with joins without the Analysis Filter displaying an invalid column name error. |
| Embedding | You can now use ‘inputCheckboxList’ in an embedded application after upgrading to 14.0-SP1. |
| InfoGo | When selecting Metadata, InfoGo no longer displays duplicate table names after selecting the ‘Apply Column Selection' button. |
| AG - Data Tab | When the constant rdDisableMetadataColumn is set to "True", the Analysis Grid will use live metadata when you apply changes to the Data tab. |
| Bookmarks | Bookmarks now retain their filter when you add an Analysis Filter and save your changes. |
| SSRM - Pie Charts | The Pie Chart format now displays as expected when applying an Analysis Grid that uses a Data Column with a custom format containing a percentage value to an Author Dashboard/Report. |
| AG - Analysis Grid | You no longer receive a JSON error in your Analysis Grid after exporting a report and applying an additional filter. |
| Bookmarks | You can now utilize the ‘Add to Gallery’ and ‘Export’ options in a shared bookmark when using 12.8 SSRM with the Logi Info v14 engine. |
| Exporting | Exporting a table to Excel/CSV no longer throws an ‘Object reference not set to an instance of an object’ error when the Dashboard contains a chart and a table. |
| Columns | You can now use an ampersand in column names without receiving an XML error. |
| Exporting | Group Header Rows with DataColumns greater than 11 no longer return an error when exporting to Excel. |
| SSRM - Dashboard | Adding a crosstab gallery file to your Dashboard no longer returns an error. |

## Logi Info v14.0 Service Pack 1 Resolved Issues

| Title | Description |
| --- | --- |
| AG - Friendly Column Name | Data columns with special characters (like &) in the Friendly Column Name no longer return an XSL error in the Analysis Grid. |
| SSRM - SQLServer Session State | Using 'SQLServer' session state in web.config and viewing existing Analysis Grid bookmarks, or creating a new analysis bookmark, no longer returns the following exception: Unable to serialize the session state. In 'StateServer' and 'SQLServer' mode, ASP.NET will serialize the session state objects, and as a result non-serializable objects or MarshalByRef objects are not permitted. |
| StateServer and SQLServer Session State | You no longer receive a SerializationException at rdServer.rdErrorMessage for scheduled tasks when the session state mode is StateServer or SQL Server in Info 12.8 and 14.0. |
| Forecast Bars | Forecast bars (Forecast Regression Linear/Trend) now display properly in your Dashboard and Report Author. |
| AG - Extra Label Columns | Adding Extra Label Columns to your Crosstab now displays the names of the selected columns separated by a comma, as expected. |
| Chart Drill To | The Chart Drill To feature in your Dashboard now properly responds to the constant 'rdDisableMetadataColumnCheck'. |
| InfoGo - Metadata Column | The Metadata Column ‘FriendlyName’ is no longer a required attribute for Info 14 users. |
| SSRM - Aggregate Filter | You no longer receive an error when adding an Aggregate Filter using a custom query. |
| PDF Export | Exporting to PDF now produces the correct data for each additional tab. |
| Java Scheduler Service | Java scheduler service on Linux now sends emails as expected when specifying a time zone. |
| AG - Loading Icon | The Analysis Grid now displays the loading icon while opening or updating a chart as expected in Info 14. |
| AG - Data Display | The most recent data now displays accordingly when updating an existing Analysis Grid. |
| Formulas | You can now create a new formula and replace an existing formula using the created one without receiving an error upon reopening the bookmark. |
| Static Tab Elements | Static tab elements with different IDs now work as expected after refresh. |

## Logi Info v14.0 Feature Enhancements

| Title | Description |
| --- | --- |
| [Bookmark Validation Utility](https://devnet.logianalytics.com/hc/en-us/articles/4419723127703-Logi-Info-v14-0-Enhancements-#SSRM_-_Bookmark_Validation_Utility) | A new Bookmark Validation tool is available that allows Developers or System Administrators to identify broken bookmarks and find solutions after applying any database, metadata, or security change. |
| [Data Table Bookmarks - Save Sort and Column Order](https://devnet.logianalytics.com/hc/en-us/articles/4419723127703-Logi-Info-v14-0-Enhancements-#DataTable_Bookmarks_-_Save_Sort_and_Column_Order) | Report authors can now enable the "remember sort and column order" function in a Data Table so these changes can be stored in bookmarks. |
| [AG - Zoom Charts](https://devnet.logianalytics.com/hc/en-us/articles/4419723127703-Logi-Info-v14-0-Enhancements-#SSRM_-_Zoom_Charts) | A new attribute, "Allow Zoom Control", is now available to enable zoom control for Analysis Grid configuration. |
| [AG - Aggregate Filters](https://devnet.logianalytics.com/hc/en-us/articles/4419723127703-Logi-Info-v14-0-Enhancements-#AG-Aggregate_Filters) | You can now use aggregates to filter your Analysis Grid. |
| [AG - Aggregate and Group Formulas](https://devnet.logianalytics.com/hc/en-us/articles/4419723127703-Logi-Info-v14-0-Enhancements-#AG_-_Aggregate_and_Group_Formulas) | You can now use aggregates and group functions in formulas in your Analysis Grid. |
| [AG - Add/Remove Extra Crosstab Label Column](https://devnet.logianalytics.com/hc/en-us/articles/4419723127703-Logi-Info-v14-0-Enhancements-#AG_-_Add/Remove_Extra_Crosstab_Label_Column) | You now have the ability to add or remove Extra Label Columns to a Crosstab Table in your Analysis Grid. |
| [AG - Additional Series](https://devnet.logianalytics.com/hc/en-us/articles/4419723127703-Logi-Info-v14-0-Enhancements-#AG_-_Additional_Series) | You now have the ability to add or remove additional Analysis Grid chart series. |
| [API Call](https://devnet.logianalytics.com/hc/en-us/articles/4419723127703-Logi-Info-v14-0-Enhancements-#API_Call) | It is now easier to handle multi-step API calls. This enhancement applies when making an API call to get an authorization token and then passing the result of the API call number into the Authorization Header of an API endpoint. Additionally, the RequestHeader element is now a child element of Metadata in your \_Settings file, enabling you to use authentication to access the metadata URL identified in your Metadata element. |
| [Crosstab Grouping and Summary](https://devnet.logianalytics.com/hc/en-us/articles/4419723127703-Logi-Info-v14-0-Enhancements-#Crosstab_Grouping) | You now have the ability to add Group Headers and Summary to your Crosstab Tables. |
| [Scheduler Time Zone Support](https://devnet.logianalytics.com/hc/en-us/articles/4419723127703-Logi-Info-v14-0-Enhancements-#Scheduler_-_Timezone_Support) | You now have the option to provide a time zone for scheduled tasks. |
| [Disable Metadata Check at Runtime](https://devnet.logianalytics.com/hc/en-us/articles/4419723127703-Logi-Info-v14-0-Enhancements-#Disable_Metadata_Check_at_Runtime) | You now have the option to disable the metadata check at runtime and use what is in the bookmark already via the constant rdDisableMetadataColumnCheck. |
| [DMF Conditional Attribute](https://devnet.logianalytics.com/hc/en-us/articles/4419723127703-Logi-Info-v14-0-Enhancements-#DMF_Conditional_Attribute) | The Definition Modifier File (DMF) element now includes a condition attribute that enables loading of the DMF. To apply the DMF, set the attribute to "True". |
| [Input Date Highlight](https://devnet.logianalytics.com/hc/en-us/articles/4419723127703-Logi-Info-v14-0-Enhancements-#Input_Date_Highlight) | The calendar reflecting the Input Date element now highlights both today's date (default), and the selected date. |
| [HTML Attribute Params](https://devnet.logianalytics.com/hc/en-us/articles/4419723127703-Logi-Info-v14-0-Enhancements-#HTML_Attribute_Params) | As a report developer, you can now add "HTML Attribute Params" to other HTML-like elements (Image, Label, Division), so you can apply your application to work with other framework or libraries easier. |
| Charting Library Upgrade | We made improvements to our underlying charting library. |

## Logi Info v14.0 Resolved Issues

| Title | Description |
| --- | --- |
| SSRM - Analysis Grid ActiveSQL with PostgreSQL | Aggregate queries no longer time out when using PostGres and performing sum, then calculating aggregates on formula columns. |
| SSRM - 12.6 Metadata | The constant, rdDisableMetadataColumnCheck, was enhanced to allow modifications to the metadata, without affecting existing bookmarks (Analysis Grid, Dashboards, and Report Author). |

## Deprecated Features

| Title | Description |
| --- | --- |
| Apache FOP | Apache FOP was deprecated. The .NET version is no longer compiled or distributed, while the Java version can still be distributed, minus its supporting libraries. Supported libraries include: avalon-framework-4.2.0.jar, batik-all-1.7.jar, fop.jar, serializer-2.7.1.jar, xalan-2.7.2.jar, and xmlgraphics-commons-1.5.jar. The rdXslFoTemplate.jar is still compiled; however, the .Net version of rdXslFoTemplate is no longer compiled. |
| Apache Hadoop and Hive | Hadoop drivers were deprecated from Info Java. The following libraries were removed: hadoop-core-0.20.2.jar, hive-exec-0.13.0.jar, hive-jdbc-0.13.0.jar, hive-service-0.13.0.jar, libfb303-0.9.1.jar, and libthrift-0.9.1.jar. |
