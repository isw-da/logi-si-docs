---
title: "Logi Info v12 Release Notes"
id: 4409573704471
section: "Release Notes - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4409573704471-Logi-Info-v12-Release-Notes
updated_at: 2022-04-06T06:10:43Z
---

# Logi Info v12 Release Notes

# Logi Info v12 Release Notes

Please select the following link to view a Chrome browser update likely to affect all Info customers this year: [Critical Chrome Browser Update](https://devnet.logianalytics.com/hc/en-us/articles/4415831044375).

This topic describes feature enhancements, resolved issues, and important information for Logi Info v12.

* [Info v12.8 Service Pack 4 Resolved Issues](#Info_v12.8_Service_Pack_4_Resolved_Issues)
* [Info v12.8 Service Pack 3 Resolved Issues](#Info_v12.8_Service_Pack_3_Resolved_Issues)

To purchase this product, contact [US Sales](mailto:salesteam@logianalytics.com?subject=I%20am%20interested%20in%20purchasing%20this%20product,%20please%20contact%20me. "US Sales email address.") or [UK Sales](mailto:emea_sales@logianalytics.com?subject=I%20am%20interested%20in%20purchasing%20this%20product.%20Please%20contact%20me. "Email address for UK sales team.").

To view the Release Notes for this product version, along with previous product versions, see the [Info Release Notes page](https://clm.logianalytics.com/rdPage.aspx?rdReport=RelNotesINF "Info Release Notes").

## Info v12.8 Service Pack 4 Resolved Issues

| Title | Description |
| --- | --- |
| AG - Data Display | The most recent data now displays accordingly when updating an existing Analysis Grid. |
| StateServer and SQLServer Session State | You no longer receive a SerializationException at rdServer.rdErrorMessage for scheduled tasks when the session state mode is StateServer or SQL Server. |
| Replace Function | Info now responds quickly when you use the Replace function using @Request tokens without values in .NET. |
| Dashboard | Adding Global Filters to your Dashboard now displays paging properly. |
| Series.Pie Chart | The Condition attribute now works as expected with the Action.PopupOption applied to a Series.Pie chart. |

## Info v12.8 Service Pack 3 Resolved Issues

| Title | Description |
| --- | --- |
| Joining Datasets | You no longer receive the Object Reference Error introduced in 12.8 SP2 hotfix when joining datasets. |
| Procedure.SQL | Using the attribute CData=False with Procedure.SQL no longer returns the error Keyword not supported: ‘allow zero datetime’. |
| Export PDF | The ability to display or hide the title of the exported PDF reports can be now correctly controlled using the constant 'rdPdf508Compliant'. Setting this constant to 'False' will remove the default title. |
| Chart DrillThrough | The Chart DrillThrough pop-up now displays properly when using a condition to show/hide a chart. |
| Tokens | The tokens @Function.PageNumber~ and @Function.PageCount~ now work in Java when KeepShowElements is set to ‘True’. |
| AG - Metadata Joins | Analysis Grid metadata joins now work properly. |
| SSRM - ActiveSQL Joins | Table joins using the Active Query Builder interface now generate ActiveSQL datatables as expected. |
| ActiveSQL Error | You no longer receive an ActiveSQL error when your Custom Table contains a comment. |
| SSRM - New Analysis Icon | Selecting the New Analysis icon from the menu on the left-hand side in SSRM now auto-creates a new bookmark analysis, as expected. |
| Input Radio Button | Submitting a page after selecting an option from the Input Radio Button no longer flashes, and now displays the correct value in the label. |
| Export Excel/CSV | The checkbox structure now works properly when using a checkbox and a button with Action.NativeExcel or Action.CSV, and the Target.NativeExcel or Target.CSV element with the RequestForwarding attribute set to ‘True’. |
| SSRM - Dashboards | You no longer receive the 'This panel’s data is no longer available' error. |
| InfoGo - Analysis | The Analysis page no longer displays unexpected characters at the bottom of your screen after modifying a filter. |
| AG - Group Header Row | The Group Header Row now displays values properly after grouping two columns and removing the first group. |
| AG - Shared Bookmark | You no longer see any other controls other than sort when an analysis is shared with you. |
| AG - Metadata Tables | The Analysis Grid Query Builder now loads tables from the metadata file based on your security rights. |
| SSRM - Shared Reports | Removing a column from the metadata in the original report no longer displays an error message, and in turn, automatically renders the appropriate metadata in the shared report. |
| Export Excel | Duplicate table cells are no longer visible if you select Hide Duplicates when exporting to Excel in Info 12.7-12.8 SP1. |
| AG - Export Excel | The Merge Duplicate Cells feature in an Analysis Grid table now works properly when exporting the report to Excel. |
| Chart Tokens | Chart tokens added to a Link Parameters element in a Chart.XY element now properly resolve in Info 12.7 and 12.8. |
| JSON and REST | Using control characters with JSON and REST datalayers no longer causes an invalid character error. |
