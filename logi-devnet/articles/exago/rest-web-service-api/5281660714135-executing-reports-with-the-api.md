---
title: "Executing Reports with the API"
id: 5281660714135
section: "REST Web Service API"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281660714135-Executing-Reports-with-the-API
updated_at: 2022-05-03T22:07:51Z
---

# Executing Reports with the API

# Executing Reports with the API

> ![red exclamation point](https://devnet.logianalytics.com/hc/article_attachments/5432173635607/criticalicon.gif "Important")
>
> This version of the .NET API documentation is deprecated. A new version can be found at <https://exagoapi.logianalytics.com>.

There are two different ways to use the Exago APIs to perform report execution. This guide discusses the main differences and provides examples for both types in each API.

* **[API Action](#API)** is the most comprehensive way to run executions, and supports all types of reports. This is the only way to run composite reports such as Dashboards and Chained Reports. This method launches an Exago session into the browser via URL, and thus usually requires the use of an iframe. This also means that all interactive Report Viewer or ExpressView (*v2016.3+*) features are supported.
* **[GetExecute()](#GetExecu)** executes reports on the back-end and returns bare HTML, JSON, CSV, or binary data. GetExecute supports non-composite (Advanced, Express and CrossTab) reports and ExpressView (as of *v20191.31+*, *2019.2.19+* and *v2020.1.5+*). Using this method you do not have to launch any visible instance of Exago for the user, and can simply use it as a calculation engine.

  > ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
  >
  > GetExecute methods are not supported by **Remote Execution** in versions *pre-v2019.1.15*. In *v2019.1.15+*, all calls of the GetExecute() functions will use the Remote Execution servers if configured.
  >
  > To disable this behavior, disable remote executions for the session with the API.

## Overview

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Launch Method | Supported Report Types | .NET Supported Output Types | REST Supported Output Types |
| [API Action](#API) | Redirect browser frame to Exago session URL | All types | Interactive Report Viewer, Dashboard Viewer, ExpressView designer, or PDF, RTF, Excel, CSV |
| [GetExecute](#GetExecu) | Data returned directly to calling method | Advanced, Express, CrossTab, ExpressView\* | HTML, CSV, PDF, RTF, Excel, JSON | HTML, CSV, PDF, RTF, Excel, JSON |

\* GetExecute() for ExpressView is supported in *v20191.31+*, *2019.2.19+* and *v2020.1.5+* only.

## API Action

API sessions in Exago have a property called *action type*, which determines what part of Exago should be launched when the session is opened. Action types include executing a report, loading a report into the editor, loading a report into the scheduler, opening a section of the UI, etc.

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> API Action is also referred to as *GetUrlParamString*, because this is the general term for the methods which return the session redirect URL.

To tell the session to execute a report, set the action type to **ExecuteReport**.

Actions which load reports, such as Execute or Edit, work on the *active report* object. This is another property that must be set. This is done differently for each API: details are in the included examples.

> ![red exclamation point](https://devnet.logianalytics.com/hc/article_attachments/5432173635607/criticalicon.gif "Important")
>
> For security reasons, always set the **action type** and the **active report** explicitly. Although setting an active report defaults to execute, if a report fails to load and an action has not been specified, Exago will launch into the full Web Application user interface. This could cause users to have unintended levels of access.

Once you’ve finished setting the session variables, call `GetUrlParamString()`. This finalizes the session and creates a single-use URL string. This is done differently for each API; details are in the included examples. The URL is used to direct a browser window or iFrame to an Exago instance where the specified action takes place. The user can then interact with the report like normal.

See the following sections for examples. Variable names and arguments are placeholders.

### .NET API

1. ```
   //Create an API object and load a report object into it
   API myAPI = new Api(appPath);
   Report myReport = (Report)myApi.ReportObjectFactory.LoadFromRepository(reportPath);
   ```
2. ```
   //Set the desired output type.
   myReport.ExportType = wrExportType.Html;
   ```
3. ```
   //Save the modified report back to the API object
   myApi.ReportObjectFactory.SaveToApi(myReport);
   ```
4. ```
   //Set the API Action to execute the report
   myApi.Action = wrApiAction.ExecuteReport;
   ```
5. ```
   //Call GetUrlParamString() to close the session and retrieve the URL for it
   string url = netApi.GetUrlParamString(homePage);
   ```

### REST Web Service API

To use REST, create the session and pass the session variables. Take note of the sessionId and UrlParamString.

**POST /sessions**

Payload:

```
{
 "Page": homePage,
 "ApiAction": "ExecuteReport",
 "ExportType": "Html",
 "ReportSettings":
 {
  "ReportPath": reportPath
 }
}
```

Response (*some params omitted*):

```
{
 "sid": sessionId,
 "AppUrl": urlParamString
}
```

## GetExecute

There are four provided *GetExecute* methods. Each return a different data representation of the report. Not every API supports every data type; see [Overview](#Overview).

* **GetExecuteHtml:** Typically used for web viewing
* **GetExecuteCsv:** Plain-text format readable by spreadsheet applications
* **GetExecuteData:** Byte array of binary data
* **GetExecuteJson** v2016.3+: Typically used for asynchronous client-server communication

Since GetExecute does not require loading the Exago UI, calling *GetUrlParamString* is not required. Report interactivity is also not supported when executing reports via the GetExecute functions. However, the following Server Events are triggered in order to ensure that the data returned accurately reflects the report design:

* [Global Event: OnReportExecuteInit](https://devnet.logianalytics.com/hc/en-us/articles/5281591136663-Global-Event-OnReportExecuteInit)
* [Global Event: OnReportExecuteStart](https://devnet.logianalytics.com/hc/en-us/articles/5281599371543-Global-Event-OnReportExecuteStart)
* [Global Event: OnReportExecuteEnd](https://devnet.logianalytics.com/hc/en-us/articles/5281622175511-Global-Event-OnReportExecuteEnd)
* [Global Event: OnAfterReportExportSuccess](https://devnet.logianalytics.com/hc/en-us/articles/5281621560215-Global-Event-OnAfterReportExportSuccess)

See the following sections for examples. Variable names and arguments are placeholders.

### .NET

1. ```
   //First create an API session and load a report object.
   API myAPI = new Api(appPath);
   Report myReport = (Report)myApi.ReportObjectFactory.LoadFromRepository(reportPath);
   ```
2. ```
   //Then call the appropriate GetExecute() method for the desired data type.
   string reportHtml = myReport.GetExecuteHtml();
   ```

### REST Web Service API

When using the REST Web Service API, the initialization call creates a session ID string, which is a required URL parameter in all subsequent method calls. Note that the session URL is generated immediately, and altered dynamically as modifications are made to the session.

1. First create an API session. Take note of the session ID.**POST /sessions**

   Response (*some params omitted*):

   ```
   {
    "Id": sessionId
   }
   ```
2. Then execute the selected report. Supported types are HTML, CSV, PDF, RTF, Excel, JSON.**POST /reports/execute/{type}?sid=”sessionId”**

   Payload:

   ```
   {
    "ReportPath": "InventoryCategories",
     "DataType" : "Data"
   }
   ```

   Sample Response:

   ```
   Status: 200 OK

   {
     "ReportPath":  "InventoryCategories",
     "ExportType":  "csv",
     "DataType":    "Data",
     "ExecuteData": ""Categories"rn"Seafood"rn"Produce"rn"Beverages"rn",
     "IsError":     false,
     "ErrorList":   null
   }
   ```

For more information, see [REST — GetExecute](https://devnet.logianalytics.com/hc/en-us/articles/5281630138647-REST-GetExecute).
