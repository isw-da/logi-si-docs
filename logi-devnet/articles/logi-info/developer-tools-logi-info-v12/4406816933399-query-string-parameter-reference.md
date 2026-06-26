---
title: "Query String Parameter Reference"
id: 4406816933399
section: "Developer Tools - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406816933399-Query-String-Parameter-Reference
updated_at: 2024-04-04T18:23:15Z
---

# Query String Parameter Reference

# Query String Parameter Reference

Logi products use a number of **reserved words** to identify **tokens** and special **query string parameters**. This topic presents the query string parameters available for use in Logi Info.

If you're looking for information about tokens, see [Token Reference](https://devnet.logianalytics.com/hc/en-us/articles/4406817899415-Token-Reference).

Query string parameters are useful for passing data between web applications and use the familiar syntax:

> http://<URL>?<Parameter>=<Value>http://<URL>?<Parameter1>=<Value1>&<Parameter2>=<Value2>

In Logi reports, **@Request** tokens are used to retrieve the data POSTed by an HTML form and the values from parts of the **query string** used to call reports. The following special @Request token identifiers are also reserved words and have special meanings in Logi reports:

| Parameter | Description |
| --- | --- |
| rdAcRefreshData | For use with the **Analysis Chart** element. Refreshes the chart's data from the data source while maintaining any chart customizations the user has made during this session. To refresh data, call report with this parameter set to *True*. |
| rdAcReset | For use with the **Analysis Chart** element. Users' settings are automatically maintained during the session; clear these settings by calling the report with the rdAcReset parameter set to *True*. |
| rdAgLoadSaved | For use with the **Analysis Grid** element. Users' runtime customizations of the grid can be saved *between* sessions and Logi Info developers can implement this using the process task Procedure.Save Analysis Grid. A saved Analysis Grid can be reloaded using the rdAgLoadSaved parameter: *rdAgLoadSaved=myFileName.xml* |
| rdAgRefreshData | For use with the **Analysis Grid** element. Refreshes the grid's data from the data source while maintaining any grid customizations the user has made during this session. To refresh data, call report with this parameter set to *True*. |
| rdAgReset | For use with the **Analysis Grid** element. Users' settings are automatically maintained during the session; clear these settings by calling the report with the rdAgReset parameter set to *True*. |
| rdAfReset | For use with the **Analysis Filter** element. Users' settings are automatically maintained during the session; clear these settings by calling the report with the rdAfReset parameter set to *True*. |
| rdDebugPdf | When set to *True*, runs the PDF report and returns the HTML rather than generating a PDF from the HTML. |
| rdDgLoadSaved | For use with the **Dimension Grid** element. Users' runtime customizations of the grid can be saved *between* sessions and Logi Info developers can implement this using the process task Procedure.Save Dimension Grid. A saved Dimension Grid can be reloaded using the rdDgLoadSaved parameter: *rdDgLoadSaved=myFileName.xml* |
| rdDgRefreshData | For use with the **Dimension Grid** element. Refreshes the grid's data from the data source while maintaining any grid customizations the user has made during this session. To refresh data, call report with this parameter set to *True*. |
| rdDgReset | For use with the **Dimension Grid** element. Users' settings are automatically maintained during the session; clear these settings by calling the report with the rdDgReset parameter set to *True*. |
| rdFormLogon | Set to *True* when using custom logon forms. |
| rdMobile | Set to *True* to indicate that the report definition specified in the rdReport parameter is a Mobile Reports definition. |
| rdOgLoadSaved | For use with the **OLAP Grid** element. Users' runtime customizations of the grid can be saved *between* sessions and Logi Info developers can implement this using the process task Procedure.SaveOlapGrid. A saved OLAP Grid can be reloaded using the rdAOLoadSaved parameter: *rdOgLoadSaved=myFileName.xml* |
| rdOgRefreshData | For use with the **OLAP Grid** element. Refreshes the grid's data from the data source while maintaining any grid customizations the user has made during this session. To refresh data, call report with this parameter set to *True*. |
| rdOgReset | For use with the **OLAP Grid** element. Users' settings are automatically maintained during the session; clear these settings by calling the report with the rdOgReset parameter set to *True*. |
| rdPaging | Specify either *Interactive*, *Printable* or *NoPaging*. |
| rdPassword | The password value used during login when using security. |
| rdProcess | Specifies the file name (without a file extension) of a process definition that contains a task to execute. |
| rdPrompt | When set to *True*, a page listing all @Request tokens referenced in the definition file is displayed. The user can display default values for each parameter by specifying rdPromptxxxxx at the prompt, where *xxxxx* is the name of the request parameter. |
| rdReport | Specifies a report definition to run. |
| rdReportFormat | Specify any of the following formats: *PDF*, *NativeExcel*, *NativeWord*, *CSV*, *HtmlExport*, *HtmlEmail*, *Excel*, *Word*, *XML*, or *GoogleSpreadsheet* |
| rdShowModes | Specifies ShowModes defined for display in the current report. |
| rdSort | Indicates the column and direction of a DataTable sort. The format of the query string variable is: rdSort=*<dataTableID>*~*<columnName>*~*<columnDataType>*~*<Ascending|Descending>*~ |
| rdTaskID | Specifies a Task ID to execute. |
| rdTaskLogFilename | Returns the name of the logfile created by Task Manager for a specific job. This token is used within the Process definition that creates the job. |
| <*TabsElementID*> | When a page containing a **Tabs** element is submitted, a request variable is automatically generated named for the ID of the Tabs element and assigned the value of the ID of the currently selected Tab Panel.  Example: *@Request.MyTab~ = "Tab1"* |
| rdTemplate | Specify the template definition to run. |
| rdUserName | The User Name value used during login when using security. |
