---
title: "Advanced Options"
id: 5281548966167
section: "Advanced Reports"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281548966167-Advanced-Options
updated_at: 2022-05-03T22:09:25Z
---

# Advanced Options

# Advanced Options

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> The system administrator can enable or restrict access to certain **Advanced Options**. Check with them for more information.

The following **Advanced Options** are available in the Report Designer, for both Advanced Reports and CrossTabs:

* ![JoinOption.png](https://devnet.logianalytics.com/hc/article_attachments/5432459157015/joinoption.png)**[Joins](#Joins)** — fine control over how the data objects on a report relate to each other.
* ![Event.png](https://devnet.logianalytics.com/hc/article_attachments/5432429108503/event.png) **[Events](#Events)**— link a **Server Event** to the report. Server Events are custom bits of functionality created by the system administrator that occur when certain application triggers occur such as when the report is loaded, saved or during the execution cycle.
* ![Vector.png](https://devnet.logianalytics.com/hc/article_attachments/5432326620311/vector.png)**Show Generated SQL** — view the generated SQL query which retrieves the data used on the report
* ![Parameters.png](https://devnet.logianalytics.com/hc/article_attachments/5432429120535/parameters.png)**[Parameters](#Report-L)** — define reusable system variables, called Parameters, on the report.

To access these advanced options:

* (*v2021.1+*) Click on the **Advanced**![Advanced.png](https://devnet.logianalytics.com/hc/article_attachments/5432397774999/advanced.png)![DropDownArrow2.png](https://devnet.logianalytics.com/hc/article_attachments/5432176827159/dropdownarrow2.png) menu on the toolbar, then choose one of the Advanced Options from the menu  
  ![f18C10n14M.png](https://devnet.logianalytics.com/hc/article_attachments/5432448142487/f18c10n14m.png)
* (*pre-v2021.1*) Click on the ![report-settings-menu.png](https://devnet.logianalytics.com/hc/article_attachments/5432394966167/report-settings-menu.png)**Report Settings** menu on the toolbar, hover over **Advanced**  then choose one of the options  
  ![CLHzrBJ7Km.png](https://devnet.logianalytics.com/hc/article_attachments/5432326828567/clhzrbj7km.png)

## Joins

If a report has two or more data objects, then information will only appear if the objects match. Using the **Joins** dialog, however, you may specify information you want to display regardless of whether or not it only exists in one of the data objects.

See [Advanced Reports: Joins](https://devnet.logianalytics.com/hc/en-us/articles/5281549160087-Advanced-Reports-Joins)

## Events

Event handlers may be applied to the report by advanced users for additional functionality.

![screen.events_window.png](https://devnet.logianalytics.com/hc/article_attachments/5432326848023/screen.events_window.png)

1. Click ![Add2.png](https://devnet.logianalytics.com/hc/article_attachments/5432238606103/add2.png)**Add** to add a new event to the list.
2. Choose a server event trigger from the **Event** dropdown list. See Table A below for a list of server event names.
3. Choose a server event action from the **Action** dropdown list. The actions available here are determined by the custom code entered into the application by the system administrator.
4. Click **Okay** to save the server event to the report and close the dialog, or **Cancel** to close the dialog without saving.

An event can be removed from a report using the **Delete**![image006.png](https://devnet.logianalytics.com/hc/article_attachments/5432441028375/image006.png) icon.

Upon triggering the event — for example, *OnReportExecuteStart* will be triggered at the start of the report’s execution — the associated action will take place.

Table A — Server Event Descriptions

| Server Event Name | Description |
| --- | --- |
| OnDataCombined | Called after all data is retrieved and combined from all data sources. |
| OnReportFailValidation | Called when a report fails validation while being loaded for editing or execution. |
| OnReportExecuteInit | Called after the report is loaded at the beginning of an execution, but before any processing has occurred. |
| OnReportExecuteStart | Called at beginning of report execution processing. |
| OnReportExecuteEnd | Called at end of report execution processing. |
| OnWebServiceExecuteEnd | Called after data is retrieved from a Web Service Method. |
| OnExecuteSqlStatementConstructed | Called after SQL statement due to report execution is constructed allowing any changes to be made. |
| OnFilterSqlStatementConstructed | Called after SQL statement due to filter dropdown is constructed allowing any changes to be made. |
| OnParameterSqlStatementConstructed | Called after SQL statement due to parameter dropdown is constructed allowing any changes to be made. |
| OnOkFiltersDialog | Called after Ok button in Filter execution dialog is clicked. |
| OnOkParametersDialog | Called after Ok button in Parameter execution dialog is clicked. |
| OnLoadReportParameters | Called when the report parameters are loaded but before any processing has occurred. |
| OnScheduledReportExecuteStart | Called at beginning of scheduled report execution. |
| OnScheduledReportComplete | Called upon completed execution of a scheduled report prior to further processing regardless of whether or not the report executed successfully |
| OnScheduledReportExecuteSuccess | Called upon successful execution of a scheduled report prior to further processing. |
| OnChartPreRender | Called just before rendering a chart. |
| OnConfigLoadStart | Called just after configuration file is loaded. |
| OnConfigLoadEnd | Called after configuration file is loaded, any changes are made, and host application container is redirected to the reporting application. |
| OnRenameFolderStart | Called just before renaming a report. |
| OnRenameFolderEnd | Called after a report is renamed. |
| OnDataFieldsRetrieved | Called after data fields are retrieved for a specific data object. |
| OnGetUserPreference | Called to retrieve a user preference. |
| OnSetUserPreference | Called to set a user preference. |
| OnReportSaveStart | Called before a report is saved. |
| OnAfterLoadReportsList | Called after reports built in this application have been loaded into the report tree object, for the purpose of allowing additional items to be loaded into the report tree. |
| OnExceptionThrown | Called when an application exception is thrown. |
| OnExportCsvCell | Called prior to exporting a CSV cell for the purpose of overriding the standard export results. |
| OnAfterReportExportSuccess | Called at the end of a successful report export. |

## Show Generated SQL v2019.1–v2021.1

## Show SQL v2021.1+

This dialog displays the SQL statement that will be sent to the appropriate data sources in order to execute the report.

![F6dRQ8Zlgt.png](https://devnet.logianalytics.com/hc/article_attachments/5432448295447/f6drq8zlgt.png)

The SQL statement shown in the **Execution SQL** window is the exact statement that will be sent to the databases. It is generated after applying sorts, filters, parameters, and other items that affect the constructed SQL.

## Report-Level Parameters **v2019.1.3+**

Advanced users may also define their own report-level parameters. The **Parameters** window provides an interface for users to view existing non-hidden system-level parameters and create new parameters that are only present on the report.

![75d2QJWHcj.png](https://devnet.logianalytics.com/hc/article_attachments/5432448371863/75d2qjwhcj.png)

1. Click the **Add** button located in the top-right corner.
2. Define a unique **Name**. This value will act as the parameter’s identifier within the report.
3. Specify a **Type** for the parameter, the following are available:
   * String
   * Date
   * Integer
   * Decimal
   * Boolean
4. Enter a default or fixed **Value**. If left blank then the value will be interpreted as `null`.
5. Specify whether or not to **Prompt** the user for a value upon report execution.
6. Define the **Prompt Text**, the message that will appear when prompting the user for a value. A value for this field is required if the parameter is prompting.

![XgjUi1nGLU.png](https://devnet.logianalytics.com/hc/article_attachments/5432368681751/xgjui1nglu.png)

Prompting parameter window

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Tip")
>
> Report-level and system-level prompting parameters appear in the same prompting parameter window at run time.

Report-level parameters can be reused throughout the report in the same manner as non-hidden system-level parameters. They may be used as cell values or within filters, sorts, and calculations. To utilize a parameter within a cell or formula, surround its **Name** with ‘@’ symbols (@*ParameterName*@).

For example, the following formula outputs *True* if an employee’s revenue is greater than or equal to the value of the Sales Quota parameter and *False* if otherwise:

```
{OrderDetails.UnitPrice}*{OrderDetails.Quantity} >= @SalesQuota@
```

### Using Report-Level Parameters in Dashboards and Chained Reports

Like system-level parameters, report-level parameters may be used and set to prompt for values in **Dashboards** and **Chained Reports** when the associated **Advanced Report** is added as an existing report.

![bnTskA7PWX.png](https://devnet.logianalytics.com/hc/article_attachments/5432225396503/bntska7pwx.png)

A report-level parameter defined on a Dashboard.

**Legacy Dashboard *pre-v2019.2* interface:**

![3Ip3hFZfcz.png](https://devnet.logianalytics.com/hc/article_attachments/5432431812375/3ip3hfzfcz.png)

A report-level parameter defined on a Dashboard. Note that the Dashboard option is disabled.

Within composite reports, however, these parameters can only take affect on the report-level and cannot be set to take affect on the **Dashboard**– or composite-level. This means that these parameters are only applicable on their associated **Advanced Reports** and cannot be modified to also apply to other reports or visualizations within a **Dashboard** or other composite report.
