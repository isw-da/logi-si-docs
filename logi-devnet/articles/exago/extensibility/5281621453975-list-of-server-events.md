---
title: "List of Server Events"
id: 5281621453975
section: "Extensibility"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281621453975-List-of-Server-Events
updated_at: 2022-05-03T22:09:00Z
---

# List of Server Events

# List of Server Events

![Server Events categorized by activity](https://devnet.logianalytics.com/hc/article_attachments/5432281614999/server_events_categorized.png)

Server events categorized by activity

## Startup

[Global Event: OnConfigLoadStart](https://devnet.logianalytics.com/hc/en-us/articles/5281583209367-Global-Event-OnConfigLoadStart)— Occurs when the configuration of Exago is initially loaded. Expects a void return.

[Global Event: OnConfigLoadEnd](https://devnet.logianalytics.com/hc/en-us/articles/5281598746391-Global-Event-OnConfigLoadEnd)— Occurs after the last API changes have been made to Exago’s configuration. Expects a void return.

[Global Event: OnGetUserPreferences](https://devnet.logianalytics.com/hc/en-us/articles/5281598997271-Global-Event-OnGetUserPreferences)— Called to retrieve user preferences when entering the application and editing/executing reports.

[Global Event: OnAfterLoadReportsList](https://devnet.logianalytics.com/hc/en-us/articles/5281590543127-Global-Event-OnAfterLoadReportsList)v2016.3+ — Occurs after reports created in Exago have been loaded in the report tree object, for the purpose of allowing additional items to be loaded in the report tree.

## User Interaction

[Global Event: OnReportFailValidation](https://devnet.logianalytics.com/hc/en-us/articles/5281622228759-Global-Event-OnReportFailValidation)v2017.1+ — Occurs when a user attempts to edit or run a report which has errors.

[Global Event: OnDataFieldsRetrieved](https://devnet.logianalytics.com/hc/en-us/articles/5281613541655-Global-Event-OnDataFieldsRetrieved)— Occurs after Data Fields are retrieved from specific Data Objects. Expects a Data Table to be returned to indicate how to display the Data Fields.

[Global Event: OnFilterSqlStatementConstructed](https://devnet.logianalytics.com/hc/en-us/articles/5281598977943-Global-Event-OnFilterSqlStatementConstructed)— Occurs before the data source is queried to populate the filter dropdown. Expects an SQL string to be returned.

[Global Event: OnReportSaveStart](https://devnet.logianalytics.com/hc/en-us/articles/5281605616279-Global-Event-OnReportSaveStart)— Occurs at the beginning of the report save process.

[Global Event: OnRenameFolderStart](https://devnet.logianalytics.com/hc/en-us/articles/5281591075863-Global-Event-OnRenameFolderStart)— Occurs when a user attempts to rename a folder. Expects a string to be returned to indicate if execution should proceed.

[Global Event: OnRenameFolderEnd](https://devnet.logianalytics.com/hc/en-us/articles/5281599193751-Global-Event-OnRenameFolderEnd)— Occurs when a folder has been renamed. Any return value will be ignored.

## Report Execution

[Global Event: OnReportFailValidation](https://devnet.logianalytics.com/hc/en-us/articles/5281622228759-Global-Event-OnReportFailValidation)v2017.1+ — Occurs when a user attempts to edit or run a report which has errors.

[Global Event: OnScheduledReportExecuteStart](https://devnet.logianalytics.com/hc/en-us/articles/5281591273879-Global-Event-OnScheduledReportExecuteStart)v2018.1+ — Occurs when report execution begins on a scheduler service. Expects a string to be returned to indicate if execution should proceed.

[Global Event: OnReportExecuteStart](https://devnet.logianalytics.com/hc/en-us/articles/5281599371543-Global-Event-OnReportExecuteStart)— Occurs when report execution begins. Expects a string to be returned to indicate if execution should proceed.

[Global Event: OnReportExecuteInit](https://devnet.logianalytics.com/hc/en-us/articles/5281591136663-Global-Event-OnReportExecuteInit)v2019.1.9+ — Occurs slightly before **OnReportExecuteStart** before Report Viewer metadata is created. Expects a string to be returned to indicate if execution should proceed.

[Global Event: OnLoadReportParameters](https://devnet.logianalytics.com/hc/en-us/articles/5281605273623-Global-Event-OnLoadReportParameters)— Passes a list of Parameter elements that can be reordered or modified before they are sent to the client for display.

[Global Event: OnParameterSqlStatementConstructed](https://devnet.logianalytics.com/hc/en-us/articles/5281613842199-Global-Event-OnParameterSqlStatementConstructed) — Occurs after a parameter dropdown object is constructed. Allows for modifying the object SQL.

[Global Event: OnOkParametersDialog](https://devnet.logianalytics.com/hc/en-us/articles/5281613799959-Global-Event-OnOkParametersDialog)— Occurs when Okay is clicked on the Parameter Execution Window. Expects a string to be returned to indicate if execution should proceed.

[Global Event: OnOkFiltersDialog](https://devnet.logianalytics.com/hc/en-us/articles/5281583469847-Global-Event-OnOkFiltersDialog)— Occurs when Okay is clicked on the Filter Execution Window. Expects a string to be returned to indicate if execution should proceed.

[Global Event: OnExecuteSqlStatementConstructed](https://devnet.logianalytics.com/hc/en-us/articles/5281613621399-Global-Event-OnExecuteSqlStatementConstructed)— Occurs before the data source is queried for report execution. Expects an SQL string to be returned.

[Global Event: OnWebServiceExecuteEnd](https://devnet.logianalytics.com/hc/en-us/articles/5281583896343-Global-Event-OnWebServiceExecuteEnd)— Occurs when a web service data source returns data. Expects an xml string to be returned.

[Global Event: OnDataCombined](https://devnet.logianalytics.com/hc/en-us/articles/5281613493399-Global-Event-OnDataCombined)— Occurs when data is combined and initially processed. Expects a Data Table to be returned.

[Global Event: OnReportExecuteEnd](https://devnet.logianalytics.com/hc/en-us/articles/5281622175511-Global-Event-OnReportExecuteEnd)— Occurs when a report execution finishes. Return value will be ignored.

[Global Event: OnExportCsvCell](https://devnet.logianalytics.com/hc/en-us/articles/5281590816407-Global-Event-OnExportCsvCell)— Occurs prior to exporting a CSV cell for the purpose of overriding the standard export results.

[Global Event: OnScheduledReportComplete](https://devnet.logianalytics.com/hc/en-us/articles/5281622290839-Global-Event-OnScheduledReportComplete)v2017.1+ — Occurs when a scheduled report execution completes, regardless of whether it was successful or not.

[Global Event: OnScheduledReportExecuteSuccess](https://devnet.logianalytics.com/hc/en-us/articles/5281591294615-Global-Event-OnScheduledReportExecuteSuccess)— Occurs when a scheduled report is executed. Expects a Boolean to be returned to indicate if the report should be sent as scheduled or intercepted.

[Global Event: OnAfterReportExportSuccess](https://devnet.logianalytics.com/hc/en-us/articles/5281621560215-Global-Event-OnAfterReportExportSuccess)v2019.1.1+ — Occurs when a report successfully exports.

## Miscellaneous

[Global Event: OnSetUserPreferences](https://devnet.logianalytics.com/hc/en-us/articles/5281591335063-Global-Event-OnSetUserPreferences)— Called to save user preferences when a user specifies startup reports or saves interactive HTML changes as a user report.

[Global Event: OnExceptionThrown](https://devnet.logianalytics.com/hc/en-us/articles/5281583292311-Global-Event-OnExceptionThrown)— Occurs when an exception is thrown in the user interface. Used to log additional information to the [Accessing the Log File](https://devnet.logianalytics.com/hc/en-us/articles/5281647183383-Accessing-the-Log-File).
